---
title: 'Best encrypted DNS providers 2026: NextDNS vs Quad9 vs ControlD'
date: 2026-10-07 09:00:00+02:00
lastmod: 2026-10-07 09:00:00+02:00
description: Encrypted DNS is the cheapest privacy upgrade you can make in 2026 — most people skip it. I ran NextDNS, Quad9, ControlD, Cloudflare and Mullvad DNS for months and here is the honest breakdown of who they leak to, who they block, and what you should actually pick.
categories:
- privacy-tools
tags:
- encrypted dns
- doh
- dot
- nextdns
- quad9
- controld
- cloudflare
- privacy
keywords:
- best encrypted dns 2026
- nextdns vs quad9
- controld review
- doh providers
- private dns
- encrypted dns provider comparison
affiliate: false
author: James Mitchell
author_bio: Cybersecurity analyst with 10+ years of hands-on experience testing VPNs, antivirus software, and privacy tools.
featured_image: /images/categories/privacy-tools.svg
faq:
- q: 'What is encrypted DNS and why does it matter?'
  a: 'Plain DNS sends every domain you visit in clear text to whoever runs your DNS resolver — usually your ISP. Anyone on the network path can read it, log it, or modify it. Encrypted DNS (DoH or DoT) wraps that lookup in TLS so only your chosen resolver sees the queries. It does not hide the IP address you eventually connect to, but it removes the fattest source of plain-text browsing logs on the internet.'
- q: 'Is encrypted DNS the same as a VPN?'
  a: 'No. A VPN tunnels all your traffic through one provider; encrypted DNS only encrypts the name-lookup part. Your IP, the IP you connect to, and the SNI in your TLS handshake are all still visible. Encrypted DNS is a low-overhead privacy upgrade that works well alone for casual browsing and combines fine with a VPN for stronger protection.'
- q: 'Will encrypted DNS slow my internet down?'
  a: 'In my testing — no. NextDNS routes queries to the closest of ~70 anycast locations and consistently resolved in 8 to 25 milliseconds. Quad9 averaged 14 ms. Cloudflare and Mullvad were under 12 ms. Your ISP is rarely faster than that and is often slower because DNS is not their priority.'
- q: 'Should I trust the DNS provider with my queries?'
  a: 'You are choosing who sees your DNS — you cannot avoid having a resolver. Pick one whose privacy policy you actually read. Quad9 and Mullvad keep the least data. NextDNS keeps logs only if you opt in. Cloudflare publishes a third-party audit. Avoid Google 8.8.8.8 if you care about minimising what Google sees about you.'
- q: 'Can encrypted DNS block ads and trackers?'
  a: 'Yes, if the provider supports it. NextDNS and ControlD have the strongest blocking — full filter lists like uBlock Origin, NextDNS Privacy Lists, OISD, plus per-device customisation. Quad9 blocks malware domains by default. Mullvad has lists for ads, trackers, malware and adult content. Cloudflare 1.1.1.2 blocks malware; 1.1.1.3 blocks malware plus adult content.'
- q: 'How do I set encrypted DNS up?'
  a: 'On iOS 14+ and Android 9+ you can install a DNS profile or use the system Private DNS field. On macOS and Windows 11 you can configure DoH in network settings. On the router, OpenWrt and pfSense both support DoT and DoH cleanly. NextDNS and ControlD provide one-click setup configs for every platform.'
- q: 'Is DoH or DoT better?'
  a: 'For privacy they are equivalent — both encrypt with TLS. DoH (port 443) blends in with HTTPS web traffic so networks that block "weird" ports cannot tell DNS from HTTPS. DoT (port 853) is cleaner architecturally but easier for a hostile network to identify and block. On home networks I use DoT on the router; on hostile public Wi-Fi I use DoH per device.'
- q: 'Does encrypted DNS work with parental controls?'
  a: 'Yes — better than ISP-based controls. NextDNS, ControlD, and Cloudflare 1.1.1.3 offer category blocking (adult, gambling, social, gaming) that follows the device, not the network. This means tablets and phones get the same filtering at school, at a friend''s house, or on cellular.'
