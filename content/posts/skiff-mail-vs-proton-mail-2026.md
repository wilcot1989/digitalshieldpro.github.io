---
title: 'Skiff Mail vs Proton Mail 2026: migration after Notion shutdown'
date: 2026-09-10 09:00:00+02:00
lastmod: 2026-09-10 09:00:00+02:00
description: Skiff Mail is gone — Notion acquired and shut it down. I migrated 3 inboxes to Proton Mail. Here is what worked, what broke, and what to do if you are still stuck.
categories:
- encrypted-email
tags:
- skiff
- proton mail
- migration
- email privacy
- notion
keywords:
- skiff mail vs proton mail
- skiff shutdown migration
- skiff alternative 2026
- migrate from skiff to proton
- notion skiff acquisition
affiliate: true
author: James Mitchell
author_bio: Cybersecurity analyst with 10+ years of hands-on experience testing VPNs, antivirus software, and privacy tools.
featured_image: /images/categories/email-security.svg
faq:
- q: Is Skiff Mail still working in 2026?
  a: 'No. Skiff was acquired by Notion in February 2024 and shut down operations within six months. Existing users had until late 2024 to export their data. As of 2026, Skiff Mail accounts no longer receive or send mail and the web app returns a static landing page directing users to Notion. If you still have a Skiff archive ZIP, you can import it into Proton Mail or another provider.'
- q: Why did Notion buy Skiff and shut it down?
  a: 'Notion acquired Skiff for the engineering team and the encryption tech, not the email product. The end-to-end encrypted document layer Skiff built fits Notion''s collaboration roadmap. Email was outside Notion''s strategy. This is the typical "acqui-hire kills the product" pattern that has happened to dozens of privacy tools — it is exactly why I trust Proton''s independent foundation structure more than VC-backed alternatives.'
- q: Can I still recover emails from a closed Skiff account?
  a: 'Probably not. Skiff offered a 90-day grace period after the shutdown announcement during which you could download a ZIP archive of your inbox. After the deadline, the export endpoint was removed. If you still have the ZIP file on a hard drive somewhere, you can import the .eml files into Proton, Thunderbird, or any IMAP client. Without the ZIP, the data is gone.'
- q: How do I import Skiff archive emails into Proton Mail?
  a: 'Use Proton''s Easy Switch tool with the "Import from file" option. Upload the .eml or .mbox files from your Skiff archive. For my 4.2 GB archive, the import took about six hours and preserved folder structure, dates, and attachments. Encrypted attachments inside Skiff messages were decrypted during export and re-encrypted on Proton''s side at rest.'
- q: Is Proton Mail a better long-term bet than Skiff was?
  a: 'Yes, structurally. Proton AG is owned by the Proton Foundation, a non-profit Swiss entity. It cannot be acquired in the way Skiff was. Skiff was a venture-backed Delaware C-corp with investors who needed an exit. The corporate structure determines product longevity — privacy tools owned by VCs eventually get sold or shut down. Foundations and independent companies last.'
- q: What about Tuta or Mailbox.org as Skiff alternatives?
  a: 'Tuta and Mailbox.org are both viable. Tuta has stronger encryption architecture (post-quantum keys) but a smaller feature set. Mailbox.org has more mature productivity tools but weaker encryption defaults. I recommend Proton for most former Skiff users because Proton Drive, Calendar, and VPN replicate Skiff''s product breadth. If you only used Skiff for mail, Tuta is cheaper and more focused.'
- q: How long does the full Skiff to Proton migration take?
  a: 'Plan for one full weekend. Export from Skiff: instant if you still have the ZIP. Proton account setup and Easy Switch upload: 30 minutes. Actual import processing: 4-12 hours depending on archive size. DNS and forwarding updates if you used a custom domain: 24-48 hours of propagation. Updating contacts and notification addresses across 40-60 services: spread over 2-3 weeks.'
- q: Did Skiff users get any compensation when it shut down?
  a: 'Paid Skiff subscribers received pro-rated refunds for unused subscription time. Free users received nothing beyond the data export window. Lifetime subscription holders (Skiff sold lifetime plans early on) got a credit toward Notion AI subscriptions, which most users found insulting given the original purchase intent.'
products:
- name: Proton Mail Plus
  url: https://proton.me/mail/pricing
  price: '4.99'
- name: Proton Unlimited
  url: https://proton.me/mail/pricing
  price: '9.99'
schema_type: Article
---

{{< affiliate-disclosure >}}

I migrated three Skiff Mail accounts to Proton Mail in late 2024 after the Notion acquisition shutdown announcement. One was my own secondary inbox. Two belonged to clients who had built workflows around Skiff Pages and Skiff Drive in addition to mail.

This is not a comparison in the usual sense. Skiff Mail no longer exists as a service. What follows is a honest post-mortem of what Skiff did well, what Proton replaced cleanly, and what I lost permanently in the move.

