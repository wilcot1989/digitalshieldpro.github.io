---
title: 'How to verify PGP signatures 2026: a practical guide'
date: 2026-09-22 09:00:00+02:00
lastmod: 2026-09-22 09:00:00+02:00
description: PGP signatures are useless if you do not actually verify them. Here is the step-by-step I follow for software releases, email, and identity claims — including the trust-on-first-use trap.
categories:
- encrypted-email
tags:
- pgp
- gpg
- signature verification
- guide
- email security
keywords:
- how to verify pgp signature
- gpg verify signature
- verify software signature
- pgp fingerprint check
- web of trust
affiliate: true
author: James Mitchell
author_bio: Cybersecurity analyst with 10+ years of hands-on experience testing VPNs, antivirus software, and privacy tools.
featured_image: /images/categories/email-security.svg
faq:
- q: What does verifying a PGP signature actually prove?
  a: 'Two things, conditionally. First, the signed content was not modified after signing — the cryptographic hash matches. Second, the message was signed by someone holding the private key corresponding to a specific public key. What it does NOT prove on its own is that the public key actually belongs to the person you think it does. Identity-to-key binding requires separate verification (in-person fingerprint check, web of trust, or notarized publication).'
- q: How do I verify a signature in Thunderbird?
  a: 'Open the signed message. Thunderbird displays a "verified signature" badge at the top if the sender''s public key is in your keyring. Click the badge for details: signing key fingerprint, signing time, and trust level. If the key is not in your keyring, Thunderbird shows "unverified signature" — you can import the key from the message or fetch it from a key server.'
- q: How do I verify a software release signature on the command line?
  a: 'Three steps. First, download the software file (e.g. tor-browser-15.0.tar.xz) and the signature file (tor-browser-15.0.tar.xz.asc). Second, import the developer''s public key (gpg --recv-keys KEYID or download and import manually). Third, run gpg --verify tor-browser-15.0.tar.xz.asc tor-browser-15.0.tar.xz. The output should say "Good signature from..." with the developer name. If it says "BAD signature" or "Can''t check signature: No public key" then either the file is tampered or you do not have the correct key.'
- q: What is a key fingerprint and how do I check it?
  a: 'A fingerprint is a SHA-1 or SHA-256 hash of the public key, typically displayed as 40 hex characters in groups of 4. It is short enough to read out loud or print on a business card. To check: get the claimed fingerprint from a trusted out-of-band source (the developer''s personal website, a printed handout, an in-person meeting), then compare against the key in your keyring with gpg --fingerprint KEYID. They must match exactly.'
- q: What is "trust on first use" and why is it dangerous?
  a: '"Trust on first use" (TOFU) is the practice of importing a public key the first time you receive a message from someone, without verifying the fingerprint independently. The key is trusted simply because it arrived with the message. The danger: if an attacker intercepts your first communication and substitutes their key, you trust the attacker''s key forever. Real verification requires comparing the fingerprint through a separate channel BEFORE you trust the key.'
- q: How does the web of trust work?
  a: 'You sign other people''s public keys after verifying their fingerprints in person. Their keys then carry your signature, vouching for them. When you encounter a key you have not personally verified, you can check whether it has been signed by someone you have already verified — transitively, this builds a "web of trust." In 2026 the web of trust is largely deprecated due to historic key-server spam attacks, but the concept lives on in modern alternatives like Signed Sigsum and Notary.'
- q: Do I need to verify signatures on every email?
  a: 'No — that level of paranoia is impractical. Most email signatures are informational. Verify signatures when the stakes warrant it: software downloads (always), security advisories (always), large financial transactions (always), and any time the message itself claims something that would be unverifiable without the signature ("this is your court summons", "this is the actual key for X"). For routine encrypted email, the encryption is the protection — signature verification is mostly for non-repudiation.'