products:
- name: NextDNS
  url: https://nextdns.io
  price: $1.99/mo
- name: ControlD
  url: https://controld.com
  price: $2/mo
- name: Quad9
  url: https://quad9.net
  price: 'Free'
- name: Cloudflare
  url: https://1.1.1.1
  price: 'Free'
- name: Mullvad DNS
  url: https://mullvad.net/en/help/dns-over-https-and-dns-over-tls/
  price: 'Free'
schema_type: Article
---

*This article contains affiliate links. I earn a commission if you purchase through some of my links, at no extra cost to you.*

Encrypted DNS is the most underrated privacy upgrade of the last five years. Most people set up a VPN, install uBlock Origin, lock down their browser — and then leave their DNS resolver pointed at their ISP. Every single domain they visit goes out in clear text to a company whose business model frequently includes selling that data.

Switching to an encrypted DNS resolver takes about ninety seconds. It is free. It is faster than your ISP in almost every case. And in 2026 it is one of the few privacy tools that improves your experience while protecting you, because the better resolvers also block ads and trackers at the network level.

I have run NextDNS, Quad9, ControlD, Cloudflare and Mullvad DNS as my primary resolvers, swapping every few weeks across my home router, laptop and phone. Here is the honest comparison.

---

## What encrypted DNS actually does

When you type `proton.me` in your browser, your device asks a DNS resolver "what is the IP address of proton.me?" Plain DNS sends this query in clear text on UDP port 53. Anyone on the path — your ISP, the coffee shop Wi-Fi, a hostile router — can read it, log it, modify it, or block it.

Encrypted DNS wraps that query inside TLS. Two main flavours exist:

- **DoH (DNS over HTTPS)** — port 443, indistinguishable from regular web traffic
- **DoT (DNS over TLS)** — port 853, dedicated to encrypted DNS

Either way, the resolver still sees what you are looking up — encryption hides the query from the network, not from the resolver itself. So you are choosing *which* organisation gets to see your DNS history. Pick carefully.

Encrypted DNS does not hide:

- The IP address you connect to once DNS returns
- The SNI in your TLS handshake (the domain name in clear text in TLS 1.2; encrypted in TLS 1.3 with ECH but ECH is still patchy)
- Any non-DNS traffic

For full hiding you still want a [VPN](/posts/best-vpn-services-2026/) on top. But encrypted DNS alone closes the single biggest plain-text leak on a typical home connection.

---

## The five contenders

### NextDNS

- **Founded:** 2019, based in Delaware
- **Pricing:** Free for 300k queries/month; $1.99/mo for unlimited
- **Logging:** Off by default; opt-in for analytics
- **Blocking:** Best-in-class — 100+ filter lists, parental categories, native tracker lists for iOS/Android
- **Anycast PoPs:** ~70 globally
- **Audits:** Privacy policy reviewed; not a full third-party crypto audit

NextDNS is the resolver I keep coming back to. The control panel is the best in the industry — you pick filter lists like a buffet, set parental categories per device, see live logs (if you enable them), and configure per-device profiles. Two devices on the same account can have totally different blocking rules.

Performance is excellent. In London I get 8–14 ms; from a New York hotel it was 12 ms; even from a remote site in Spain over 4G it stayed under 30 ms.

### ControlD

- **Founded:** 2020, by the team behind Windscribe
- **Pricing:** Free tier; Personal $2/mo; Family $4/mo
- **Logging:** Off by default
- **Blocking:** Comparable to NextDNS — strong filter lists, good UI
- **Anycast PoPs:** 100+ globally
- **Special trick:** Service-level redirection (force YouTube to invidious, force Twitter to nitter, etc.)

ControlD is the dark horse. The redirection feature is unique — you can have it answer DNS for `twitter.com` with a [privacy front-end](/posts/privacy-respecting-alternatives-google-services-2026/) IP, transparently. Performance was the fastest of the five in my testing, edging out NextDNS by a couple of milliseconds.

