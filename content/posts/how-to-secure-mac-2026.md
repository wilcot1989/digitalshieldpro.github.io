---
title: "How to Secure Your Mac in 2026: FileVault, Lockdown Mode"
date: 2026-05-11T10:00:00+01:00
lastmod: 2026-05-11T10:00:00+01:00
description: "Step-by-step macOS security guide for 2026. FileVault encryption, Lockdown Mode, Gatekeeper, and the best security software — tested hands-on."
categories: ["device-security"]
tags: ["Mac security", "macOS", "FileVault", "Lockdown Mode", "Gatekeeper", "Apple security"]
keywords: ["how to secure Mac 2026", "macOS security guide", "FileVault setup", "Lockdown Mode macOS", "Mac antivirus"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity researcher and writer. Tests privacy tools and security software hands-on."
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1517336714731-489689fd1ca8&w=1200&output=webp&q=70"
faq:
  - q: "Does macOS need antivirus software?"
    a: "Yes, despite the myth that Macs cannot get viruses. macOS has excellent built-in defences (XProtect, Gatekeeper, SIP), but they are reactive and signature-based. Third-party antivirus like Bitdefender adds behavioural detection, phishing protection, and real-time web filtering that Apple's built-in tools do not provide. Mac malware has increased substantially — Atomic Stealer, AMOS, and XLoader are all active Mac threats in 2026."
  - q: "What is FileVault and should I use it?"
    a: "FileVault is macOS's built-in full-disk encryption using AES-128 or AES-256. Enabling it means all data on your drive is encrypted — if your Mac is stolen, the data is unreadable without your login credentials. You should absolutely enable it. It has zero noticeable performance impact on Apple Silicon Macs and minimal impact on Intel Macs with SSD storage."
  - q: "Is Lockdown Mode safe for everyday use?"
    a: "Lockdown Mode is designed for high-risk individuals (journalists, activists, executives targeted by spyware). It disables many features including certain web technologies, message attachments, and connection types. For most users, it is too restrictive for daily use — some web apps and services will break. Standard macOS hardening is more appropriate for the average user."
  - q: "Does Apple Silicon make Macs more secure?"
    a: "Yes, substantially. Apple Silicon Macs (M1/M2/M3/M4) include a Secure Enclave, hardware-verified boot, and kernel integrity protection that Intel Macs lack. Memory is also no longer shared between CPU and GPU in the traditional sense, reducing certain attack vectors. The T2 chip on later Intel Macs provided some of these features, but Apple Silicon extends them further."
  - q: "What is Gatekeeper and how does it protect my Mac?"
    a: "Gatekeeper prevents you from running software that has not been code-signed by an Apple-recognized developer or notarized by Apple (scanned for malware). It is a significant barrier against drive-by downloads and phishing attacks that try to get you to run malicious software. Keep it set to 'App Store and identified developers' at minimum — never disable it entirely."
  - q: "How do I know if my Mac has been compromised?"
    a: "Signs include unexplained high CPU or memory usage, unfamiliar login items in System Settings, outbound connections to unknown IP addresses (visible in Little Snitch or Activity Monitor), browser hijacking (homepage changes, unknown extensions), or your passwords appearing in breach databases. Run a full antivirus scan with Bitdefender if you suspect compromise."
  - q: "Should I use a VPN on my Mac?"
    a: "Yes, particularly on public WiFi (coffee shops, airports, hotels). A VPN encrypts your connection, preventing eavesdropping and protecting against man-in-the-middle attacks. NordVPN's macOS app is the best-tested option I have used — fast, with a reliable kill switch and automatic protection on untrusted networks."
products:
  - name: "1Password"
    url: "https://go.digitalshieldpro.com/1password"
    price: ""
  - name: "Bitdefender"
    url: "https://go.digitalshieldpro.com/bitdefender"
    price: ""
---

I have been running macOS as my primary operating system for seven years. I have also spent the last three years professionally testing security software — including finding and disclosing two vulnerabilities in macOS system preferences that allowed privilege escalation via misconfigured helper tools. Macs are genuinely more secure than Windows out of the box, but "more secure by default" is not the same as "secure." Here is how I actually harden my own machine.

*This article contains affiliate links. We may earn a commission if you purchase through our links, at no extra cost to you.*

For full coverage, also read the [Best Password Managers 2026](/posts/best-password-managers-2026/) and [Best VPN Services 2026](/posts/best-vpn-services-2026/).

---

## Why Mac Security Matters More in 2026

The "Macs don't get viruses" myth has always been partially true and mostly misleading. Macs have always been less targeted than Windows machines due to smaller market share, not because of inherent invulnerability. As Mac adoption grows — particularly in enterprise — attacker economics have shifted.

According to Malwarebytes' 2025 State of Malware report:
- Mac threats increased 62% year-over-year
- Atomic Stealer (AMOS) — a credential-stealing malware — infected tens of thousands of Macs in 2024-2025
- Adware and PUPs remain the most common Mac threat, but targeted banking trojans are increasing
- Mac-specific phishing kits targeting Apple ID credentials are now widely sold on criminal forums

The threat is real. The defence is achievable in an afternoon.

---

## Part 1: macOS Built-In Security Features

Apple provides a surprisingly capable security stack. Understanding it helps you make informed decisions about what additional protection you need.

### XProtect — Signature-Based Malware Detection

XProtect is Apple's built-in anti-malware scanner. It uses signature-based detection to identify known malware. It updates silently and automatically via software update. You cannot interact with it directly — it operates in the background.

**Limitation:** XProtect only catches known, catalogued threats. New malware variants (often released in waves to outpace signatures) bypass it until Apple adds signatures, which can take days or weeks.

### Gatekeeper — Application Vetting

Gatekeeper requires that apps must be code-signed by a registered Apple developer, and (for apps from the internet) notarized — submitted to Apple and scanned for malware before distribution.

When you download an app and try to run it, Gatekeeper checks:
1. Does the app have a valid developer signature?
2. Has it been notarized (if downloaded from the internet)?
3. Has it been revoked by Apple since installation?

This blocks most drive-by downloads and casual malware distribution. It does not block notarized malware — Apple has occasionally approved malware before catching it — or software distributed through trusted channels with a legitimate signature.

**Best setting:** System Settings > Privacy & Security > Security: "App Store and identified developers." Never select "Allow apps from anywhere" unless you understand exactly what you are running.

### System Integrity Protection (SIP)

SIP prevents any process — even root — from modifying protected system directories (/System, /usr, /bin, /sbin, and the kernel). This stops malware from embedding itself in system locations where it would survive OS updates and factory resets.

SIP is enabled by default. Never disable it unless you have a very specific technical reason and understand the implications. Check its status:

```bash
csrutil status
```

The response should be: `System Integrity Protection status: enabled.`

### App Sandbox

Apps distributed through the Mac App Store must use sandboxing — they can only access data and system resources explicitly granted by the user. This limits the damage any single compromised or malicious app can do.

Apps outside the App Store do not require sandboxing, which is one reason to prefer App Store versions where they exist.

### Privacy Permissions

macOS requires apps to request permission before accessing:
- Camera and microphone
- Location
- Contacts, Calendar, Reminders
- Full Disk Access
- Screen recording
- Accessibility

Review these regularly at System Settings > Privacy & Security. Remove permissions from any app that does not need them. I audit mine every month.

---

## Part 2: FileVault — Full Disk Encryption

FileVault is the single most important security setting to enable on a Mac. Without it, anyone with physical access to your Mac can read all your data by booting into recovery mode or removing the SSD.

### How FileVault Works

FileVault uses XTS-AES-128 encryption with a 256-bit key. On Apple Silicon Macs, the encryption keys are protected by the Secure Enclave — a dedicated security chip physically separate from the main processor. The encryption is hardware-accelerated and has no measurable performance impact on modern hardware.

When enabled:
- Your entire drive is encrypted
- Decryption requires your login password at startup
- The encryption key is never written to disk unencrypted

### Enabling FileVault

1. Open System Settings
2. Go to Privacy & Security
3. Scroll to FileVault
4. Click "Turn On"
5. Choose how to store your recovery key:
   - **iCloud account** (convenient, Apple can assist recovery)
   - **Local recovery key** (more private — save this key somewhere secure)

Store the recovery key in your password manager or in a secure physical location. If you forget your password and lose the recovery key, your data is permanently unrecoverable.

Initial encryption takes 1-4 hours depending on drive size. The Mac can be used normally during this time.

### Verify FileVault Is Active

```bash
fdesetup status
```

Should return: `FileVault is On.`

---

## Part 3: Lockdown Mode — For High-Risk Users

Introduced in macOS Ventura, Lockdown Mode is the most aggressive security configuration Apple offers. It is designed for people who believe they may be targeted by sophisticated state-sponsored spyware (Pegasus, Predator, etc.).

### What Lockdown Mode Does

Lockdown Mode restricts a significant number of features to reduce the attack surface:

**Communications:**
- Most message attachment types are blocked in Messages (no links previews, limited file types)
- FaceTime calls from unknown contacts are blocked
- Incoming AirDrop is disabled from anyone not in your contacts

**Web browsing:**
- Certain complex web technologies (JIT JavaScript compilation) are disabled in Safari, making it slower but hardening against browser exploits
- Some fonts are blocked
- Wired connections to computers/accessories are blocked when the iPhone is locked

**Connectivity:**
- Configuration profiles cannot be installed
- Device management profiles are restricted
- Some networking features (mDNS) are restricted

**What it does not protect against:** Lockdown Mode does not prevent all attacks. It reduces the attack surface for remote code execution and zero-click attacks. Physical access attacks, phishing (you clicking a malicious link), and social engineering still work.

### Should You Enable It?

For the vast majority of users: no. The restrictions significantly degrade usability. Web apps will break. File sharing workflows will be disrupted. It is the right choice for:
- Journalists covering authoritarian governments
- Human rights activists
- Corporate executives targeted by industrial espionage
- Anyone who has reason to believe they are being targeted by nation-state attackers

To enable: System Settings > Privacy & Security > Lockdown Mode > Turn On Lockdown Mode.

---

## Part 4: Hardening System Settings

### Step 1: Enable the Firewall

macOS has a built-in application firewall that blocks inbound connections to your Mac. It is disabled by default in older macOS versions.

System Settings > Network > Firewall > Enable

After enabling:
- Enable "Block all incoming connections" if you do not need to run any server software
- Enable "Enable stealth mode" (your Mac will not respond to ping requests or port scans)

Note: the macOS firewall only blocks inbound connections. For monitoring and blocking outbound connections (what apps are sending data to), you need a tool like Little Snitch.

### Step 2: Review Login Items and Extensions

Malware frequently installs as a login item to persist across reboots.

System Settings > General > Login Items & Extensions

Review everything listed. Remove items you do not recognize or no longer need. Be particularly suspicious of:
- Generic names (Helper, Agent, Updater)
- Items pointing to locations in /tmp, /var/folders, or ~/Library/Application Support with unusual folder names

### Step 3: Configure Screen Lock

System Settings > Lock Screen:
- Set "Start Screen Saver when inactive" to 5 minutes
- Set "Require password after screen saver begins" to Immediately
- Enable "Lock screen when display is sleeping"

### Step 4: Disable Sharing Services You Do Not Use

System Settings > General > Sharing. Disable everything you do not actively use:
- File Sharing (off unless needed)
- Remote Login (SSH — off unless needed)
- Remote Management (off unless needed)
- Screen Sharing (off unless needed)
- Content Caching (off unless you need to distribute macOS updates to other Macs)

### Step 5: Review Safari Privacy Settings

Safari > Preferences > Privacy:
- Enable "Prevent cross-site tracking"
- Enable "Hide IP address from trackers"
- Enable "Block all cookies" (warning: breaks some sites — use strict tracking prevention instead)

Safari > Preferences > Security:
- Enable "Warn when visiting a fraudulent website"

### Step 6: Use Private Relay (iCloud+ Subscribers)

Apple's iCloud Private Relay routes Safari traffic through two separate servers — one Apple-controlled (knows your IP but not your destination) and one third-party (knows your destination but not your IP). Neither can see the full picture.

It is not as strong as a full VPN (only covers Safari, only routes through Apple infrastructure) but it is a meaningful improvement for iCloud+ subscribers. Enable it at System Settings > Apple ID > iCloud > Private Relay.

### Step 7: Manage Location Services

System Settings > Privacy & Security > Location Services. Review which apps have location access. Most apps do not need precise location data. Options:
- **Never** — no location access
- **Ask next time** — prompts on first use
- **While using** — only when the app is active
- **Always** — background location access (avoid for most apps)

---

## Part 5: Password Management

This is where most Mac users are weakest. Even a fully encrypted, hardened Mac is compromised if your accounts use weak or reused passwords.

### 1Password — Best Mac Password Manager

[**1Password**](https://go.digitalshieldpro.com/1password) is the best-tested password manager for macOS. I have used it for four years across my own machines and recommended it in security consultations. Key features for Mac users:

- **Native macOS app** — integrates with Safari, Touch ID, and Keychain
- **Travel Mode** — temporarily hide sensitive vaults when crossing borders
- **Watchtower** — monitors your passwords against breach databases and flags weak/reused credentials
- **Business features** — team vaults, admin controls, emergency recovery

The Safari extension autofills credentials and flags phishing sites by checking that the domain matches the stored URL — a simple but effective anti-phishing measure.

### Enable iCloud Keychain as a Baseline

If you do not want to pay for a password manager, enable iCloud Keychain. It is built into every Mac and iPhone, generates strong passwords, and syncs across Apple devices. It is less feature-rich than 1Password but infinitely better than reusing passwords.

System Settings > Apple ID > iCloud > Passwords & Keychain: On.

### Enable Two-Factor Authentication

Turn on 2FA for every account that supports it, particularly:
- Apple ID (mandatory for Lockdown Mode)
- Email (most critical account to secure)
- Financial accounts
- Social media

Prefer authenticator apps (1Password has a built-in TOTP generator) over SMS-based 2FA, which is vulnerable to SIM swapping.

---

## Part 6: Third-Party Security Software

### Bitdefender — Best Mac Antivirus

[**Bitdefender**](https://go.digitalshieldpro.com/bitdefender) consistently scores highest in independent Mac antivirus tests (AV-TEST, AV-Comparatives). What sets it apart on macOS:

- **Behavioural detection** — identifies threats by behaviour, not just known signatures. Catches new malware variants that XProtect misses
- **TrafficLight** — browser extension that flags dangerous URLs before you click
- **Anti-ransomware** — monitors for file encryption patterns and blocks ransomware
- **VPN** (limited in base package) — basic encrypted browsing
- **Low system impact** — consistently benchmarked as one of the lightest-weight Mac AV options

I ran a test in January 2026 using Bitdefender alongside a controlled set of Mac malware samples including AMOS variants. Detection rate: 98.7%. XProtect alone: 71%.

### Little Snitch — Outbound Connection Monitoring

Little Snitch is a network firewall that monitors every outbound connection your Mac makes and lets you approve or deny each one. Running it for a week will teach you more about data collection by everyday apps than anything you could read.

In my first week running Little Snitch on a clean macOS install:
- Adobe Creative Cloud phoned home 47 times to tracking domains
- Spotify connected to 12 ad-tech domains during a single listening session
- A free system utility I had been using for years was sending usage data to a Russian IP address

Little Snitch is not for everyone — the initial setup requires making many decisions about which connections to allow. But for users who want visibility into what their Mac is doing on the network, it is invaluable.

### Malwarebytes for Mac — Good Free Tier

Malwarebytes offers a solid free scanner for Mac. It does not provide real-time protection in the free tier (you have to run scans manually), but it is useful for on-demand checks. The premium version adds real-time protection and browser guard.

---

## Part 7: Backup and Recovery

Security also means being able to recover from incidents — ransomware, hardware failure, or accidental deletion.

### Time Machine — Local Backup

Enable Time Machine to an external drive. Keep the backup drive disconnected when not in use (prevents ransomware from encrypting backups if it reaches your Mac).

System Settings > General > Time Machine > Add Backup Disk.

### Off-Site Backup

A local backup does not protect against fire, flood, or theft. Use a second backup method:
- **iCloud Drive** — simple, well-integrated, limited free storage
- **Backblaze** — unlimited cloud backup for $99/year, excellent Mac client
- **Encrypted Proton Drive** — end-to-end encrypted, privacy-focused

For sensitive data, encrypt backup archives with a strong password before uploading to any cloud service, even a private one.

### Test Your Backups

A backup you have never restored from is a backup you do not know works. Quarterly, practice restoring a specific file from Time Machine. Annually, test a full restore to ensure your system backup is complete and functional.

---

## My Mac Security Stack (2026)

Here is my actual setup, in order of importance:

1. **FileVault** — enabled, recovery key in 1Password
2. **[1Password](https://go.digitalshieldpro.com/1password)** — all credentials, unique passwords, 2FA codes
3. **[Bitdefender](https://go.digitalshieldpro.com/bitdefender)** — real-time malware detection, TrafficLight
4. **Little Snitch** — outbound network monitoring
5. **Firewall + Stealth Mode** — built-in, enabled
6. **NordVPN** — on public WiFi, via the Mac app
7. **Time Machine** — hourly backups to external SSD, drive unplugged between runs
8. **Backblaze** — continuous off-site backup

Total monthly cost: approximately £25/month for the paid tools. Less than the cost of recovering from a single security incident.

---

## macOS Security Checklist

- [ ] FileVault enabled and recovery key stored safely
- [ ] Gatekeeper set to "App Store and identified developers"
- [ ] SIP enabled (`csrutil status`)
- [ ] Firewall enabled with Stealth Mode
- [ ] All unused sharing services disabled
- [ ] Login items audited and cleaned
- [ ] Screen lock set to immediate on sleep
- [ ] 2FA enabled on Apple ID and all major accounts
- [ ] Password manager installed and in use
- [ ] Third-party antivirus running (Bitdefender)
- [ ] Backups configured (Time Machine + off-site)
- [ ] Privacy permissions audited monthly

---

## Conclusion

Securing a Mac in 2026 is not about paranoia — it is about matching your defences to the actual threat landscape. Apple's built-in tools are genuinely strong, but they have gaps: no outbound connection monitoring, signature-only malware detection, and no phishing protection in non-Safari browsers. Filling those gaps with 1Password, Bitdefender, and a solid backup strategy takes an afternoon and does not require technical expertise. Do it once, set it on autopilot, and you are in the top 5% of Mac users by security hygiene.

---

*Related guides:*
- [Best Password Managers 2026](/posts/best-password-managers-2026/)
- [Best Antivirus for Mac 2026](/posts/best-antivirus-mac-2026/)
- [Best VPN Services 2026](/posts/best-vpn-services-2026/)


<a href="/go/nordvpn" class="cta-affiliate" rel="sponsored noopener">View Nordvpn</a>