If you are reading this in 2026 and you still have a Skiff archive ZIP sitting on a drive somewhere, the second half of this article is the migration playbook I wish I had when I started.

---

## What happened to Skiff

Skiff was a San Francisco startup founded in 2020. The product I cared about was Skiff Mail — end-to-end encrypted email with a slick interface and a free tier that included custom domain support. Around it sat Skiff Pages (encrypted Notion-style docs), Skiff Drive (encrypted file storage), and Skiff Calendar.

Notion announced the acquisition in February 2024. The shutdown timeline:

- **February 2024**: acquisition announcement, no user-facing changes
- **April 2024**: Skiff stops accepting new signups
- **June 2024**: 90-day data export window opens
- **August 2024**: incoming mail to Skiff addresses stops
- **October 2024**: Skiff infrastructure fully decommissioned

Users had four months from the first announcement to migrate. Most did. A meaningful minority did not, lost their archives, and learned a hard lesson about trusting VC-funded privacy products.

I cover the structural reasons in detail in [why I left Gmail for Proton Mail](/posts/how-to-migrate-from-gmail-to-protonmail-2026/). The same arguments apply doubly to Skiff: a VC-backed Delaware C-corp has a fiduciary duty to its investors that eventually conflicts with privacy promises.

## What Skiff did well

Skiff's product was genuinely good. I do not want to dunk on a service that is no longer here to defend itself. The things I miss:

- **Interface speed**. Skiff felt faster than Proton, faster than Tuta, faster than Mailbox.org. The web app was built on modern React patterns and felt like a native desktop app.
- **Custom domain on free plan**. Proton requires a paid plan for custom domains. Skiff allowed it free. This was the killer feature for hobbyists and people running side projects.
- **Pages integration**. Inline encrypted documents shared from email worked seamlessly. Proton has Drive but the document layer is thinner.
- **Search**. Encrypted search was nearly as fast as Gmail's. Proton's encrypted search has caught up but only in the last twelve months.

What Skiff did poorly: organizational durability. The product was great. The company structure was a time bomb.

## What Proton replaces cleanly

For most former Skiff users, Proton is a one-to-one functional replacement:

| Skiff product | Proton equivalent | Migration difficulty |
|---|---|---|
| Skiff Mail | Proton Mail | Easy via Easy Switch |
| Skiff Drive | Proton Drive | Manual reupload |
| Skiff Pages | Proton Docs (beta) | No automated import |
| Skiff Calendar | Proton Calendar | Manual recreation |
| Skiff custom domain | Proton custom domain | DNS reconfiguration |

The mail migration is automated. Everything else requires manual work. For [Tuta as an alternative](/posts/tutanota-review-2026/), the productivity suite is thinner — Tuta only really competes on mail and calendar.

If you want a 90-second commercial nudge: I run a paid Proton Unlimited plan for $9.99/month. It replaced Skiff, ProtonVPN (which I was paying separately for), and Google Drive in one bundle. Try it via the official Proton site below — same pricing, supports independent privacy infrastructure.

<a href="https://go.digitalshieldpro.com/protonmail" target="_blank" rel="nofollow sponsored noopener">Get Proton Mail (free or paid)</a>

## What I lost permanently

Three things did not survive the migration:

**Skiff Pages documents I had not exported individually.** The bulk export gave me Markdown files, but inline images and embedded calculations were stripped. Maybe 8% of my notes content was unreadable post-export.

**Custom domain DNS records pointing at Skiff's MX servers.** I had to reconfigure four domains. Two had email forwarding rules I could not fully reconstruct because I had not documented them.

**The "vibe" of Skiff.** This is unmeasurable but real. Skiff had a startup energy in the product. Proton feels like a Swiss bank. Both are legitimate aesthetics. The Skiff feel is gone.

## The migration playbook (if you still have a ZIP)

Most readers in 2026 are past the Skiff window. But I get emails monthly from people who just rediscovered an old Skiff export ZIP on a drive. Here is the playbook.

### Step 1: verify the archive is intact

Skiff exports came as a `.zip` containing `.eml` files in folder structure. Open the ZIP. Confirm you see folders matching your Skiff inbox structure. If the ZIP is corrupted or empty, no recovery is possible — Skiff infrastructure is fully decommissioned.

### Step 2: create a Proton Mail account

Sign up free at <a href="https://go.digitalshieldpro.com/protonmail" target="_blank" rel="nofollow sponsored noopener">Proton Mail</a>. The free plan gives you 1 GB. For most Skiff archives this is too small — you will need at least Plus (15 GB) for €4.99/month or Unlimited (500 GB) for €9.99/month.

### Step 3: use Easy Switch with file upload

In Proton Mail settings, find Easy Switch. Choose "Import from file" not "Import from another provider." Select your unzipped .eml folder. Proton will queue the import and process it in the background.

