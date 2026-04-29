---
title: 'Cryptomator Review 2026: client-side encryption for any cloud'
date: 2026-09-22 09:00:00+02:00
lastmod: 2026-09-22 09:00:00+02:00
description: I encrypted my Dropbox, Google Drive, and OneDrive with Cryptomator for 10 months. €15 one-time on mobile, free desktop, fully open source. Here is what works.
categories:
- privacy-tools
tags:
- cryptomator
- encrypted cloud storage
- dropbox encryption
- file encryption
- privacy
keywords:
- cryptomator review 2026
- encrypt dropbox files
- cryptomator vs veracrypt
- client side encryption cloud
- encrypted google drive
affiliate: true
author: James Mitchell
author_bio: Cybersecurity analyst with 10+ years of hands-on experience testing VPNs, antivirus software, and privacy tools.
featured_image: /images/categories/privacy-tools.svg
faq:
- q: What does Cryptomator actually do?
  a: 'Cryptomator creates an encrypted "vault" — a folder of encrypted files — that you store in any cloud sync service (Dropbox, Google Drive, OneDrive, iCloud Drive, pCloud, Mega, anything). You unlock the vault on your device with a password and Cryptomator transparently decrypts files as you open them. The cloud provider only ever sees encrypted blobs. They cannot read your files even if their employees, government, or hackers get access to your account.'
- q: How is Cryptomator different from Boxcryptor?
  a: 'Boxcryptor was the dominant client-side encryption tool until Dropbox acquired it in 2022 and shut down the consumer product. Boxcryptor users were forced to migrate. Cryptomator picked up most of those users because it does the same thing, is open source (Boxcryptor was closed), and has no acquisition risk — it is run by Skymatic, an independent German company that has refused acquisition offers publicly.'
- q: Is Cryptomator really free?
  a: 'Desktop apps (Windows, macOS, Linux) are 100% free and open source. Mobile apps (iOS, Android) are paid: €14.99 one-time for iOS, €13.99 one-time for Android. There is no subscription. The mobile apps are paid because Skymatic uses that revenue to fund continued development. Desktop being free + mobile being one-time is one of the most user-friendly pricing models in the privacy software space.'
- q: How does Cryptomator compare to Cryptomator Hub?
  a: 'Cryptomator (the free product) is for individuals — single-user vaults. Cryptomator Hub is the team/business product where multiple users share an encrypted vault with managed access control, billed per user per month. For personal use, the free Cryptomator is what you want. For businesses sharing encrypted folders across employees, Hub is the path. This review covers the personal product.'
- q: Does Cryptomator work with iCloud Drive on iPhone?
  a: 'Yes. The Cryptomator iOS app integrates with iCloud Drive, Files app, Dropbox, Google Drive, OneDrive, pCloud, WebDAV, and S3. You point Cryptomator at the cloud location, unlock the vault with your password, and use the Files app or share-sheet integration to access encrypted files. Edits sync back to the cloud automatically encrypted. Works the same on Android with similar cloud provider support.'
- q: Can I share encrypted Cryptomator files with someone else?
  a: 'Yes, with caveats. The recipient needs Cryptomator and your vault password. The vault is shared the same way you would share any cloud folder (Dropbox shared link, Google Drive shared folder, etc.) plus you communicate the password out-of-band. This works but is clunky for multi-user scenarios. For team sharing, use Cryptomator Hub. For one-off sharing, use the free product with shared cloud folder.'
- q: How does Cryptomator compare to Tresorit or Proton Drive?
  a: 'Tresorit and [Proton Drive](/posts/protonmail-review-2026/) are full encrypted cloud storage services — they provide both the storage and the encryption. Cryptomator is just the encryption layer on top of cloud storage you already have. If you want one product that does everything, Tresorit or Proton Drive are easier. If you want to keep using Dropbox/Google/OneDrive and add encryption on top, Cryptomator is the only practical answer.'
- q: What happens if I lose my Cryptomator password?
  a: 'You lose access to that vault. Cryptomator generates a 256-bit master key from your password using scrypt — there is no backdoor and no recovery option. Cryptomator does support a "recovery key" which is a 256-character string you save during vault creation; if you have the recovery key, you can reset the password. If you have neither the password nor the recovery key, the data is gone. Save the recovery key in a [password manager](/posts/best-password-managers-2026/) or print it and store in a safe.'