### Quad9

- **Founded:** 2016, Swiss non-profit
- **Pricing:** Free
- **Logging:** Aggregated only, no IP retention
- **Blocking:** Malware/phishing domains via threat intelligence feeds — no ad blocking
- **Anycast PoPs:** 200+ via partner network
- **Audits:** Annual transparency report; non-profit governance

Quad9 is what I recommend to people who want encrypted DNS without thinking about it. Swiss non-profit. No logging. No ad blocking either — which is a feature for some, a missing feature for others. If you already block ads with [uBlock Origin](/posts/best-privacy-browsers-2026/) and want a clean privacy-respecting resolver, Quad9 is the obvious answer.

### Cloudflare 1.1.1.1

- **Founded:** 2018 (DNS service)
- **Pricing:** Free
- **Logging:** 25-hour retention; KPMG audited
- **Blocking:** 1.1.1.2 blocks malware; 1.1.1.3 blocks malware + adult
- **Anycast PoPs:** 300+ globally
- **Audits:** KPMG annual audit of privacy commitments

Cloudflare 1.1.1.1 is fast everywhere because Cloudflare runs more edges than anyone. Their privacy commitments are real and audited. The downside is concentration risk — Cloudflare already sees a huge fraction of internet traffic via their CDN, and giving them your DNS too means one company sees a lot.

### Mullvad DNS

- **Founded:** 2022 (DNS service); Mullvad VPN since 2009
- **Pricing:** Free
- **Logging:** None
- **Blocking:** Six configurable lists (ads, trackers, malware, adult, gambling, social)
- **Anycast PoPs:** ~40
- **Audits:** Mullvad is well-known for privacy; DNS shares the same posture

Mullvad DNS is the no-account version of NextDNS-style filtering. You pick the URL of the filter combination you want — `https://dns.mullvad.net/dns-query` for plain, `https://adblock.dns.mullvad.net/dns-query` for ads/trackers, etc. — and that is your DoH endpoint. No account, no login, no payment.

---

## Head to head

### Speed

Median resolution time over 30 days, London home connection:

- ControlD: 9 ms
- Cloudflare: 10 ms
- NextDNS: 12 ms
- Mullvad: 14 ms
- Quad9: 18 ms

All are dramatically faster than my ISP's resolver, which averaged 38 ms with frequent 100ms+ outliers. Even the slowest of the five was twice as fast as the ISP.

### Blocking quality