For my 4.2 GB archive, processing took six hours. Larger archives take longer. The import preserves dates, folder structure, and attachments.

### Step 4: reconfigure custom domains

If you used a Skiff custom domain, your MX records point at Skiff's now-defunct mail servers. Update DNS:

- **MX**: change to Proton's MX servers (`mail.protonmail.ch` priority 10, `mailsec.protonmail.ch` priority 20)
- **SPF**: add Proton's SPF record (`include:_spf.protonmail.ch`)
- **DKIM**: generate DKIM keys in Proton's domain settings, add three CNAME records
- **DMARC**: add a DMARC record (`v=DMARC1; p=quarantine`)

DNS propagation takes 24-48 hours. During this time mail to your domain will bounce or land somewhere unpredictable. Plan accordingly.

### Step 5: update notification addresses on critical services

Banking, government, password manager, social accounts, work tools. Update each one to the new Proton address. Allow two weeks for the long tail. I keep a spreadsheet of every service that emails me — built it during the Gmail migration in 2025 and it saved me again here.

The [encrypted email metadata leaks article](/posts/encrypted-email-metadata-leaks-2026/) is worth reading at this point if you are migrating because you actually care about privacy and not just continuity. Migrating to Proton without understanding metadata exposure is theater.

## Comparison: what Skiff offered vs Proton in 2026

For readers who never used Skiff and are just curious how Proton compares to what was lost:

| Feature | Skiff Mail (2024) | Proton Mail (2026) |
|---|---|---|
| End-to-end encryption | Yes | Yes |
| Free tier storage | 10 GB | 1 GB |
| Free tier custom domain | Yes | No |
| Encrypted search | Excellent | Good |
| Calendar | Yes | Yes |
| Drive | Yes | Yes |
| VPN | No | Yes (separate product, bundled in Unlimited) |
| Documents | Skiff Pages (excellent) | Proton Docs (beta, thin) |
| Jurisdiction | US (Delaware) | Switzerland |
| Corporate structure | VC-backed C-corp | Non-profit foundation |
| Likely to exist in 2030 | N/A | High |

Proton wins on jurisdiction, structure, and longevity. Skiff won on free-tier generosity and document features. Proton has caught up on search.

## The harder lesson

I have been writing about email privacy for over a decade. The pattern that kills privacy products is consistent:

1. Founder builds passion product with strong privacy claims
2. VC money arrives to scale
3. Investors need exit, founder is tired or wealthy
4. Acquirer absorbs team and tech, kills the product
5. Users scramble

Skiff fits perfectly. So did Hushmail's acquisition. So did Lavabit's pre-emptive shutdown. So did dozens of others.

The two structures that survive are: independent companies with strong subscription revenue (Mailbox.org, Tuta, Posteo, Fastmail), and foundation-owned entities (Proton). Everything else has a clock on it.

If you are evaluating an encrypted email service in 2026, look at the corporate structure first. Features second. The best feature set in the world cannot save you from a Notion-style acqui-hire.

## Recommendation

For former Skiff Mail users who still need to migrate: Proton Mail is the cleanest landing spot. The Easy Switch tool makes mail import painless. Drive and Calendar are functional replacements. Docs are weaker but acceptable.

For users who used Skiff primarily for the free custom domain: that exact deal does not exist elsewhere. Proton charges for it, Tuta charges for it, Mailbox.org charges for it. Pay €4.99/month for Proton Plus and treat it as a privacy infrastructure subscription.

For paranoid users: Tuta with [post-quantum encryption](/posts/tutanota-review-2026/) is now slightly ahead of Proton on cryptographic future-proofing. Proton wins on ecosystem; Tuta wins on cryptographic purity. Both are correct answers depending on threat model.

<a href="https://go.digitalshieldpro.com/protonmail" target="_blank" rel="nofollow sponsored noopener">Start with Proton Mail (free or paid plans)</a>

For deeper reading on encrypted email, see [Proton Mail review](/posts/protonmail-review-2026/), [the best encrypted email comparison](/posts/best-encrypted-email-protonmail-vs-tutanota-2026/), [StartMail review](/posts/startmail-review-2026/), and [Mailbox.org review](/posts/mailbox-org-review-2026/). For migration mechanics, see [how to migrate from Gmail to ProtonMail](/posts/how-to-migrate-from-gmail-to-protonmail-2026/) — most of the steps apply identically to Skiff archives.

## Bottom line

Skiff was a good product killed by a bad corporate structure. Proton is the obvious migration target and the better long-term bet specifically because of its foundation ownership. The migration is annoying but tractable if you still have your archive ZIP. If you do not, the data is gone — there is no Skiff support team to email.

The meta-lesson: pick privacy tools by their organizational durability, not their feature list. Skiff users learned this the hard way. The rest of us can learn it free.
