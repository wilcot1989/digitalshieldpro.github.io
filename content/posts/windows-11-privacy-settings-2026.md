---
title: "Windows 11 Privacy Settings 2026: The Complete Lockdown"
date: 2026-06-19T09:00:00+01:00
lastmod: 2026-06-19T09:00:00+01:00
description: "Microsoft's telemetry, Recall AI, and advertising features send your data by default. Here's exactly how to lock down Windows 11 for maximum privacy in 2026."
categories: ["device-security"]
tags: ["Windows 11", "privacy", "telemetry", "Microsoft Recall", "data collection", "privacy settings", "Windows security"]
keywords: ["Windows 11 privacy settings", "disable Windows 11 telemetry", "Windows Recall privacy", "Windows 11 lock down guide 2026"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity researcher and writer. Tests privacy tools and security software hands-on."
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1517336714731-489689fd1ca8&w=1200&output=webp&q=70"
faq:
  - q: "Does Windows 11 really send my data to Microsoft by default?"
    a: "Yes. A freshly installed Windows 11 Home or Pro system enables diagnostic data collection, advertising IDs, location access, app activity tracking, and personalized ad delivery by default. The telemetry settings alone can transmit hardware identifiers, crash reports, typed text samples, app usage patterns, and browsing behavior from Edge. Optional components like Recall and Cortana collect even more. Disabling these features takes about 30 minutes but significantly reduces what Microsoft collects."
  - q: "What is Windows Recall and should I disable it?"
    a: "Windows Recall is an AI feature that takes periodic screenshots of your screen, runs OCR on them, and stores a searchable timeline of everything you have done on your PC. Microsoft stores this data locally on Copilot+ PCs using an encrypted SQLite database. However, security researchers in 2024 demonstrated that the database could be extracted by malware running with standard user privileges. For most users, the privacy risk of having every email, banking screen, document, and browser tab recorded outweighs the convenience. I disable it on all my machines."
  - q: "What is a Windows 11 advertising ID and how do I turn it off?"
    a: "Windows 11 assigns each user account a unique advertising identifier used by apps and Microsoft to track behavior across sessions and deliver targeted ads. You can disable it in Settings > Privacy & Security > General, where you toggle off 'Let apps show me personalized ads by using my advertising ID.' This does not prevent all ads but stops cross-app behavior tracking tied to that identifier."
  - q: "Will disabling telemetry break Windows Update?"
    a: "No. Setting diagnostic data to the minimum 'Required' level does not affect Windows Update, Windows Defender definitions, or any core functionality. The 'Required' level only sends crash reports and basic hardware information needed for Microsoft to fix critical bugs. Optional telemetry — the kind used for advertising and product improvement — can be disabled entirely without affecting system stability."
  - q: "Does a VPN or antivirus help with Windows privacy?"
    a: "A VPN hides your network traffic from your ISP and prevents IP-based tracking but does not stop Windows itself from sending telemetry to Microsoft. For that, you need the privacy settings changes described in this guide. Antivirus software like Bitdefender includes optional privacy features and firewall controls that can block outbound connections to tracking domains, adding a second layer of protection."
  - q: "Are third-party Windows privacy tools like O&O ShutUp10 safe to use?"
    a: "O&O ShutUp10++ and similar tools are widely used and generally safe, but apply changes with one click that may have unintended side effects — for example, disabling SmartScreen or Windows Update delivery optimization alongside the privacy features you actually want to disable. I prefer making changes manually so I understand exactly what each setting does. That said, ShutUp10 is a reasonable starting point if you review its recommendations item by item before applying."
  - q: "How often do I need to re-check Windows 11 privacy settings?"
    a: "After every major Windows 11 feature update. Microsoft has a documented history of re-enabling telemetry and adding new data collection features during major updates. The Windows 11 23H2 and 24H2 updates both introduced new defaults that required privacy-conscious users to re-apply their settings. Schedule a 20-minute review after each feature update, or check after each Patch Tuesday for significant changes."
  - q: "Does disabling location services affect apps like maps?"
    a: "Yes, partially. Disabling system-wide location access in Settings > Privacy & Security > Location prevents apps from accessing your precise GPS position. However, apps can still estimate your rough location from your IP address unless you use a VPN. If you use a maps or weather app you trust, you can allow location access for that specific app while blocking all others using per-app location permissions."
products:
  - name: "Bitdefender"
    url: "https://go.digitalshieldpro.com/bitdefender"
    price: ""
---

I set up a fresh Windows 11 Home install last month and ran Wireshark for the first hour. The telemetry traffic was constant — connection attempts to `settings-win.data.microsoft.com`, `vortex.data.microsoft.com`, `watson.telemetry.microsoft.com`, and a dozen more Microsoft endpoints. Before I had even opened a single app or typed a search query, Windows had already sent several megabytes of data home.

This is not a conspiracy theory. It is designed behavior, documented in Microsoft's privacy statement. The question is not whether Windows collects data — it does — but how much of it you are willing to hand over and how to reduce that surface area.

I have been locking down Windows 11 machines for clients since the OS launched. This guide covers every meaningful privacy setting, what it actually does, and the specific steps to change it. I also cover the Recall AI feature, which is new enough that most guides still miss it.

---

## What Windows 11 Collects by Default

Before we get to the fixes, understanding what you are dealing with helps you prioritize.

### Diagnostic Data (Telemetry)

Windows 11 sends two tiers of diagnostic data by default on consumer systems:

**Required diagnostic data** — This is the minimum Microsoft claims it needs. It includes:
- Device and hardware identifiers
- Operating system version and configuration
- Crash reports and error logs
- Basic app install/uninstall events

**Optional diagnostic data** — This is where the real collection happens:
- Browsing history in Edge, including URLs visited
- Typed text samples from search and input fields
- App usage patterns and session durations
- Inking and typing data if you use a touchscreen or stylus
- Audio input samples from voice features
- Detailed error reports including memory dumps

On a fresh install, Windows 11 Home defaults to Optional. Windows 11 Pro defaults to Required, but upgrades from Home often inherit Optional. I have seen enterprise machines deployed with Optional enabled because IT teams did not explicitly set group policy.

### The Advertising ID

Every Windows 11 user account gets a unique advertising identifier — essentially a tracking cookie baked into the OS. Apps signed into the Microsoft Store, system apps, and third-party apps with Microsoft advertising integration can all access this ID to build a behavioral profile.

Microsoft's advertising platform uses this to serve personalized ads inside Windows, inside apps, and on MSN and Bing. Third-party apps can read the same ID and correlate your behavior across their service with what Microsoft knows about you.

### Location, Camera, and Microphone

Location is on by default for the system and multiple built-in apps. Camera and microphone permissions are granted liberally. Windows Update, Cortana, and Weather access location without many users realizing it.

### Activity History

Windows tracks every app you open, file you access, and URL you visit in a local timeline. By default in a Microsoft account setup, this history syncs to Microsoft's servers to enable "Timeline" features across devices.

### Microsoft Recall

I will cover this in detail below because it is the most invasive feature Microsoft has shipped in years.

---

## Step 1: Set Telemetry to the Minimum

**Path:** Settings > Privacy & Security > Diagnostics & Feedback

1. Under **Diagnostic data**, select **Required diagnostic data** (or **Send required diagnostic data**)
2. Turn off **Improve inking and typing**
3. Turn off **Tailored experiences**
4. Turn off **View diagnostic data** (this just closes the diagnostics viewer, but you can leave it on if you want to see what is collected)
5. Under **Feedback frequency**, set to **Never**

On Windows 11 Pro, you can enforce the minimum via Group Policy: Computer Configuration > Administrative Templates > Windows Components > Data Collection and Preview Builds > Allow Diagnostic Data, set to **Enabled** with value **1 (Required)**.

**What this does:** Stops Windows from sending browsing history, typed text, app usage patterns, and audio samples. You will still send crash reports and basic hardware info, which is a reasonable tradeoff for receiving targeted bugfixes.

---

## Step 2: Disable the Advertising ID

**Path:** Settings > Privacy & Security > General

Toggle off all four options:
1. **Let apps show me personalized ads by using my advertising ID**
2. **Let websites show me locally relevant content by accessing my language list**
3. **Let Windows improve Start and search results by tracking app launches**
4. **Show me suggested content in the Settings app**

**What this does:** Removes the cross-app tracking identifier that links your behavior across Microsoft's advertising network and third-party apps. Ads will still appear in apps, but they will not be personalized based on your activity profile.

---

## Step 3: Disable or Neuter Microsoft Recall

Recall is Microsoft's AI-powered screenshot feature available on Copilot+ PCs (those with a dedicated NPU). It takes a screenshot approximately every 5 seconds, performs optical character recognition on the content, and stores a searchable semantic index of everything on your screen.

**To disable Recall entirely:**

**Path:** Settings > Privacy & Security > Recall & Snapshots

1. Toggle **Save Snapshots** to Off
2. If the toggle is grayed out, open Windows Security > App & Browser control > Recall > turn off

Alternatively, from PowerShell (run as administrator):
```
Dism /Online /Disable-Feature /FeatureName:Recall
```

If you must use Recall, apply these mitigations:
- **Exclude sensitive apps:** Under Recall settings, add your banking apps, password manager, email client, and browser to the exclusion list
- **Limit storage:** Set the maximum snapshot storage to the minimum allowed (usually 10 GB)
- **Enable Windows Hello authentication:** Recall requires authentication before displaying snapshots, so ensure Windows Hello is configured with a strong PIN or biometric

**Why I am firm on disabling this:** Security researcher Kevin Beaumont demonstrated in 2024 that the Recall database, stored at `%LOCALAPPDATA%\CoreAIPlatform.00\UKP\`, could be read by any process running as the current user. No privilege escalation required. A single piece of malware running in the user context could exfiltrate your entire screenshot history silently. Microsoft has patched specific extraction tools but the fundamental design — unencrypted accessible database — has not changed enough for me to trust it on client machines.

---

## Step 4: Lock Down Location Services

**Path:** Settings > Privacy & Security > Location

1. Toggle **Location services** to Off (this disables location for all apps)
2. If you want per-app control instead, leave Location services on and scroll through the **Choose apps that can use your location** list — disable everything except apps you explicitly use for navigation

**Specifically check and disable location for:**
- Cortana
- Weather (use a weather website instead)
- News
- Windows Search
- Microsoft Edge

**For stricter control:** Disable the **Location history** toggle, which stops Windows from storing a log of your physical location.

---

## Step 5: Restrict Camera and Microphone Access

**Path:** Settings > Privacy & Security > Camera

1. Verify **Camera access** is On (this is the system toggle)
2. Under **Let apps access your camera**, scroll through and disable every app that does not genuinely need camera access
3. Focus on: **Microsoft Edge**, **Cortana**, **Windows Search**, **Mail**

Repeat the same process at Settings > Privacy & Security > Microphone.

**Note on the system toggle:** Turning off camera or microphone system access is a hard block — it overrides individual app permissions. If you rarely use video calls, you can leave these off and only enable them when needed.

---

## Step 6: Disable Activity History and Timeline

**Path:** Settings > Privacy & Security > Activity History

1. Uncheck **Store my activity history on this device**
2. If signed into a Microsoft account, uncheck **Send my activity history to Microsoft**
3. Click **Clear history** to delete what has already been collected

**Path:** Settings > Privacy & Security > Search Permissions > History

1. Set **Search history on this device** to Off
2. Set **Search history** under your Microsoft account to Off (this clears it from the cloud)

---

## Step 7: Disable Notification and App Permissions

**Path:** Settings > Privacy & Security > Notifications

Disable **Allow apps to access notifications** entirely, or scroll through and revoke access from any app that does not need it. Notification content can include sensitive data — email subjects, SMS previews, banking alerts — that apps with notification access can read.

**Also check:**
- **Account info** (Settings > Privacy > Account info) — Disable for all apps except those that genuinely need it
- **Contacts** — Disable unless you use a specific app that requires contact sync
- **Calendar** — Disable for all Microsoft Store apps
- **Call history** — Disable entirely on desktop
- **Email** — Disable for all except your actual email client

---

## Step 8: Lock Down Microsoft Edge (If You Use It)

Edge has its own telemetry separate from Windows. If you use Edge:

**Edge Settings > Privacy, Search, and Services:**
1. Set **Tracking prevention** to **Strict**
2. Disable **Personalize your web experience**
3. Disable **Help improve Microsoft products by sending optional diagnostic data about how you use the browser**
4. Disable **Search and service improvement**
5. Disable **Shopping assistance in Microsoft Edge**
6. Under **Address bar and search**, change the default search engine from Bing to DuckDuckGo or a privacy-respecting alternative

Disable the Edge password manager if you use a dedicated password manager — Edge's password sync means your credentials may end up on Microsoft's servers.

---

## Step 9: Audit Startup Apps and Background Processes

Privacy settings only cover Microsoft's own data collection. Third-party apps often install background services with their own telemetry.

**Path:** Task Manager > Startup Apps

Go through every enabled startup item and disable anything you do not need running immediately at boot. Pay attention to:
- **App update services** — Often send usage telemetry to vendors
- **Cloud sync clients** — OneDrive, Dropbox, etc. all have privacy settings worth reviewing
- **Hardware manufacturer utilities** — Lenovo Vantage, HP Support Assistant, and similar tools are notorious for aggressive telemetry

---

## Step 10: Use a Local Account Instead of a Microsoft Account

This is the most impactful single change you can make. A Microsoft account links all of your Windows activity to a cloud profile. A local account keeps everything on-device.

**To switch to a local account:**
1. Settings > Accounts > Your info
2. Click **Sign in with a local account instead**
3. Follow the prompts to create a local username and password

**Tradeoffs:** You lose access to Microsoft Store purchases tied to your account, OneDrive sync, and cross-device features. For most privacy-focused users, this is a worthwhile exchange.

If you must use a Microsoft account (e.g., for workplace compliance), go to Settings > Accounts > Sign-in options and disable **Use my sign-in info to automatically finish setting up my device and reopen my apps after an update or restart**.

---

## Adding a Security Layer: Bitdefender

The settings above reduce what Windows sends to Microsoft, but they do not protect you from third-party apps, browser exploits, phishing sites, or malware that installs its own tracking components.

I run [Bitdefender Total Security](https://go.digitalshieldpro.com/bitdefender) alongside these privacy settings because its anti-tracker feature actively blocks tracking scripts, its firewall gives me per-application network control, and its privacy audit feature flags apps with excessive permissions.

Bitdefender's **Privacy Firewall** is particularly useful here — it lets me see which processes are making outbound connections and block anything I do not recognize. This is how I first noticed several telemetry endpoints in a fresh Windows 11 install; Bitdefender flagged unusual connection patterns from a preinstalled app.

---

## Windows 11 Privacy Settings Checklist

For quick reference, here is every change covered in this guide:

| Setting | Path | Action |
|---------|------|--------|
| Diagnostic data | Privacy & Security > Diagnostics & Feedback | Set to Required |
| Improve inking and typing | Privacy & Security > Diagnostics & Feedback | Off |
| Tailored experiences | Privacy & Security > Diagnostics & Feedback | Off |
| Advertising ID | Privacy & Security > General | Off |
| Microsoft Recall | Privacy & Security > Recall & Snapshots | Snapshots Off |
| Location services | Privacy & Security > Location | Off or per-app |
| Camera access | Privacy & Security > Camera | Per-app control |
| Microphone access | Privacy & Security > Microphone | Per-app control |
| Activity history | Privacy & Security > Activity History | Off |
| Search history | Privacy & Security > Search Permissions | Off |
| Notification access | Privacy & Security > Notifications | Per-app control |
| Local account | Accounts > Your info | Switch to local |

---

## What These Changes Will Not Fix

Be honest with yourself about what this guide does and does not cover:

**Remains active after these changes:**
- Microsoft Defender telemetry (minimal and necessary for threat intelligence)
- Windows Update metadata (required for updates to function)
- IP address visibility to any website you visit (use a VPN for this)
- Third-party app telemetry from apps you install yourself
- Browser fingerprinting by websites (requires browser hardening separately)

**For deeper network-level blocking,** tools like Pi-hole or pfSense with blocklists can intercept telemetry at the DNS level before it leaves your network. That is beyond the scope of this guide but worth exploring if you manage a home network.

---

## Final Thoughts

A fresh Windows 11 install in 2026 is not private by default — it is a telemetry machine that you happen to also do your work on. That is not a bug; it is a revenue model. Microsoft is a data company as much as a software company, and Windows is one of its primary data collection surfaces.

The 30 minutes you spend working through this checklist meaningfully reduces that collection. You will not achieve perfect privacy on a Windows machine — the OS is closed source and Microsoft can change behavior in updates — but you can substantially limit what gets sent and ensure you are not opted into the most aggressive collection features by default.

Re-check these settings after every major Windows feature update. And for the threats that come from outside Windows itself — phishing, malware, browser exploits — a well-configured security suite like [Bitdefender](https://go.digitalshieldpro.com/bitdefender) adds protection that privacy settings alone cannot provide.


<a href="https://go.digitalshieldpro.com/bitdefender" class="cta-affiliate" rel="nofollow noopener sponsored" target="_blank">View Bitdefender</a>

## Related guides

- [Chromebook Security Guide 2026: Family Link, Extensions](/posts/chromebook-security-guide-2026/)
- [How to Secure Your Mac in 2026: FileVault, Lockdown Mode](/posts/how-to-secure-mac-2026/)
- [Facebook & Instagram Privacy 2026: Lockdown Guide](/posts/facebook-instagram-privacy-settings-2026/)
- [Best Antivirus for Windows 11 in 2026](/posts/best-antivirus-for-windows-11-2026/)
- [Build Your Complete Digital Privacy Stack 2026](/posts/best-privacy-stack-2026/)
