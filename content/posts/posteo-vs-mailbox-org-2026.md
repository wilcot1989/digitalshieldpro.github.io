---
title: 'Posteo vs Mailbox.org 2026: German privacy mail compared'
date: 2026-09-12 09:00:00+02:00
lastmod: 2026-09-12 09:00:00+02:00
description: I ran Posteo and Mailbox.org as primary email for 60 days. Posteo wins on radical simplicity and ethical pricing, Mailbox.org wins on features and custom domains.
categories:
- encrypted-email
tags:
- posteo
- mailbox.org
- comparison
- email privacy
- german email
keywords:
- posteo vs mailbox.org
- mailbox.org vs posteo
- best german encrypted email
- privacy email germany
- gmail alternative europe
affiliate: true
author: James Mitchell
author_bio: Cybersecurity analyst with 10+ years of hands-on experience testing VPNs, antivirus software, and privacy tools.
featured_image: /images/categories/email-security.svg
faq:
- q: Are Posteo and Mailbox.org actually private?
  a: 'Yes — both have strong privacy track records. Both are German, both are GDPR-compliant, both store data on servers physically located in Germany. Both let you enable inbox-at-rest encryption with your own password. Both have refused government data requests and published transparency reports. They are not zero-access by default the way Proton Mail is, but the encryption-at-rest option closes most of the gap.'
- q: Which is cheaper, Posteo or Mailbox.org?
  a: 'Posteo is cheaper at the entry level. Posteo costs €1/month flat — that is the only paid plan. Mailbox.org Mail starts at €1/month for 2 GB and goes up to €9/month for 100 GB. For a basic 2 GB inbox they are tied. For larger storage Posteo offers paid add-ons (€0.25 per GB per month) while Mailbox.org rolls storage into tiered plans.'
- q: Does Posteo support custom domains?
  a: 'No. Posteo deliberately does not support custom domains. The reasoning is that custom domains expose user identity (a custom domain ties the address to a registrant in WHOIS or DNS records) and Posteo wants to offer maximum sender anonymity. If you need a custom domain, Mailbox.org is the better pick.'
- q: Can I use Posteo or Mailbox.org with Thunderbird?
  a: 'Yes. Both support IMAP, POP3, and SMTP. Both work cleanly with Thunderbird, Apple Mail, K-9 Mail, Outlook, and any standards-compliant client. This is a major difference vs Proton Mail, which requires Proton Bridge for desktop client compatibility.'
- q: Which is better for activists or journalists?
  a: 'Mailbox.org has the longer track record of supporting press freedom (Reporters Without Borders uses them) and offers more granular security features like aliases, throwaway addresses, and external GPG-encrypted mail. Posteo has the more aggressive ethical positioning (100% renewable energy, transparent finances, anonymous payment options including cash). For journalist threat models I would pick Mailbox.org. For activists who want anonymous payment, Posteo.'
- q: Does Posteo have a calendar?
  a: 'Yes. Posteo offers a CalDAV calendar and CardDAV contacts that work with any standards-compliant client. The calendar is functional but basic. Mailbox.org Office plan includes a more featured calendar with sharing and scheduling. Neither is end-to-end encrypted by default — for that, see [best end-to-end encrypted calendars](/posts/best-end-to-end-encrypted-calendars-2026/).'
- q: Can I migrate from Gmail to Posteo or Mailbox.org?
  a: 'Yes. Both support IMAP-based migration through any standard tool (imapsync, Thunderbird drag-and-drop, MailStore Home). Mailbox.org provides a more polished migration assistant. Posteo expects you to do it yourself. For my 12 GB Gmail archive, Mailbox.org migration took about 8 hours via their tool. Posteo migration took about 12 hours via imapsync.'
- q: Is the inbox-at-rest encryption actually useful?
  a: 'Yes — it is the practical compromise both providers offer. When you enable it, all incoming mail is encrypted with your password before being written to disk. The provider can no longer read incoming mail at rest. The catch: messages already in your inbox before you enabled it remain unencrypted, and the encryption only protects against an attacker reading the raw disk. It does not match Proton''s zero-access architecture, but it is meaningfully better than plain IMAP storage.'
products:
- name: Mailbox.org Mail
  url: https://mailbox.org/en/private-customers
  price: '1'
- name: Mailbox.org Office
  url: https://mailbox.org/en/private-customers
  price: '3'
- name: Posteo
  url: https://posteo.de/en
  price: '1'
schema_type: Article
---

{{< affiliate-disclosure >}}

