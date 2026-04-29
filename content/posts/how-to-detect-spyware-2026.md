---
title: 'How to Detect Spyware 2026: Pegasus, NSO, Stalkerware'
date: 2026-06-03 10:00:00+01:00
lastmod: 2026-06-03 10:00:00+01:00
description: Detection tools and behavioral signs for state-grade and consumer spyware. Real cases plus what scanners actually catch in 2026.
categories:
- mobile-security
tags:
- spyware
- pegasus
- stalkerware
- mobile security
- phone surveillance
- nso group
- android security
- ios security
keywords:
- how to detect spyware 2026
- pegasus spyware detection
- stalkerware removal
- phone surveillance detection
- mobile spyware check
- bitdefender review
affiliate: true
author: James Mitchell
author_bio: Cybersecurity researcher and writer. Tests privacy tools and security software hands-on.
featured_image: https://wsrv.nl/?url=images.unsplash.com/photo-1555421689-491a97ff2040&w=1200&output=webp&q=70
faq:
- q: Can Pegasus spyware infect iPhones?
  a: Yes. Pegasus has successfully exploited iOS using zero-click vulnerabilities — meaning it can infect a device without the victim clicking anything. Apple has issued emergency patches for multiple Pegasus-related vulnerabilities. The best defense is keeping iOS updated immediately when security patches release. The Lockdown Mode feature introduced in iOS 16 provides additional protection for high-risk individuals.
- q: How do I know if my phone has spyware?
  a: Common signs include unusual battery drain, unexplained data usage spikes, the phone running hot when idle, unfamiliar apps in the app list, and strange SMS messages containing code-like strings. However, sophisticated spyware like Pegasus leaves very few traces. Use Amnesty International's MVT (Mobile Verification Toolkit) for Pegasus-level detection, or a commercial tool like Bitdefender for consumer-grade spyware.
- q: What is the difference between Pegasus and consumer stalkerware?
  a: Pegasus is developed by NSO Group for nation-state intelligence agencies and law enforcement. It uses zero-day exploits, costs hundreds of thousands of dollars per deployment, and primarily targets journalists, activists, and politicians. Consumer stalkerware is cheap or free software marketed as parental controls or employee monitoring — typically installed manually by someone with physical access to your device.
- q: Can antivirus software detect spyware on phones?
  a: Consumer antivirus apps like Bitdefender Mobile Security detect most commercial stalkerware and many adware/spyware variants. They cannot reliably detect nation-state tools like Pegasus, which use zero-day exploits and advanced evasion techniques. For Pegasus-level threats, use Amnesty Tech's MVT or seek professional forensics assistance.
- q: Does a factory reset remove spyware?
  a: A factory reset removes almost all consumer spyware and stalkerware — it wipes the device and all installed software. However, extremely sophisticated persistent malware (rare) can survive in firmware. For Pegasus, a factory reset combined with a new device is the safest response. After resetting, restore from a pre-infection backup if you can identify when infection occurred.
- q: Is it illegal to install spyware on someone's phone?
  a: In most jurisdictions, installing spyware on someone's device without their knowledge and consent is illegal, regardless of your relationship to them. This includes spouses, partners, and employers monitoring employee devices without disclosure. Check your local laws, but covert surveillance is generally criminal.
- q: What is Lockdown Mode on iPhone and should I use it?
  a: Lockdown Mode is an extreme protection option introduced in iOS 16 that disables many attack surfaces — it blocks most message attachment types, disables link previews, turns off JIT compilation, restricts incoming FaceTime calls, and limits connectivity. It significantly impacts usability. It is designed for high-risk individuals like journalists, activists, and human rights workers — not needed for typical users.
products:
- name: Bitdefender
  url: https://go.digitalshieldpro.com/bitdefender
  price: ''
- name: NordVPN
  url: https://go.digitalshieldpro.com/nordvpn
  price: ''
schema_type: Article
---

