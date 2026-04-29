---
title: "How to Encrypt Files in 2026: VeraCrypt, Cryptomator"
date: 2026-05-30T10:00:00+01:00
lastmod: 2026-05-30T10:00:00+01:00
description: "Step-by-step guide to encrypting files on Windows, macOS, and Linux using VeraCrypt and Cryptomator."
categories: ["encryption"]
tags: ["file encryption", "veracrypt", "cryptomator", "data security", "encryption tools"]
keywords: ["how to encrypt files 2026", "veracrypt tutorial", "cryptomator review", "file encryption software", "encrypt files windows mac linux"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity researcher and writer. Tests privacy tools and security software hands-on."
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1614064641938-3bbee52942c7&w=1200&output=webp&q=70"
faq:
  - q: "Is VeraCrypt safe to use in 2026?"
    a: "Yes. VeraCrypt has been independently audited multiple times — most recently with findings addressed in the 1.25 release cycle. It uses AES-256, Twofish, and Serpent ciphers and remains the gold standard for free open-source disk encryption. No backdoors have ever been found."
  - q: "What is the difference between VeraCrypt and Cryptomator?"
    a: "VeraCrypt creates encrypted containers or fully encrypts drives/partitions. Cryptomator encrypts files individually and is designed for cloud storage like Dropbox or Google Drive. For local disk encryption use VeraCrypt; for cloud sync use Cryptomator."
  - q: "Can I encrypt files without any software on Windows?"
    a: "Windows 10 Pro and 11 Pro include BitLocker for drive encryption and EFS (Encrypting File System) for individual files. However, BitLocker keys are often tied to your Microsoft account and EFS has known recovery complexity issues. For sensitive data, dedicated tools like VeraCrypt give you more explicit control."
  - q: "Does encrypting files slow down my computer?"
    a: "Modern CPUs include AES-NI hardware acceleration, so the performance hit from AES-256 encryption is typically less than 5% on most read/write operations. You will not notice slowdowns during normal use. Only systems older than around 2013 might show measurable lag."
  - q: "What happens if I forget my VeraCrypt password?"
    a: "There is no recovery option. If you forget the password and have no backup of the header, the data is permanently inaccessible. This is a feature, not a bug — but it means you must store your passphrase in a password manager or write it down and store it securely offline."
  - q: "Can I use Cryptomator on mobile devices?"
    a: "Yes. Cryptomator has official apps for Android and iOS. The mobile apps cost a one-time fee (around $15) while the desktop version is free. The apps connect to your cloud provider directly and decrypt files on the fly."
  - q: "Is it legal to encrypt my files?"
    a: "In most countries, yes — encrypting personal files is completely legal. A small number of countries restrict strong encryption or require disclosure of keys under certain legal proceedings. If you are operating in a high-risk jurisdiction, check local regulations."
products:
  - name: "NordVPN"
    url: "https://go.digitalshieldpro.com/nordvpn"
    price: ""
---

I have been encrypting files for over a decade, and in that time I have watched people lose access to their data in two ways: someone stole it, or they got locked out of their own encrypted drive. Both outcomes are preventable. In 2026, file encryption is easier than it has ever been — and there is no longer any excuse to store sensitive documents unprotected.

This guide is about doing it right. I will walk you through two tools I use personally — VeraCrypt for local containers and full-disk encryption, and Cryptomator for cloud-synced vaults — with actual step-by-step instructions, not just a features overview.

*This article contains affiliate links. I earn a small commission if you purchase through my links, at no extra cost to you.*

---

## Why File Encryption Still Matters in 2026

In 2025, the Identity Theft Resource Center reported 3,205 publicly disclosed data breaches in the US alone. The Verizon 2025 Data Breach Investigations Report found that 74% of breaches still involve the human element — but the underlying stolen asset in the majority of cases is unencrypted data sitting on a device, drive, or cloud account.

Encryption does not prevent a breach from happening. What it does is make the stolen data useless. If a thief takes your laptop, an encrypted drive shows them nothing. If a cloud provider is compromised, encrypted files remain opaque even to the attacker with full server access.

The threat model I work with most often:

- **Lost or stolen device** — most common, most practical threat for most people
- **Cloud provider breach** — relevant if you store anything sensitive on Dropbox, Google Drive, or iCloud
- **Insider threat** — relevant for businesses, less so for individuals
- **Legal discovery / government access** — relevant for journalists, activists, lawyers

For the first two threats, VeraCrypt and Cryptomator address the risk directly and for free.

---

## Tool Overview: VeraCrypt vs Cryptomator

Before diving into setup, here is how the two tools differ at a fundamental level.

### VeraCrypt

VeraCrypt is the successor to TrueCrypt after TrueCrypt was abandoned in 2014. It encrypts entire drives, partitions, or creates encrypted container files that act like virtual drives. You mount the container, work with the files normally, then dismount it — the data is encrypted at rest and in transit.

**Best for:**
- Encrypting a full external hard drive or USB drive
- Creating a secure vault on your local machine
- Deniable encryption (hidden volumes)
- High-security local file storage

**Platforms:** Windows, macOS, Linux
**Price:** Free, open-source

### Cryptomator

Cryptomator takes a different approach: it encrypts each file individually using its own cloud-agnostic vault format. You create a vault in your Dropbox, Google Drive, or any synced folder, and Cryptomator encrypts files before they leave your machine. The cloud provider never sees unencrypted content.

**Best for:**
- Cloud storage you do not fully trust
- Files you need synced across devices via Dropbox/Google Drive
- Users who want transparent, per-file encryption

**Platforms:** Windows, macOS, Linux, Android, iOS
**Price:** Desktop free; mobile apps are one-time ~$15 purchase

---

## Part 1: How to Use VeraCrypt

### Installation

Download VeraCrypt from the official site at veracrypt.fr. Always verify the signature before installing — the site provides SHA-256 and PGP signatures for every release. This takes two minutes and guarantees you downloaded the real binary.

On Windows: run the standard installer. On macOS: install the .dmg, but note you will also need macFUSE installed first (available at osxfuse.github.io). On Linux: install via your package manager or compile from source.

### Creating an Encrypted Container File

This is the most practical use case for most people — a secure vault file you can move around like any other file.

**Step 1: Open VeraCrypt and click "Create Volume"**

You will see three options:
- Create an encrypted file container
- Encrypt a non-system partition/drive
- Encrypt the system partition/drive

Select "Create an encrypted file container" for now.

**Step 2: Choose Standard or Hidden Volume**

Standard VeraCrypt volume is what 99% of people need. A Hidden volume lets you create a decoy container — more on that below.

**Step 3: Pick a location and filename**

Navigate to where you want the container file. I keep mine in a folder called "Archive" — nothing suspicious about a file called "backup.vc" sitting alongside other files. The filename does not matter; the encryption is in the content.

**Step 4: Choose encryption algorithm**

AES is the default and the right choice for almost everyone. It uses hardware acceleration on modern CPUs and has never been broken in practice. If you want extra paranoia, you can choose AES-Twofish-Serpent cascaded encryption, but you will see a performance hit and the practical security difference is negligible.

For hash algorithm, leave it at SHA-512.

**Step 5: Set the volume size**

VeraCrypt containers are fixed size. Decide how much space you need — 5 GB, 20 GB, 50 GB. You cannot easily resize later, so plan ahead. I typically create containers 20-30% larger than I think I need.

**Step 6: Set a strong passphrase**

This is the most critical step. Your passphrase is the only protection between an attacker and your data. Use a random passphrase of at least 20 characters — ideally 30+ characters using a mix of words, numbers, and symbols. Store it in your password manager immediately.

Do not use a password you use anywhere else. Do not use your name or anything memorable. Random is the only correct approach.

**Step 7: Format the volume**

VeraCrypt will ask you to move your mouse randomly to generate entropy for the encryption key. Move your mouse around for at least 30 seconds. Then click Format. Depending on size, this takes 30 seconds to a few minutes.

### Mounting and Using Your Vault

1. Open VeraCrypt
2. Click "Select File" and find your container
3. Click "Mount"
4. Enter your passphrase
5. The container appears as a new drive letter (Windows) or mount point (macOS/Linux)
6. Work with files normally
7. When done, click "Dismount" in VeraCrypt

The mounted drive behaves like any normal drive. Drag files in, open documents, save changes. Everything written to it is encrypted automatically.

**Important habit:** Always dismount before putting your laptop to sleep or leaving it unattended. A mounted volume is accessible to anyone who sits down at your computer.

### Full-Drive Encryption with VeraCrypt

For encrypting an entire external drive or USB stick:

1. Back up all data on the drive first — formatting will erase everything
2. In VeraCrypt, select "Create Volume" → "Encrypt a non-system partition/drive"
3. Select your external drive from the list (be very careful to select the right drive)
4. Follow the same steps as above — set passphrase, format

After formatting, the drive is completely encrypted. Every time you plug it in, VeraCrypt will ask for the passphrase before mounting it.

### System Drive Encryption (Windows)

System encryption protects your entire Windows installation. If someone removes your hard drive or boots from a USB, they see only encrypted garbage.

1. In VeraCrypt, select "Create Volume" → "Encrypt the system partition or entire system drive"
2. Follow the wizard — it will create a rescue disk first (required)
3. Run the pre-test to verify your system can boot with the new bootloader
4. After a successful pre-test, encryption starts

This takes several hours on a full drive but runs in the background. Afterward, every boot requires your VeraCrypt passphrase before Windows loads.

**Note for macOS users:** Use FileVault instead for system encryption. Apple's T2 and M-series chips handle system encryption at a hardware level that VeraCrypt cannot match on Apple silicon.

### Hidden Volumes (Deniable Encryption)

VeraCrypt's hidden volume feature is remarkable: you create two volumes in the same container, each with a different passphrase. Enter passphrase A and you see harmless files. Enter passphrase B and you see the actually sensitive material.

If someone forces you to reveal your passphrase (rubber-hose cryptanalysis), you give them passphrase A. There is no way to prove a hidden volume exists.

To set this up, choose "Hidden VeraCrypt volume" during the creation wizard. You will create the outer volume first, put some plausible decoy content on it, then create the hidden volume within the free space of the outer container.

This is relevant for journalists, activists, or anyone operating under an authoritarian government. For most people, a standard volume is sufficient.

---

## Part 2: How to Use Cryptomator

### Installation and Setup

Download Cryptomator from cryptomator.org. It is open-source and the desktop version is completely free. After installation:

1. Open Cryptomator
2. Click "Add Vault" → "Create New Vault"
3. Navigate to your cloud sync folder (e.g., your Dropbox or Google Drive folder)
4. Create a folder for the vault — I use a name like "Encrypted" or "Vault"
5. Set a passphrase

That is it. Cryptomator creates a vault structure inside that folder. When your cloud provider syncs, it uploads the encrypted vault files — individual encrypted chunks, not the original files.

### Adding and Accessing Files

When you want to add files:

1. Open Cryptomator
2. Click the unlock icon next to your vault
3. Enter your passphrase
4. The vault mounts as a virtual drive
5. Copy or move files into it
6. When done, lock the vault

The files are now encrypted on your drive and in the cloud. Your cloud provider sees only encrypted chunks — they cannot read the file names, content, or metadata.

### Why Per-File Encryption Matters for Cloud

The key architectural difference from VeraCrypt is that Cryptomator encrypts each file individually. This means:

- When you update one file, only that file's encrypted version needs to re-upload
- Sync is efficient — no re-uploading an entire 10 GB container because you edited one document
- The cloud provider syncs normally; they just cannot read the content

For a VeraCrypt container synced via Dropbox, every change to any file inside modifies the container, triggering a re-sync of the entire container. For a 10 GB VeraCrypt vault, that means uploading 10 GB every time you change a single document. Cryptomator avoids this entirely.

---

## Part 3: Built-In Options Worth Knowing

### BitLocker (Windows Pro and Enterprise)

If you are on Windows 10 Pro or Windows 11 Pro, BitLocker is already installed. It offers:

- Full-drive and external drive encryption
- TPM integration for transparent login (no passphrase required at boot)
- Recovery keys stored in your Microsoft account or Active Directory

For most Windows users, BitLocker is the right answer for system encryption. The concern I have with it is the recovery key backup to Microsoft accounts — if you are protecting data from government access, that is a problem. For protecting against laptop theft, it is fine.

**How to enable:** Right-click on a drive in Windows Explorer → "Turn on BitLocker."

### FileVault (macOS)

FileVault is macOS's built-in full-disk encryption. On Apple silicon Macs, it is backed by the Secure Enclave — a dedicated hardware chip that makes brute-force attacks practically impossible.

**How to enable:** System Settings → Privacy & Security → FileVault → Turn On.

FileVault recovery keys can be stored in your Apple ID account or written down locally. For high-security use cases, store the key locally only.

### LUKS (Linux)

Linux Unified Key Setup is the standard for Linux disk encryption. Most Linux distributions offer LUKS encryption during installation.

For encrypting after installation or for containers:

```
# Create an encrypted container file
dd if=/dev/urandom of=vault.img bs=1M count=500
cryptsetup luksFormat vault.img
cryptsetup luksOpen vault.img myVault
mkfs.ext4 /dev/mapper/myVault
mount /dev/mapper/myVault /mnt/vault
```

LUKS supports multiple keyslots, meaning you can have multiple passphrases for the same encrypted volume — useful for team access or backup passphrases.

---

## My Personal Encryption Setup

Here is how I actually organize things in 2026:

**Local sensitive files:** VeraCrypt container, 50 GB, stored on my main machine. Password stored in my password manager. I mount it when I need it, dismount when I am done.

**External backup drive:** Full VeraCrypt encryption. The drive stays encrypted always. I mount it once a week for backups, then lock it.

**Cloud documents:** Cryptomator vault inside my Google Drive folder. Work documents, client files, anything I need synced but do not want Google indexing.

**System drive:** FileVault on my MacBook (M2). BitLocker on my Windows workstation.

This covers all my realistic threat scenarios. Laptop stolen: nothing accessible. Cloud hacked: encrypted garbage. Backup drive lost: same.

---

## Choosing the Right Encryption Algorithm

VeraCrypt gives you several encryption options. Here is when each makes sense:

**AES-256 (default):** The right choice for 99% of users. AES has been the global encryption standard since 2001, has never been broken in practice, and is hardware-accelerated on virtually all modern CPUs. Performance is excellent and security is beyond reproach.

**Twofish:** A finalist in the AES selection process alongside Rijndael (which became AES). Twofish is extremely well-studied and considered secure. Performance is slightly slower than AES without hardware acceleration.

**Serpent:** The most conservative choice — Serpent was considered to have the highest security margin of the AES finalists but was not selected due to performance. In 2026, Serpent is more than adequate; it is just slower.

**Cascaded algorithms (AES-Twofish, AES-Twofish-Serpent):** Using multiple encryption algorithms in sequence means an attacker needs to break all of them. The practical security gain over single AES is negligible — AES has not been broken and likely will not be in our lifetimes. The performance cost is significant. Cascaded encryption is for people with extremely specific paranoia requirements, not general use.

**Recommendation:** Use AES. If you feel strongly about using an alternative, use Twofish or Serpent. Cascaded algorithms are not worth the performance hit for any realistic use case.

For the hash algorithm, SHA-512 is the correct choice — it is used to derive the actual encryption key from your passphrase. SHA-256 is also fine. Whirlpool is an alternative if you want something different from the SHA family.

---

## Encrypting Specific File Types

Different file types warrant different approaches:

### Sensitive Documents (Tax Records, Legal Files, Medical Records)

These belong in a VeraCrypt container or folder-level Cryptomator vault. They are accessed infrequently enough that the mounting/dismounting workflow is not a friction point.

Recommended structure:
```
VeraCrypt container (20-50 GB)
├── Financial/
│   ├── Tax returns/
│   └── Bank statements/
├── Legal/
├── Medical/
└── Identity/
    ├── Passport scan
    └── Insurance cards
```

### Photos and Videos (Privacy Concern)

Personal photos with location data, photos of sensitive documents, or anything you do not want accessible to an attacker. Cryptomator vault in your cloud storage is ideal — photos stay synced but the cloud provider cannot access them.

Before adding photos to any encrypted vault, consider stripping EXIF metadata from them first. Even in an encrypted vault, if those photos are later shared elsewhere, the metadata travels with them.

### Code and Work Projects

If you work on confidential client projects, a VeraCrypt container for client work keeps everything isolated. When you finish a project and archive it, the encrypted container travels cleanly without risk.

For active development work, Cryptomator in a cloud-synced folder lets you work normally while keeping code away from the cloud provider.

### Cryptocurrency and Private Keys

These deserve the highest-security treatment: a dedicated VeraCrypt container with a strong passphrase (different from all other passphrases), stored on an offline device, with the passphrase written down and stored in a separate physical location from the device. The vault for private keys should never be connected to the internet.

---

## Common Mistakes to Avoid

**Leaving containers mounted.** A mounted VeraCrypt volume is just an open folder. Anyone with access to your computer can read it. Dismount when you walk away.

**Weak passphrases.** Encryption is only as strong as the passphrase protecting it. "Password123" with AES-256 is still trivially crackable. Use a random passphrase from your password manager.

**No passphrase backup.** Forgetting your VeraCrypt password means permanent data loss. Store it in your password manager. Write it down and keep it in a safe. Never rely on memory alone.

**Using cloud storage for VeraCrypt containers without Cryptomator.** As explained above, this causes massive re-sync overhead. Use Cryptomator for cloud sync.

**Encrypting backups but not verifying them.** Test your encrypted backup restore process at least twice a year. I have seen people discover their backup was corrupted only when they actually needed it.

**Encrypting without a backup.** Encryption and backup are two different things. An encrypted drive that fails is still a failed drive — your data is gone. Always maintain an encrypted backup on a separate physical device.

**Over-complicated setups you do not maintain.** The best encryption setup is one you actually use consistently. A simple VeraCrypt container with a strong passphrase that you use every day is far better than an elaborate multi-layer setup that is so inconvenient you stop using it after a week.

---

## Encryption and the Law: What You Need to Know

In most countries, encrypting your files is entirely legal. However, there are situations where law can intersect with encryption:

**Key disclosure laws:** Several countries, including the UK (RIPA Part III), Australia, Canada, and others have laws that can require you to provide encryption keys under certain legal proceedings. In the UK, refusing to provide a key when ordered to do so is a criminal offense. In the US, there is an ongoing legal debate about whether compelling key disclosure violates Fifth Amendment protections.

**This affects threat models:** If you are encrypting data to protect it from government access specifically, research the key disclosure laws in your jurisdiction.

**VeraCrypt's plausible deniability:** Hidden volumes specifically address key disclosure scenarios — you can provide the outer volume passphrase under legal compulsion while the inner volume's existence remains unverifiable. This is a legitimate use of VeraCrypt for people in relevant situations.

**Employment:** If you encrypt files on work equipment, review your employment contract. Many companies have policies about encryption keys for work-related data.

For personal data protection against the most common threats — theft, unauthorized access, cloud provider breach — legal concerns are not relevant. Encrypt your files.

---


<a href="https://go.digitalshieldpro.com/nordpass" class="cta-affiliate" rel="nofollow noopener sponsored" target="_blank">View Nordpass →</a>

## Conclusion

File encryption in 2026 is accessible, free, and fast. VeraCrypt handles local containers and full-drive encryption with proven security and complete open-source transparency. Cryptomator solves the cloud sync problem without sacrificing sync efficiency.

There is no good reason to keep sensitive files unencrypted. The tools are free, the setup takes less than 30 minutes, and the protection is real. A stolen laptop with VeraCrypt-encrypted drives costs you hardware. Without encryption, it costs you your data, your identity, and potentially your finances.

Start with a VeraCrypt container for your most sensitive files. If you use cloud storage for anything important, add a Cryptomator vault. These two tools together cover virtually every practical threat scenario for individuals and small businesses alike.


<a href="/go/nordpass" class="cta-affiliate" rel="sponsored noopener">View Nordpass</a>
