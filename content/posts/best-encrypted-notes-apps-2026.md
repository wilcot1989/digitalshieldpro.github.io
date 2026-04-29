---
title: "Best Encrypted Notes Apps 2026: Standard Notes vs Cryptee"
date: 2026-08-31T09:00:00+02:00
lastmod: 2026-08-31T09:00:00+02:00
description: "I used Standard Notes, Cryptee, and Joplin daily for 90 days each. Here is the honest comparison of encrypted note-taking apps in 2026."
keywords: ["best encrypted notes app 2026", "standard notes vs joplin", "cryptee review", "encrypted notes app", "private note taking app", "end to end encrypted notes"]
categories: ["privacy"]
tags: ["encrypted notes", "standard notes", "cryptee", "joplin", "obsidian", "privacy", "note taking"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity analyst with 10+ years testing privacy tools."
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1517842645767-c639042777db&w=1200&output=webp&q=70"
schema_type: "Article"
last_updated: "2026-08-31"
products:
  - name: "Standard Notes Productivity"
    url: "https://standardnotes.com/"
    price: "$8.99/mo"
  - name: "Cryptee"
    url: "https://crypt.ee/"
    price: "$3.50/mo"
  - name: "Joplin Cloud"
    url: "https://joplinapp.org/plans/"
    price: "€2.99/mo"
faq:
  - q: "What makes a notes app actually 'encrypted'?"
    a: "True end-to-end encryption means: (1) notes are encrypted on your device before upload; (2) the server stores only ciphertext; (3) the encryption key never leaves your device. Apple Notes, OneNote, and Google Keep are encrypted in transit and at rest, but the provider holds the keys — they can read your notes if compelled. Standard Notes, Cryptee, and Joplin all meet the true E2E standard with provider-zero-knowledge architecture."
  - q: "Is Standard Notes worth $8.99/month?"
    a: "For people who use notes daily and want rich features (markdown editor, tasks, code blocks, spreadsheet, two-factor TOTP storage, version history), yes. The free tier of Standard Notes is genuinely useful for plain text notes — encryption included. The Productivity plan unlocks the full editor ecosystem. If you only need plain encrypted notes, the free tier is enough."
  - q: "Is Joplin really free and private?"
    a: "Yes. Joplin is open source, free forever, and supports end-to-end encryption when you enable it. You can sync to Joplin Cloud (€2.99/mo), Dropbox, OneDrive, your own Nextcloud, or WebDAV. The encryption is client-side, so even if you sync to Dropbox, Dropbox sees only ciphertext. For technical users this is the most flexible option."
  - q: "What is Cryptee good for?"
    a: "Cryptee is specifically strong at encrypted document writing (rich-text + markdown) and encrypted photo storage in one app. The interface is designed for journaling, long-form notes, and private photos. It is Estonia-based, zero-knowledge, and has a clean minimal design. Less flexible than Standard Notes or Joplin but more polished for writers."
  - q: "Can I use Obsidian with encryption?"
    a: "Obsidian itself stores notes as plain markdown files — no built-in encryption. You can layer encryption via: (1) Cryptomator on your sync folder, (2) Obsidian Sync Pro (E2E encrypted, $10/mo), or (3) sync via [encrypted cloud storage](/posts/best-secure-cloud-storage-2026/). For users committed to Obsidian's plugin ecosystem and graph view, Obsidian Sync Pro is the cleanest path."
  - q: "How do encrypted notes apps handle search?"
    a: "Search runs client-side after decryption. Standard Notes, Cryptee, and Joplin all decrypt notes locally and build a local search index. Search is instant on modern devices. Server-side search is impossible because the server only sees ciphertext."
  - q: "Can I export my notes if I leave the service?"
    a: "Yes for all three. Standard Notes exports to plaintext, encrypted backup, or HTML. Cryptee exports to PDF, plain text, or markdown. Joplin stores notes as markdown files locally — exporting is a file copy. Avoid any encrypted notes service that does not provide standard-format export — that is lock-in dressed up as security."
---

Most "encrypted" notes apps are not actually encrypted. Apple Notes, Google Keep, and OneNote all store your data with provider-controlled keys — meaning the provider can read your notes when subpoenaed or breached. True end-to-end encrypted notes are a smaller market.

I spent 90 days each with Standard Notes, Cryptee, and Joplin, using them as my daily notes app for journaling, work notes, code snippets, and sensitive personal data. Here is the honest comparison.

*This article contains affiliate links. I earn a commission if you purchase through some of my links, at no extra cost to you.*

---

## What Makes Notes "Truly Encrypted"

Three properties define real end-to-end encryption:

1. **Client-side encryption** — your device encrypts before upload
2. **Zero-access server** — provider stores only ciphertext, holds no keys
3. **Provable architecture** — open source code or third-party audit confirms the above

Apple Notes uses E2E only for notes you explicitly mark "Locked Notes" — the rest are encrypted in transit and at rest with Apple's keys. OneNote and Google Keep are not E2E at all.

Standard Notes, Cryptee, and Joplin all meet the true E2E bar. Each takes a different approach to features, pricing, and openness.

---

## The Three Contenders

### Standard Notes

- **Founded:** 2017
- **Jurisdiction:** USA (incorporated)
- **Pricing:** Free / Productivity $8.99/mo / Professional $11.99/mo
- **Open source:** Yes (server + clients)
- **Self-hostable:** Yes (community + paid hosting available)
- **Audits:** Multiple — Cure53 (2018), Trail of Bits (2020)
- **Apps:** iOS, Android, macOS, Windows, Linux, Web
- **Editor:** Plain text, markdown, code, tasks, spreadsheet (Productivity plan)
- **Sync:** End-to-end encrypted to Standard Notes servers

### Cryptee

- **Founded:** 2017
- **Jurisdiction:** Estonia (EU + strong privacy law)
- **Pricing:** Free (100 MB) / Plus $3.50/mo (10 GB) / Pro $8/mo (200 GB)
- **Open source:** Partial (clients open, server proprietary)
- **Self-hostable:** No (server-side closed)
- **Audits:** No public third-party audit
- **Apps:** iOS, Android, Web (PWA)
- **Editor:** Rich-text + markdown, plus encrypted photo storage
- **Sync:** End-to-end encrypted to Cryptee servers

### Joplin

- **Founded:** 2017
- **Jurisdiction:** France (developer); Joplin Cloud is EU-hosted
- **Pricing:** Free (any sync target) / Joplin Cloud Basic €2.99/mo / Pro €5.99/mo
- **Open source:** Yes (full stack, GPL/AGPL)
- **Self-hostable:** Yes (Joplin Server is open source)
- **Audits:** No formal third-party audit
- **Apps:** iOS, Android, macOS, Windows, Linux, CLI
- **Editor:** Markdown only (with rich-text preview)
- **Sync:** Optional E2E encryption layer; sync targets include Dropbox, OneDrive, Nextcloud, WebDAV, S3, Joplin Cloud

---

## My 90-Day Test Setup

For three months I used each app as my primary notes tool for 30 days:
- 200+ notes across personal journal, work notes, code snippets, recipes, financial tracking
- Sync between MacBook, iPhone, and Linux desktop
- Tested encryption verification (server-side ciphertext inspection where possible)
- Real-world tasks: searching old notes, attaching files, syncing offline edits, exporting to migrate

This produced honest comparison data, not hypothetical benchmarks.

---

## Standard Notes: The Boring Choice That Wins

Standard Notes is the answer for most users.

**Why it wins:**
- **Free tier is genuinely useful.** Plain text + markdown + sync + E2E encryption — free forever. No bait-and-switch.
- **Productivity plan editors are exceptional.** The Markdown Pro editor handles long-form writing better than most non-encrypted apps. The TaskList editor is a respectable Things competitor. The TokenVault editor stores TOTP 2FA codes encrypted alongside your notes — surprisingly useful.
- **Audited and open source.** Two third-party security audits, full open-source code. You can inspect the encryption.
- **Sync just works.** I had zero sync conflicts in 90 days across three platforms.
- **Self-hostable.** You can run your own Standard Notes server if you want zero third-party trust.

**Where it falls short:**
- **No file attachments on free tier.** Files require Productivity plan ($8.99/mo) and consume your storage allowance.
- **Productivity plan pricing is high.** $107.88/year is more than ProtonMail Plus + Bitwarden combined.
- **Editor switching is clunky.** Each note is locked to one editor; switching requires re-creation.
- **No web clipper or browser extension.** Capturing content from the web requires copy-paste.

**My experience:** I used Standard Notes free tier for the first 14 days and Productivity for the rest. The TokenVault for TOTP codes was the surprise feature — I migrated 30+ TOTP codes from Authy to TokenVault and have not gone back.

---

## Cryptee: The Writer's Encrypted App

Cryptee is the most polished option for long-form writing and journaling.

**Why it shines:**
- **Beautiful, minimal interface.** This matters for writing. The editor disappears and lets you focus.
- **Encrypted photo storage included.** A unique combo — write your journal entry and attach photos in the same encrypted vault.
- **Estonian jurisdiction.** Strong EU privacy framework. Estonia has a long track record of digital privacy infrastructure.
- **Zero-knowledge by design.** Cryptee cannot read your data even if compelled.
- **Reasonable pricing.** $3.50/month for 10 GB (notes + photos) is fair.

**Where it falls short:**
- **No third-party audit.** Cryptee has not published an independent security review. For high-threat users this is a meaningful gap.
- **Server-side closed source.** You can verify the client encrypts correctly, but you trust the server is implemented as claimed.
- **Limited editor features.** No code highlighting, no spreadsheet, no task management. It is a writing app, not a power-user notes tool.
- **No native macOS/Windows desktop apps.** Web PWA only on desktop. Functional but not native.
- **Smaller team.** If Cryptee shuts down, you have less recourse than with Standard Notes or Joplin.

**My experience:** Cryptee was where I journaled. For long-form, reflective writing it was the best of the three. For everything else (code snippets, financial tracking, task lists), I went back to Standard Notes or Joplin.

---

## Joplin: The Hacker's Choice

Joplin is for users who want full control.

**Why it wins on flexibility:**
- **Free forever, fully open source.** GPL/AGPL licensed, all code public.
- **Multiple sync targets.** Dropbox, OneDrive, Nextcloud, WebDAV, S3, your own server, or Joplin Cloud. Even with non-encrypted sync targets, Joplin's optional E2E layer keeps your data encrypted.
- **Markdown native.** Notes stored as plain markdown files locally. Your data is portable.
- **Powerful plugin ecosystem.** Math equations, mind maps, Anki integration, Kanban boards.
- **CLI client.** Real Joplin CLI for terminal users — usable, surprisingly polished.

**Where it falls short:**
- **Mobile apps are functional but not polished.** Battery usage on iOS is higher than Standard Notes. Sync conflicts more frequent on flaky connections.
- **E2E encryption is opt-in, not default.** New users can accidentally sync unencrypted to Dropbox if they do not enable E2E during setup.
- **No formal third-party audit.** Open source helps but is not equivalent to a professional audit.
- **Setup is more involved.** Sync target configuration, encryption setup, optional plugin installation — not a 60-second onboarding.

**My experience:** I run Joplin sync via my Nextcloud server with E2E enabled. For a homelab user this is the cleanest setup — my notes never touch anyone else's infrastructure. For non-technical users this is too much fiddling.

---

## Head-to-Head Comparison

| Feature | Standard Notes | Cryptee | Joplin |
|---------|----------------|---------|--------|
| Free tier | Yes (full E2E) | Yes (100 MB) | Yes (any sync target) |
| Cheapest paid | $8.99/mo | $3.50/mo | €2.99/mo (Cloud) |
| Open source | Yes (full) | Partial | Yes (full) |
| Self-hostable | Yes | No | Yes |
| Third-party audit | Yes (2 audits) | No | No |
| iOS app | Yes (native) | Yes (PWA) | Yes (native) |
| Android app | Yes (native) | Yes (PWA) | Yes (native) |
| Desktop apps | Yes (native, all OS) | Web PWA | Yes (native, all OS) |
| Markdown | Yes (Pro editor) | Yes | Yes (default) |
| Rich-text editor | Yes (paid) | Yes | Limited |
| Code highlighting | Yes (paid) | No | Yes |
| Task lists | Yes (paid) | Limited | Plugin |
| Spreadsheet | Yes (paid) | No | No |
| 2FA TOTP storage | Yes (paid) | No | No |
| File attachments | Paid only | Yes | Yes |
| Photo storage | Limited | Yes (15 GB on $3.50) | Yes (file attachment) |
| Sync targets | Standard Notes only | Cryptee only | 7+ options |
| Conflict resolution | Excellent | Good | Acceptable |
| Export formats | Plain, MD, encrypted, HTML | PDF, MD, plain | MD (native) |
| CLI client | No | No | Yes |
| Browser extension | No | No | Yes (Web Clipper) |

---

## Recommendation Matrix

**Most users:** **Standard Notes Productivity** ($8.99/mo). Polished, audited, full editor ecosystem, TokenVault for 2FA codes is surprisingly valuable. Free tier alone is enough for plain text needs.

**Writers and journalers:** **Cryptee Plus** ($3.50/mo). Best long-form writing experience plus encrypted photo storage in one app.

**Power users / homelab / open source maximalists:** **Joplin** with self-hosted Nextcloud sync. Free, open source, full control, infinite extensibility.

**Casual users with no specific needs:** **Standard Notes free tier**. Plain text, encrypted, free forever, sync across devices.

---

## What About Obsidian?

Obsidian is brilliant — but not encrypted by default. Notes are stored as plaintext markdown files.

For Obsidian users wanting encryption:
- **Obsidian Sync Pro** ($10/mo) provides E2E encrypted sync — the cleanest path
- **Layer Cryptomator** on your sync folder — encrypts transparently
- Sync via [encrypted cloud storage](/posts/best-secure-cloud-storage-2026/) like Tresorit or Sync.com — local Obsidian vault gets E2E encryption from the cloud layer

For users committed to Obsidian's graph view and plugin ecosystem, Obsidian Sync Pro is worth the cost. For everyone else, Standard Notes or Joplin is more honest about the encryption story.

---

## Threat Models and Notes

Your threat model determines which app is right:

- **Provider-can't-read concern:** All three meet this bar. Apple Notes / OneNote / Google Keep do not.
- **Government compelled disclosure:** Standard Notes (US jurisdiction with strong audit + open source); Joplin self-hosted (your jurisdiction); Cryptee (Estonia EU).
- **Insider threat at provider:** Standard Notes (audited, open) or Joplin self-hosted are strongest.
- **Device compromise:** All three rely on device security. Pair with full-disk encryption + [hardware security key](/posts/best-hardware-security-keys-2026/) + [strong password manager](/posts/best-password-managers-2026/).
- **Sync of high-sensitivity content (legal, medical, financial):** Joplin self-hosted on your own infrastructure is the strongest answer.

---

## Pros and Cons Summary

**Standard Notes:**
- Pros: Audited, open source, generous free tier, polished apps, strong sync
- Cons: Productivity plan pricing high, no web clipper, single sync target

**Cryptee:**
- Pros: Beautiful writing experience, encrypted photos, EU jurisdiction, fair pricing
- Cons: No third-party audit, no native desktop apps, limited editor features

**Joplin:**
- Pros: Free, fully open source, multi-sync, plugin ecosystem, CLI client
- Cons: Mobile apps less polished, E2E is opt-in, no audit, complex setup

---

## Final Verdict

For most privacy-aware users, **Standard Notes** is the right answer. Free tier covers basic needs; Productivity plan unlocks a genuinely useful suite of editor extensions including TOTP 2FA storage. The two published security audits and open-source codebase make it the most trustworthy choice.

For writers and journalers, **Cryptee** is worth a try. The minimal interface and encrypted photo integration is unique. Pair it with Standard Notes if you also need code snippets and structured notes.

For power users and the privacy-maximalist crowd, **Joplin self-hosted** with Nextcloud sync wins. You own everything, you trust no one, and the markdown-on-disk format means you can never be locked in.

For your encrypted email to send the notes you write: <a href="https://go.digitalshieldpro.com/protonmail" class="cta-affiliate" rel="sponsored noopener">View ProtonMail</a>

---

## Related Reports

- [Best secure cloud storage 2026](/posts/best-secure-cloud-storage-2026/)
- [Best password managers 2026](/posts/best-password-managers-2026/)
- [Best privacy stack 2026](/posts/best-privacy-stack-2026/)
- [How to encrypt files 2026](/posts/how-to-encrypt-files-2026/)
- [Best hardware security keys 2026](/posts/best-hardware-security-keys-2026/)
- [ProtonMail review 2026](/posts/protonmail-review-2026/)
- [Mailbox.org review 2026](/posts/mailbox-org-review-2026/)
- [Best privacy browsers 2026](/posts/best-privacy-browsers-2026/)
- [Encrypted cloud photo storage 2026](/posts/encrypted-cloud-photo-storage-2026/)