products:
- name: Cryptomator (Desktop)
  url: https://cryptomator.org/downloads/
  price: '0'
- name: Cryptomator iOS
  url: https://apps.apple.com/app/id953086535
  price: '14.99'
- name: Cryptomator Android
  url: https://play.google.com/store/apps/details?id=org.cryptomator
  price: '13.99'
schema_type: Review
---

{{< affiliate-disclosure >}}

I have used Cryptomator for 10 months as the encryption layer over my Dropbox, Google Drive, and OneDrive accounts. The use case: I cannot fully migrate off these services because work and family share files there. But I do not want my actual important files visible to those providers.

Cryptomator solves this exact problem. Free on desktop, €15 one-time on mobile, fully open source, zero subscription. After 10 months I am ready to write the honest review.

Short answer: Cryptomator is the right answer for users who need to keep using mainstream cloud storage but want client-side encryption on the files that matter. It is not a replacement for [Proton Drive](/posts/protonmail-review-2026/) or Tresorit — those are full encrypted cloud services. Cryptomator is the layer between you and your existing cloud.

*Note: Cryptomator does not have an affiliate program. This review contains no referral links to Cryptomator.*

---

## What Cryptomator Is

Cryptomator is an open-source client-side encryption tool. It creates an encrypted "vault" in any folder — typically a cloud-synced folder like Dropbox, Google Drive, or OneDrive. You unlock the vault with a password and use the unlocked vault as a virtual drive on your computer. Files inside the vault are encrypted on your device before they sync to the cloud.

The cloud provider sees: a folder full of encrypted files with random names. They cannot tell what the files are, what they contain, or anything except the approximate size of each encrypted blob.

You see: a normal folder with normal file names that you can open, edit, and save. Cryptomator decrypts on the fly as you access files.

The encryption is AES-256 with HMAC-SHA256 for file integrity. The master key is derived from your password using scrypt with strong parameters. The architecture has been audited multiple times and the audit reports are public.

## Why Not Just Use Proton Drive or Tresorit?

Fair question. The answer depends on your situation:

**If you can migrate your cloud entirely**, [Proton Drive](/posts/protonmail-review-2026/) or Tresorit are easier. One product, end-to-end encrypted by default, no extra layer to manage.

**If you cannot migrate** because work uses Google Workspace, family shares photos via iCloud, or your collaboration partners insist on Dropbox: Cryptomator lets you keep using those services while encrypting the files that matter.

I am in the second camp. My team uses Google Workspace. My family shares photos via iCloud. I cannot move all of that. Cryptomator lets me encrypt my personal sensitive files (financial records, contracts, medical documents) on top of those existing cloud accounts.

## Setup

Cryptomator setup takes about 10 minutes:

1. **Download** the desktop app from cryptomator.org. Free for Windows, macOS, Linux.
2. **Create a vault.** Pick a location — I chose a folder inside my Dropbox.
3. **Set a strong password.** Cryptomator suggests at least 12 characters; I use 24+ from a [password manager](/posts/best-password-managers-2026/).
4. **Save the recovery key.** Cryptomator generates a 256-character recovery key. Print it or save in a password manager. This is your "lost password" emergency exit.
5. **Unlock the vault.** Cryptomator mounts it as a virtual drive on your computer.
6. **Use it like a folder.** Drop files in. They encrypt and sync to Dropbox.
7. **Mobile setup.** Install Cryptomator iOS or Android (€14.99 / €13.99). Point it at the same cloud location. Unlock with the same password.

The encrypted vault syncs across all your devices via the cloud provider's existing sync. You unlock it locally on each device.

## What Works Well

**Cross-cloud compatibility.** I have vaults in Dropbox, Google Drive, OneDrive, and iCloud Drive simultaneously. Each works. The cloud provider does not know or care.

**Performance.** Reading and writing encrypted files is fast. AES-256 encryption is hardware-accelerated on every modern CPU. I have not noticed lag in daily use.

**File-level granularity.** Each file is encrypted individually inside the vault. Changes to one file only re-sync that file, not the entire vault. This works correctly with cloud sync delta-update algorithms.

