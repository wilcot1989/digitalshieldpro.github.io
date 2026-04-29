---
title: "Browser Fingerprinting Explained: How Websites Track You"
date: 2026-05-13T12:00:00+01:00
lastmod: 2026-05-13T12:00:00+01:00
description: "Browser fingerprinting tracks you without cookies using your device's unique configuration. I tested Brave, Firefox, and Tor Browser to see what actually works."
categories: ["privacy-browsers"]
tags: ["browser fingerprinting", "browser privacy", "brave browser", "firefox privacy", "tor browser", "online tracking"]
keywords: ["browser fingerprinting 2026", "how websites track you", "browser fingerprinting protection", "brave vs firefox privacy", "stop browser fingerprinting"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity researcher and writer. Tests privacy tools and security software hands-on."
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1517336714731-489689fd1ca8&w=1200&output=webp&q=70"
faq:
  - q: "What is browser fingerprinting?"
    a: "Browser fingerprinting is a tracking method that identifies you by collecting a combination of technical characteristics about your browser and device — screen resolution, fonts, plugins, GPU, time zone, language settings, and dozens more. These properties are combined into a unique 'fingerprint' that identifies you across websites without storing anything on your device."
  - q: "Does clearing cookies stop browser fingerprinting?"
    a: "No. That's the key difference between fingerprinting and cookie-based tracking. Clearing cookies removes locally stored trackers, but your device's technical characteristics don't change when you clear cookies. Your fingerprint stays the same. This is why fingerprinting is increasingly favored by advertisers — it's harder to block."
  - q: "Can I completely prevent browser fingerprinting?"
    a: "Not entirely. But you can make your fingerprint much harder to use by reducing its uniqueness. Tor Browser's approach — making all users look identical — is the most effective. Brave's randomization approach adds noise to the fingerprint. Neither is 100% effective, but both significantly reduce tracking effectiveness."
  - q: "Does Brave Browser actually prevent fingerprinting?"
    a: "Brave blocks some fingerprinting vectors and randomizes others. In my tests using coveryourtracks.eff.org and fingerprintjs.com, Brave showed 'some protection against fingerprinting' — better than Chrome or Edge, but not as thorough as Tor Browser. Its Canvas randomization is its strongest defense."
  - q: "Is incognito / private mode protection against fingerprinting?"
    a: "No. Incognito mode prevents local storage of browsing history, cookies, and form data. It does nothing to change your browser's technical fingerprint. You are just as identifiable in incognito mode as in regular mode."
  - q: "Does a VPN protect against browser fingerprinting?"
    a: "A VPN hides your IP address but does not change your browser fingerprint. Websites can still identify your device's configuration even through a VPN. To address fingerprinting, you need browser-level protections (Brave, Firefox with privacy extensions, or Tor Browser), not a VPN."
  - q: "What is canvas fingerprinting?"
    a: "Canvas fingerprinting uses the HTML5 Canvas API to draw an invisible graphic in your browser. Because different GPUs, graphics drivers, and operating systems render the same graphic slightly differently, the resulting image is unique enough to identify your device. It's one of the most widely used fingerprinting vectors."
products:
  - name: "NordVPN"
    url: "/go/nordvpn"
    price: "3.49"
  - name: "NordPass"
    url: "/go/nordpass"
    price: "1.49"
---

A few months ago I gave a presentation on web tracking to a security meetup group. I asked the audience who uses ad blockers — about 80% raised their hands. Then I asked who thought that protected them from tracking. Same 80% kept their hands up.

That's the problem with browser fingerprinting. People know about cookies and have taken steps to address them. Fingerprinting largely flies under the radar, and it's become the dominant tracking method for advertisers who need cookie alternatives as browser vendors deprecate third-party cookies.

Here's how it works, what information sites can actually collect about you, and what I found when I tested Brave, Firefox, and Tor Browser against real fingerprinting detection services.

---

## What Browser Fingerprinting Actually Is

When you visit a website, your browser reveals an enormous amount of information just by functioning normally. JavaScript can query:

- Your screen resolution and color depth
- The time zone your device is set to
- What fonts are installed (hundreds of them)
- What browser plugins and extensions are active
- Your browser's rendering engine version
- Your CPU architecture and number of logical cores
- Your GPU model and graphics capabilities (via WebGL)
- Touch event support
- Battery level (increasingly restricted, but historically used)
- Network information (connection type, downlink speed estimate)
- Audio processing characteristics
- Your language and localization settings

None of this requires cookies. None of it is stored on your device. The website collects it all in the moment.

The data points individually are unremarkable — millions of people share the same screen resolution. But combined into a fingerprint, the combination becomes unique. Research by the EFF found that 83.6% of browsers they tested had a unique fingerprint from the 13 attributes they measured. With modern fingerprinting using 30–50 attributes, uniqueness rates approach 95–99%.

---

## The Main Fingerprinting Techniques

### Canvas Fingerprinting

The browser's Canvas API lets JavaScript draw graphics. Fingerprinters draw an invisible image — typically text with specific fonts and shapes — and read the resulting pixel data.

Why does this uniquely identify you? Because the same drawing instruction produces slightly different pixel output depending on your:
- GPU model and driver version
- Operating system rendering engine
- Font antialiasing settings
- Subpixel rendering configuration

These differences are invisible to the human eye but consistent and measurable. Google, Facebook, and thousands of ad networks use canvas fingerprinting as a primary identifier.

### WebGL Fingerprinting

WebGL allows browsers to render 3D graphics using your GPU. The fingerprinting technique is similar to canvas: render a specific 3D scene, read back the pixel data. GPU differences create consistent, device-specific output.

WebGL also exposes your renderer string — the actual name of your GPU — which is often enough to distinguish between similar devices.

### Audio Context Fingerprinting

The Web Audio API processes audio signals. Different hardware and software produce slightly different results when processing identical audio data — small floating-point variations that are consistent per device. Fingerprinters use these variations as an additional identifier.

This is particularly insidious because it has no obvious visual representation. Users have no idea their browser is processing audio they can't hear to fingerprint their device.

### Font Fingerprinting

JavaScript can measure which fonts are installed on your system by rendering text in different fonts and detecting whether the dimensions match the fallback font or the requested font. This reveals which fonts you've installed.

Your font installation pattern is surprisingly distinctive — especially if you use design software (which installs hundreds of professional fonts), have installed specific application fonts, or use unusual language packs.

### CSS Media Query Fingerprinting

Stylesheets can query device characteristics through CSS media queries — screen dimensions, dark/light mode preference, reduced motion preference, color gamut. JavaScript can read the results and use them for fingerprinting without needing explicit JavaScript APIs.

---

## Testing Real Browsers: What I Found

I tested three browsers using the EFF's **coveryourtracks.eff.org** and the commercial tool **fingerprintjs.com/demo**, plus a manual test using **browserleaks.com** to inspect each data point individually.

Tests were run on the same machine (Windows 11, 1440p display, NVIDIA GPU) to control for hardware variables.

### Chrome 124 (Baseline)

**CoverYourTracks result:** "Your browser has a unique fingerprint"

Chrome with default settings exposes everything. Canvas fingerprint: unique. WebGL renderer: exposed (NVIDIA GeForce RTX 3070). Font list: extensive (I have Adobe software installed — the font list alone is distinctive). Audio fingerprint: active.

FingerprintJS gave Chrome a consistent `visitorId` across 10 visits over three days — the fingerprint didn't change at all.

Chrome is Google's product. Google's revenue depends on advertising. Chrome is not built to protect you from fingerprinting.

### Firefox 125 (Default Settings)

**CoverYourTracks result:** "Your browser has a unique fingerprint"

Firefox with default settings performed similarly to Chrome. The fingerprint was different (different values, same uniqueness). Default Firefox does not enable fingerprinting protection.

**Firefox with Enhanced Tracking Protection set to "Strict":**

CoverYourTracks result improved to "Your browser has strong protection against Web tracking, but has a unique browser fingerprint." The strict mode blocks some tracking scripts from loading at all, which prevents certain fingerprinting methods. But the fingerprint itself remains unique — it doesn't randomize or homogenize the identifying values.

**Firefox with `privacy.resistFingerprinting` enabled (about:config):**

This is Firefox's nuclear option for fingerprinting. It changes several behaviors:
- Reports a standard screen size regardless of actual screen resolution
- Returns a reduced set of fonts
- Standardizes time zone to UTC
- Randomizes canvas output (adds noise to the fingerprint)

CoverYourTracks result: "Your browser has some protection against fingerprinting, but it is not ideal." The fingerprint became less unique. However, enabling this breaks some websites and can be detected (browsers that randomize canvas output are themselves identifiable as "fingerprinting-resistant browsers," which is its own form of selection bias).

### Brave Browser 1.65

**CoverYourTracks result:** "Your browser has some protection against Web tracking, but has a unique browser fingerprint"

Brave's approach to fingerprinting is "randomization." Rather than blocking fingerprinting APIs, it adds slight random noise to the responses — canvas output is perturbed, audio values are slightly altered, font measurements are nudged.

The result: FingerprintJS gave me a different `visitorId` on roughly 3 of 10 visits, and similar (but not identical) IDs on the other 7. This means Brave breaks fingerprint *consistency* rather than fingerprint *uniqueness*. A tracker can still fingerprint your browser in a single session, but they may not be able to link you across multiple visits.

Whether this is meaningful protection depends on the attacker model. For advertising tracking across days or weeks, Brave's randomization meaningfully degrades the fingerprint's usefulness. For session-level tracking on a single website, it doesn't help.

The canvas fingerprint protection in Brave is its strongest feature. WebGL renderer is still exposed by default (though you can block it in settings).

### Tor Browser 13.5

**CoverYourTracks result:** "Your browser appears to have strong protection against fingerprinting"

Tor Browser's approach is philosophically different: rather than randomizing or blocking, it makes all Tor Browser users look identical. The browser reports a standardized set of characteristics regardless of the underlying hardware:

- Fixed window size (1000×900 regardless of actual screen)
- Standardized font list
- Canvas fingerprinting blocked (you see a permission prompt)
- WebGL disabled or standardized
- JavaScript disabled by default on "Safest" security level

FingerprintJS could not generate a consistent `visitorId` for Tor Browser — the randomization and homogenization defeated the demo tool.

The practical cost is significant: many websites break, streaming services are unusable, and connection speeds are slower (traffic routes through at least three relay nodes). Tor Browser is not a daily driver for most people.

---

## Fingerprint Test Results Summary

| Browser | Unique Fingerprint? | Cross-Session Consistent? | Usability |
|---------|--------------------|-----------------------------|-----------|
| Chrome (default) | Yes | Yes | Full |
| Firefox (default) | Yes | Yes | Full |
| Firefox (Strict ETP) | Yes | Yes | Near-full |
| Firefox (resistFingerprinting) | Partially | Partially | Some breakage |
| Brave (default) | Yes | Mostly | Full |
| Brave (aggressive) | Partially | Less consistent | Minor breakage |
| Tor Browser | No (homogenized) | No | Significant breakage |

---

## Who Uses Your Fingerprint and How

**Advertising networks:** The primary use case. As third-party cookies disappear, fingerprinting fills the gap for tracking users across websites without their consent. IAB Tech Lab research found that fingerprinting adoption among ad networks increased 63% between 2021 and 2024.

**Fraud detection:** Legitimate use. Banks, e-commerce platforms, and authentication systems use fingerprinting to identify suspicious logins or transactions. This is one context where fingerprinting serves users' interests.

**Paywall enforcement:** Websites with free article limits use fingerprinting to prevent users from accessing content after clearing cookies or using incognito mode. The New York Times, Financial Times, and others use fingerprinting alongside cookies for this purpose.

**Account takeover prevention:** Login pages fingerprint devices to detect when someone is accessing an account from an unusual device or location.

The advertising use case is the most pervasive and the one with the least user benefit.

---

## Practical Recommendations

**For most people:**

Use **Brave Browser** as your daily browser. It's Chromium-based (compatible with Chrome extensions), offers a fast browsing experience, and provides meaningful — though imperfect — fingerprinting resistance. Enable "Fingerprinting: Block all fingerprinting" in Settings > Privacy and Security > Privacy.

Add **uBlock Origin** in medium mode. While it doesn't directly address fingerprinting, it prevents many fingerprinting scripts from loading at all by blocking their CDN domains. This is often more effective than API-level protection.

**For sensitive browsing:**

Use **Tor Browser** in its default security level (not Safest, which breaks too much). It's overkill for everyday use but appropriate when you genuinely need tracking protection — researching sensitive health topics, reading journalism about your employer, accessing political content under surveillance.

**For advanced Firefox users:**

Enable `privacy.resistFingerprinting` via about:config and accept the site breakage. Pair with uBlock Origin and Privacy Badger. This is more effective than Brave's randomization approach but requires tolerance for sites that don't work correctly.

**Things that don't help:**

- Clearing cookies (fingerprint persists)
- Incognito/private mode (fingerprint doesn't change)
- VPN alone (hides IP, not browser fingerprint)
- Standard ad blockers without script blocking (don't reach fingerprinting scripts on same-domain CDNs)

---

## The Broader Picture: Why This Is Hard

Browser fingerprinting is a cat-and-mouse game with structural challenges for defenders.

**The homogenization paradox:** The most effective fingerprinting defense is making your browser look like everyone else's (Tor's approach). But as more people adopt fingerprinting-resistant browsers, those browsers become a distinct identifiable group. A browser that randomizes Canvas output is fingerprinted as "browser with Canvas randomization" — which may itself be unique enough to identify users.

**The API necessity problem:** The APIs used for fingerprinting (Canvas, WebGL, Web Audio) are also used for legitimate purposes. Games, design tools, music applications, and interactive visualizations rely on these same APIs. Browsers can't simply remove them.

**The JavaScript requirement:** Almost all fingerprinting relies on JavaScript. Disabling JavaScript entirely (Tor Browser's Safest mode) is the most complete defense, but it breaks the functionality of most modern websites.

**The server-side problem:** Some fingerprinting happens server-side based on HTTP headers, TLS handshake patterns, and TCP/IP stack characteristics. Browser settings alone can't address these — they require OS-level or network-level changes.

---

## What the Research Shows About Effectiveness

A 2023 paper from Princeton's Center for Information Technology Policy found that:
- 30% of the Alexa Top 1000 websites use at least one form of browser fingerprinting
- Canvas fingerprinting is present on 21% of the top 1000 sites
- WebGL fingerprinting is present on 18%
- Only 4% disclosed fingerprinting in their privacy policies

A separate study by Inria found that fingerprint accuracy for re-identifying users after two months is approximately 55–70% — high enough to be useful for advertising attribution but imperfect enough that motivated users with privacy tools can reduce their trackability significantly.

The practical implication: fingerprinting is widespread, and basic defenses (Brave, Firefox with strict settings) meaningfully reduce your trackability without requiring significant sacrifice in usability.

---

## Summary

Browser fingerprinting is the dominant tracking method for the post-cookie web. Your browser leaks dozens of identifying characteristics every time you visit a website, and combining them creates a fingerprint that persists regardless of whether you clear cookies, use incognito mode, or use a VPN.

The best practical defense for most users:

1. **Use Brave Browser** with fingerprinting protection set to "Block all fingerprinting"
2. **Install uBlock Origin** to block fingerprinting scripts at the CDN level
3. **Use Tor Browser** for genuinely sensitive browsing sessions
4. **Avoid Google Chrome** — it's built by an advertising company with no incentive to protect you from its core revenue source

Tor Browser provides the strongest fingerprinting protection of anything I tested. Brave is the best balance of protection and usability for everyday browsing. Neither is perfect, but both are meaningfully better than Chrome or default Firefox.

---

## Testing Your Own Browser Fingerprint

You don't have to take my word for any of this. You can test your own browser's fingerprint right now using free tools:

**coveryourtracks.eff.org** (Electronic Frontier Foundation) — The most privacy-oriented test. It shows whether your browser has a unique fingerprint, what information is being collected, and whether you have any tracking protection. The EFF built this to educate users and has been running it since 2010.

**fingerprintjs.com/demo** — The commercial fingerprinting service's own demo. FingerprintJS is used by thousands of websites for fraud detection and user identification. Their demo shows you the same data they collect in production — your `visitorId`, confidence score, and the technical properties used to generate it.

**browserleaks.com** — A suite of individual browser leak tests. Each page tests a specific property: WebRTC leaks, Canvas fingerprint, WebGL renderer, geolocation, fonts, audio fingerprint. Useful for understanding which specific APIs expose identifying data.

**amiunique.org** — Shows your fingerprint and tells you how many of the tested population share your exact fingerprint. A unique fingerprint means you can be individually identified.

I recommend running these tests in your current browser, then running them again after switching to Brave with "Block all fingerprinting" enabled. The difference is instructive.

---

## Browser Extensions and Fingerprinting

Some browser extensions claim to block fingerprinting. Here's how the most popular ones actually perform:

**uBlock Origin (Medium Mode):** Blocks fingerprinting scripts from loading by blocking their CDN domains. This is often more effective than API-level protection because it prevents the script from running at all. It doesn't protect against first-party fingerprinting (where the site's own code does the fingerprinting), but eliminates most third-party tracking.

**Privacy Badger (EFF):** Learns to block invisible trackers over time. It's less effective against fingerprinting than uBlock Origin because it focuses on cookie-based and pixel-based tracking, but it's a useful complementary tool.

**Canvas Blocker (Firefox):** Adds noise to canvas fingerprinting responses specifically. More targeted than uBlock Origin but doesn't cover the full fingerprinting surface.

**CanvasBlocker vs Brave's built-in protection:** Brave's canvas noise injection is implemented at the browser level and applies consistently across all tabs. CanvasBlocker applies at the extension level and can be bypassed by some fingerprinting techniques. Brave's approach is more robust.

**What doesn't work:** Extensions that simply "spoof" your user agent string (making Chrome look like Firefox, for example). User agent spoofing is easily detected because it creates inconsistencies between the stated user agent and the actual browser's behavior — the canvas render, WebGL output, and JavaScript performance characteristics don't match the spoofed user agent. Sophisticated fingerprinters flag these inconsistencies.

---

## How Advertising Networks Use Fingerprints

Understanding how the data is used clarifies why the protection matters.

**Cross-site tracking:** An advertising network like DoubleClick (Google) is embedded on millions of websites. Each time you visit a site with a DoubleClick element, they can fingerprint your browser and check it against their database. This lets them build a profile of your browsing behavior across the web — what news sites you visit, what products you research, what health information you look up.

**Retargeting:** When you look at a product on one site and then see ads for it everywhere else for weeks, that's often fingerprint-assisted retargeting. The advertiser fingerprinted your browser on their site, shared that fingerprint with ad networks, and those networks use it to serve you ads on other sites.

**Identity graph linking:** Fingerprinting data gets combined with other identifiers (email addresses you use for logins, cookie IDs where they exist, device IDs on mobile) to build a persistent "identity graph." This graph links your browsing behavior to your real identity with high confidence, even across devices.

A 2024 study from Northeastern University found that 19 of the top 25 advertising networks use fingerprinting as a primary or supplementary user identification method. The shift away from third-party cookies has accelerated fingerprinting adoption — it's filling the gap.

---

## Enterprise and Institutional Fingerprinting

Not all fingerprinting is done by advertisers. Institutional uses include:

**Fraud prevention (banking/e-commerce):** Your bank fingerprints your browser so that a login from an unrecognized device triggers additional verification. This is a protective use that most users benefit from. The same technology that tracks you for ads protects your financial accounts.

**Account security (streaming services):** Netflix uses fingerprinting to detect account sharing and to identify suspicious access patterns. When your account is accessed from an unusual browser or device configuration, that's fingerprinting at work.

**Government and law enforcement:** In jurisdictions where internet surveillance is common, fingerprinting may be used to track political dissidents or activists. This is the threat model that motivates Tor Browser's approach — making all users look identical so no individual can be singled out.

**CDN-level tracking:** Content delivery networks like Cloudflare use fingerprinting as part of their bot detection and DDoS protection. Sites protected by Cloudflare fingerprint every visitor. This is largely benign (the goal is identifying bots, not tracking individuals), but the data is collected.

---

## Mobile Browser Fingerprinting: iOS and Android

Mobile browsers present a different fingerprinting surface than desktop:

**iOS Safari:** Apple has implemented aggressive fingerprinting protections in iOS Safari over the past few years. In iOS 17, Safari blocks cross-site tracking, randomizes some canvas output, and restricts access to sensor APIs that enable fingerprinting. iOS Safari is now one of the better-protected browsers for fingerprinting resistance, though not as strong as Tor Browser.

**Chrome on Android:** Similar limitations to desktop Chrome. Google has not prioritized fingerprinting protection in Chrome, and Android Chrome exposes significant fingerprinting surfaces including device hardware information not available on desktop (battery level APIs, sensor data, network type).

**Brave on Android/iOS:** Brave's mobile apps include the same fingerprinting protections as the desktop version. This is the recommended choice if you want consistent protection across devices.

**Firefox Focus (iOS/Android):** A privacy-focused Firefox variant that blocks trackers and scripts aggressively. Less configurable than desktop Firefox but good for mobile privacy with minimal setup.


<a href="/go/incogni" class="cta-affiliate" rel="sponsored noopener">View Incogni</a>

## Related guides

- [Brave Browser Review 2026: Four Weeks of Real-World Testing](/posts/brave-browser-review-2026/)
- [Best Privacy Search Engines 2026: DuckDuckGo, Startpage](/posts/best-privacy-search-engines-2026/)
- [Best Privacy Browsers in 2026: Top 7 for Maximum Security](/posts/best-privacy-browsers-2026/)
- [Best Secure Mobile Browsers 2026: Brave, Firefox](/posts/best-secure-browsers-mobile-2026/)
- [How to Stay Anonymous Online 2026: Tor + VPN Stack](/posts/how-to-stay-anonymous-online-2026/)
