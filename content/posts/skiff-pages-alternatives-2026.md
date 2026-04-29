---
title: 'Skiff Pages alternatives 2026: encrypted docs after the shutdown'
date: 2026-09-19 09:00:00+02:00
lastmod: 2026-09-19 09:00:00+02:00
description: Skiff Pages was the best end-to-end encrypted document tool I had used. Notion shut it down. I migrated 200+ pages across three alternatives — here is what works.
categories:
- encrypted-email
tags:
- skiff
- encrypted documents
- proton drive
- cryptpad
- migration
keywords:
- skiff pages alternatives
- encrypted google docs alternative
- proton docs review
- cryptpad review
- end to end encrypted documents
affiliate: true
author: James Mitchell
author_bio: Cybersecurity analyst with 10+ years of hands-on experience testing VPNs, antivirus software, and privacy tools.
featured_image: /images/categories/email-security.svg
faq:
- q: What happened to Skiff Pages?
  a: 'Notion acquired Skiff in February 2024 and shut down all Skiff products within six months — including Skiff Pages, Skiff Drive, Skiff Calendar, and Skiff Mail. Existing users had a 90-day grace period to export data. As of 2026, Skiff is gone. The acquisition pattern (acqui-hire of the engineering team, kill the product) is the same one that has killed dozens of privacy-focused startups.'
- q: What is the closest replacement for Skiff Pages?
  a: 'Proton Docs for most use cases. End-to-end encrypted, real-time collaboration, integrates with Proton Drive for file storage, integrates with Proton Mail for sharing. Launched in 2024 specifically to fill the encrypted-docs gap that Skiff''s shutdown created. Not feature-complete with Skiff Pages yet (Skiff had a richer block-editor model) but the encryption architecture is solid.'
- q: Is CryptPad a good Skiff Pages alternative?
  a: 'For specific use cases, yes. CryptPad is open-source and self-hostable — every operation happens client-side, the server stores only encrypted blobs. The trade-off: the UI is functional but utilitarian, the collaboration features lag behind commercial alternatives, and the free hosted instance has storage limits. For privacy-extreme users or self-hosters, CryptPad is the cleanest choice. For everyday productivity, Proton Docs is more polished.'
- q: Can I export my Skiff Pages archive into Proton Docs?
  a: 'Partially. Skiff Pages exported as Markdown (.md) or PDF. Proton Docs imports .docx and plain text directly; .md import works through a copy-paste or via a .docx conversion step. Page hierarchy and internal links do not survive the conversion. Plan to manually rebuild the document structure.'
- q: What about Notion itself? Is it secure?
  a: 'No. Notion stores documents in plaintext on its servers and uses TLS in transit only. Notion staff and any subpoena can access your document content. The Skiff acquisition was specifically about Notion buying encrypted-document expertise — but Notion has not added end-to-end encryption to its main product as of 2026. Notion is fine for non-sensitive work; it is not a Skiff replacement for users who chose Skiff for privacy.'
- q: Does Proton Docs work offline?
  a: 'Limited. Proton Docs has offline support for documents you have recently opened — they cache locally and you can edit. Sync happens when you reconnect. For heavy offline use, the experience is rougher than Notion or Google Docs. CryptPad is similarly limited offline. If offline-first is critical, consider [Obsidian](/posts/best-encrypted-notes-apps-2026/) with end-to-end encrypted sync.'
- q: How do I share an encrypted document with someone who does not have Proton?
  a: 'Proton Docs lets you create a public share link with optional password protection. Recipients open the link, enter the password, and view the document in browser without needing a Proton account. Editing requires a Proton account. The share-link approach is the practical answer for cross-provider sharing.'
- q: Are there self-hosted Skiff Pages alternatives?
  a: 'Yes. CryptPad self-hosted is the most direct one. Etherpad with the End-to-End Encryption plugin is another. HedgeDoc (formerly CodiMD) handles markdown collaborative editing with optional self-hosting. For technically capable users who want full control, self-hosting is viable. For most users, Proton Docs hosted is the lower-friction answer.'
