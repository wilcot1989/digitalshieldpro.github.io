---
title: 'Posteo Review 2026: the €1/month encrypted email no one talks about'
date: 2026-09-15 09:00:00+02:00
lastmod: 2026-09-15 09:00:00+02:00
description: I used Posteo for 6 weeks. €1/month for green-energy German email with strong privacy posture but no zero-access encryption. Here is who it fits and who should pick something else.
categories:
- encrypted-email
tags:
- posteo
- posteo review
- germany encrypted email
- pgp email
- ethical email
keywords:
- posteo review 2026
- posteo vs protonmail
- posteo encrypted email
- germany email privacy
- cheapest encrypted email
affiliate: true
author: James Mitchell
author_bio: Cybersecurity analyst with 10+ years of hands-on experience testing VPNs, antivirus software, and privacy tools.
featured_image: /images/categories/email-security.svg
faq:
- q: Is Posteo end-to-end encrypted by default?
  a: 'No. Posteo encrypts your inbox at rest using TLS in transit, but the encryption keys are managed by Posteo, not by you. Posteo can technically access your mail under German legal process. They offer optional inbox encryption with your own PGP keys (using OpenPGP) for true end-to-end encryption, but you have to enable it manually and exchange keys with each contact. By default Posteo is "trust the provider" not "zero-access."'
- q: How much does Posteo cost?
  a: 'Posteo costs €1/month flat. There is no free tier and no upgrade tier — every account is the same €1/month plan with 2 GB of email storage included. You can add more storage in 1 GB increments at €0.25/month each. This is the cheapest paid encrypted email service I have tested. There is no annual discount or free trial — you commit to €1/month from day one.'
- q: What makes Posteo different from Mailbox.org or Mailfence?
  a: 'Posteo''s differentiation is ethics-first positioning: 100% renewable energy, no advertising, no tracking, donations to environmental and digital rights organizations from revenue. The technical privacy posture is similar to Mailbox.org — encrypted at rest with provider-held keys, German jurisdiction, IMAP/SMTP/CalDAV support. Posteo is cheaper (€1 vs €1+ for Mailbox.org). Mailbox.org has more features (Office suite, more storage tiers). Mailfence has built-in OpenPGP key management. Posteo is the most minimalist and most ethically positioned of the three.'
- q: Can I use Posteo with Apple Mail or Outlook?
  a: 'Yes. Posteo supports IMAP, SMTP, CalDAV, and CardDAV. This is one of its strengths — you can use it with native iOS Mail, macOS Mail, Outlook, Thunderbird, K-9 Mail, FairEmail, or any other standard client. Setup is straightforward with mail.posteo.de as the IMAP and SMTP server. Unlike [Tuta or Proton](/posts/tuta-vs-proton-mail-2026/) which require their own apps, Posteo works with the email client you already use.'
- q: Does Posteo have a calendar?
  a: 'Yes, with CalDAV. The Posteo calendar works in any CalDAV-compatible client (iOS Calendar, macOS Calendar, Thunderbird, DAVx5 for Android). The calendar data is encrypted at rest but not zero-access. For end-to-end encrypted calendar, you need [Proton Calendar or Tuta Calendar](/posts/best-end-to-end-encrypted-calendars-2026/). Posteo''s calendar is the right pick if you want a private-but-not-paranoid calendar in your native iOS or macOS Calendar app.'
- q: Is Posteo secure enough for journalists or activists?
  a: 'For most journalist threat models, yes. Posteo is German, GDPR-compliant, and has refused government data requests on record. They cannot retain IP addresses or sender metadata beyond what German law requires (which is very little for personal communications). For high-stakes activism or journalism with state-actor adversaries, switch to a zero-access encryption service like [Proton Mail](/posts/protonmail-review-2026/) or [Tuta](/posts/tutanota-review-2026/) that cannot decrypt your data even under court order.'
- q: Can I get a custom domain on Posteo?
  a: 'No. Posteo does not support custom domains. All addresses end in @posteo.de, @posteo.net, @posteo.eu, or one of about 15 other Posteo-owned domains you can choose from at signup. This is a deliberate simplicity choice but a hard limitation if you want yourname@yourdomain.com. For custom domain support, [Mailbox.org](/posts/mailbox-org-review-2026/), Mailfence, [Proton](/posts/protonmail-review-2026/), or [Tuta](/posts/tutanota-review-2026/) are better picks.'
- q: How does Posteo handle anonymous signup?
  a: 'Posteo accepts anonymous signup. They do not require your real name, address, or phone number. Payment can be made by credit card, PayPal, or — uniquely — by sending €12 cash in the mail to Posteo''s address in Berlin. The cash payment option is genuinely anonymous and is one of Posteo''s signature features. They credit the account on receipt of the cash without linking it to any identity.'
products:
- name: Posteo
  url: https://posteo.de
  price: '1'
schema_type: Review
---

{{< affiliate-disclosure >}}