- q: What if a signature shows "expired" or "revoked"?
  a: 'Treat it as unsigned. Expired keys can no longer be used to make new signatures (any new signature with an expired key indicates clock manipulation or improper handling). Revoked keys have been publicly marked as compromised by the key owner — never trust signatures with a revoked key. Both states show clearly in Thunderbird, GnuPG, and other tools. If you see one, contact the sender through a separate channel.'
products:
- name: Proton Mail Plus
  url: https://proton.me/mail/pricing
  price: '4.99'
- name: YubiKey 5C
  url: https://www.yubico.com/product/yubikey-5c/
  price: '55'
schema_type: HowTo
---

{{< affiliate-disclosure >}}

PGP signatures are useless if you do not actually verify them. I see this constantly: developers publish signed software releases, users download the software but never check the signature. Sources sign emails to journalists, journalists never verify them. The signature exists; it is functionally decoration.

This is the practical guide to verifying PGP signatures the way it is supposed to be done. I cover three workflows I do regularly: verifying software releases (Tor Browser, GPG itself, OpenWrt), verifying email signatures from contacts, and verifying public key fingerprints before trusting a new identity.

The single most important point: a verified signature only proves that the message was signed by someone holding a specific private key. It does NOT prove that key belongs to the person you think it does. The hard part is binding the key to a real-world identity.

---

## What a PGP signature actually proves

Before the how-to, the conceptual basics. A PGP signature is a cryptographic operation that binds three things together:

1. The content of a message or file (via a hash)
2. A public key (which has a corresponding private key)
3. A timestamp

If you have the public key and you run a verification operation, you can confirm that:

- The content has not been modified since signing
- Whoever signed it had access to the corresponding private key at signing time

What this does NOT confirm:

- That the public key belongs to the named person
- That the named person actually authored the content (someone could have tricked them into signing)
- That the private key was not stolen

Identity-to-key binding is the hard part. It requires out-of-band verification — meeting in person, checking a fingerprint published in a trusted location, or building a web of trust.

For more on the encryption fundamentals see [encrypted email vs PGP](/posts/encrypted-email-vs-pgp-2026/).

## Workflow 1: Verifying a software release

This is the workflow most people should learn first. It comes up every time you download security-sensitive software.

Example: verifying a Tor Browser download.

**Step 1: Download the software AND the signature.** Tor Browser downloads from torproject.org/download/ include both. Get tor-browser-linux-x86_64-15.0.tar.xz and tor-browser-linux-x86_64-15.0.tar.xz.asc.

**Step 2: Get the Tor Project signing key.** Two options.

Option A — fetch from a key server:

```
gpg --auto-key-locate nodefault,wkd --locate-keys torbrowser@torproject.org
```

Option B — download the public key file from the Tor Project's website and import:

```
gpg --import tor-developer-key.asc
```

**Step 3: Verify the fingerprint.** This is the critical step that most people skip. The Tor Project publishes the signing key fingerprint on multiple separate channels (the official website, the Tor Project blog, archive.org snapshots, multiple developer Twitter accounts). Get the fingerprint from at least two independent sources. Then check:

```
gpg --fingerprint torbrowser@torproject.org
```

The output shows the key fingerprint. It must exactly match the fingerprint published on torproject.org. If it does not match, an attacker may have intercepted your key fetch.

**Step 4: Verify the signature.**

```
gpg --verify tor-browser-linux-x86_64-15.0.tar.xz.asc tor-browser-linux-x86_64-15.0.tar.xz
```

Expected output:

```
gpg: Signature made [date] using RSA key ID [keyid]
gpg: Good signature from "Tor Browser Developers (signing key) <torbrowser@torproject.org>"
```

If the signature is good and the fingerprint matched in step 3, you have verified the software is what the Tor Project published.

**Step 5: Install and run only after verification passes.** Never run a binary whose signature failed verification — even if the file looks legitimate. That is the entire point of the verification process.

## Workflow 2: Verifying an email signature

Email signatures are a different threat model. The signature is usually fine; the question is whether the sending key actually belongs to the claimed person.

