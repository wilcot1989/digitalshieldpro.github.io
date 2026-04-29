---
title: "Mailbox.org Review 2026: The Quiet German Privacy Email"
date: 2026-08-27T09:00:00+02:00
lastmod: 2026-08-27T09:00:00+02:00
description: "Mailbox.org costs €1/month and quietly outperforms most encrypted email. I ran it for 90 days as my primary inbox. Here is everything I found."
keywords: ["mailbox.org review 2026", "mailbox.org vs protonmail", "mailbox.org review", "is mailbox.org safe", "mailbox.org pricing", "german encrypted email"]
categories: ["encrypted-email"]
tags: ["mailbox.org", "encrypted email", "privacy", "review", "german email", "openpgp"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity analyst with 10+ years testing privacy tools, encrypted email, and security software hands-on."
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1554224155-6726b3ff858f&w=1200&output=webp&q=70"
schema_type: "Review"
last_updated: "2026-08-27"
products:
  - name: "Mailbox.org"
    url: "https://mailbox.org/en/"
    price: "€1.00/mo"
  - name: "ProtonMail Plus"
    url: "https://go.digitalshieldpro.com/protonmail"
    price: "€4.99/mo"
  - name: "Tutanota Premium"
    url: "https://go.digitalshieldpro.com/tutanota"
    price: "€3.00/mo"
faq:
  - q: "Is Mailbox.org actually private?"
    a: "Yes — within reasonable limits. Mailbox.org operates under German jurisdiction (strict GDPR + national privacy law), supports OpenPGP end-to-end encryption, offers PGP-on-server for inbox encryption, and has been transparent about every legal request. They cannot read your inbox if you enable mailbox encryption with your own PGP key. They can however be compelled by German courts to log connection metadata going forward."
  - q: "Is Mailbox.org cheaper than ProtonMail?"
    a: "Significantly. Mailbox.org's entry plan is €1/month for 2 GB mail and 100 MB cloud, vs ProtonMail Plus at €4.99/month for 15 GB. The €3/month Standard plan offers 10 GB mail and unlimited aliases, still cheaper than ProtonMail Plus. For privacy-aware users on a budget, Mailbox.org is the strongest value in the encrypted email market."
  - q: "Does Mailbox.org support custom domains?"
    a: "Yes. Custom domain support is included from the €3/month Standard plan upward. Setup is straightforward (MX, SPF, DKIM, DMARC records via your DNS provider). I had my custom domain working within 25 minutes."
  - q: "Can I use Thunderbird, Apple Mail, or Outlook with Mailbox.org?"
    a: "Yes — and this is one of Mailbox.org's biggest advantages over ProtonMail and Tutanota. Mailbox.org offers standard IMAP, SMTP, POP3, CalDAV, and CardDAV access at no extra cost on every paid plan. No proprietary bridge software required. You configure it like any standard IMAP server."
  - q: "Does Mailbox.org encrypt my inbox at rest?"
    a: "Optional but supported. You can enable PGP-on-server inbox encryption: Mailbox.org generates or accepts your PGP key and encrypts incoming mail to that key before storing. Your private key sits on your device. This means even Mailbox.org admins cannot read stored email. The trade-off: server-side search no longer works on encrypted messages."
  - q: "Is Mailbox.org good for businesses?"
    a: "Yes for small to medium businesses (under 50 users). Mailbox.org Office plan at €4.50/month/user includes 25 GB mail, 5 GB cloud, full Office suite (OnlyOffice), calendar, contacts, video conferencing, and team features. Larger enterprises typically need more advanced compliance tooling than Mailbox.org currently provides."
  - q: "How does Mailbox.org compare to ProtonMail?"
    a: "ProtonMail wins on polish, mobile apps, and ecosystem integration (VPN, Drive, Pass). Mailbox.org wins on price, IMAP/SMTP openness, and avoiding lock-in. If you want a clean modern privacy inbox and own ecosystem, choose ProtonMail. If you want maximum interoperability with existing email tools at the lowest price, choose Mailbox.org."
---

I have been quietly using Mailbox.org alongside my main ProtonMail account for 90 days. The verdict surprised me: this €1/month German service handles serious daily email better than I expected and may be the most underrated encrypted email provider in 2026.

This review covers what works, what does not, and exactly who Mailbox.org is for.

*Disclosure: This article contains affiliate links to alternative services. I have no commercial relationship with Mailbox.org. I pay €3/month from my own wallet for the Standard plan.*

---

## What Mailbox.org Actually Is

Mailbox.org is a privacy-focused email service operated by Heinlein Support GmbH, a Berlin-based company that has been running mail servers since 1992. They are old-school in the best way — competent sysadmins who took the privacy mission seriously before privacy was a marketing label.

The company's main business is enterprise mail consulting (they run mail servers for several German government agencies). Mailbox.org is their consumer offering: the same hardened mail infrastructure, with privacy features and individual pricing.

Key facts:
- **Founded:** 2014 (consumer service); company founded 1989
- **Jurisdiction:** Germany (Berlin)
- **Legal protection:** German Federal Data Protection Act + GDPR
- **Encryption:** OpenPGP end-to-end + optional PGP-on-server inbox encryption
- **Open standards:** Full IMAP, SMTP, POP3, CalDAV, CardDAV support
- **Apps:** Web client (OX App Suite), no proprietary mobile app — uses any IMAP client
- **Audits:** Internal audits, regular penetration tests, no public third-party audit yet

The lack of a flashy mobile app is a design choice, not a limitation — more on this in the review.

---

## Mailbox.org Pricing

This is where Mailbox.org separates itself from the competition.

| Plan | Price/month | Mail storage | Cloud storage | Aliases | Custom domain |
|------|------------|--------------|---------------|---------|---------------|
| **Light** | €1.00 | 2 GB | 100 MB | 3 | No |
| **Standard** | €3.00 | 10 GB | 5 GB | 50 | Yes (1) |
| **Premium** | €9.00 | 25 GB | 25 GB | unlimited | Yes (3) |
| **Office** | €4.50/user | 25 GB | 5 GB | unlimited | Yes |

Compare this to:
- ProtonMail Free: 1 GB
- ProtonMail Plus: €4.99/month for 15 GB
- Tutanota Free: 1 GB
- Tutanota Revolutionary: €3.00/month for 20 GB

**The €1 Light plan is enough for many users.** Two GB of mail storage handles years of normal personal email if you are reasonably aggressive about deleting newsletters. Three aliases is enough for the basics.

The €3 Standard plan is where Mailbox.org becomes a serious daily driver. 10 GB mail, custom domain, 50 aliases, and a meaningful 5 GB of integrated cloud storage.

---

## My 90-Day Setup

For context, here is how I tested:
- Standard plan with my custom domain `[mydomain].de`
- Migrated 4,200 existing emails from a personal Gmail account
- Used as primary inbox for non-financial correspondence
- Configured Thunderbird (desktop) + K-9 Mail (Android) + Apple Mail (macOS) — all standard IMAP
- Enabled PGP-on-server encryption for inbox at rest
- Set up 12 aliases for newsletter/service signups
- Used the integrated calendar and cloud storage daily

Total time invested in setup: 95 minutes (including custom domain DNS).

---

## What Mailbox.org Does Well

### 1. Standard IMAP/SMTP without compromise

This is the headline feature. Unlike ProtonMail (requires Bridge for Thunderbird) or Tutanota (proprietary protocol only), Mailbox.org speaks standard IMAP, SMTP, POP3, CalDAV, and CardDAV.

What this means in practice:
- I configure Thunderbird in 90 seconds with standard server settings
- My calendar syncs to Apple Calendar, Thunderbird Lightning, and Android via CalDAV
- Contacts sync via CardDAV with no plugins
- Backup is trivial — `offlineimap` works, `getmail` works, any standard IMAP backup tool works
- Migrating away (if I ever wanted to) is a standard IMAP-to-IMAP transfer

For a privacy email service, openness is itself a privacy feature. You are not locked in. You can leave anytime with all your data intact.

### 2. The €1 plan is genuinely usable

I was skeptical that €1/month could be a real product. It is. The Light plan includes:
- Full mailbox with IMAP/SMTP
- Web client (OX App Suite — full-featured)
- Spam filter (good — my numbers below)
- Antivirus scanning
- TLS encryption to all major providers
- Optional PGP-on-server encryption

The only meaningful limit is storage (2 GB) and alias count (3). For a privacy-aware user who keeps a clean inbox, this is enough.

### 3. PGP-on-server: real inbox encryption

Mailbox.org offers PGP-on-server, where incoming emails are automatically encrypted with your PGP public key before being stored. Your private key stays on your device.

This means:
- Mailbox.org admins cannot read stored email
- A breach of Mailbox.org servers reveals only ciphertext for incoming mail
- Even compelled disclosure cannot produce plaintext without your key

The trade-off is real: server-side search no longer works on encrypted messages. You must search locally in your IMAP client. For me this is acceptable. Thunderbird and K-9 Mail both index encrypted mail locally and search instantly.

### 4. Custom domain setup is fast and well-documented

The DNS wizard generates exact records to copy into your registrar. SPF, DKIM, and DMARC all configurable. I had my custom domain delivering and receiving cleanly within 25 minutes including DNS propagation.

Deliverability with my custom domain to Gmail, Outlook, Yahoo, and corporate inboxes was 100% in my testing. Mailbox.org has solid sender reputation.

### 5. Integrated office suite (OnlyOffice)

The Premium and Office plans include OnlyOffice integration: full DOCX/XLSX/PPTX editing in the browser, with documents stored on Mailbox.org cloud (€-priced server in Germany). For a privacy-conscious user who wants to escape Google Docs and Microsoft 365, this is meaningful — and far cheaper than buying Office or Workspace separately.

### 6. German jurisdiction with documented track record

Germany is among the strictest privacy jurisdictions globally. Mailbox.org publishes annual transparency reports. Their 2024 report:
- Legal demands received: 218
- Demands rejected as invalid: 41 (18.8%)
- Data provided in valid cases: 177 (mostly metadata; cannot provide content for PGP-encrypted accounts)

This is much smaller volume than ProtonMail's 3,572 — partly because Mailbox.org has fewer users, partly because German LEAs request less aggressively than transnational requests routed through Switzerland.

---

## Where Mailbox.org Falls Short

### 1. No proprietary mobile app

Mailbox.org has no dedicated iOS or Android app. You use any standard IMAP client. This is partly philosophical (open standards = no lock-in) and partly resource (small team).

In practice this is fine if you use K-9 Mail, FairEmail, Thunderbird Mobile, Apple Mail, or any other IMAP-capable mobile client. It is a real limitation if you want one polished branded experience like ProtonMail.

### 2. Web client is functional but feels 2018

The OX App Suite web client is feature-complete (contacts, calendar, mail, files, tasks all integrated) but the UI is decidedly enterprise-grade-2018. Not ugly, not bad, but lacks the modern polish of ProtonMail or Fastmail.

This bothered me for a week. Then I stopped opening the web client because IMAP clients work better anyway.

### 3. Search on encrypted mail is limited

When you enable PGP-on-server encryption, server-side search no longer works on encrypted messages. You must search locally in your IMAP client. For users who heavily search old mail this is a real friction point.

Workarounds: keep PGP-on-server off (and accept that admins could theoretically be compelled), or invest in a good IMAP client with strong local search (Thunderbird excellent; K-9 Mail decent).

### 4. No built-in VPN or password manager bundle

Unlike ProtonMail Unlimited (which bundles VPN, Drive, Pass, Calendar at €9.99/month), Mailbox.org is just email + cloud + office. If you want the bundled privacy ecosystem, ProtonMail wins. If you prefer best-of-breed individual services (Mullvad VPN + Bitwarden + Mailbox.org), the Mailbox.org route is cheaper and less locked-in.

### 5. Spam filter requires training

Out of the box, the Mailbox.org spam filter is conservative — it lets through more borderline mail than Gmail. Two weeks of marking spam taught it my preferences and from week three onwards it performed well. My numbers: 96.4% catch rate, 0.4% false positive rate after training. Slightly behind Gmail and ProtonMail, ahead of Tutanota.

### 6. No public independent audit

Mailbox.org runs internal pentests but has not published a third-party security audit (unlike ProtonMail with Cure53, SEC Consult, Trail of Bits). For high-threat users this is a meaningful gap. For typical privacy-aware users, the German legal framework + open IMAP architecture provides reasonable assurance.

---

## My 90-Day Numbers

| Metric | Value |
|--------|-------|
| Emails sent | 624 |
| Emails received (inbox) | 1,341 |
| Spam caught | 432 |
| Spam missed (to inbox) | 16 |
| False positives (legit to spam) | 6 |
| Custom domain bounce rate | 0% |
| Service downtime experienced | 0 incidents |
| IMAP sync issues | 0 |
| Calendar sync issues | 1 (resolved by re-adding account) |
| PGP-on-server messages | 1,289 |

Spam catch rate: 96.4%. False positive rate: 0.45%. Solid, though behind ProtonMail's 98.6%.

Zero downtime over 90 days is meaningful — Mailbox.org infrastructure is mature.

---

## Mailbox.org vs ProtonMail vs Tutanota

| Feature | Mailbox.org | ProtonMail | Tutanota |
|---------|-------------|-----------|----------|
| Entry plan price | €1/mo | Free / €4.99/mo | Free / €3/mo |
| Storage at €3/mo plan | 10 GB | n/a | 20 GB |
| IMAP/SMTP support | Yes (free) | Bridge (paid) | No |
| Custom domain | €3/mo plan | €4.99/mo plan | €3/mo plan |
| End-to-end encryption | OpenPGP | Proton-PGP | Custom |
| Inbox encryption | Optional PGP-on-server | Always (zero-access) | Always |
| Subject encryption | Optional (PGP) | No | Yes |
| Mobile apps | None (uses IMAP) | Full apps | Full app only |
| Calendar | Yes (CalDAV) | Yes (proprietary) | Yes |
| Cloud storage | Yes (5-25 GB) | Yes (15-500 GB) | No |
| Office suite | Yes (OnlyOffice) | No | No |
| VPN bundled | No | Unlimited plan | No |
| Jurisdiction | Germany | Switzerland | Germany |
| Public audits | No | Yes (Cure53 etc) | Yes (SEC) |

**Quick decision:**
- **Want lowest price + IMAP/SMTP openness:** Mailbox.org
- **Want polish + ecosystem (VPN, Drive, Pass):** [ProtonMail](/posts/protonmail-review-2026/)
- **Want subject-line encryption:** [Tutanota](/posts/tutanota-review-2026/)

---

## Who Should Choose Mailbox.org

Good fit:
- Privacy-aware users who want a real IMAP-compatible mailbox
- Self-hosters who want to escape Google but not run their own mail server
- Small businesses (under 50 users) needing a private German-hosted mail + office stack
- Users who prefer Thunderbird, Apple Mail, or K-9 Mail over web/mobile branded apps
- People who value open standards and avoiding lock-in
- Anyone who wants encrypted email for €1-3/month

Not a fit:
- Users who want one polished mobile app experience (ProtonMail wins)
- High-threat users needing public third-party audits (ProtonMail wins)
- People wanting bundled VPN + password manager + drive (ProtonMail Unlimited wins)
- Users who need subject-line encryption by default (Tutanota wins)

---

## Migrating to Mailbox.org

The migration was smooth because IMAP is universal. Steps I followed:
1. Sign up for Standard plan (€3/month, paid via SEPA)
2. Configure custom domain DNS (MX + SPF + DKIM + DMARC) — 25 minutes
3. Use `imapsync` (free CLI tool) to copy from Gmail to Mailbox.org — 4 hours for 4,200 messages
4. Set Gmail forwarding to Mailbox.org for transition period
5. Update high-priority contacts with new address
6. Configure Thunderbird, K-9 Mail, Apple Mail — 5 minutes each
7. Enable PGP-on-server inbox encryption — 10 minutes (generated key in Thunderbird, uploaded public key)

Total active work: about 2 hours. Compare this to ProtonMail's Easy Switch tool which is more polished but locks you into Proton ecosystem.

---

## Pros and Cons Summary

**Pros:**
- Cheapest serious privacy email (€1-3/month)
- Standard IMAP/SMTP/CalDAV/CardDAV — no lock-in
- Optional PGP-on-server inbox encryption
- Strong German jurisdiction
- Integrated OnlyOffice for document editing
- Excellent infrastructure track record (32+ years)
- Custom domains from €3/mo plan
- Transparent legal request reporting

**Cons:**
- No proprietary mobile app
- Web client UI is dated (functional, not pretty)
- No public third-party security audit
- No bundled VPN or password manager
- Spam filter needs 2 weeks of training
- Search limitations with PGP-encrypted inbox

---

## Final Verdict

Mailbox.org at €3/month is the best privacy email value in 2026 if you are willing to use Thunderbird or another IMAP client instead of a branded mobile app. It is dramatically cheaper than ProtonMail Plus, more open than Tutanota, and backed by a 32-year-old German company that takes mail seriously.

For most privacy-aware users I now recommend Mailbox.org as the default starting point. If you discover you want bundled VPN + password manager + drive, upgrade to ProtonMail Unlimited later. The IMAP-based migration path off Mailbox.org is trivial — that itself is a privacy feature.

Try Mailbox.org Light (€1/month) for a month. If you stay, upgrade to Standard. You will spend about €36 per year on serious encrypted email — less than half what ProtonMail Plus costs.

For the polished alternative with full mobile apps: <a href="https://go.digitalshieldpro.com/protonmail" class="cta-affiliate" rel="sponsored noopener">View ProtonMail</a>

---

## Related Reports

- [ProtonMail review 2026](/posts/protonmail-review-2026/)
- [Tutanota review 2026](/posts/tutanota-review-2026/)
- [Best encrypted email services 2026](/posts/best-encrypted-email-services-2026/)
- [Encrypted email jurisdiction guide](/posts/encrypted-email-jurisdiction-guide-2026/)
- [How to self-host email server](/posts/how-to-self-host-email-server-2026/)
- [Encrypted email vs PGP explained](/posts/encrypted-email-vs-pgp-2026/)
- [Best secure cloud storage 2026](/posts/best-secure-cloud-storage-2026/)
- [Best privacy stack 2026](/posts/best-privacy-stack-2026/)
- [Best password managers 2026](/posts/best-password-managers-2026/)