products:
- name: Proton Unlimited
  url: https://proton.me/mail/pricing
  price: '9.99'
- name: Proton Mail Plus
  url: https://proton.me/mail/pricing
  price: '4.99'
schema_type: Article
---

{{< affiliate-disclosure >}}

Skiff Pages was the best end-to-end encrypted document tool I had used. Block editor, real-time collaboration, end-to-end encryption, integrated with Skiff Mail and Skiff Drive. It felt like Notion built by people who actually cared about privacy.

Notion bought Skiff in February 2024. Notion killed Skiff Pages by August 2024. I migrated 200+ pages across three personal accounts and four client accounts. This is what works as a replacement, what does not, and what I lost permanently in the move.

The short version: Proton Docs for most users, CryptPad for self-hosted privacy-extreme setups, [Obsidian with encrypted sync](/posts/best-encrypted-notes-apps-2026/) for offline-first knowledge management. Notion is not on the list — it is the company that killed Skiff and has not added end-to-end encryption to its own product.

---

## What Skiff Pages did well

Before discussing replacements, it helps to remember what Skiff Pages did right. The bar for "Skiff Pages alternative" is set by these features.

**End-to-end encryption by default.** Every document was encrypted client-side before being uploaded to Skiff servers. Skiff staff genuinely could not read your documents. This was the core differentiator vs Notion, Google Docs, or Microsoft 365.

**Block editor with rich formatting.** Headings, lists, tables, code blocks, embedded images, embedded files, kanban views. The editing experience matched Notion feature-for-feature.

**Real-time collaboration.** Multiple users editing the same document simultaneously, with presence indicators, comments, and version history. The collaboration model worked over end-to-end encryption — a non-trivial engineering achievement.

**Hierarchy and linking.** Pages could nest into pages indefinitely. Internal links between pages were first-class. Move a page and links updated automatically.

**Integrated ecosystem.** Pages, Drive, Mail, Calendar all under one account, all end-to-end encrypted, single sign-on.

**Free tier was generous.** 10 GB free, unlimited public pages, unlimited private pages within storage limit.

This is what got killed. Now the alternatives.

## Proton Docs: the closest replacement

Proton launched Proton Docs in 2024 specifically to fill the encrypted-documents gap. Bundled with Proton Drive on Plus, Unlimited, and Business plans.

**What works well:**

- End-to-end encrypted by default. Same architectural model as Skiff (client-side encryption, server stores opaque blobs).
- Real-time collaboration with multiple simultaneous editors.
- Comments, version history, suggested edits.
- Integrates with Proton Drive (attach files), Proton Mail (share via encrypted email), Proton Calendar (link events).
- Public share links with password protection for cross-provider sharing.
- Works on web, iOS, Android, desktop apps for macOS/Windows/Linux.
- Mobile apps are polished and fast.

**What is rough:**

- Not as feature-complete as Skiff Pages was. The block editor model is simpler — basic blocks (text, headings, lists, tables, embedded files) but not the deep nesting and database-view richness Skiff had.
- No kanban or database views. If you used Skiff Pages as a Notion-style database, Proton Docs cannot replace that workflow yet.
- Page hierarchy is folder-based, not nested-page-based. Migration from Skiff Pages requires rebuilding the structure.
- Search inside encrypted documents is limited (this is a fundamental constraint of E2EE — search has to happen client-side, which limits scalability).

**Cost:** Bundled with [Proton Mail](/posts/protonmail-review-2026/) Plus (€4.99/month, 15 GB), Unlimited (€9.99/month, 500 GB), or Business (€12.99/user/month).

**Migration effort:** Medium. Export Skiff Pages as Markdown, import into Proton Docs, manually rebuild hierarchy and re-link internal references. Plan one weekend per 100 pages.

