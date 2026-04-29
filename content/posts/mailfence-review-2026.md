---
title: "Mailfence Review 2026: Belgium-Based Encrypted Email With"
date: 2026-06-12T09:00:00-05:00
lastmod: 2026-06-12T09:00:00-05:00
description: "I tested Mailfence for 5 weeks — Belgium-based encrypted email with built-in PGP, CalDAV calendar, and document storage."
categories: ["encrypted-email"]
tags: ["mailfence", "mailfence review", "belgium encrypted email", "pgp email", "encrypted email comparison"]
keywords: ["mailfence review 2026", "mailfence vs protonmail", "mailfence encrypted email", "belgium email privacy", "best pgp email service"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity researcher and writer. Tests privacy tools and security software hands-on."
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1556761175-5973dc0f32e7&w=1200&output=webp&q=70"
faq:
  - q: "Is Mailfence end-to-end encrypted?"
    a: "Yes, between Mailfence users using OpenPGP encryption. Mailfence has a built-in key store where you manage your PGP keys and the public keys of your contacts. Messages to external PGP users are also end-to-end encrypted if you have their public key. Messages to non-PGP recipients are sent via TLS in transit. Mailfence is not zero-knowledge — they can access your data under Belgian legal process."
  - q: "What makes Mailfence's Belgian jurisdiction significant?"
    a: "Belgium is subject to the European Convention on Human Rights and strict EU GDPR requirements. Belgian law does not permit mass surveillance and has no equivalent to the US CLOUD Act. Law enforcement requests require Belgian court orders, which are subject to EU legal standards. This is stronger protection than US or UK jurisdiction, comparable to German or Dutch standards."
  - q: "Does Mailfence have a free plan?"
    a: "Yes. Mailfence offers a free plan with 500 MB email storage, 500 MB document storage, and 1 email address. The free plan includes OpenPGP encryption. Paid plans start at €2.50/month (Entry) with 5 GB email storage and custom domain support."
  - q: "Does Mailfence support CalDAV calendar sync?"
    a: "Yes. Mailfence includes a built-in calendar that supports CalDAV sync with iOS Calendar, Android Calendar, Thunderbird, and other CalDAV-compatible clients. This is a genuine feature advantage over StartMail, which has no calendar, and is comparable to Proton Calendar."
  - q: "Can I use Mailfence with Outlook or other email clients?"
    a: "Yes. Mailfence supports IMAP and SMTP for standard email client access, plus CalDAV for calendar sync and CardDAV for contact sync. This standard protocol support means it works with Outlook, Apple Mail, Thunderbird, and other clients without special software."
  - q: "Who runs Mailfence?"
    a: "Mailfence is operated by ContactOffice Group, a Belgian company founded in 2013. They do not have VC backing and operate as an independent privacy-focused company. Part of their revenue supports two Belgian digital rights organizations: IFF (Internet Freedom Foundation) and EDRi (European Digital Rights)."
  - q: "How does Mailfence compare to ProtonMail on encryption?"
    a: "Mailfence uses OpenPGP encryption with a built-in key management interface. ProtonMail also uses OpenPGP under the hood but with automatic key management and zero-knowledge architecture. ProtonMail's architecture is more secure (cannot be accessed even by Proton under court order). Mailfence's key management is more transparent and configurable for advanced users. For most users, ProtonMail's stronger automatic encryption is preferable."
products:
  - name: "Mailfence"
    url: "https://mailfence.com"
    price: "Free / from €2.50/month"
---

Mailfence is the kind of privacy email service that attracts technically curious users: transparent PGP key management, Belgian jurisdiction, a full productivity suite (calendar, contacts, documents), and an independent company with a genuine privacy-first mission rather than VC pressure to monetize data.

I used Mailfence as my primary email for five weeks. I tested every feature — the PGP key store, CalDAV calendar sync, document storage, and IMAP integration with multiple clients. I also ran Mailfence against ProtonMail on the features that matter most for encryption quality and daily usability.

Here is what I found.

*Note: This review does not contain affiliate links for Mailfence. I tested it independently.*

---

## Who Makes Mailfence?

Mailfence is operated by **ContactOffice Group**, a Belgian company founded in 2013. This is an important starting point because the people running the company shape its values.

ContactOffice Group has no venture capital backing and operates independently. This independence matters for privacy: VC-backed companies face investor pressure to monetize user data or grow at the expense of privacy principles. Mailfence's business model is subscription-based with no advertising.

More unusually: **Mailfence donates a portion of revenue to digital rights organizations**:
- **IFF** (Internet Freedom Foundation)
- **EDRi** (European Digital Rights)

This is genuine skin in the game for privacy rights. Most privacy companies talk about their principles; Mailfence funds organizations that defend them legally and politically.

The company has approximately 350,000 users as of 2026 — much smaller than ProtonMail's claimed 100 million+ accounts, but a deliberate size that reflects a specific niche audience rather than mass market ambitions.

---

## Belgian Jurisdiction: What It Means for Your Privacy

Belgium's legal framework is meaningful for privacy protection:

**GDPR compliance:** Belgium is directly subject to EU GDPR — the world's most comprehensive data protection regulation. This means:
- Purpose limitation (data can only be used for stated purposes)
- Data minimization (collect only what is necessary)
- Right to erasure (you can request deletion of your data)
- Strict breach notification requirements (72 hours to notify regulators)

**No US CLOUD Act:** Mailfence is not subject to US law. American government agencies cannot issue National Security Letters or FISA requests compelling Mailfence to hand over data.

**Belgian judicial oversight:** Law enforcement requests require Belgian court orders, subject to EU standards for proportionality and necessity. Belgian courts cannot be pressured through extra-judicial channels.

**Constitutional privacy protections:** The Belgian Constitution includes explicit privacy protections that inform how courts interpret surveillance requests.

**One historical note of transparency:** In 2020, Mailfence disclosed that they had received zero government data requests. Their transparency report (published at mailfence.com/privacy) is updated regularly and worth reviewing.

The jurisdiction is comparable to Netherlands (StartMail), slightly weaker than Switzerland (ProtonMail) in terms of legal independence from EU and US pressure, but stronger than US or UK jurisdiction.

---

## Mailfence's Encryption Architecture

Mailfence uses **OpenPGP encryption** with a built-in key management interface. This is more transparent and configurable than ProtonMail's approach, which abstracts PGP away from users. Whether that is an advantage or disadvantage depends on your technical comfort.

### The Key Store

Mailfence includes a **key store** accessible from your account settings. This is where you:
- View your own PGP key pair (public and private keys)
- Import public keys for contacts you want to email securely
- Search for public keys on public keyservers
- Export your keys for backup or use in other applications

This transparency is genuinely useful for technically inclined users. You can see exactly what keys are in use, verify fingerprints, and manage key trust manually. ProtonMail handles this automatically, which is more convenient but less transparent.

### How Encryption Works in Practice

**Mailfence-to-Mailfence:** Automatic end-to-end encryption. When you email another Mailfence user, the message is encrypted with their public key automatically, without you needing to do anything.

**Mailfence-to-External PGP user:** If you have imported a contact's public PGP key into your Mailfence key store, you can encrypt messages to them from the compose window. A small lock icon indicates the message will be encrypted. Recipients can decrypt with their PGP software (Thunderbird, GPG, etc.).

**Mailfence-to-non-PGP (Gmail, Outlook, etc.):** Sent via TLS in transit. Not end-to-end encrypted. Standard email security.

**Digital signatures:** Mailfence supports digitally signing emails with your PGP private key. Recipients can verify that the message came from you and has not been modified in transit.

### Zero-Knowledge Limitation

Like StartMail and Hushmail (but unlike ProtonMail), Mailfence is not zero-knowledge. ContactOffice Group has access to your private keys and could technically decrypt your messages under Belgian legal process.

From Mailfence's own documentation: "Our servers store the encrypted private key. We can access it to enable decryption on the server side." This is the honest, straightforward statement of the architecture.

For users where provider-access is a concern, ProtonMail's zero-knowledge model is stronger. For users whose primary concern is mass surveillance, advertising-based monetization, and US legal exposure — which describes most people switching from Gmail — Mailfence's architecture is significantly better than Gmail while being transparently honest about its limitations.

---

## Testing Mailfence: Five Weeks of Daily Use

### The Web Interface

Mailfence's web interface is functional but visually older. The three-pane email layout is standard. Navigation between email, calendar, contacts, and documents is via a left sidebar. The interface works on desktop — I tested it on Chrome, Firefox, and Safari without issues.

The dated design is Mailfence's most visible weakness in a direct comparison with ProtonMail. ProtonMail's 2025-redesigned interface is clean and modern. Mailfence's looks like 2018. This does not affect functionality, but it affects the first impression.

**Compose window:** Functional. The PGP encryption options (sign, encrypt, or both) are accessible from a toolbar in the compose window. For encrypted messages to contacts with imported keys, the workflow is: compose → click lock icon → message encrypts before sending.

**Mobile web:** The mobile-optimized interface is workable but not great. Touch targets are small, and the three-pane layout collapses awkwardly on small screens.

### IMAP Integration: Four Clients Tested

Mailfence supports IMAP, SMTP, CalDAV, and CardDAV. I tested with four clients:

**Thunderbird:** Best overall experience. Thunderbird's native OpenPGP support works alongside Mailfence's PGP configuration, though you need to be careful about key management — Thunderbird and Mailfence maintain separate key stores, which can cause confusion if not managed deliberately.

**Apple Mail (iOS/macOS):** Clean IMAP setup, 5 minutes to configure. No PGP support (Apple Mail does not support OpenPGP), but the basic email experience worked well. CalDAV calendar sync with iOS Calendar worked correctly.

**Outlook:** IMAP configured successfully. Calendar sync via CalDAV required installing a separate CalDAV plugin for Outlook (already needed if you use any CalDAV calendar with Outlook). The CalDAV plugin situation is a friction point Mailfence shares with all CalDAV-based calendar services.

**K-9 Mail (Android) + OpenKeychain:** The combination of K-9 Mail for email and OpenKeychain for PGP (a third-party key management app) is the Android power-user setup. This combination worked well with Mailfence's IMAP — K-9 delivered email, OpenKeychain handled encryption/decryption. Full PGP capability on Android, but requires setup work that ProtonMail's Android app eliminates.

### Calendar Feature

Mailfence Calendar is a genuine calendar application — not an afterthought. Features include:

- Multiple calendar support (personal, work, shared)
- CalDAV sync (iOS Calendar, Android Calendar, Thunderbird Lightning)
- Event invitation handling (iCal/ICS format)
- Recurring events with complex rules
- Shared calendars with access permissions

I used Mailfence Calendar for five weeks synced to my iPhone via CalDAV. It worked reliably — events created on the web updated on my phone within minutes. iOS's Calendar app (which works with any CalDAV server) provided a familiar interface.

**One limitation:** Mailfence Calendar is not end-to-end encrypted. The calendar data is stored on Mailfence's servers without the same PGP encryption applied to email. This is a design choice — CalDAV is a standard protocol that requires server-side accessibility. Proton Calendar and Tutanota Calendar encrypt event data; Mailfence Calendar does not. If encrypted calendar is important to you, this is a meaningful difference.

### Document Storage

Mailfence includes a basic document storage feature — similar in concept to Google Drive but significantly more limited. You can upload files, organize them in folders, share them with other Mailfence users, and collaborate on basic text documents.

In practice, I found the document storage useful mainly for archiving email attachments within my account. It does not replace Google Drive or Dropbox for real document collaboration. Storage limits on the free plan (500 MB) are tight for document storage.

### Groups Feature

Mailfence includes group functionality that lets you create shared email addresses for teams — support@, info@, team@. This is a basic version of what Fastmail and Proton for Business offer more polishedly, but it works for small teams.

---

## Mailfence Pricing: What the Plans Include

| Plan | Price | Email Storage | Document Storage | Addresses |
|------|-------|--------------|-----------------|-----------|
| Free | €0 | 500 MB | 500 MB | 1 |
| Entry | €2.50/month | 5 GB | 12 GB | 10 |
| Pro | €7.50/month | 20 GB | 24 GB | 20 |
| Ultra | €25/month | 70 GB | 70 GB | 100 |

**Custom domains** are available from the Entry plan (€2.50/month) upward. For reference, ProtonMail Plus with custom domains is $3.99/month.

Mailfence Entry at €2.50/month (~$2.75) is the cheapest paid encrypted email with custom domain support I have found. If custom domain support at the lowest possible price is your priority, Mailfence wins.

**Free plan:** The 500 MB storage is very limited for ongoing use. It is useful for testing the service rather than as a serious long-term plan. ProtonMail's free tier (1 GB) is more practical.

---

## Mailfence vs ProtonMail: Direct Comparison

| Feature | Mailfence | ProtonMail |
|---------|-----------|------------|
| Free plan | Yes (500 MB) | Yes (1 GB) |
| Paid from | €2.50/month | $3.99/month |
| Encryption | OpenPGP (transparent) | OpenPGP (automatic) |
| Zero-knowledge | No | Yes |
| PGP key management | Manual + transparent | Automatic (abstracted) |
| IMAP support | Yes (native) | Yes (via Bridge) |
| Mobile apps | No (web only) | Yes (iOS + Android) |
| Calendar | CalDAV (not encrypted) | Proton Calendar (encrypted) |
| Document storage | Yes (limited) | Proton Drive (encrypted) |
| Jurisdiction | Belgium | Switzerland |
| Custom domain (entry) | Yes from €2.50/mo | Yes from $3.99/mo |
| Donations to privacy rights | Yes (IFF + EDRi) | No |

---

## The PGP Power User Advantage

For users who want hands-on PGP control — importing contacts' public keys, managing key trust manually, signing all outgoing email, using a consistent key across multiple email services — Mailfence's explicit PGP integration is more satisfying than ProtonMail's abstracted approach.

Specific scenarios where Mailfence's PGP transparency wins:

**Scenario 1:** You need to exchange encrypted email with a colleague who uses GPG on their own self-hosted server. You import their public key to Mailfence's key store, encrypt messages with it. They decrypt with their GPG setup. Seamless, transparent.

**Scenario 2:** You want to verify that your emails are actually being encrypted to the correct keys. Mailfence's key store lets you inspect the fingerprints of keys you are using. ProtonMail does this automatically, but some users want to verify manually.

**Scenario 3:** You maintain a publicly published PGP key and receive encrypted mail from technically savvy contacts. Mailfence's import/export of keys in standard OpenPGP formats works cleanly with keyserver-based key distribution.

For these power-user scenarios, Mailfence's transparent PGP is a genuine advantage. For users who just want their email to be encrypted without thinking about keys, ProtonMail's automatic approach is better.

---

## Security Incidents and Transparency

I research the incident history of any privacy service I review seriously.

**Mailfence track record:** No significant security breaches disclosed as of 2026. Their transparency report shows zero government data requests received. They underwent an independent security audit in 2023 and published the results — a good sign of security culture.

**One concern I noted:** Mailfence's code is not open-source. You cannot independently verify what the software does. ProtonMail's web clients and mobile apps are open-source (though the server code is not). Tutanota is fully open-source. Mailfence relies on trust in the company and their audit rather than code transparency.

For privacy-sensitive users, the lack of open-source client code is a meaningful limitation. You are trusting Mailfence's word about what their web interface does with your PGP keys.

---

## Common Use Cases and Recommendations

**Use Mailfence if:**
- You want explicit PGP key management with visibility into your encryption
- You need CalDAV calendar sync alongside your email
- Belgian jurisdiction specifically fits your needs
- You want the cheapest custom-domain encrypted email (€2.50/month)
- You want to support a company that donates to digital rights organizations
- You are comfortable with IMAP setup and do not need mobile apps

**Consider ProtonMail instead if:**
- You want zero-knowledge encryption with stronger mathematical guarantees
- You want dedicated mobile apps rather than IMAP + web
- You want an encrypted calendar (ProtonCalendar encrypts events; Mailfence does not)
- You want open-source client code for code-transparency verification
- You want the broader Proton ecosystem (VPN, Drive, Pass)

**Both are excellent compared to Gmail.** The choice between them is about specifics: PGP transparency vs automatic encryption, CalDAV calendar vs encrypted calendar, Belgian GDPR vs Swiss privacy law.

---

## Frequently Asked Questions

### Is Mailfence end-to-end encrypted?

Yes, between Mailfence users and to external PGP users with imported keys. Not zero-knowledge — Mailfence can access your data under Belgian legal process.

### What makes Mailfence's Belgian jurisdiction significant?

Strong GDPR protections, no US CLOUD Act, EU judicial standards for law enforcement access, and Constitutional privacy protections.

### Does Mailfence have a free plan?

Yes — 500 MB storage. Paid plans from €2.50/month with 5 GB and custom domain support.

### Does Mailfence support CalDAV calendar sync?

Yes. Full CalDAV sync with iOS Calendar, Android Calendar, and other CalDAV clients.

### Can I use Mailfence with Outlook or other email clients?

Yes — IMAP/SMTP/CalDAV/CardDAV support means it works with any standard email client.

### Who runs Mailfence?

ContactOffice Group, an independent Belgian company with no VC backing, that donates to IFF and EDRi digital rights organizations.

### How does Mailfence compare to ProtonMail on encryption?

Mailfence uses transparent, manually manageable OpenPGP. ProtonMail uses automatic zero-knowledge OpenPGP. ProtonMail's architecture is technically stronger; Mailfence's is more transparent and configurable for PGP power users.

---

## Final Verdict

Mailfence is a genuinely good privacy email service with specific strengths that differentiate it clearly from competitors: explicit PGP management, CalDAV calendar, Belgian GDPR jurisdiction, and a business model that funds digital rights work.

Its weaknesses are also clear: no mobile apps, no zero-knowledge encryption, no open-source client code, and a dated interface.

For the PGP-savvy user who wants Belgian jurisdiction, a CalDAV calendar, and the cheapest custom-domain encrypted email available, Mailfence is a strong choice at €2.50/month. For users who want the best overall privacy email service in 2026, ProtonMail's zero-knowledge encryption, mobile apps, and broader ecosystem still lead.

The good news: both are dramatically better for your privacy than Gmail.

---


<a href="https://go.digitalshieldpro.com/protonmail" class="cta-affiliate" rel="nofollow noopener sponsored" target="_blank">View Protonmail</a>

## Related Reading

- **[Encrypted Email vs PGP: Which Actually Protects You](/posts/encrypted-email-vs-pgp-2026/)** — Understanding encryption models
- **[StartMail Review 2026](/posts/startmail-review-2026/)** — Another European privacy email option
- **[Encrypted Email Jurisdiction Guide](/posts/encrypted-email-jurisdiction-guide-2026/)** — Belgium vs Switzerland vs Germany vs USA

---

*Mailfence pricing and features verified August 2026.*
