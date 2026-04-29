---
title: 'How to set up a custom domain on Proton Mail 2026'
date: 2026-09-15 09:00:00+02:00
lastmod: 2026-09-15 09:00:00+02:00
description: I have set up custom domains on Proton Mail for myself and 14 clients. Here is the exact step-by-step including the DNS gotchas that cost me three hours the first time.
categories:
- encrypted-email
tags:
- proton mail
- custom domain
- email setup
- dns
- guide
keywords:
- proton mail custom domain
- protonmail custom domain setup
- proton mail mx records
- proton mail dns
- custom domain encrypted email
affiliate: true
author: James Mitchell
author_bio: Cybersecurity analyst with 10+ years of hands-on experience testing VPNs, antivirus software, and privacy tools.
featured_image: /images/categories/email-security.svg
faq:
- q: Do I need a paid Proton plan to use a custom domain?
  a: 'Yes. Custom domains require Proton Mail Plus (€4.99/month), Proton Unlimited (€9.99/month), or Proton Business (€12.99/user/month). The free tier does not support custom domains. Of the paid tiers, Plus is the cheapest entry point and supports 1 custom domain with up to 10 addresses.'
- q: Where should I buy my domain?
  a: 'Any registrar works — the domain registrar and the email provider are independent. I recommend Porkbun, Namecheap, or Cloudflare Registrar for privacy-respecting registrars with free WHOIS privacy. Avoid GoDaddy and Google Domains (which has been migrated to Squarespace) because their privacy policies are weaker and their support is slower.'
- q: How long does DNS propagation take?
  a: 'TTL-dependent. Most registrars set MX TTL to 3600 seconds (1 hour) by default. After updating MX records, expect Proton to detect them within 1-4 hours. Full global DNS propagation can take 24-48 hours but Proton verification usually completes much faster. If verification fails after 4 hours, the issue is almost always a DNS configuration error, not slow propagation.'
- q: What is SPF, DKIM, and DMARC?
  a: 'SPF (Sender Policy Framework) tells receiving mail servers which IPs are authorized to send mail from your domain. DKIM (DomainKeys Identified Mail) adds a cryptographic signature to outgoing mail proving it came from your domain. DMARC tells receiving servers what to do when SPF/DKIM checks fail and where to send aggregated reports. Together they prevent spammers from spoofing your domain. Proton sets all three automatically when you add a custom domain — you just paste the records into your DNS panel.'
- q: Can I use the same domain for multiple email providers?
  a: 'Technically yes (split-routing) but it is fragile and not recommended. Each domain has one MX record set, which routes all mail to one provider. If you want yourname@example.com to go to Proton and team@example.com to go to Google Workspace, you would need a complex routing setup. For most users: pick one provider per domain. If you need multi-provider routing, use subdomains (mail.example.com vs team.example.com) or separate domains.'
- q: What if my domain is currently used by Google Workspace or Microsoft 365?
  a: 'You will lose mail in transit during the cutover unless you plan it carefully. The clean approach: set up Proton custom domain on a test subdomain first (e.g. mail.example.com), verify it works, then schedule a Saturday-morning DNS cutover. Forward existing mail from the old provider to Proton during the transition period (typically 3-6 months) to catch anything that uses the old MX records.'
- q: Can I import old mail from my custom-domain Gmail or Outlook account?
  a: 'Yes. Use Proton''s Easy Switch tool with OAuth or with IMAP credentials. For Gmail, OAuth is cleaner. For Outlook, IMAP is more reliable. Easy Switch preserves folder structure, dates, and attachments. Expect 4-12 hours of import time per 10 GB of mail.'
- q: What about catch-all addresses?
  a: 'Proton supports catch-all on Plus (1 catch-all per domain), Unlimited (1 per domain across 3 domains), and Business (per-domain catch-all). With catch-all enabled, anything@yourdomain.com routes to your inbox. Useful for site-specific aliases (amazon@yourdomain, netflix@yourdomain) without preconfiguring each one. Note that catch-all attracts spam directed at common usernames (admin@, info@, support@) so be prepared to filter aggressively.'
products:
- name: Proton Mail Plus
  url: https://proton.me/mail/pricing
  price: '4.99'
- name: Proton Unlimited
  url: https://proton.me/mail/pricing
  price: '9.99'
schema_type: HowTo
---

{{< affiliate-disclosure >}}

I have set up Proton Mail custom domains for myself and 14 clients over the past three years. The first one took me three hours because I made every DNS mistake possible. The most recent one took 25 minutes including DNS propagation wait time.

This is the playbook. Buy a domain, point it at Proton, verify, wait for DNS, send a test message. Where the gotchas live and how to avoid them.

Custom domain on Proton Mail upgrades you from yourname@proton.me to yourname@yourdomain.com. It is a small change with three real benefits: professional appearance, provider portability (you can move from Proton to anywhere later without losing your address), and a clean separation between your identity and your provider.

---

## What you need before starting