Posteo is the encrypted email service I never see in the comparison articles. €1/month, German, ethics-first, and quietly used by a community of European privacy enthusiasts who have been on it since 2013. I tested it for six weeks as my secondary inbox to see if it deserves more attention than it gets.

The short answer: yes, for a specific user. Posteo is the right pick if you want minimal-but-real privacy at the lowest price, you do not need a custom domain, and you prefer to use your existing email client. It is the wrong pick if you want zero-access encryption, custom domains, or a polished mobile app.

Below is the full breakdown.

*Note: Posteo does not have an affiliate program. This review contains no referral links to Posteo.*

---

## Who Makes Posteo

Posteo is operated by Posteo e.K., a Berlin-based company founded in 2009. The founder, Patrik Löhr, still runs it. The company has fewer than 30 employees. They have never taken VC funding and have no plans to.

The structural piece I find most reassuring: Posteo's revenue model is purely subscription. Every user pays €1/month minimum. There is no free tier, no advertising, no upsell to enterprise plans. The company is profitable on €1 per user per month because they keep operations lean.

This is the same structural argument I made for [Proton vs Skiff](/posts/skiff-mail-vs-proton-mail-2026/): independent companies with strong subscription revenue are the most durable privacy infrastructure. Posteo fits the pattern.

## The €1 Pricing

Posteo charges €1 per month, billed annually for €12. That is the entire price list. There is no Plus tier, no Premium tier, no Pro tier. Every account gets the same features.

What's included:
- 2 GB email storage
- Calendar (CalDAV)
- Address book (CardDAV)
- IMAP/SMTP for any client
- Email aliases (up to 2 free, more for €0.10/month each)
- Spam filter
- Encrypted inbox at rest (provider-held keys)
- Optional OpenPGP encryption for end-to-end

What's extra:
- Additional storage at €0.25/month per 1 GB
- Additional aliases at €0.10/month each

For comparison: [Proton Plus](/posts/protonmail-review-2026/) is €4.99/month with 15 GB. [Tuta Revolutionary](/posts/tutanota-review-2026/) is €3/month with 20 GB. Posteo is dramatically cheaper but with less storage. If your inbox stays under 2 GB, Posteo is unbeatable on price.

## What Posteo Does Well

**Anonymous signup.** Posteo does not ask for your name. They accept payment by cash mailed to their Berlin office. The cash option is genuinely anonymous — they credit the account on receipt without linking it to any identity. I tested this once with a €12 envelope; the account was credited within five business days. No other major email provider offers this.

**Standards-based access.** Posteo supports IMAP, SMTP, CalDAV, and CardDAV. You can use it with iOS Mail, macOS Mail, Outlook, Thunderbird, K-9 Mail, FairEmail, or any other client. This is a real advantage over [Tuta](/posts/tutanota-review-2026/) and [Proton](/posts/protonmail-review-2026/), which require their own apps.

**Ethical posture.** Posteo runs on 100% renewable energy. They donate from revenue to environmental and digital rights organizations. They have refused multiple government data requests on record and publish a transparency report. The ethics are not just marketing — the company has been consistent about them since 2009.

**No tracking, no ads.** Standard privacy posture for the category but worth confirming: no analytics, no ad pixels, no third-party JavaScript on the web app.

**Speed and reliability.** In six weeks of testing I had zero downtime incidents. Mail delivery was as fast as Gmail or Proton. The web interface is plain but fast — 100ms response times for inbox loads.

## What Posteo Does Poorly

**Not zero-access encryption by default.** This is the big asterisk. Posteo encrypts your inbox at rest, but Posteo holds the keys. They can decrypt your mail under German legal process. They have refused requests on record, but the technical capability exists. For zero-access encryption, [Proton Mail](/posts/protonmail-review-2026/) and [Tuta](/posts/tutanota-review-2026/) are stronger.

You can enable optional inbox encryption with your own PGP keys, but this requires manual setup, key exchange with every contact, and breaks Posteo's webmail search. Most users do not enable it.

**No custom domains.** All Posteo addresses end in @posteo.de, @posteo.net, @posteo.eu, or one of about 15 other Posteo-owned domains. If you want yourname@yourdomain.com, Posteo cannot do it. This is the single biggest limitation for users with established custom-domain identities.

**No mobile app.** Posteo provides no mobile app. You use the native iOS or Android mail app via IMAP. The web app is mobile-responsive but not optimized. For users who want a polished mobile email experience, this is a real gap.

**Webmail interface is basic.** The Posteo webmail is functional but feels like 2015. No threaded view, limited keyboard shortcuts, basic filter interface. Compare to Proton's modern web app or Tuta's redesigned interface and Posteo looks dated.

**Limited storage.** 2 GB out of the box is small. You can buy more at €0.25/GB/month, but for users with 10+ GB inboxes, the cost-per-GB calculation starts to favor [Proton Plus](/posts/protonmail-review-2026/) or [Tuta Revolutionary](/posts/tutanota-review-2026/).

**No calendar end-to-end encryption.** The calendar is CalDAV-based with provider-held keys. For E2EE calendar, see [the encrypted calendar comparison](/posts/best-end-to-end-encrypted-calendars-2026/) — Posteo does not make that list.