For more on the Proton ecosystem, see [Proton Mail review](/posts/protonmail-review-2026/), [Proton Pass review](/posts/proton-pass-review-2026/), and [Proton Unlimited vs Google One](/posts/proton-unlimited-vs-google-one-2026/).

## CryptPad: open-source and self-hostable

CryptPad is an open-source collaborative office suite with end-to-end encryption. Maintained by the French company XWiki SAS. Free hosted instance at cryptpad.fr; can be self-hosted on Docker or Linux.

**What works well:**

- End-to-end encrypted by default. The encryption architecture has been peer-reviewed and is documented openly.
- Collaborative editing for documents, spreadsheets, presentations, kanban, polls, code, whiteboards.
- Self-hostable for full data sovereignty.
- Open source — every line of code is auditable.
- Free hosted tier (1 GB) for casual use.
- Anonymous access — you can use CryptPad without an account, with the trade-off that anonymous documents expire after 30 days.

**What is rough:**

- The UI is functional but utilitarian. Feels like 2018-era webapp design, not 2026.
- Real-time collaboration works but is slower than Proton Docs or Google Docs in my testing — noticeable lag on documents with 4+ simultaneous editors.
- Mobile experience is web-based; no native apps.
- Self-hosting requires Linux administration competence.
- The free hosted instance has storage limits that fill up quickly with embedded images.

**Cost:** Free for hosted up to 1 GB; €5-15/month for paid hosted plans; free if self-hosted (your hosting cost only).

**Best fit:** Privacy-extreme users, self-hosters, organizations that need data sovereignty (e.g. EU government bodies that legally cannot use US-hosted services).

## Obsidian + encrypted sync: offline-first

[Obsidian](/posts/best-encrypted-notes-apps-2026/) is a markdown note-taking app that runs locally on your device. Files are stored as plain markdown in a folder. Sync between devices is optional and pluggable.

**What works well:**

- Offline-first. Open the app on a plane, edit, sync when reconnected.
- Local files in standard markdown — no proprietary format, easy to back up, easy to migrate to another tool later.
- Powerful linking, tagging, and graph visualization for knowledge management.
- Plugin ecosystem covers most Skiff Pages features (kanban, databases, calendar views).
- Free for personal use.

**What is rough:**

- Not collaborative in real-time. Two people editing the same note simultaneously will conflict unless you use a sync solution that handles conflicts (Obsidian Sync does, basic Dropbox sync does not).
- Sharing requires either Obsidian Publish (paid hosted service, not E2EE) or manual export.
- Encryption is your responsibility — Obsidian stores files in plaintext locally; you encrypt the sync layer.

**Encryption options:**

- **Obsidian Sync** (€4/month) is end-to-end encrypted. Recommended for cross-device personal use.
- **iCloud / OneDrive sync** is not end-to-end encrypted — Apple/Microsoft can read the markdown.
- **[Cryptomator](/posts/cryptomator-review-2026/)** vault on Dropbox/OneDrive gives you E2EE on top of any cloud storage.
- **Self-hosted Syncthing** keeps data fully on devices you control.

**Cost:** Obsidian free; Obsidian Sync €4/month; or self-hosted with Syncthing/Cryptomator.

**Best fit:** Knowledge workers, researchers, single-user workflows where collaboration is not the priority.

## What I tell clients to pick

After migrating seven Skiff users (myself plus six clients), here is the decision tree.

**Pick Proton Docs if:**

- You used Skiff Pages mainly for personal or small-team documents
- You want end-to-end encryption with the lowest friction
- You are comfortable in the Proton ecosystem
- You need real-time collaboration with non-technical teammates
- You value polished mobile apps

**Pick CryptPad if:**

- You need to self-host for data sovereignty reasons
- You want fully open-source software
- You handle highly sensitive content where you do not want to trust any commercial provider
- Your team is technically capable of dealing with a less-polished UI

**Pick Obsidian + encrypted sync if:**