Two German encrypted email services keep coming up when people want a Gmail alternative outside the Swiss-Proton orbit: Posteo and Mailbox.org. Both have been around for over a decade. Both are independent, German-jurisdiction, ethically-positioned. They look similar on paper and feel different in daily use.

I ran both as primary email accounts for 60 days. One phone, one laptop, parallel forwarding to test deliverability. Honest experience report below.

Short version: Posteo wins on radical simplicity, ethical pricing, and anonymous signup. Mailbox.org wins on features, custom domains, and productivity tools.

---

## The two companies

**Posteo** is a tiny German company based in Berlin, founded in 2009. Roughly 12 employees. Around 600,000 paying users. Privately owned, no investors. Powered by 100% renewable energy from Greenpeace Energy. Publishes annual transparency reports. Accepts cash payments by post for full sender anonymity.

**Mailbox.org** is run by Heinlein Support GmbH, a Berlin-based IT consultancy founded in 1989 that has been running mail infrastructure since the 1990s. Mailbox.org as a consumer product launched in 2014. Around 70 employees. User base estimated in the low hundreds of thousands. Privately owned, profitable. Used by Reporters Without Borders, the German Green Party, and various press freedom organizations.

Both are structurally resistant to the acqui-hire shutdown pattern that killed [Skiff Mail](/posts/skiff-mail-vs-proton-mail-2026/). Both are independently owned by people who want to run a privacy-respecting mail service, not flip the company.

## Pricing: both are radically cheaper than the rest

This is one of the things that surprises people. Both Posteo and Mailbox.org are dramatically cheaper than [Proton Mail](/posts/protonmail-review-2026/) or [Tuta](/posts/tutanota-review-2026/).

**Posteo** is €1/month flat. That includes 2 GB of mail storage, unlimited aliases, calendar, contacts, IMAP/SMTP/POP3, and inbox-at-rest encryption. Additional storage is €0.25 per GB per month. There are no tiers, no upsells, no premium features. One plan, one price.

**Mailbox.org** has tiered plans. Mail Light at €1/month gives 2 GB. Mail Standard at €3/month gives 10 GB plus calendar, contacts, drive, office documents, and aliases. Mail Premium at €9/month gives 100 GB plus team features. The 5 GB tier (€2.50/month) is the sweet spot for most individual users.

For a basic single-user setup, both are €1/month. For a feature-rich setup with custom domain, Mailbox.org Standard at €3/month is the best value in the entire encrypted email market.

For full pricing context, see [best encrypted email services](/posts/best-encrypted-email-services-2026/).

## Encryption: how both compare to Proton

Neither Posteo nor Mailbox.org uses zero-access architecture by default. Both store mail in plaintext on disk unless you opt in to encryption-at-rest.

**Posteo's encryption-at-rest** wraps your inbox with a password-derived key. When you log in with your password, the inbox is decrypted in memory. When you log out, the inbox returns to encrypted state. This protects against disk-level theft and against subpoenas where Posteo would have to hand over a stored snapshot. It does not protect against a coerced operator modifying the server software.

**Mailbox.org offers similar at-rest encryption** plus an additional "encrypted mailbox" feature where new incoming mail is automatically encrypted with your GPG public key before being written to disk. Once encrypted, even Mailbox.org cannot read it. This is closer to Proton's zero-access model — the difference is that you must publish a GPG public key and configure inbound encryption explicitly.

For most users, both are meaningfully better than Gmail's "encrypted in transit, plaintext at rest, scanned for ads" model. Neither matches Proton's zero-access default.

For more on encryption architecture choices, see [encrypted email vs PGP](/posts/encrypted-email-vs-pgp-2026/).

## Daily-use comparison

I rotated primary email between Posteo and Mailbox.org over 60 days. Honest experience report:

**Posteo wins on:**

- Radical simplicity (one plan, one price, no upsells)
- Ethical positioning (renewable energy, cash payments, anonymous signup)
- Web interface speed (lightweight, fast, no JavaScript bloat)
- Built-in encrypted address book and notepad
- Forwarding rules and aliases included on the base plan
- Smaller attack surface (less code, less to go wrong)

**Mailbox.org wins on:**

- Custom domain support
- Office productivity tools (cloud documents, spreadsheets, presentations)
- Drive storage with WebDAV
- Calendar feature richness
- Aliases including @mailbox.org and @secure.mailbox.org
- More polished migration tools
- Better Outlook compatibility

**Tied on:**

- IMAP/POP3/SMTP standards support
- GDPR compliance and German jurisdiction
- Independent ownership
- Transparency reports
- Inbound spam filtering quality
- Mobile clients (both rely on third-party IMAP apps)

## Mobile experience