Example: a journalist receives an encrypted+signed email from a source claiming to be "Alex Kim, security researcher at Acme Corp."

**Step 1: Open the message in a PGP-aware client.** Thunderbird with native OpenPGP, Apple Mail with GPG Suite, K-9 Mail with OpenKeychain, or [Mailvelope on Gmail web](/posts/best-pgp-email-clients-2026/).

**Step 2: Read the signature status.** The client shows whether the signature is valid (cryptographically) and whether the signing key is trusted (identity-bound).

- **Valid signature, trusted key:** the message has not been tampered AND you have previously verified that this key belongs to Alex Kim.
- **Valid signature, untrusted key:** the message has not been tampered, but you have not verified the key-to-identity binding.
- **Invalid signature:** the message has been tampered with OR was signed by a different key than the one you have for Alex.

**Step 3: For an untrusted key, verify the fingerprint out of band.** Call Alex on a verified phone number. Read the first 8 hex groups of the fingerprint. Have Alex read theirs back. If they match, mark the key as trusted in your keyring.

**Step 4: For an invalid signature, do not trust the message.** Contact Alex through a verified channel and ask whether they sent it. The signature failure could be malicious tampering or could be a key mismatch (Alex regenerated their key).

For the full set of PGP-aware email clients, see [best PGP-compatible email clients](/posts/best-pgp-email-clients-2026/).

## Workflow 3: Verifying a public key fingerprint

This is the foundational workflow that makes everything else possible. If you can reliably verify fingerprints, you can build trust in keys, signatures, and signed software.

**Method A: In-person verification.** The strongest. Meet the person, exchange business cards or QR codes containing the fingerprint, compare digit-by-digit. Common at security conferences, key-signing parties, journalist-source meetings.