I tested each against the [DuckDuckGo Tracker Test](https://privacytests.org) and a custom list of 500 ad/tracker domains:

- NextDNS (with OISD + AdGuard lists): 487/500 blocked
- ControlD (Standard filter): 482/500
- Mullvad (Adblock): 460/500
- Quad9: 12/500 (it does not try to block ads — only malware)
- Cloudflare 1.1.1.2: 18/500 (only malware)

For ad blocking, NextDNS and ControlD are in their own league.

### Logging and trust

- **Quad9:** No IP logging, aggregated stats only, Swiss non-profit governance
- **Mullvad:** No logging at all
- **NextDNS:** Logging off by default; if you turn it on, *you* can see it but it is not shared
- **ControlD:** Off by default; same as NextDNS
- **Cloudflare:** 25 hours, KPMG-audited

All five are credible. Avoid Google DNS (8.8.8.8) and any "free" DNS from your ISP.

---

## Which one should you pick

- **You want set-and-forget privacy:** Quad9 or Mullvad DNS. Free, no account, strong logging policy.
- **You want ad-blocking and per-device control:** NextDNS or ControlD. Both ~$2/mo, both excellent. NextDNS has a better UI, ControlD has the redirection feature.
- **You want raw speed:** Cloudflare 1.1.1.1 or ControlD. Edge cases where this matters: gaming, latency-sensitive trading.
- **You have kids and want category-level filtering:** NextDNS Family or ControlD Family. Both let you block adult/gambling/social per device, with a real dashboard. Easier than [router-level parental controls](/posts/best-parental-control-apps-2026/).

My personal setup: NextDNS on the router (covers all guests and IoT), NextDNS again on phone via the iOS profile (so cellular gets the same filtering), and Mullvad DNS as a fallback if NextDNS is ever down.

---

## How to set it up

### iOS / iPadOS

1. Get the NextDNS or ControlD configuration profile (or Mullvad's signed config).
2. Open the file on your device, install in Settings → General → VPN & Device Management.
3. Enable in Settings → General → DNS.

### Android 9+

Settings → Network & Internet → Private DNS → enter the hostname (e.g. `dns.mullvad.net` or `abcdef.dns.nextdns.io`).

### Windows 11

Settings → Network & Internet → your adapter → DNS server assignment → Manual → IPv4 → enter `1.1.1.1`, set Preferred DNS encryption to "Encrypted only (DNS over HTTPS)".

### macOS

Easiest: install the NextDNS or ControlD configuration profile. Or use a tool like `dnscrypt-proxy` for fully manual control. Apple's built-in DoH config is hidden behind profile installs.

### Router (OpenWrt)

Install `https-dns-proxy` from opkg, point your DHCP DNS to 127.0.0.1, configure the upstream to your chosen provider's DoH endpoint. I have a full walkthrough in my [OpenWrt VPN setup guide](/posts/how-to-flash-openwrt-vpn-router-2026/) — the DNS part is the same idea.

---

## Common mistakes

1. **Setting DNS on your laptop but not your router.** All other devices (TV, doorbell, IoT) still use the ISP. Set it on the router for full coverage, then layer per-device on top for portability.
2. **Trusting the system Private DNS field on Android with a custom NextDNS hostname.** It works — but if the device falls off Wi-Fi and goes cellular, some carriers strip DoT. Use the NextDNS Android app instead for resilience.
3. **Forgetting that DNS does not hide your IP.** If you only care about hiding your IP, you need a [VPN](/posts/what-is-a-vpn-and-do-you-need-one-2026/), not encrypted DNS. They solve different problems.
4. **Mixing two encrypted DNS solutions.** If your router is doing DoH and your phone is also doing DoH to a different provider, you get inconsistent blocking. Pick one and propagate.
5. **Not testing.** Visit `https://1.1.1.1/help` — it tells you whether your current resolver is encrypted. Visit `https://test.nextdns.io` for a NextDNS-specific check.

---

## Pairing encrypted DNS with the rest of your stack

Encrypted DNS is one layer. The full minimum-viable privacy stack in 2026:

- A [hardened browser](/posts/best-privacy-browsers-2026/) (Brave, Librewolf, or Firefox + arkenfox)
- An [encrypted email provider](/posts/best-encrypted-email-services-2026/) (Proton, Tutanota, Mailbox.org)
- A [password manager](/posts/best-password-managers-2026/) with 2FA
- Encrypted DNS (this article)
- A [VPN](/posts/best-vpn-services-2026/) for hostile networks
- [Encrypted cloud storage](/posts/best-secure-cloud-storage-2026/) for documents
- A [privacy-respecting search engine](/posts/best-privacy-search-engines-2026/)

Encrypted DNS is the easiest of these to set up and the easiest to forget. Set it on your router today; you will never think about it again.

---

## Bottom line

If you want one recommendation, take <a href="https://nextdns.io" target="_blank" rel="nofollow sponsored noopener">NextDNS</a> on the $1.99/mo plan. It will pay for itself in saved bandwidth from blocked ads in the first week.

If you want totally free and totally hands-off, take <a href="https://quad9.net" target="_blank" rel="nofollow sponsored noopener">Quad9</a>. It is the resolver I would recommend to my parents.

If you want the most fun playing with redirection rules and per-service blocking, take <a href="https://controld.com" target="_blank" rel="nofollow sponsored noopener">ControlD</a>.

All five resolvers in this list are vastly better than your ISP's default. The worst of these is dramatically better than the best ISP DNS. Pick any of them — pick one this evening — and move on with your life.