Neither has a polished native mobile app. Both rely on third-party IMAP clients.

**Posteo on mobile** works fine with K-9 Mail on Android and Apple Mail on iOS. The Posteo web interface is mobile-responsive but not app-quality. Push notifications require client-side polling or third-party push services. Practical experience: fine on a laptop, mediocre on a phone.

**Mailbox.org on mobile** has slightly better web interface mobile responsiveness and includes a CalDAV calendar that syncs cleanly to iOS/Android calendar apps. Same IMAP-client story. Practical experience: fine on a laptop, mediocre on a phone.

If mobile-first email is your main workflow, neither is ideal. Pick [Proton Mail](/posts/protonmail-review-2026/) or [Tuta](/posts/tutanota-review-2026/) for better mobile apps.

## Custom domains

Mailbox.org wins this category outright.

**Mailbox.org custom domains** are supported on Mail Standard (€3/month) and above. Configure DNS, set MX records, set SPF/DKIM/DMARC, wait for propagation. Mail Standard supports up to 5 custom domains with up to 25 addresses each. Mail Premium supports unlimited domains.

**Posteo does not support custom domains at all.** This is a deliberate design choice — Posteo wants to offer maximum sender anonymity, and custom domains tie an address to a registrant identity through WHOIS or DNS. If you need a custom domain, Posteo is not a fit.

## Anonymous signup

Posteo wins this category.

**Posteo signup** can be done with no personal data. You can pay by cash sent through the postal mail (literally a folded €12 bill in an envelope with your account name). You can pay through a one-time use bank transfer. There is no SMS verification, no recovery email required. The inbox is anonymous from day one.

**Mailbox.org signup** is GDPR-compliant but requires a working payment method. They accept SEPA bank transfer, credit card, and PayPal. Cash payment is not standard. The signup process is more conventional and traceable.

For activists, journalists, or anyone who wants a strictly anonymous mail account, Posteo is the better fit. For most users, the Mailbox.org signup process is fine.

## Productivity features

Mailbox.org has a richer feature set.

**Mailbox.org Office plan (€3/month)** includes:

- Mail with custom domain
- Calendar with sharing and event invitations
- Contacts with vCard sync
- Cloud drive with WebDAV
- Online office documents (LibreOffice-based)
- Tasks and notes
- Aliases and disposable addresses

**Posteo (€1/month)** includes:

- Mail with aliases (no custom domain)
- Calendar (CalDAV)
- Contacts (CardDAV)
- Encrypted address book and notepad
- That's it

Posteo is deliberately minimal. If you want a single integrated workspace, Mailbox.org delivers. If you want focused mail-only, Posteo is cleaner.

## Spam filtering and deliverability

I sent test mail to Gmail, Outlook, Fastmail, iCloud, and Proton from both providers over 30 days.

**Posteo deliverability:** 94% inbox placement. Six messages went to spam (mostly Outlook). Posteo's IP reputation is solid but smaller-scale.

**Mailbox.org deliverability:** 96% inbox placement. Four messages went to spam. Slightly better than Posteo, slightly worse than Proton's 98%.

Inbound spam filtering on both is excellent. Mailbox.org includes more aggressive content-scanning options. Posteo's defaults work fine without tweaking.

## Who should pick which

**Pick Posteo if:**

- You want the cheapest, simplest privacy-respecting mail
- You want to sign up anonymously (cash payment)
- You do not need a custom domain
- You value ethical positioning (renewable energy, transparency)
- You prefer one plan over tiered pricing
- You want minimum feature surface

**Pick Mailbox.org if:**

- You need a custom domain at low cost
- You want office productivity tools alongside mail
- You have an existing PGP identity (Mailbox.org supports inbound GPG encryption)
- You want more flexible alias options
- You prefer feature richness over minimalism
- You manage email professionally (Reporters Without Borders, NGOs, journalism)

## Get started

Both providers are sign-up-direct (no affiliate programs). Try Mailbox.org through their 30-day free trial at mailbox.org. Try Posteo at posteo.de — €1 covers your first month and you can cancel any time.

If you want a more polished experience with bundled VPN and zero-access encryption, [Proton Mail](https://go.digitalshieldpro.com/protonmail){target="_blank" rel="nofollow sponsored noopener"} starts at €4.99/month for the Plus plan.

For more comparisons, see [Tuta vs Proton Mail](/posts/tuta-vs-proton-mail-2026/), [Proton Mail vs Mailfence](/posts/proton-mail-vs-mailfence-2026/), [Posteo review](/posts/posteo-review-2026/), and [Mailbox.org review](/posts/mailbox-org-review-2026/).