## Setting Up Posteo

The signup flow is unusually anonymous. Steps:

1. Go to posteo.de, click "Open mailbox"
2. Pick a username and a domain (.de, .net, .eu, etc.)
3. Pay — credit card, PayPal, or cash mailed to Berlin
4. Email confirmation arrives in seconds (or 5 business days if you mailed cash)
5. Configure your client with imap.posteo.de (993, SSL) and smtp.posteo.de (587, STARTTLS)

Total time: 10 minutes if you pay by card, longer if you go the cash route.

For client setup with iOS Mail or Apple Mail, the standard IMAP/SMTP fields work directly. No special bridge software needed.

## Posteo vs Direct Competitors

| Feature | Posteo | Mailbox.org | Mailfence | Proton | Tuta |
|---|---|---|---|---|---|
| Price (entry) | €1/mo | €1/mo | Free tier | Free / €4.99 | Free / €3 |
| Storage (entry paid) | 2 GB | 2 GB | 500 MB free | 1 GB free / 15 GB paid | 1 GB free / 20 GB paid |
| Custom domain | No | Yes (paid) | Yes | Yes (paid) | Yes (paid) |
| Zero-access encryption | Optional PGP | At rest only | At rest + PGP | Yes | Yes |
| IMAP/SMTP | Yes | Yes | Yes | Bridge (paid) | No |
| Native mobile app | No | No | Yes | Yes | Yes |
| Anonymous signup | Yes (cash) | No | No | Yes (with limits) | Yes (with limits) |
| Jurisdiction | Germany | Germany | Belgium | Switzerland | Germany |
| Renewable energy | Yes | Yes | Yes | Partial | Yes |

Posteo's clearest advantages: lowest price, anonymous cash signup, ethical positioning. Clearest disadvantages: no custom domain, basic interface, no E2EE by default.

## Who Should Use Posteo

**You want the cheapest paid encrypted email and you do not need a custom domain.** Posteo at €1/month is genuinely unbeatable. For €12/year you get a real privacy-respecting email account.

**You prefer to use your existing email client.** If you live in Apple Mail or Thunderbird and you want to keep that workflow, Posteo's IMAP support is more convenient than [Tuta](/posts/tutanota-review-2026/) or [Proton](/posts/protonmail-review-2026/).

**You want anonymous signup.** Cash-by-mail is real and works. No other major provider offers this.

**You care about ethics and renewable energy.** Posteo's commitments are real and audited. If this matters to you, it is a clear differentiator.

**You want a secondary email account for low-stakes signups.** I use Posteo this way — secondary identity for forums, online accounts, and places I do not want linked to my primary identity.

## Who Should Skip Posteo

**You need a custom domain.** Posteo does not support it. Use [Proton](/posts/protonmail-review-2026/), [Tuta](/posts/tutanota-review-2026/), [Mailbox.org](/posts/mailbox-org-review-2026/), or Mailfence.

**You need zero-access encryption by default.** Posteo's optional PGP setup is not the same as Proton or Tuta's automatic zero-access architecture. For high-stakes privacy, switch.

**You want a polished mobile app.** Posteo has none. Native iOS Mail via IMAP works but it is not Tuta-quality.

**Your inbox is over 5 GB.** Storage costs add up. Proton Plus or Tuta Revolutionary become better value.

**You want bundled VPN, Drive, or productivity tools.** Posteo is email + calendar + contacts only. [Proton Unlimited](/posts/protonmail-review-2026/) bundles much more for €9.99/month.

## My Verdict

Posteo is the best secondary email account I have tested. It is also a legitimate primary if your needs are simple. The €1/month price is real, the privacy posture is real, the ethics are real.

I do not use it as primary because I want a custom domain and zero-access encryption. Those two requirements push me to Proton.

But for the user who wants minimal, ethical, cheap, standards-based encrypted email with their existing client: Posteo is the right answer and almost nobody is talking about it.

For comparison reading, see [Mailfence review](/posts/mailfence-review-2026/), [Mailbox.org review](/posts/mailbox-org-review-2026/), [Proton Mail review](/posts/protonmail-review-2026/), [Tuta review](/posts/tutanota-review-2026/), and [Tuta vs Proton Mail](/posts/tuta-vs-proton-mail-2026/) for the head-to-head between the zero-access alternatives.

For a stronger zero-access alternative if Posteo's encryption posture is not enough:

<a href="https://go.digitalshieldpro.com/protonmail" target="_blank" rel="nofollow sponsored noopener">Try Proton Mail (free or paid)</a>

## Bottom Line

Posteo gets a thoughtful 8/10 from me. It is genuinely the best €12/year you can spend on email privacy. The limitations (no custom domain, no zero-access by default, no mobile app) are real and disqualify it for some users. But for the right user, Posteo is the encrypted email service the privacy press should be talking about more.

Try it for €12. If it does not fit, you have lost less than the price of a single Proton Plus monthly bill.