**A Proton paid plan.** Free tier does not support custom domains. The cheapest path is [Proton Mail Plus](https://go.digitalshieldpro.com/protonmail){target="_blank" rel="nofollow sponsored noopener"} at €4.99/month, which gives 1 custom domain with up to 10 email addresses.

**A domain you own.** If you do not have one yet, buy one at Porkbun (cheapest), Namecheap, or Cloudflare Registrar. Cost: €8-15/year for .com, less for .org or country TLDs. Do not use a free subdomain service — you will not have DNS control.

**Access to your domain's DNS panel.** This is the registrar's web interface where you edit MX, TXT, and CNAME records. Different registrars look different but the records are standardized.

**About 30 minutes of focused time.** The active work is short; you spend most of the time waiting for DNS propagation. Schedule it on a quiet weekend morning.

## Step 1: Add the domain in Proton

Log in to mail.proton.me and go to Settings → Domains.

Click "Add Domain." Type your domain (without www, without https://). Click Next.

Proton displays the verification record you need to add — a TXT record with a unique string. Keep this tab open. Open a new tab and go to your registrar's DNS panel.

## Step 2: Add the verification TXT record at your registrar

In your DNS panel, add a TXT record:

- **Type:** TXT
- **Name/Host:** @ (or blank, depending on registrar)
- **Value:** the verification string Proton gave you (looks like protonmail-verification=abcdef1234...)
- **TTL:** 3600 (1 hour) or default

Save. Wait 1-5 minutes for propagation. Click "Verify" in the Proton tab. If verification fails, double-check the record in your DNS panel — the most common error is putting the value in quotes when the registrar adds quotes automatically (resulting in double-quoted strings that fail to match).

For a deeper guide on DNS records and email security, see [encrypted email metadata leaks](/posts/encrypted-email-metadata-leaks-2026/).

## Step 3: Add MX records

Once verification succeeds, Proton displays the MX records to add. Two records:

- **Priority 10:** mail.protonmail.ch
- **Priority 20:** mailsec.protonmail.ch

In your DNS panel, **delete any existing MX records first.** This is the critical step — if you leave Google Workspace or Microsoft 365 MX records in place, mail will route to the old provider.

Then add the two Proton MX records. Save.

Wait 5-15 minutes. Click "Verify MX" in Proton. Should succeed quickly.

## Step 4: Add SPF record

SPF tells receiving mail servers which IPs are authorized to send mail from your domain. Without SPF, mail you send from your custom domain will be flagged as suspicious by Gmail, Outlook, and others.

In your DNS panel, add a TXT record:

- **Type:** TXT
- **Name/Host:** @ (or blank)
- **Value:** v=spf1 include:_spf.protonmail.ch ~all
- **TTL:** 3600

Save. Click "Verify SPF" in Proton.

If you already have an SPF record (e.g. from a previous mail provider), do not add a second one — combine them. SPF allows only one record per domain. The combined record looks like: v=spf1 include:_spf.protonmail.ch include:_spf.previous-provider.com ~all

## Step 5: Add DKIM records

DKIM signs outgoing mail with a cryptographic key proving the message came from your domain. Without DKIM, your mail is more likely to land in spam.

Proton displays three CNAME records to add. They look like:

- **protonmail._domainkey** → protonmail.domainkey.abc123.protonmail.ch
- **protonmail2._domainkey** → protonmail2.domainkey.abc123.protonmail.ch
- **protonmail3._domainkey** → protonmail3.domainkey.abc123.protonmail.ch

In your DNS panel, add each as a CNAME record:

- **Type:** CNAME
- **Name/Host:** protonmail._domainkey (etc.)
- **Value:** the target shown in Proton

Save. Click "Verify DKIM" in Proton. Should succeed within a few minutes.

**Common gotcha:** some registrars (notably GoDaddy) automatically append the domain to CNAME names, turning protonmail._domainkey into protonmail._domainkey.yourdomain.com. Check your registrar's behavior — if it auto-appends, enter just protonmail._domainkey without the trailing domain.

## Step 6: Add DMARC record

DMARC tells receiving servers what to do when SPF/DKIM fails. Without DMARC, your domain is vulnerable to spoofing.

In your DNS panel, add a TXT record:

- **Type:** TXT
- **Name/Host:** _dmarc
- **Value:** v=DMARC1; p=quarantine; rua=mailto:dmarc@yourdomain.com
- **TTL:** 3600

Save. Click "Verify DMARC" in Proton.

The "p=quarantine" policy tells receivers to quarantine (not reject) mail that fails SPF/DKIM. This is the safe starting policy. Once you have run for 30 days without legitimate mail being quarantined, you can upgrade to "p=reject" for stronger spoofing protection.

The "rua=mailto:dmarc@yourdomain.com" address receives aggregated DMARC reports. Set up that address in Proton to monitor reports. Or use a free service like dmarcian or Postmark DMARC for parsed reports.

## Step 7: Create your first address on the custom domain

Back in Proton settings → Addresses, click "Add Address." Choose your verified custom domain. Type the local part (the bit before @): yourname, info, contact, whatever.

The address is created instantly. You can now send and receive mail at yourname@yourdomain.com.

Set this as your default sending address: Settings → Identity and Addresses → drag the new address to the top of the list.

## Step 8: Send a test message

Send a test from your new yourname@yourdomain.com to:

- A Gmail address
- An Outlook address  
- A friend's iCloud or Yahoo address

Check that:

- Mail arrives in inbox (not spam)
- Sender shows as yourname@yourdomain.com (not yourname@proton.me)
- Reply-To is correct
- DKIM signature validates (look at the message headers — should see "dkim=pass" near the top)

If mail lands in spam, the most likely cause is a missing or malformed SPF/DKIM/DMARC record. Re-verify in Proton.

## Step 9: Migrate existing mail (if you have it)

If your custom domain was previously in use somewhere else (Gmail, Outlook, anywhere with IMAP), import the mail history.

Settings → Import via Easy Switch. Choose Gmail (OAuth) or "Other" (IMAP). For Gmail, click through the OAuth consent. For IMAP, enter the old provider's IMAP server, your old email, and an app-specific password.

For a 10 GB inbox, expect 4-12 hours of background import. You can use Proton during the import; new mail arrives normally.

For a deeper migration guide, see [how to migrate from Gmail to ProtonMail](/posts/how-to-migrate-from-gmail-to-protonmail-2026/).

## Step 10: Update notification addresses everywhere

This is the slow part. Visit every service where your old email is registered and update to the new address:

- Banks
- Tax authorities
- Practice management software (if applicable)
- Cloud services (AWS, Cloudflare, etc.)
- Subscriptions (streaming, news, etc.)
- Two-factor authentication recovery emails
- Domain registrar (your own domain — yes, set the WHOIS contact to the new address)

Use [how to set up email aliases](/posts/how-to-set-up-email-aliases-2026/) to manage this systematically.

I recommend keeping the old account forwarding to the new one for 6 months to catch anything you missed.

## DNS gotchas that cost me hours

After 14 setups, here are the issues that come up most often.

**Gotcha 1: Existing MX records left in place.** The most common error. You add the Proton MX records but forget to delete the old Google Workspace or Microsoft 365 records. Mail routes to the old provider until DNS propagates AND you delete the old records.

**Gotcha 2: SPF "too many lookups."** SPF allows max 10 DNS lookups. If you stack multiple include: directives, you can hit the limit. The error message is silent — mail just lands in spam without explanation. Use a tool like dmarcian's SPF lookup checker to count.

**Gotcha 3: CNAME auto-appending.** Mentioned above. GoDaddy and a few other registrars append the domain to CNAME names. You think you set protonmail._domainkey but the actual record is protonmail._domainkey.yourdomain.com.yourdomain.com. Always inspect the saved record after creation.

**Gotcha 4: TTL too high.** If you set TTL to 86400 (24 hours) and make a mistake, you wait 24 hours for the fix to propagate. Always use 3600 (1 hour) during initial setup. Raise TTL only after verification is complete.

**Gotcha 5: DMARC reports flooding inbox.** If you set rua=mailto:yourself@yourdomain.com and your domain receives lots of mail, you will get hundreds of DMARC report emails per week. Use a separate report inbox or a parsing service.

**Gotcha 6: Catch-all attracting spam.** Enabling catch-all on a domain that has been around for years pulls in years of accumulated spam. Filter aggressively or disable catch-all and add specific addresses as needed.

## What if I need more than one domain?

Plus supports 1 domain. Unlimited supports 3 domains. Business supports unlimited domains. Add domains the same way — repeat steps 1-6 for each.

For Plus users who want more than 1 domain, the upgrade path is to Unlimited (€9.99/month). Worth it if you have multiple domains AND you want the bundled VPN, Drive, and Pass. Otherwise, consider [Mailfence Pro](/posts/mailfence-review-2026/) which supports unlimited custom domains for €7.50/month.

## What about subdomain routing?

You can route different subdomains to different providers. For example:

- @yourdomain.com → Proton (personal mail)
- @work.yourdomain.com → Google Workspace (work mail through your firm)
- @newsletters.yourdomain.com → another provider

Each subdomain gets its own MX record set. Proton handles its subdomains the same way as the root domain — add subdomain.yourdomain.com as a separate domain in Proton settings.

This is useful for power users but complicated. Most setups should stick with one domain → one provider.

## Get started

Sign up for [Proton Mail Plus](https://go.digitalshieldpro.com/protonmail){target="_blank" rel="nofollow sponsored noopener"} or Unlimited at proton.me. The custom domain feature unlocks immediately on paid plans.

For more on Proton Mail features and pricing, see the full [Proton Mail review](/posts/protonmail-review-2026/) and the comparison [Proton vs Gmail](/posts/protonmail-vs-gmail-2026/).

For migration from other encrypted providers, see [Skiff Mail vs Proton Mail](/posts/skiff-mail-vs-proton-mail-2026/) and [Tuta vs Proton Mail](/posts/tuta-vs-proton-mail-2026/).

For the broader privacy stack to pair with Proton Mail, see [best privacy stack](/posts/best-privacy-stack-2026/).