**Method B: Verified phone call.** Call a number you have independently verified (e.g. through their employer's official directory). Read the fingerprint out loud, ask them to read theirs. Match.

**Method C: Trusted out-of-band publication.** The fingerprint is published in multiple independent locations under the person's control: their personal website, their Twitter profile, their HN comment history, their employer's bio page, a Keybase profile, archived web snapshots from before any compromise. Compare the fingerprint across all of them.

**Method D: Web of trust.** Someone you have verified has signed the new person's key. The chain of trust transitively vouches for the new key. This was the dominant model in the 1990s and 2000s but has weakened due to the [SKS keyserver spam attacks of 2019](/posts/encrypted-email-vs-pgp-2026/) and the resulting deprecation of public keyservers.

**Method E: TOFU (Trust on First Use).** The dangerous one. You import the key the first time you encounter it, no verification. Modern PGP clients default to this for convenience. It is the right choice for low-stakes communication. It is the wrong choice for journalist-source contact, financial verification, or software release signing.

## The fingerprint format

A modern OpenPGP fingerprint looks like this:

```
9E0F 1B5F E8FE 4C4D D9B0  6B26 8888 9999 AAAA BBBB
```

Forty hex characters, grouped in five-character blocks. Some tools display it without spaces. Some display only the last 16 characters ("long key ID") or last 8 ("short key ID"). Always use the full fingerprint for verification — short key IDs are vulnerable to collision attacks.

Display the fingerprint of a key in your keyring:

```
gpg --fingerprint email@example.com
```

Or:

```
gpg --fingerprint KEYID
```

## Common mistakes

After running verification workflows for years, here are the mistakes I see most often.

**Mistake 1: Verifying short key IDs instead of full fingerprints.** Short key IDs (8 hex characters) can be collided by attackers in a few hours of CPU time. Always check the full 40-character fingerprint.

**Mistake 2: Fetching keys from public key servers without verification.** SKS key servers are spammy and unreliable. Modern key servers (keys.openpgp.org) verify email control before accepting key uploads, which is better — but you still need to verify fingerprints out of band before trusting the key.

**Mistake 3: TOFU on high-stakes correspondence.** If your threat model includes targeted attacks (journalism, activism, legal), Trust on First Use is not enough. Verify fingerprints out of band before the first sensitive message.

**Mistake 4: Ignoring expired/revoked warnings.** Tools warn you for a reason. An expired key cannot make new signatures legitimately. A revoked key has been declared compromised. Both states should stop the workflow.

**Mistake 5: Verifying software signatures using the same channel as the download.** If you download Tor Browser from torproject.org and fetch the signing key from torproject.org, an attacker who controls torproject.org (DNS hijack, server compromise) controls both. Get the fingerprint from a separate trusted source — archive.org snapshots, the Tor Project's printed materials at conferences, a developer's personal website.

**Mistake 6: Skipping verification because "it works."** "I downloaded the file and it runs fine, so it must be legitimate." Malware is designed to run fine. Verification is the only way to detect tampering before damage occurs.

## Tools

**On the command line:**

- **GnuPG (gpg)** — the canonical OpenPGP tool. Available on every Linux distribution, macOS via Homebrew, Windows via Gpg4win.
- **Sequoia PGP** — a modern Rust-based reimplementation. Cleaner interface, fewer footguns. Worth learning if you are starting fresh.

**In email clients:**

- **Thunderbird** — native OpenPGP since version 78. The desktop standard.
- **Apple Mail + GPG Suite** — clean integration on macOS.
- **K-9 Mail + OpenKeychain** — the Android default.
- **[Mailvelope](/posts/how-to-encrypt-gmail-without-leaving-2026/)** — browser extension for Gmail/Outlook web.

**For hardware-backed verification:**

- **YubiKey OpenPGP applet** — hardware key holds your private key; signing operations happen on-device.
- **Nitrokey** — open-hardware alternative.
- **SoloKey** — open-source alternative with a smaller footprint.

For the hardware key comparison see [YubiKey vs Nitrokey vs SoloKey](/posts/yubikey-vs-nitrokey-vs-solokey-2026/).

## My personal verification policy

For full transparency, here is the policy I follow.

**Always verify:**

- Software downloads (Tor Browser, GPG, operating system images, security tools)
- Security advisories from organizations I follow
- Cryptographic protocol implementations (OTR, Signal Protocol, Sigsum)
- Anything purporting to be from a public figure I have a verified key for

**Verify on first contact:**

- New email correspondents who plan to exchange encrypted mail with me
- New journalists, activists, or sources I work with
- New developers I plan to download software from

**TOFU is acceptable:**

- Casual encrypted correspondence (friends and family who use Proton Mail)
- One-off encrypted messages where the stakes are low
- Test messages during initial encryption setup

**Verify out of band before trust:**

- Anyone claiming to be a public figure
- Anyone planning to send me a payment, contract, or legal document
- Anyone whose key arrives via a channel I do not fully trust

The point is to apply effort proportional to the stakes. Heavy verification for high-stakes correspondence; lighter for low-stakes; none for purely informational signatures.

## Get started

For email-based PGP verification, [Proton Mail](https://go.digitalshieldpro.com/protonmail){target="_blank" rel="nofollow sponsored noopener"} Plus or [Mailfence](/posts/mailfence-review-2026/) gives you OpenPGP support. Pair it with Thunderbird (free) for desktop verification.

For hardware-backed verification, a [YubiKey](https://www.yubico.com/product/yubikey-5c/) holds your signing keys on a tamper-resistant device. The OpenPGP applet works with Thunderbird, GnuPG, and most PGP-aware tools.

For more on the broader PGP ecosystem, see [encrypted email vs PGP](/posts/encrypted-email-vs-pgp-2026/), [best PGP-compatible email clients](/posts/best-pgp-email-clients-2026/), and [encrypted email metadata leaks](/posts/encrypted-email-metadata-leaks-2026/).

For hardening the operating system you do verification on, see [best privacy-focused operating systems](/posts/best-privacy-operating-systems-2026/).