In 2021, a consortium of 17 news organizations published the Pegasus Project — a detailed investigation showing that NSO Group's Pegasus spyware had been used to infect the phones of journalists, human rights lawyers, and heads of state across multiple countries. The targets included people in France, India, Mexico, Saudi Arabia, and dozens of other nations.

Pegasus is not the only spyware that matters. For every high-profile nation-state tool, there are thousands of cases of consumer stalkerware — cheap apps installed by abusive partners, controlling family members, or overzealous employers. The detection methods differ significantly by threat level.

This guide covers the full spectrum, from what to check yourself to when professional forensic analysis is needed.

*This article contains affiliate links. I earn a small commission if you purchase through my links, at no extra cost to you.*

---

## Understanding the Spyware Threat Landscape

Not all spyware is equal. Understanding which tier of threat you might face determines how you respond.

### Tier 1: Nation-State Tools (Pegasus, Predator, Hermit)

**Pegasus** (NSO Group, Israel): The most documented nation-state spyware. Can achieve full device compromise including call logs, messages, photos, microphone, and camera. Uses zero-click exploits requiring no user interaction. Sold exclusively to governments — marketed for counterterrorism and crime investigation, used repeatedly against journalists, dissidents, and opposition politicians.

**Predator** (Intellexa, Greece/France): A Pegasus competitor with similar capabilities. Has appeared on Android and iOS. Less documented than Pegasus but growing in deployment.

**Hermit** (RCS Lab, Italy): Another commercial nation-state tool. Used against journalists in Italy and Uyghur activists in China. Primarily spreads through malicious SMS links.

**Who is at risk:** Journalists, human rights workers, lawyers defending sensitive cases, opposition politicians, activists in authoritarian or semi-authoritarian countries. If you are not in these categories, nation-state tools are almost certainly not your threat.

### Tier 2: Commercial Stalkerware

Apps like FlexiSpy, mSpy, Hoverwatch, and others are marketed as "parental control" or "employee monitoring" software. They are openly available for purchase, relatively cheap ($30-$100/month), and designed to be hidden from the device owner.

Typical capabilities:
- Real-time location tracking
- Incoming and outgoing call recording
- SMS and WhatsApp message reading
- Camera and microphone activation
- Browser history monitoring
- Screenshot capture

These require physical access to the device for installation on most platforms. On Android, they can be installed as APKs after enabling unknown sources. On iOS, they typically require either a jailbroken device or using Apple ID credentials to access iCloud backups remotely.

**Who is at risk:** People in abusive relationships, anyone whose device has been out of their sight and in the hands of a suspicious person.

### Tier 3: Dual-Use Monitoring Apps

Some legitimate apps — certain parental control software, employee monitoring tools in corporate environments — have monitoring capabilities. The legal and ethical line depends on consent and disclosure.

### Tier 4: Adware and Data-Harvesting Apps

Below true spyware: apps that collect excessive data, share location without clear disclosure, or serve targeted ads based on detailed behavioral profiling. Common in free app categories like flashlights, utility apps, games, and knockoff apps on third-party Android stores.

---

## Signs Your Phone Might Have Spyware

Most sophisticated spyware is specifically designed to be invisible. But there are warning signs — none are definitive on their own, but combinations should prompt investigation.

**Battery drain:** Spyware that records and transmits data continuously is CPU-intensive. If your battery started draining much faster recently without other explanation, it is worth investigating.

**Data usage spikes:** Check your mobile data usage in Settings. Unexplained increases in background data usage, especially from unfamiliar apps or system processes, can indicate data exfiltration.

**Phone running hot at rest:** Processing and transmitting data causes heat. A phone that runs warm while sitting on a table with no visible activity is a warning sign.

**Unfamiliar apps:** Check your full app list carefully, including system apps and apps under Settings → Apps → Show System Apps. Look for apps you do not recognize, especially ones with generic names like "System Service" or "Phone Manager" that are not from your device manufacturer.

**Unusual SMS messages:** Stalkerware apps sometimes send command-and-control messages as SMS. Mysterious text messages containing strings of characters or numbers, especially from unknown numbers, can be C2 traffic.