**Mobile integration.** The iOS app integrates with the Files app via the standard Files extension. I can browse my Cryptomator vault inside Files alongside iCloud Drive and Google Drive. Tap a file and it opens in the appropriate app.

**Open source.** Code is on GitHub under GPLv3. The encryption library is independently auditable. Multiple public audits have been published. This is real auditability, not just marketing.

**No vendor lock-in.** Cryptomator vaults are a documented file format. If Skymatic disappears tomorrow, the vault is still readable by any tool that implements the format. There is at least one alternative implementation.

**One-time mobile pricing.** No subscription. €15 once and you have the iOS app forever. This is increasingly rare in the privacy software space.

**Active development.** Skymatic ships updates regularly. Bug reports are addressed. The software does not feel abandoned.

## What Is Rough

**Multi-user sharing is awkward.** If you want to share an encrypted vault with someone else, both of you need Cryptomator and the same password. The password sharing has to happen out-of-band (text, in person). For families or teams who want shared encrypted storage, this is friction. Cryptomator Hub solves this with managed access control but costs per user per month.

**Cloud provider quirks.** Some cloud providers do strange things with sync. Google Drive's selective sync can confuse Cryptomator. OneDrive's "Files On-Demand" mode requires careful configuration. Dropbox is the smoothest. I had two Google Drive sync incidents in 10 months that required manual cleanup.

**Mobile editing has limitations.** On iOS, opening a Word document from a Cryptomator vault works but the edited file does not always save back correctly through the share sheet. The pattern is: open, edit, save to a temp location, manually move back to vault. Friction.

**No cloud-side preview.** Cloud providers cannot generate thumbnails or previews of encrypted files. If you store photos in a Cryptomator vault, the cloud's web interface shows random encrypted file names — you cannot browse the vault from a web browser without the desktop or mobile app.

**Two-step file access.** You unlock the vault, then access files. On iPhone this means opening Cryptomator, unlocking, then navigating. Not as smooth as Files-app-direct-to-Dropbox.

**Search is limited.** You can search inside an unlocked vault. You cannot search across multiple locked vaults. For users with multiple vaults, this is a real limitation.

## What I Encrypt

For full transparency, what is in my Cryptomator vaults vs what stays unencrypted:

**Encrypted (in Cryptomator vaults):**

- Tax records and financial documents
- Medical records and insurance documents
- Employment contracts and HR documents
- Identity documents (passport scans, IDs)
- Personal journals and writing drafts
- Client contracts and NDAs
- Crypto wallet seed phrase backups (with extra encryption layer)

**Not encrypted (regular cloud sync):**

- Family photos shared with relatives
- Work documents inside Google Workspace shared drives
- Software project files (already in Git, encrypted at rest there if needed)
- Public-facing PDFs and writing
- Travel itineraries and bookings

The split is: anything I would mind a cloud provider's employee or a hacker reading goes in Cryptomator. Anything that is already public or low-stakes stays in regular cloud sync.

## Cryptomator vs VeraCrypt

VeraCrypt is the other major open-source encryption tool people compare Cryptomator to. They solve different problems:

**VeraCrypt** creates encrypted disk images or partitions. The whole image is one file. Changing one byte inside the encrypted disk requires re-syncing the entire image to the cloud.

**Cryptomator** encrypts individual files inside a vault. Changing one file syncs only that file.

For cloud sync use cases, Cryptomator is dramatically better. VeraCrypt is right for local disk encryption (encrypting a USB drive, encrypting a system partition).

If you need both — local disk encryption and cloud-synced encryption — use both tools for different purposes. They do not conflict.

## Cryptomator vs Proton Drive

| Dimension | Cryptomator | Proton Drive |
|---|---|---|
| Storage included | None (you provide) | 1 GB free, 500 GB on Unlimited |
| End-to-end encrypted | Yes | Yes |
| Open source | Yes | Partial |
| Cross-platform | Yes (5 OSes) | Yes |
| Cloud provider choice | Any | Proton-only |
| Mobile app cost | €13.99-14.99 once | Bundled |
| Multi-user sharing | Limited (Hub for teams) | Yes |
| Web access | No (apps only) | Yes |
| Cost (excluding cloud) | €0 desktop + €15 mobile once | $4.99-9.99/mo |

