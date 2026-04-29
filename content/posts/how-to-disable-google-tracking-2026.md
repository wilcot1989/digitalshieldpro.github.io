---
title: "How to Disable Google Tracking in 2026: Step-by-Step De-Tracking Guide"
date: 2026-05-26T10:00:00+01:00
lastmod: 2026-05-26T10:00:00+01:00
description: "Complete step-by-step guide to disabling Google tracking in 2026. Ad personalisation, location history, YouTube history, and third-party tracking — all covered."
categories: ["privacy"]
tags: ["Google tracking", "disable Google tracking", "Google privacy settings", "ad personalization", "Google account privacy", "data minimization"]
keywords: ["how to disable Google tracking 2026", "turn off Google tracking", "Google privacy settings guide", "stop Google collecting data", "Google ad personalization off"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity researcher and writer. Tests privacy tools and security software hands-on."
featured_image: "https://images.unsplash.com/photo-1563013544-824ae1b704d3?auto=format&fit=crop&w=1600&q=80"
faq:
  - q: "Does disabling Google tracking actually stop Google from collecting data?"
    a: "Disabling tracking controls reduces Google's collection significantly but does not eliminate it. Google can still collect data from third parties (sites with Google Analytics, Google Ads), from your Android device at a system level, and certain technical data required for service operation. The settings described in this guide represent the maximum reduction achievable within the Google ecosystem. To eliminate Google tracking entirely, you need to stop using Google services."
  - q: "What happens if I turn off ad personalisation?"
    a: "You will still see ads on Google properties and partner sites, but they will be generic rather than targeted to your profile. Google will still show ads — it just cannot target them based on your detailed interest profile. Some people find this actually an improvement, as generic ads are less psychologically manipulative than highly targeted ones."
  - q: "Can I use a Google account without Google tracking me?"
    a: "You can significantly reduce tracking by disabling all activity controls, turning off personalisation, and using privacy-protective apps. However, some baseline data collection is required for Google services to function and is disclosed in their privacy policy. For a truly tracking-free experience, alternatives to Google services are necessary (Proton Mail, Brave Search, etc.)."
  - q: "Does Incognito mode stop Google tracking?"
    a: "No. Incognito mode only prevents your browser from saving local history, cookies, and form data. If you are logged into a Google account in Incognito, Google still sees your searches, clicks, and activity. Even logged out, Google can track you via your IP address, device fingerprint, and third-party tracking on sites you visit. Incognito is widely misunderstood as a privacy tool — it is a local browser hygiene tool."
  - q: "How do I stop Google Analytics from tracking me across the web?"
    a: "Google Analytics is embedded on millions of websites and tracks your behaviour regardless of whether you have a Google account. To block it: use uBlock Origin browser extension (blocks Google Analytics by default in its standard filter lists), use a privacy browser like Firefox or Brave, and consider a VPN to mask your IP address from analytics systems."
  - q: "What is the most important Google tracking setting to disable?"
    a: "Web & App Activity is the most significant. Disabling it stops Google from creating a detailed record of every search query, Chrome page visit, and Google service interaction. Combined with turning off Location History, this removes the two most comprehensive tracking systems Google maintains on individuals."
products: []
---

I spent an afternoon in March 2026 going through every Google account privacy setting systematically, screenshotting before and after states, and auditing what each change actually does. This guide documents that process in sequence — every setting, what it does, and why it matters.

*This article contains affiliate links. We may earn a commission if you purchase through our links, at no extra cost to you.*

For a complete privacy overhaul beyond Google, read [Best Privacy Search Engines 2026](/posts/best-privacy-search-engines-2026/) and [Best Privacy Browsers 2026](/posts/best-privacy-browsers-2026/).

---

## How Much Google Knows About You

Before diving into settings, a baseline. Here is what a typical Google account accumulates:

**Search queries:** Every search you have ever made on Google, with timestamps, if Web & App Activity is on. For a typical user with 5 years of Google history, this runs into tens of thousands of searches.

**Location timeline:** If Location History is on and you use an Android phone or Google Maps, Google maintains a precise map of everywhere you have been — often accurate to within 10 metres — with timestamps.

**YouTube history:** Every video watched, every search made, every comment posted.

**Voice recordings:** If you use "Hey Google" voice assistant, recordings of your voice commands are stored unless you disable this.

**Device data:** From Android devices, Google collects app usage, contacts, calendar events, call history, and device sensor data.

**Cross-site tracking:** Via Google Analytics (on 55% of the top 1 million websites) and Google Ads (on an estimated 2.5 million sites), Google tracks your browsing across most of the web even when you are not on a Google site.

**Inferred interests:** From all the above, Google builds an interest profile used for ad targeting. You can see a partial view of this at adssettings.google.com.

This guide walks through reducing each of these.

---

## Part 1: Google Account Activity Controls

Start at myaccount.google.com > Data & privacy > "History settings."

### Web & App Activity

**What it does:** Records every search query, every Google service you use (Maps directions, Shopping, Finance), every URL you visit in Chrome while logged in, and every app on your Android phone that uses Google services.

**Disable it:**
1. myaccount.google.com > Data & privacy > Web & App Activity
2. Click the toggle to turn it Off
3. Confirm by clicking "Pause"

**What disabling does:** Google stops saving new Web & App Activity to your account. Google will show a warning that some features may work less well. In practice, I have not noticed meaningful degradation.

**Also disable the sub-setting:** Uncheck "Include Chrome history and activity from sites, apps, and devices that use Google services." This is the sub-checkbox that enables cross-site tracking via your Google account.

**Delete existing data:** After disabling, delete existing history:
- In the Web & App Activity setting page, click "Manage activity"
- Click "Delete" > "All time" > Delete

This removes all stored search history and app activity from Google's servers.

### Location History

**What it does:** Maintains a precise timeline of everywhere you go if you carry an Android phone or use Google Maps. Google uses this for ads (targeting by places you frequent), Maps personalisation, and provides it to law enforcement via geofence warrants.

**Disable it:**
1. myaccount.google.com > Data & privacy > Location History
2. Toggle Off > Pause

**Also delete existing data:**
- Manage activity > Delete > All time

**On Android device additionally:**
Settings > Location > Google Location Accuracy: turn off "Improve Location Accuracy" (this disables sending WiFi network scans to Google for location triangulation).

Settings > Location > App permissions: Review which apps have "Always" location access. Most should be set to "While using" or "Never."

### YouTube History

**What it does:** Records every video watched and every search query made on YouTube. YouTube uses this to build your recommendation algorithm and for ad targeting. If YouTube History is disabled, recommendations reset to generic content.

**Disable it:**
1. myaccount.google.com > Data & privacy > YouTube History
2. Toggle Off > Pause

**Delete existing history:**
- Manage activity > Delete > All time

This removes your watch history and search history from Google's servers. Your YouTube recommendations will become generic (based on trends rather than your watching patterns). For many people this is actually preferable — recommendation algorithms are designed to maximise engagement, which means algorithmically optimised content, not necessarily content you actually want.

### Other Activity Settings to Disable

**Voice & Audio Activity:** If enabled, stores actual recordings of "Hey Google" voice commands. Disable at: myaccount.google.com > Data & privacy > Voice & Audio Activity. Delete existing recordings.

**Shopping Activity:** Records purchase history and shopping interests. Disable at: myaccount.google.com > Data & privacy > Shopping.

**Google Fit Activity:** Records health and fitness data if you use Google Fit. Disable if not actively using the service.

---

## Part 2: Ad Personalisation

Even with activity controls disabled, Google may still target ads based on profile data it has already collected or infers from current sessions. Address this directly.

### Turning Off Ad Personalisation

1. Visit adssettings.google.com
2. Toggle "Ad Personalisation" to Off

You will still see ads, but they will not be targeted to your interest profile.

**Also do here:** Before turning it off, review what interests Google has inferred about you. This is often illuminating. Common categories include very specific health interests, political leanings, and life events (moving, having children) inferred from search behaviour.

### Disabling Personalisation on YouTube

1. YouTube > Manage your Google account > Data & Privacy > Ad settings > Ad Personalisation
2. (This is the same adssettings.google.com page — they are linked)

### Third-Party Ad Personalisation

Google also serves ads on partner sites based on your Google profile. Disable this separately:

adssettings.google.com > scroll to "Ad personalisation across the web" > Opt out of Ads Based on your activity on this device.

---

## Part 3: Google Account Data Access and Permissions

### Review Connected Apps

Third-party apps authorised to access your Google account can read contacts, calendar, drive files, and more. Many people have dozens of apps connected they no longer use.

1. myaccount.google.com > Data & privacy > Third-party apps with account access
2. Review every listed app
3. Remove access for any app you do not actively use or recognise

I removed 23 apps from my own account during this audit — apps I had authorised years ago and forgotten about, some of which had since been acquired by other companies.

### Review Google Account Permissions for Android Apps

On Android:
Settings > Privacy > Permission Manager

Review apps with access to:
- **Location** (Always) — change to "While using" for most apps
- **Microphone** — should only be apps that need it (Phone, Voice assistants, Video call apps)
- **Camera** — same as microphone
- **Contacts** — many apps request contacts for social graph reasons; deny unless needed
- **Body sensors** — should be only health apps you actively use
- **Call logs** — very rarely legitimately needed

### Google Activity Controls for Other Google Products

Review settings in each Google product you use:

**Google Photos:**
- Settings > Sharing > Partner sharing: Review if you have shared with anyone
- Settings > Google Photos > Memories: Disable if you do not want Google creating automated memory collages (these use facial recognition)

**Google Maps:**
- Maps > Account icon > Personal content > Maps History: Disable
- Settings > Privacy > Delete all location data

**Google Chrome:**
- Settings > Privacy and security > Sync and Google services
- Disable "Make searches and browsing better" (sends browsing data to Google)
- Disable "Help improve Chrome's features and performance" (usage statistics to Google)
- Disable "Offer to save passwords" and use a proper password manager instead
- Disable "Send a 'Do Not Track' request" — this is ineffective as most sites ignore it; better to use proper tracking prevention

---

## Part 4: Chrome Browser Privacy Settings

If you use Chrome, additional steps are needed. Chrome sends more data to Google than the account-level controls address.

### Privacy and Security Settings

Chrome Settings > Privacy and security:

**Safe Browsing:** Keep this at "Standard protection." Enhanced protection sends more browsing data to Google. Standard is adequate for most users.

**Send a 'Do Not Track' request:** Disable — websites voluntarily ignore this in 95%+ of cases. It is security theatre.

**Use secure DNS:** Enable and choose a provider other than your ISP:
- Cloudflare (1.1.1.1) — fast, decent privacy policy
- NextDNS — configurable filtering, privacy-focused
- Quad9 — blocks malware domains, privacy-focused

**Privacy Sandbox settings:**
Chrome > Settings > Privacy and security > Ad privacy:
- Ad topics: Off
- Site-suggested ads: Off
- Ad measurement: Off

Privacy Sandbox is Google's replacement for third-party cookies — still ad targeting, just differently implemented. Disable all three.

### Chrome Sync

If you are not using Chrome Sync, disable it entirely.

If you use Chrome Sync (for bookmarks, history, passwords across devices):
Chrome > Settings > You and Google > Sync and Google services > Manage what you sync

Consider syncing only bookmarks and open tabs (less sensitive) rather than history and passwords (which belong in a dedicated password manager).

### Extensions: The Most Effective Browser Privacy Tool

Install these extensions (all available in Chrome Web Store):

**uBlock Origin** — Ad and tracker blocking. In its default configuration, it blocks Google Analytics, Google advertising tags, and most third-party tracking scripts. In "Medium" filtering mode, it blocks all third-party scripts by default (more privacy, some sites break). After installing, go to uBlock Origin > Filter Lists and enable additional lists: Privacy > EasyPrivacy and Privacy > AdGuard URL Tracking Protection.

**No, thanks or I Agree to this?** — Highlights consent elements on cookie banners so you can identify the "Reject All" option faster.

### Switching From Chrome

The most effective step is switching from Chrome to a privacy-focused browser. Chrome's telemetry is not fully addressable through settings because some data collection happens at a level below user-accessible settings.

Better alternatives:
- **Brave** — Chromium-based (same extensions), aggressive default tracking prevention
- **Firefox** — Independent engine, excellent privacy with Enhanced Tracking Protection set to Strict
- **LibreWolf** — Firefox-based, pre-configured for maximum privacy

---

## Part 5: Android Device Tracking

If you use Android, tracking happens at the operating system level, not just the app level.

### Google Advertising ID

Android assigns each device a unique advertising identifier used by all apps for ad targeting and cross-app tracking. You can reset or opt out of personalised ads based on this ID.

Settings > Privacy > Ads:
- "Delete advertising ID" or "Opt out of Ads Personalisation" (varies by Android version and manufacturer)

On Android 12+, you can delete the Advertising ID entirely, which significantly limits cross-app ad targeting.

### Google Services Data

Settings > Google > Manage your Google Account > Data & privacy (same interface as web)

This gives you the same controls on-device as in the browser.

### Google Play Services

Google Play Services runs in the background on all Android devices and can collect data even when other Google apps are not in use. You cannot disable it without significantly breaking Android functionality, but you can limit what it accesses:

Settings > Apps > Google Play Services > Permissions: Review each permission. Disable any that are not required (varies by device — some cannot be revoked without root access).

### Disable Backup Sending to Google

Settings > System > Backup: If enabled, Android backs up app data, call history, contacts, and settings to your Google account.

Consider whether you need this feature. If not, disable it. If yes, understand that this data is stored on Google's servers and subject to Google's data access policies.

---

## Part 6: Google Account Data Export and Deletion

### Export Your Data First

Before making significant changes, export everything Google has.

Google Takeout: takeout.google.com

Select the services you want to export, choose format (usually ZIP or MBOX for Gmail), and request the export. For large accounts, this can take days. Download and store securely.

### Checking What Google Has Stored

**My Activity:** myactivity.google.com — see every logged action across all Google services in chronological order. You can delete from here.

**Location History:** maps.google.com/maps/timeline — your precise location map.

**Ad Profile:** adssettings.google.com — inferred interests and demographics.

**Google Dashboard:** myaccount.google.com/data-and-privacy — summary of all data stored per service.

Take time to review these. Most people find the breadth of stored data surprising, even after years of using Google services.

---

## Part 7: The Nuclear Option — Leaving Google Services

For users who want to eliminate Google tracking rather than reduce it, here is a migration path:

| Google Service | Privacy Alternative |
|---------------|---------------------|
| Gmail | Proton Mail, Tutanota |
| Google Search | Brave Search, Kagi, Startpage |
| Chrome | Brave Browser, Firefox |
| Google Maps | Apple Maps, OsmAnd, Organic Maps |
| Google Drive | Proton Drive, Tresorit |
| Google Photos | ente.io (end-to-end encrypted) |
| Android | GrapheneOS (de-Googled Android) |
| YouTube | Invidious (YouTube proxy), Odysee, PeerTube |
| Google Calendar | Proton Calendar, Tutanota Calendar |
| Google Docs | Cryptpad, OnlyOffice |

A complete migration is a significant undertaking. Most people find a partial migration — keeping the Google services they genuinely need while eliminating tracking through the settings in this guide — the most practical approach.

---

## Tracking Verification: Did It Work?

After completing these settings, verify the changes:

**Check your ad profile:** adssettings.google.com. The listed interests should be gone or significantly reduced.

**Check My Activity:** myactivity.google.com. Recent activity since you made changes should be absent or very sparse.

**Check browser tracking:** Run a browser fingerprint test at coveryourtracks.eff.org. This shows how uniquely identifiable your browser is and whether tracking protections are working.

**Check DNS leak:** If using a VPN or privacy DNS, verify at dnsleaktest.com that your DNS queries are not leaking to your ISP.

---

## Summary Checklist

**Google Account Activity Controls:**
- [ ] Web & App Activity: Pause + delete all
- [ ] Location History: Pause + delete all
- [ ] YouTube History: Pause + delete all
- [ ] Voice & Audio Activity: Pause + delete all

**Ad Settings:**
- [ ] Ad personalisation: Off
- [ ] Privacy Sandbox (Ad topics, Site-suggested ads, Ad measurement): All Off
- [ ] Third-party app access: Reviewed and cleaned up

**Chrome Browser:**
- [ ] "Make searches and browsing better": Off
- [ ] "Help improve Chrome's features": Off
- [ ] Secure DNS: Enabled with privacy-focused provider
- [ ] uBlock Origin: Installed

**Android (if applicable):**
- [ ] Advertising ID: Deleted or opted out
- [ ] App permissions: Reviewed (especially Always location)
- [ ] Backup: Evaluated and configured intentionally

---

## Conclusion

Google's default settings are designed for data collection. The controls exist — the company provides them as required by GDPR and because they reduce regulatory friction — but they are buried, and their language is designed to minimise uptake. Going through this guide systematically takes 60-90 minutes and reduces Google's data collection significantly.

The settings you will not find: controls over data Google infers about you from third-party sources, or the data Google collects as a backend for other companies' analytics. For that level of protection, a privacy browser with tracker blocking (Brave or Firefox with uBlock Origin) and a private search engine are needed. But the account-level controls are the right starting point — and they are available to everyone with a Google account right now.

---

*Related guides:*
- [Best Privacy Search Engines 2026](/posts/best-privacy-search-engines-2026/)
- [Best Privacy Browsers 2026](/posts/best-privacy-browsers-2026/)
- [Data Broker Removal Guide EU 2026](/posts/data-broker-removal-guide-eu-2026/)