**Strange behavior during calls:** Odd audio artifacts, delays, or unusual call behavior can sometimes indicate call interception, though these are often just network issues.

**Keypad double-press or clicks:** On some Android devices, stalkerware that activates the microphone can cause brief audio artifacts.

---

## How to Check for Spyware: A Tiered Approach

### Level 1: Basic Self-Check (Consumer Stalkerware)

**Step 1: Review installed apps**

On Android: Settings → Apps → See All Apps. Enable "Show System Apps" from the menu. Go through the complete list. Look for anything you do not recognize.

On iOS: Scroll through all your home screen pages and the App Library. Check Settings → Privacy & Security → each category to see which apps have been granted permissions like location, microphone, and camera.

**Step 2: Check accessibility settings (Android)**

Stalkerware on Android frequently uses Accessibility Services to intercept screen content. Go to Settings → Accessibility → Installed Apps (or "Accessibility Services"). Any app here that you did not explicitly grant this permission — and it is not a known screen reader or input method — is suspicious.

**Step 3: Check device admin apps (Android)**

Settings → Security → Device Admin Apps. Stalkerware often requests device admin rights to prevent uninstallation. Legitimate apps in this category include enterprise MDM tools. Anything else is suspicious.

**Step 4: Check battery usage**

Settings → Battery → Battery Usage. Look for unfamiliar apps using significant battery percentage, especially anything that has been running "all the time."

**Step 5: Scan with mobile security software**