Cryptomator wins for "I want to keep my existing cloud + add encryption." [Proton Drive](/posts/protonmail-review-2026/) wins for "I want one integrated encrypted cloud product."

## Use Case Matching

**You have Dropbox/Google/OneDrive and you cannot leave:** Cryptomator. This is the canonical use case.

**You want full encrypted cloud storage from scratch:** Proton Drive (bundled with [Proton Mail](/posts/protonmail-review-2026/)) or Tresorit.

**You need team-shared encrypted folders:** Cryptomator Hub or Tresorit Business. Cryptomator personal is not built for this.

**You have one encrypted USB drive you want to use across machines:** VeraCrypt is a better fit than Cryptomator.

**You want encryption for one specific file (a single PDF, a single archive):** GPG file encryption (gpg -c filename) is enough; Cryptomator is overkill.

**You are a journalist or activist with sensitive sources:** Cryptomator is fine for storage, but pair with [Proton Mail](/posts/protonmail-review-2026/), [hardware 2FA keys](/posts/yubikey-vs-nitrokey-vs-solokey-2026/), and [GrapheneOS](/posts/grapheneos-vs-ios-privacy-2026/) for the full posture.

## How Cryptomator Fits a Privacy Stack

For readers building coherent privacy infrastructure:

- **Email**: [Proton Mail](/posts/protonmail-review-2026/) or [Tuta](/posts/tutanota-review-2026/) — see [the comparison](/posts/tuta-vs-proton-mail-2026/)
- **Calendar**: [Encrypted calendar](/posts/best-end-to-end-encrypted-calendars-2026/)
- **VPN**: NordVPN or ProtonVPN
- **Password manager**: [Bitwarden or 1Password](/posts/best-password-managers-2026/)
- **2FA**: [Hardware key](/posts/yubikey-vs-nitrokey-vs-solokey-2026/)
- **Photos**: [Ente](/posts/ente-photos-review-2026/)
- **General files (legacy cloud)**: Cryptomator
- **General files (new cloud)**: Proton Drive or Tresorit

Cryptomator fills the "I have legacy cloud accounts I cannot abandon" gap. Combined with the rest, you get a coherent privacy stack.

<a href="https://go.digitalshieldpro.com/protonmail" target="_blank" rel="nofollow sponsored noopener">Pair with Proton Mail for full email + file privacy</a>

## My Verdict

Cryptomator is one of the most useful privacy tools I have installed in the last five years. Free on desktop, €15 once on mobile, fully open source, no subscription. The functionality is exactly what it claims. The cloud provider sees nothing.

The limitations (no multi-user sharing in the free product, no web access, awkward iOS editing) are real but tolerable. For my use case — adding encryption on top of existing cloud accounts I cannot abandon — Cryptomator is the only practical answer.

If I were starting from zero, I would use Proton Drive instead and skip the layer. But starting from where I am — Dropbox, Google Drive, OneDrive accounts with years of accumulated files and shared folders — Cryptomator is the only tool that bridges where I am to where I want to be.

For broader privacy-stack reading, see [the encrypted email comparison](/posts/best-encrypted-email-protonmail-vs-tutanota-2026/), [Posteo review](/posts/posteo-review-2026/), [Mailfence review](/posts/mailfence-review-2026/), [Ente Photos review](/posts/ente-photos-review-2026/), [GrapheneOS vs iOS](/posts/grapheneos-vs-ios-privacy-2026/), and [YubiKey vs Nitrokey vs SoloKey](/posts/yubikey-vs-nitrokey-vs-solokey-2026/).

## Bottom Line

Download the desktop app for free. Buy the mobile app once for €15. Encrypt the cloud folders you cannot move off. Stop worrying about which cloud provider's employee can read your tax returns.

Cryptomator is one of the best deals in privacy software in 2026. The pricing model alone (free desktop, one-time mobile) is the kind of model the privacy software industry needs more of. The product is also genuinely good.

For users with existing cloud accounts and important files inside them: install Cryptomator this weekend. The 10 minutes of setup is the smallest privacy-improvement-per-minute investment available in 2026.