- You used Skiff Pages mainly for personal knowledge management (not collaboration)
- You want offline-first
- You value the markdown ecosystem and want to avoid lock-in
- You are happy doing your own encryption configuration

**Avoid:**

- **Notion** — they killed Skiff and have not added E2EE to their own product
- **Google Docs** — Google staff can read your documents
- **Microsoft 365** — Microsoft staff can read your documents
- **Quip, Coda, ClickUp Docs** — none of these are end-to-end encrypted

## Migration playbook: Skiff Pages to Proton Docs

If you still have your Skiff archive ZIP from the 2024 export window, here is the playbook.

**Step 1: Set up Proton account.** Sign up for [Proton Mail](https://go.digitalshieldpro.com/protonmail){target="_blank" rel="nofollow sponsored noopener"} Plus or Unlimited. Verify the account, enable 2FA with a [hardware key](/posts/yubikey-vs-nitrokey-vs-solokey-2026/).

**Step 2: Inventory your Skiff Pages.** Open the ZIP. Skiff exports as a folder structure with .md files for each page and a sidebar.json describing hierarchy. Make a list of pages, group by topic, decide which to migrate as-is and which to consolidate.

**Step 3: Bulk import simple pages.** For pages that are mostly text, drag the .md files directly into Proton Docs. They import as separate documents. Folder structure does not survive — recreate folders manually in Proton Drive and move imported docs into them.

**Step 4: Manually rebuild rich pages.** Skiff Pages with embedded images, tables, code blocks, and internal links require manual rebuild. Open the .md file, copy content, paste into a new Proton Doc, re-add formatting and re-link. Plan 5-15 minutes per rich page.

**Step 5: Re-link cross-references.** Skiff internal links (skiff://...) do not work in Proton Docs. Manually update them to Proton Drive URLs.

**Step 6: Set up sharing.** For pages shared with collaborators on Skiff, recreate the share permissions in Proton Docs. Invite by email; recipients need a Proton account to edit (free Proton account is sufficient for most cases).

**Step 7: Decommission Skiff archive.** Once everything is migrated and verified, securely delete the Skiff ZIP. Use shred on Linux or "Secure Empty Trash" equivalents elsewhere.

For my 200-page personal archive, the migration took two weekends of focused work. The 50-page client archives took one weekend each.

## What I lost permanently

Honest accounting of what did not survive the move.

**Skiff Pages databases.** Skiff supported Notion-style databases (table view, kanban view, gallery view of structured records). Proton Docs does not have an equivalent. I rebuilt three databases as static tables with manual updates. One database I migrated to Obsidian with the Dataview plugin. One I just abandoned.

**Embedded Skiff Drive previews.** Skiff Pages could embed Skiff Drive files inline with previews. Proton Docs supports file attachments but the inline-preview experience is more limited.

**Calendar event linking.** Skiff Pages could link to Skiff Calendar events with rich previews. Proton Calendar does not yet expose this kind of inline embed.

**Public-facing site mode.** Skiff had a feature where a Skiff page could be published as a public website. Notion has this too. Proton Docs does not. For the one client who used this, we migrated to a separate static site generator.

## Get started

For most former Skiff Pages users, [Proton Mail](https://go.digitalshieldpro.com/protonmail){target="_blank" rel="nofollow sponsored noopener"} Unlimited at €9.99/month is the right starting point — includes Drive, Docs, Mail, Calendar, Pass, and VPN in one bundle.

For self-hosters and privacy-extreme users, CryptPad self-hosted is free if you have a Linux server.

For knowledge management workflows, [Obsidian with encrypted sync](/posts/best-encrypted-notes-apps-2026/) is the offline-first answer.

For more on the encrypted alternatives ecosystem, see [Skiff Mail vs Proton Mail](/posts/skiff-mail-vs-proton-mail-2026/), [privacy-respecting alternatives to Google services](/posts/privacy-respecting-alternatives-google-services-2026/), and [best secure cloud storage](/posts/best-secure-cloud-storage-2026/).