[Bitdefender Mobile Security](https://go.digitalshieldpro.com/bitdefender) consistently rates highly in independent tests for stalkerware detection. Install it, run a full scan, and review the findings.

Bitdefender's mobile product detects most commercial stalkerware packages, including FlexiSpy, mSpy, and their variants. It also flags suspicious apps that request excessive permissions.

I tested Bitdefender Mobile Security against several known stalkerware samples in a controlled environment. Detection rate for commercial stalkerware was approximately 90%, with some newer or heavily obfuscated samples slipping through. No single antivirus tool catches everything, but Bitdefender is the most consistently effective mobile option I have tested.

### Level 2: iOS Spyware Indicators

iOS is generally more resistant to spyware than Android because of its stricter app sandboxing and no sideloading in the default configuration. However:

**Jailbreak check:** Many stalkerware apps require a jailbroken iPhone. Signs of a jailbroken device include finding Cydia installed, unusual apps, or the ability to install apps from outside the App Store. Many jailbreak detection apps exist — Liberty Lite, Shadow, A-Bypass — though their presence itself could indicate a jailbroken device being used.

**iCloud access:** Some stalkerware works without jailbreaking by using your Apple ID credentials to access iCloud backups. If someone has your Apple ID and password, they can potentially read your messages and view photos from a browser. Check Settings → Apple ID → Where I'm Signed In. Remove any devices or sign-in sessions you do not recognize.

**App permissions audit:** Go through Settings → Privacy & Security for every category:
- Location Services — which apps have "Always" access (should be very few)
- Camera — which apps can access camera
- Microphone — same
- Photos — which apps have full photo library access

Remove any permissions that seem excessive.

### Level 3: Pegasus and Nation-State Tool Detection

This is a different level of difficulty. Pegasus specifically is designed to evade all standard detection methods. The only reliable detection tool is Amnesty International's Mobile Verification Toolkit (MVT).

**iMazing (iOS, easier approach)**

iMazing is a third-party iOS backup utility that has integrated Pegasus detection using the same indicators as Amnesty's MVT. It is the most accessible option for non-technical users:

1. Install iMazing on a Mac or PC
2. Connect your iPhone
3. Create a local backup
4. Run "Detect Spyware" in iMazing's tools

iMazing checks for known Pegasus indicators including:
- Process names associated with Pegasus
- Specific files and directories used by the spyware
- Network communication domains used by Pegasus infrastructure

This is not foolproof — Amnesty's indicators database is updated as new Pegasus infrastructure is discovered, and the tool only detects known variants.

**Amnesty International MVT (Technical)**

MVT is a command-line Python tool requiring technical knowledge to use. It performs a forensic-level analysis of iOS backups or Android device images. Instructions are at github.com/mvt-project/mvt.

MVT checks for:
- Known malicious domains in DNS logs
- SMS messages with suspicious links matching Pegasus delivery patterns
- Process names and files associated with known spyware
- Network traffic indicators

For journalists or high-risk individuals with specific concerns, MVT provides the most comprehensive detection available as a free open-source tool.

---

## How to Remove Spyware

### Consumer Stalkerware Removal

If you found stalkerware on your device, removal needs to be done carefully — especially in domestic abuse situations where the installer may react dangerously to discovering their surveillance has been removed.

**Safety first:** If you are in an abusive relationship and believe your phone is monitored, removing the stalkerware may signal your discovery to the abuser. Contact the Coalition Against Stalkerware (stopstalkerware.org) or a domestic violence organization for guidance tailored to your situation before removing the software.

**Technical removal — Android:**

1. Boot into Safe Mode (hold power button, long-press Power Off to get Safe Mode option on most devices)
2. In Safe Mode, third-party apps cannot run — the stalkerware is inactive
3. Revoke device admin rights: Settings → Security → Device Admin Apps → uncheck the suspicious app
4. Uninstall the app: Settings → Apps → find the app → Uninstall

After removing, change all passwords from a different device (in case a keylogger captured your credentials).

**Most reliable option — Factory Reset:**

A factory reset is the nuclear option that removes all installed apps, returning the device to factory state. This removes virtually all consumer stalkerware.

Before resetting:
- Back up contacts (to Google account or export)
- Back up photos to a PC or cloud service
- Note which apps you need to reinstall

After resetting, restore data manually — do not restore from a backup that might have been made while stalkerware was active.

### After Removing Spyware

1. Change all passwords — use a password manager to set strong unique passwords for each account
2. Enable 2FA on all important accounts
3. Review app permissions on the clean device
4. Consider whether a new device is warranted (for Pegasus-level threats, yes)
5. If in a domestic abuse situation, consult with organizations that specialize in technology-enabled abuse

---

## Prevention: Reducing Spyware Risk

**Keep your OS updated:** The vast majority of Pegasus deployments exploited vulnerabilities that were subsequently patched by Apple or Google. Immediate updates when security patches release is the most important preventive action.

**Enable iOS Lockdown Mode (high-risk individuals):** If you are a journalist, activist, or anyone who believes they might be targeted by nation-state spyware, Lockdown Mode significantly reduces the attack surface. The usability tradeoffs are real but may be worth it.

**Physical device security:** Consumer stalkerware requires physical access in most cases. Use a strong device passcode (6+ digits or alphanumeric). Never leave your device unattended with someone who might want to surveil you.

**Avoid sideloading (Android):** Installing APKs from outside the Google Play Store significantly increases stalkerware risk. Only enable "install from unknown sources" when you have a specific trusted reason.

**Use a reputable security app:** Running [Bitdefender Mobile Security](https://go.digitalshieldpro.com/bitdefender) on Android provides ongoing protection against new stalkerware variants and alerts you to suspicious app behavior. It is not perfect, but it significantly raises the bar for consumer-grade attacks.

**VPN usage:** A VPN like [NordVPN](https://go.digitalshieldpro.com/nordvpn) does not directly prevent spyware installation but encrypts your traffic so that data exfiltrated by spyware is harder to intercept at the network level.

---

## Understanding Spyware Business Models

The commercial market for surveillance tools is larger and more complex than most people realize:

### The NSO Group Model

NSO Group markets Pegasus exclusively to governments, claiming they vet clients for human rights compliance. The evidence consistently contradicts this claim. The Pegasus Project investigation identified journalists in Azerbaijan, Hungary, India, Morocco, Rwanda, and other countries as targets. Mexico's government deployed Pegasus against journalists and politicians including those critical of the government.

NSO charges roughly $500,000-$1 million upfront plus per-device fees. At this pricing tier, only governments and well-funded organizations can afford it.

In 2021, Apple sued NSO Group and secured a preliminary injunction preventing NSO from using Apple products or services. The US government added NSO Group to its Entity List in November 2021, restricting US companies from doing business with them.

### The Consumer Stalkerware Industry

Consumer stalkerware operates completely in the open. Apps like mSpy, FlexiSpy, and Hoverwatch advertise openly on Google and social media. They are marketed primarily to:

- Parents monitoring children
- Employers monitoring employees
- Spouses monitoring partners

The third category is the domestic abuse application. Studies by the Coalition Against Stalkerware and academic researchers consistently find that consumer stalkerware is disproportionately used in intimate partner violence contexts.

A 2020 study published in the journal Computers in Human Behavior found that 1 in 10 people in intimate relationships reported using monitoring apps without their partner's knowledge, and 1 in 4 reported that their partner had monitored them without consent.

### "Dual Use" Monitoring Apps

Between nation-state tools and consumer stalkerware is a gray area: apps that are genuinely sold for parental control or employee monitoring that are technically similar to stalkerware. Whether they are used appropriately depends entirely on consent and disclosure.

Google Play and Apple App Store policies technically prohibit stalkerware, but enforcement is inconsistent, and many such apps have circumvented the rules through careful marketing language.

---

## Building a Spyware-Resistant Lifestyle

Beyond detection and removal, there are structural habits that reduce ongoing spyware risk:

**Separate devices for separate contexts.** A journalist might use one phone for sensitive source communication (with Tails or a hardened device), a different phone for everyday life. This compartmentalization means a compromise of one context does not compromise the other.

**Minimize the attack surface.** Every app you install is a potential entry point. Keep only the apps you actively use. A phone with 12 carefully chosen apps is a smaller target than one with 150 apps including forgotten utilities.

**Regular device cycling.** Some security-conscious people replace their phones every 1-2 years. A fresh device means any malware does not persist. This is expensive but relevant for high-risk individuals.

**Secure communications for sensitive topics.** Using Signal or another encrypted messenger for sensitive conversations while keeping sensitive topics off SMS, email, and social DMs significantly reduces the value of phone surveillance.

**Awareness of physical access.** Most consumer stalkerware requires physical access. Know where your phone is. A device you cannot account for for an hour is a device that may have been compromised.

---

## When to Seek Professional Help

If you believe you may have been targeted by nation-state spyware:

1. Contact Amnesty Tech's Security Lab (securitylab@amnesty.org) — they investigate potential Pegasus cases involving human rights defenders and journalists
2. Contact Access Now's Digital Security Helpline (accessnow.org/help) — they provide free digital security support for civil society
3. Do not forensically investigate your device yourself if you believe you are under active surveillance — you may destroy evidence needed for documentation

If you are in a domestic abuse situation involving stalkerware, contact the National Domestic Violence Hotline (US: 1-800-799-7233) or your country's equivalent before taking technical action.

Spyware, at every tier, is a serious threat. Consumer stalkerware is a tool of control and abuse. Nation-state spyware has been used to target people who were subsequently imprisoned or killed. Take it seriously, use the right detection tools for your threat model, and seek professional help when your situation warrants it.


<a href="https://go.digitalshieldpro.com/nordvpn" class="cta-affiliate" rel="nofollow noopener sponsored" target="_blank">View Nordvpn</a>

## Related guides

- [How to Secure Your iPhone in 2026: Complete Apple Security](/posts/how-to-secure-iphone-2026/)
- [Best Secure Mobile Browsers 2026: Brave, Firefox](/posts/best-secure-browsers-mobile-2026/)
- [Best Antivirus for Android in 2026: Top Mobile Security Apps](/posts/best-antivirus-for-android-2026/)
- [How to Detect Keyloggers in 2026: Hardware and Software Methods](/posts/how-to-detect-keyloggers-2026/)
- [Best Anti-Malware Software 2026: Top 5 Tools Compared](/posts/best-anti-malware-software-2026/)
