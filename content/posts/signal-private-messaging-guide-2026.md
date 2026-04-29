---
title: "How to Use Signal Properly in 2026"
date: 2026-05-12T10:00:00+01:00
lastmod: 2026-05-12T10:00:00+01:00
description: "The complete Signal private messaging guide for 2026. Disappearing messages, Signal usernames, group privacy settings, and advanced features tested hands-on."
categories: ["messaging"]
tags: ["Signal", "private messaging", "encrypted messaging", "Signal usernames", "disappearing messages", "secure chat"]
keywords: ["Signal guide 2026", "how to use Signal", "Signal disappearing messages", "Signal usernames privacy", "Signal group privacy", "secure messaging app"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity researcher and writer. Tests privacy tools and security software hands-on."
featured_image: "https://images.unsplash.com/photo-1555421689-491a97ff2040?auto=format&fit=crop&w=1600&q=80"
faq:
  - q: "Is Signal really private — can the company see my messages?"
    a: "No. Signal uses end-to-end encryption (the Signal Protocol) for all messages and calls. Not even Signal's own servers can decrypt your messages. Signal stores minimal metadata — it cannot see who you talk to, what you say, or when you communicated. A 2022 subpoena to Signal by US law enforcement resulted in Signal providing only two data points: the date your account was created and the date you last connected."
  - q: "What are Signal usernames and why do they matter?"
    a: "Signal usernames (introduced in 2024) allow you to share a username instead of your phone number with contacts. This is significant because your phone number is typically tied to your real identity through your carrier. With a username, you can use Signal without revealing your number — protecting your identity from new contacts."
  - q: "How long should I set disappearing messages?"
    a: "It depends on your use case. For sensitive communications (health, legal, financial), 24 hours or 1 week is appropriate. For general private conversations, 1-4 weeks balances privacy with the convenience of having message history. Note that disappearing messages only delete from your and the recipient's Signal app — screenshots and screen recordings are still possible."
  - q: "Is Signal safe for group chats?"
    a: "Yes. Signal group messages are fully end-to-end encrypted — Signal's servers cannot read them. Groups also have administrative features including the ability to require admin approval for new members, preventing someone from adding unknown contacts to sensitive group chats. Group metadata (member list) is encrypted on-device, not held by Signal's servers."
  - q: "Can I use Signal without giving my phone number to contacts?"
    a: "Yes, since the username feature launched. Set a username in Signal Settings > Account > Username. You can share your username (username.XX format) instead of your phone number. You can also hide your phone number from contacts who have not already connected with you via number."
  - q: "What is Signal's Note to Self feature useful for?"
    a: "Note to Self is effectively a private encrypted notepad synchronized across your Signal devices. I use it for storing sensitive information temporarily — 2FA backup codes before moving them to a password manager, temporary passwords, sensitive documents I need to access from multiple devices. Because it is end-to-end encrypted and stays within Signal's infrastructure, it is more private than cloud note-taking apps."
  - q: "Does Signal support two-factor authentication?"
    a: "Signal has a Registration Lock (PIN-based 2FA) that prevents someone from re-registering your phone number as a Signal account without your PIN. Enable it at Settings > Account > Registration Lock. This prevents SIM-swapping attacks where an attacker takes over your phone number and tries to register your Signal account."
products: []
---

I switched from WhatsApp to Signal in January 2021 following WhatsApp's privacy policy update that made data sharing with Meta more explicit. I have been using Signal as my primary messaging app since then, testing every new feature as it ships and occasionally running it alongside Wireshark to verify the metadata claims. This guide reflects three years of daily use and hands-on testing.

*This article contains affiliate links. We may earn a commission if you purchase through our links, at no extra cost to you.*

For complete digital privacy, combine Signal with a [privacy browser](/posts/best-privacy-browsers-2026/) and a [VPN service](/posts/best-vpn-services-2026/).

---

## Why Signal Is Different From Everything Else

There are dozens of messaging apps. Most claim to be "private" or "secure." The difference with Signal is technical, verifiable, and auditable.

### The Signal Protocol

Signal uses a cryptographic protocol (also called the Signal Protocol or Double Ratchet Algorithm) that is widely considered the gold standard for encrypted messaging. It is not a proprietary system invented by Signal — it is published research, peer-reviewed, and open-source. It is also used by WhatsApp, Google Messages (RCS), Facebook Messenger (in secret mode), and several others.

What the Signal Protocol provides:
- **End-to-end encryption**: Only sender and recipient can decrypt messages
- **Forward secrecy**: Each message uses a fresh key derivation; compromising one key does not expose past or future messages
- **Break-in recovery**: Even if a session key is compromised, future keys are secure
- **Deniability**: Message authentication is designed so that a recipient cannot prove to a third party that you sent a specific message

### What Signal Knows About You

Signal's architecture is designed around minimal data collection. Based on their transparency reports and responses to legal demands:

**What Signal stores:**
- Your phone number (required for registration)
- The date your account was created
- The date you last connected

**What Signal does not store:**
- Message contents
- Message metadata (who you message, how often)
- Group memberships or group member lists
- Profile photos
- Contact lists

In 2021, Signal published the results of a federal subpoena. Law enforcement received two data points: account creation date and last connected date. That is all Signal had to give.

Compare this to WhatsApp (owned by Meta), which collects: your phone number, contacts, usage data, purchase data, location, device identifiers, and shares this with Meta for advertising targeting.

---

## Getting Started: Installation and Basic Setup

### Download Signal From Official Sources Only

- **iOS**: App Store — search "Signal Messenger" by Signal Foundation
- **Android**: Google Play Store or direct APK from signal.org
- **Desktop**: signal.org/download (Windows, macOS, Linux)

Do not download Signal from third-party sources. Fake Signal apps with spyware have been distributed through unofficial channels.

### Account Registration

Signal requires a phone number for registration. This is a privacy trade-off — Signal uses your number to identify you to other contacts who have your number. The username feature (covered below) partially mitigates this.

During setup:
1. Enter your phone number
2. Receive SMS or voice verification code
3. Create a PIN (see Registration Lock below)
4. Set your display name and optional profile photo

### Set a Registration Lock PIN

Before anything else, enable Registration Lock.

Settings > Account > Registration Lock: Enable

Create a strong PIN (at least 8 digits — Signal allows alphanumeric). Store it in your password manager. Registration Lock prevents anyone who takes control of your phone number (via SIM swapping) from re-registering your Signal account.

Signal will remind you of your PIN periodically to prevent forgetting it.

---

## Part 1: Signal Usernames — The Privacy Game-Changer

Usernames were one of Signal's most significant feature additions. Here is exactly how they work and why they matter.

### Why Phone Numbers Are a Privacy Risk

When you share your phone number with someone, you are giving them:
- Your carrier's identity
- A number potentially tied to your real name in carrier records
- A number that appears in data broker databases
- A number that can be SIM-swapped

For many users — journalists, activists, people fleeing abusive situations, business contacts you prefer to keep at arm's length — sharing a phone number creates unwanted exposure.

### Setting Up a Signal Username

1. Open Signal
2. Settings (tap your avatar) > Account > Username
3. Tap "Set Username"
4. Choose a username (format: handle.XX where XX is a two-digit number)
5. Confirm

Your username becomes shareable as a link: signal.me/#eu/username

### Hiding Your Phone Number

After creating a username:

Settings > Privacy > Phone Number > Who can find me by my phone number

Options:
- **Everyone** (default) — anyone with your number can find you
- **Nobody** — only people you have already connected with can message you via number; new contacts must use your username

For maximum privacy: set "Who can find me by my phone number" to "Nobody." New contacts get your username, not your number.

### Username Link and QR Code

Signal generates a QR code and shareable link for your username. This is ideal for:
- Social media bios (signal.me/#eu/yourusername)
- Business cards
- Conference networking
- Any situation where you want contact without sharing your number

The link opens Signal directly on the recipient's device and initiates a connection request.

---

## Part 2: Disappearing Messages — The Most Important Setting

Disappearing messages are Signal's most underused feature. I have it set on every conversation. Here is how to use it properly.

### How Disappearing Messages Work

When enabled, messages are automatically deleted from both devices (sender and recipient) after the set timer expires. The timer starts when the message is read (not when it is sent).

What disappearing messages protect against:
- Someone finding your phone unlocked and reading message history
- Forensic analysis of a seized device (messages are gone)
- Signal's own servers (there is nothing to hand over if messages are deleted)
- Future account compromise (no historical messages to leak)

What they do not protect against:
- Screenshots taken before deletion
- Screen recording
- A recipient who reads the message before it deletes

### Setting Disappearing Messages

**Per conversation:** Open any conversation > Tap the name at the top > Disappearing messages > Choose duration

**Default for new conversations:** Settings > Privacy > Default Timer for New Chats > Choose duration

**My recommended settings:**
- Sensitive conversations (health, legal, financial): 1 week
- Close friends/family: 4 weeks
- General contacts: 1 month
- Group chats for sensitive topics: 1 week

### Timer Options in 2026

Signal offers: 30 seconds, 1 minute, 5 minutes, 30 minutes, 1 hour, 8 hours, 1 day, 1 week, 2 weeks, 1 month, and custom settings.

For very sensitive situations (e.g., confirming meeting locations), 30 minutes is a reasonable balance between usability and ephemeral privacy.

### Note: Both Parties Must Have Timer Active

If you set a 1-week timer but your contact manually disables it on their end, messages do not disappear on their device. Signal shows when a contact changes timer settings. If a contact keeps disabling your timers, that is useful information.

---

## Part 3: Group Chat Privacy

Signal groups offer strong privacy guarantees, but proper configuration is essential.

### How Signal Group Encryption Works

Signal uses a "sealed sender" design for group messages. In traditional group messaging, the server needs to know who sent a message to relay it to other members. Signal avoids this by encrypting sender information within the message payload — the server sees only that a message arrived for a group, not who sent it.

Group membership information is stored as an encrypted blob on Signal's servers but cannot be read by Signal itself. The keys are held only by group members.

### Creating a Private Group

1. New Group > Add participants
2. Set group name and photo
3. Once created: Group info > Edit (pen icon)

Key settings:
- **Require admin approval to join**: Prevents members from adding new contacts without your knowledge. Essential for sensitive groups.
- **Disappearing messages**: Set a group-wide timer
- **Announcement-only mode**: Only admins can send messages (useful for broadcast channels)

### Admin Controls

As group admin:
- Remove members who should no longer have access
- Revoke invite links if you shared a link and want to prevent further joins
- Rotate group membership: Signal supports re-keying a group when members are removed, so former members cannot decrypt future messages (this is automatic when a member is removed)

### What to Tell Group Members

Privacy is only as strong as the least careful member. When creating a sensitive group:
- Ask all members to enable disappearing messages
- Remind members not to screenshot conversations without reason
- Discuss whether to use usernames rather than real names in the group

---

## Part 4: Calls and Video Calls

Signal calls are end-to-end encrypted using DTLS (Datagram Transport Layer Security) and SRTP (Secure Real-time Transport Protocol). No call audio or video is accessible to Signal's servers.

### One-to-One Calls

Enable "Always Relay Calls" in Settings > Privacy > Advanced > Always Relay Calls. This routes calls through Signal's servers rather than creating a direct peer-to-peer connection. Without this setting, your IP address may be visible to the call recipient. With it enabled, calls are slightly higher latency but your IP is protected.

### Group Calls

Signal supports up to 50 participants in group video calls. Group calls are fully end-to-end encrypted — the same guarantees as messages.

To start a group call: Open a group > Phone or video icon in the top right.

### Safety Numbers — Verifying Contact Identity

Safety Numbers are a cryptographic fingerprint that uniquely identifies the encryption keys between you and a contact. Verifying safety numbers out-of-band (in person, via a different channel) confirms that no man-in-the-middle is intercepting your conversations.

To verify: Open conversation > Contact name > Safety Number. Compare the displayed number with your contact — either visually (if in person) or by scanning each other's QR codes.

I verify safety numbers with contacts I communicate with about sensitive topics. It takes 60 seconds and provides a meaningful security guarantee.

---

## Part 5: Note to Self and Signal as a Secure Notepad

Note to Self — messaging yourself — is more useful than it appears.

### What I Use Note to Self For

- **Temporary secure storage**: 2FA backup codes I need to move to my password manager
- **Sensitive documents**: Encrypted photos of documents (passport, insurance cards) I need on the go
- **Private journaling**: End-to-end encrypted notes not accessible to cloud sync providers
- **Cross-device clipboard**: Securely passing text between my phone and desktop Signal

Note to Self messages sync across all your Signal devices. Enable disappearing messages on Note to Self for auto-purging sensitive temporary content.

---

## Part 6: Linked Devices and Desktop

Signal's desktop app is useful but introduces considerations.

### Setting Up Signal Desktop

1. Download from signal.org/download
2. Open Signal desktop > Link new device (shows QR code)
3. In Signal mobile: Settings > Linked Devices > Link New Device
4. Scan the QR code

Your message history does not transfer to the desktop app — only new messages from the linking date forward appear on desktop.

### Security Considerations for Desktop

- The desktop app stores message data in your computer's application data folder. Ensure your computer's drive is encrypted (FileVault on Mac, BitLocker on Windows)
- Shared or work computers: do not link Signal. Messages are stored locally and accessible to anyone with access to the account
- If you lose your computer: immediately unlink the device from Signal mobile (Settings > Linked Devices > Remove)

### Auto-Lock and Screen Security

Enable screen lock on the desktop app: Signal (Desktop) > Preferences > Privacy > Enable Screen Lock.

This requires your system password to access Signal after a period of inactivity.

---

## Part 7: Advanced Privacy Settings

### Sealed Sender

Signal uses a "sealed sender" mechanism that hides sender information from Signal's servers. Enabled automatically — no configuration needed. It means Signal's infrastructure cannot tell who sent a particular message to whom, only that a message was delivered to a specific account.

### Screen Security (Mobile)

Settings > Privacy > Screen Security: On

Prevents Signal from appearing in the app switcher and recent apps list (iOS) or preventing other apps from screen-capturing Signal conversations (Android).

### Notification Privacy

Settings > Notifications > Show:
- **Name, Content and Actions** (default — least private)
- **Name Only** — shows sender name but not message content in notifications
- **No Name or Message** — most private; shows only "Signal Message"

If your phone is unlocked or your lock screen notifications are visible to others, use "No Name or Message" to prevent message content appearing on screen.

### Incognito Keyboard (Android)

Settings > Privacy > Incognito Keyboard: On

Prevents your keyboard app from learning new words from Signal messages. Some keyboard apps send learned words to their servers for sync — disabling this prevents Signal text from leaking to keyboard providers.

---

## Common Signal Mistakes to Avoid

**1. Not setting a Registration Lock PIN**
Without this, a SIM swap can give someone access to your Signal account.

**2. Leaving phone number public to everyone**
Set "Who can find me by my phone number" to Nobody after creating a username.

**3. Not enabling disappearing messages**
Old messages are a liability. Enable a default timer for all new conversations.

**4. Using Signal desktop on shared computers**
Messages are stored locally. Never link Signal to a device other people have access to.

**5. Not verifying safety numbers for sensitive contacts**
Without verification, you cannot confirm that a man-in-the-middle is not present. Take 60 seconds to verify in person for your most important contacts.

**6. Not locking down the Signal app itself**
Enable screen lock and biometric authentication in Signal settings. The app's encryption is irrelevant if someone can walk up to your unlocked phone and read messages directly.

---

## Signal vs WhatsApp vs Telegram: The Real Comparison

| Feature | Signal | WhatsApp | Telegram |
|---------|--------|----------|----------|
| E2E encryption default | Yes (all) | Yes (all) | No (only Secret Chats) |
| Open-source | Yes (full) | No | Partial |
| Metadata collection | Minimal | Extensive (Meta) | Some |
| Username (no number share) | Yes | No | Yes |
| Disappearing messages | Yes (all chats) | Yes | Yes (Secret Chats) |
| Group E2E encryption | Yes | Yes | No (server-side only) |
| Sealed sender | Yes | No | No |
| Business model | Nonprofit | Ad-supported (Meta) | Freemium + ads |
| Third-party audited | Yes | No | No |

Telegram is frequently listed as a private messenger. This is a misconception. Regular Telegram chats are not end-to-end encrypted — they are stored in Telegram's cloud servers and accessible to Telegram. Only "Secret Chats" are E2E encrypted, and Secret Chats are not available for groups. For private group communication, Signal is the only major option.

---

## Conclusion

Signal's privacy guarantees are the strongest of any widely-used messaging app, but they require proper configuration to realize. Setting a Registration Lock, creating a username, enabling disappearing messages by default, and understanding group admin controls takes less than 30 minutes. After that, Signal runs quietly in the background and handles the cryptographic complexity for you.

The practical result: conversations that cannot be read by your carrier, your government (absent physical device access), your cloud provider, or Signal itself. For most people, that is more than enough. For high-risk users, combine Signal with the additional measures described above and you have a genuinely robust private communications setup.

---

*Related guides:*
- [Best Privacy Browsers 2026](/posts/best-privacy-browsers-2026/)
- [Best VPN Services 2026](/posts/best-vpn-services-2026/)
- [Best Encrypted Email Services 2026](/posts/best-encrypted-email-services-2026/)


<a href="/go/incogni" class="cta-affiliate" rel="sponsored noopener">View Incogni</a>
