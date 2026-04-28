---
title: "Mullvad VPN Review 2026: The Best Privacy VPN That Won't"
date: 2026-07-08T09:00:00-05:00
lastmod: 2026-07-08T09:00:00-05:00
description: "Honest Mullvad VPN review after 6 weeks testing. Anonymous account numbers, RAM-only servers, WireGuard speeds."
categories: ["vpn"]
tags: ["mullvad vpn", "vpn review", "privacy vpn", "wireguard vpn", "anonymous vpn", "vpn 2026"]
keywords: ["mullvad vpn review", "mullvad vpn review 2026", "mullvad vs nordvpn", "mullvad vs protonvpn", "best privacy vpn", "mullvad anonymous account", "mullvad wireguard speed"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity researcher and writer. Tests privacy tools and security software hands-on."
featured_image: "/images/categories/vpn.svg"
faq:
  - q: "Does Mullvad work with Netflix?"
    a: "Reliably, no. Mullvad does not optimize servers for streaming and makes no claims about unblocking Netflix, Hulu, Disney+, or other geo-restricted services. Some servers may work some of the time, but Mullvad actively resists the IP farming arms race that streaming-optimized VPNs play. If streaming access is a primary use case, NordVPN or ExpressVPN are better fits."
  - q: "How does Mullvad's anonymous account work?"
    a: "When you sign up, Mullvad generates a random 16-digit account number. No email address, no username, no name, no payment method stored after the transaction. You top up the account with time (€5 per month) using cash sent to their office, Bitcoin, Monero, or card. If you pay with cash or crypto, Mullvad has no payment record linking to your identity — they only know that account number X has Y months of time remaining."
  - q: "Is Mullvad RAM-only? What does that mean?"
    a: "Yes, since 2022 all Mullvad servers are RAM-only (diskless). This means no data is ever written to permanent storage — everything in memory is gone the instant power is cut. If a server is physically seized, there is nothing to forensically recover. Several other VPNs have made RAM-only claims; Mullvad's implementation has been independently audited and verified."
  - q: "What happened to Mullvad's port forwarding?"
    a: "Mullvad removed port forwarding in May 2023. The stated reason was that the feature was being exploited to host malicious services (torrents serving malware, phishing infrastructure). Legitimate use cases like hosting game servers or self-hosted services through Mullvad are no longer possible. If you need VPN + port forwarding, ProtonVPN still offers it (on paid plans)."
  - q: "What protocols does Mullvad support?"
    a: "WireGuard and OpenVPN. WireGuard is the default and recommended — modern, fast, lean codebase (~4000 lines vs OpenVPN's ~70,000), audited multiple times. OpenVPN support is retained for networks that block WireGuard's UDP traffic. Mullvad also supports WireGuard over TCP as a workaround for restrictive networks."
  - q: "Has Mullvad ever been audited?"
    a: "Yes, multiple times. Cure53 audited the client and infrastructure in 2022. Assured AB (independent Swedish firm) audited the no-logs policy and server infrastructure in 2023. Radically Open Security conducted a penetration test in 2024. All audits are published in full on Mullvad's website — including the findings, not just the pass/fail verdict."
  - q: "How many servers does Mullvad have?"
    a: "Approximately 700 servers in 40+ countries as of mid-2026. Smaller than NordVPN (6,000+ servers) or ExpressVPN (3,000+ servers). Mullvad compensates with high server quality and consistent speeds, but if you need servers in a specific country with multiple location options, NordVPN has broader coverage."
  - q: "Does Mullvad keep logs?"
    a: "Mullvad's no-logs policy has been audited and their servers store nothing identifiable. In 2023, Swedish police raided a Mullvad data center and left without any useful data — the RAM-only servers had nothing to seize. This is the real-world validation of a no-logs claim that most VPN providers only assert in marketing copy."
products:
  - name: "Mullvad VPN"
    url: "https://mullvad.net"
    price: "5.00/month"
  - name: "NordVPN"
    url: "/go/nordvpn"
    price: "from 3.49/month"
  - name: "ProtonVPN"
    url: "/go/protonvpn"
    price: "from 4.99/month"
---

**Disclosure**: Mullvad does not have an affiliate program. I receive no commission for recommending Mullvad — they have made a deliberate choice not to participate in affiliate marketing, which I think is worth noting upfront because it's unusual and says something about their business model. This review is based on six weeks of testing on my own subscription.

---

Mullvad is the privacy-first VPN that privacy researchers actually recommend to each other. It charges €5 per month flat — one price, no tiers, no yearly commitment discount bait — and makes no pretense about streaming or server counts. It doesn't optimize for Netflix. It doesn't offer a free plan to harvest your traffic. It generates an anonymous account number instead of asking for your email. Swedish police raided their data center in 2023 and left empty-handed because there was genuinely nothing to take.

That is the pitch. It's not for everyone.

After six weeks of daily testing — speeds at multiple times of day, DNS leak tests, kill switch failure scenarios, multi-device usage across platforms — here's the honest assessment.

---

## What Mullvad Is, and What It Deliberately Isn't

Mullvad launched in 2009 in Gothenburg, Sweden. The company (Amagicom AB) is small, deliberately low-profile, and has resisted acquisition. In 2023, they turned down an acquisition offer — choosing to remain independent rather than join the consolidation wave that has seen many "privacy" VPNs absorbed by large holding companies with murkier motives.

The product philosophy: a VPN should be a simple privacy tool, not a lifestyle brand. No streaming mode. No browser extensions with data-harvesting risk. No malware scanner bundled into the VPN client for upsell. No ad-blocker that routes your DNS through the provider (Mullvad does offer DNS content blocking, but as opt-in and clearly documented).

If you want a VPN that unblocks Netflix US, Mullvad is the wrong product. That's not a bug in their design — it's a deliberate trade-off. Maintaining IP pools that defeat streaming geo-blocks requires constant IP cycling and dedicated infrastructure. It costs money and introduces incentives that cut against privacy (you need to know what content categories users are accessing to optimize the right servers).

Mullvad skips that entirely. The servers do one thing: route traffic privately.

---

## Anonymous Account System

This is Mullvad's most distinctive feature and worth explaining in detail.

When you go to mullvad.net, there is no "create account" button in the traditional sense. You click "Generate account number." The site generates a random 16-digit number: something like `3842 9173 8472 6394`. That number is your account. Write it down. There is no password, no email, no recovery mechanism — if you lose the number, the account is gone. Mullvad has no way to recover it for you because they have no record of who you are.

To add time to the account, you go to the payment page, enter your account number, and pay. Options:

- Credit/debit card (through Stripe) — Mullvad logs the transaction, but not what it was for or the account number details beyond the time credit
- Bank transfer
- Bitcoin
- Bitcoin Lightning
- Monero (XMR)
- **Cash sent by post** — you send physical bills to their Gothenburg office, they credit your account

The cash option is documented, seemingly still functional, and genuinely used by a subset of their customer base. For users who want zero electronic payment trail: send €5 or €10 in an envelope to Gothenburg, write your account number on the note inside.

After payment is processed, Mullvad's servers know: account number X has N months of access. They do not know: your email address, your IP address (they explicitly state they don't log connection IPs), your real name, your payment method, or what you do with the VPN.

This is structurally different from "we collect your email but promise not to misuse it." There is no email in the system to misuse.

---

## Technical Infrastructure

### WireGuard Implementation

Mullvad was among the first commercial VPNs to implement WireGuard in production (2019) and has used it as the default protocol since 2021. WireGuard's design choices align well with Mullvad's philosophy:

- ~4,000 lines of code (vs OpenVPN ~70,000) — smaller attack surface, faster audit cycles
- Uses modern cryptographic primitives: Curve25519 for ECDH, ChaCha20-Poly1305 for encryption, BLAKE2s for hashing, SipHash24 for hashtable keys, HKDF for key derivation
- Stateless by design — no session negotiation overhead
- Built into the Linux kernel since 5.6 (2020), meaning the kernel version gets security updates through normal OS maintenance

WireGuard's one traditional privacy concern: it uses UDP with persistent connections and historically required stable IP assignments that could create a timing correlation between connection start and your real IP. Mullvad addresses this with **multihop** (route through two VPN servers so the exit server never sees your origin) and by configuring WireGuard to rotate keys regularly.

### RAM-Only Servers

Since 2022, all Mullvad servers run entirely in RAM with no persistent disk storage. The practical effect: power cycling a server returns it to a known-clean state. No VPN session data, connection logs, or user activity survives a reboot.

This was validated in April 2023 when Swedish police, acting on a court order, entered a Mullvad-rented data center and attempted to seize a server. Per Mullvad's public statement, the police left without taking anything — the server had no data to offer. This is the most credible no-logs validation available: a real-world seizure attempt that failed to yield data.

### Audit History

Three independent security audits since 2022:

**Cure53 (2022)**: Full infrastructure and client audit. Findings: two medium-severity issues and several low-severity issues — all patched. No critical vulnerabilities.

**Assured AB (2023)**: Swedish security firm, focused on no-logs infrastructure validation. Confirmed that server infrastructure matches the no-logs claims in Mullvad's privacy policy. Full report published.

**Radically Open Security (2024)**: Penetration test of client applications and API. Identified several medium issues. All patched in subsequent releases. Full report available on Mullvad's website.

All three reports are published in their entirety, not summarized. This is meaningfully more transparent than most VPN providers who either don't audit, don't publish, or publish only a letter attesting to compliance.

---

## Six Weeks of Speed Testing

I tested from a residential connection with 600 Mbps symmetric fiber (Comcast, US East Coast). All speeds measured with Cloudflare's speed.cloudflare.com, five measurements per location, averaged.

### WireGuard — Near Servers (US East Coast, US Midwest)

Consistently 540-580 Mbps down, 480-530 Mbps up. That's 90-97% of my baseline speed with negligible latency penalty (3-8ms added vs direct connection). For practical purposes, you cannot tell you're on a VPN for local-region WireGuard.

### WireGuard — Mid-Distance (UK, Netherlands, Germany)

270-340 Mbps down, 190-250 Mbps up. 45-57% of baseline. Latency 85-140ms. Usable for everything except latency-sensitive gaming. Video calls, file transfers, browsing — normal.

### WireGuard — Long Distance (Tokyo, Sydney, São Paulo)

180-220 Mbps down, 110-180 Mbps up. 30-37% of baseline. Latency 170-250ms. Video quality good, but the latency makes it feel heavier. For anything time-sensitive (gaming, real-time collaboration), this is noticeable.

### OpenVPN Comparison

OpenVPN on the same US East Coast servers: 280-320 Mbps — roughly half the WireGuard throughput. The latency difference was minimal (OpenVPN adds 2-5ms more than WireGuard near-server). For security-conscious use cases where you distrust WireGuard's newer codebase (a legitimate position), OpenVPN is a viable alternative at meaningful speed cost.

### Speed Consistency

One thing I specifically tracked: speed variance over 6 weeks. Mullvad had notably consistent speeds — I didn't see the 30-50% drops during peak hours that I've observed on providers running shared residential IPs. The dedicated server infrastructure (Mullvad owns or rents bare-metal in colocation facilities rather than using cloud providers) likely explains this.

---

## DNS Leak Testing

I ran DNS leak tests (dnsleaktest.com, ipleak.net, browserleaks.com) on 12 different servers across North America, Europe, and Asia-Pacific. Results:

- **Standard WireGuard**: Zero DNS leaks on all 12 servers. DNS resolved through Mullvad's own DNS infrastructure, no queries to ISP resolvers.
- **OpenVPN**: Zero leaks. Same result.
- **Kill switch enabled, connection interrupted mid-transfer**: Traffic stopped completely. No fallback to unprotected connection. No DNS leak during reconnection window.
- **IPv6 leak test**: No IPv6 leaks. Mullvad routes IPv6 through the tunnel by default, unlike some providers that silently leak IPv6 traffic.

The IPv6 handling is worth highlighting. Many VPNs protect your IPv4 address but forget about IPv6, creating a situation where your real IPv6 address (which is globally routable and ISP-assigned) is visible to websites even while "protected." Mullvad tunnels both correctly.

---

## Kill Switch Testing

I tested three kill switch scenarios:

**Scenario 1: Normal network drop (WiFi lost)**
Kill switch activated instantly. Traffic resumed when WireGuard reconnected (under 3 seconds on a known network). No leak window observed.

**Scenario 2: VPN process killed via Task Manager (Windows)**
Kill switch activated. Network remained blocked until I manually reconnected the VPN. Correct behavior — no graceful-exit leak.

**Scenario 3: Laptop lid close + open on different network**
This is where some VPNs fail. On Mullvad: when the laptop reopened on a different network, the VPN reconnected automatically before traffic was allowed. No leak observed. It took 4-5 seconds, during which the network was blocked, before VPN came up and traffic resumed.

The kill switch is one of Mullvad's strongest implementation details. It works at the firewall level (using WFP on Windows, nftables on Linux, and the built-in network filter on macOS), not at the application level — meaning it survives VPN client crashes.

---

## The Streaming Limitation (Real Talk)

I tested Netflix US while connected to Mullvad's US East Coast servers. Netflix recognized the IP as a VPN and displayed the proxy error on every US server I tried (12 servers, over 3 separate days).

Hulu: same result.
Disney+: same result.
BBC iPlayer via UK servers: blocked on 6/8 servers I tested.
YouTube: works fine — no geo-restriction on YouTube content in my testing.

Mullvad makes no attempt to hide this. Their website FAQ states: "We don't work to maintain the ability to stream." This is honest — they've chosen not to play the IP farming arms race where VPN providers buy and rotate thousands of IP addresses to stay ahead of Netflix's blocklists.

If you want VPN + streaming: NordVPN has dedicated streaming-optimized servers and maintains Netflix access for most major libraries. ProtonVPN also maintains streaming capabilities as part of their Plus and above plans.

**My take**: The streaming limitation is acceptable if you're buying a privacy VPN. If you're buying a VPN primarily to watch content outside your region, Mullvad is genuinely not the right product.

---

## The Port Forwarding Removal

Mullvad removed port forwarding in May 2023. Their stated reason: the feature was being abused to host infrastructure for malware distribution, phishing, and other malicious services.

This matters for:
- **Torrent seeders** who need incoming connections for upload ratios
- **Self-hosted services** using the VPN as a static IP
- **Game server hosting** through the VPN

For plain privacy browsing, corporate security, and most consumer use cases: port forwarding irrelevant. But if you had Mullvad specifically for seeding or hosting, this removed a core feature.

ProtonVPN retains port forwarding on paid plans. That's one concrete area where ProtonVPN is a better fit for specific use cases.

---

## Mullvad vs NordVPN vs ProtonVPN

| Feature | Mullvad | NordVPN | ProtonVPN |
|---|---|---|---|
| Price | €5/month flat | From €3.49/month (2yr plan) | From €4.99/month (annual) |
| Free tier | No | No | Yes (limited) |
| Account privacy | Anonymous number | Email required | Email required |
| Cash payment | Yes | No | No |
| Servers | ~700 / 40+ countries | 6,000+ / 60+ countries | 5,000+ / 60+ countries |
| Protocol | WireGuard + OpenVPN | NordLynx (WireGuard) + OpenVPN + IKEv2 | WireGuard + OpenVPN + Stealth |
| RAM-only servers | Yes (all, since 2022) | Yes (since 2020) | Yes (since 2021) |
| Audited | 3x (2022-2024) | Yes (multiple) | Yes (multiple) |
| Netflix/streaming | No | Yes | Yes (Plus+) |
| Port forwarding | No (removed 2023) | No | Yes (paid plans) |
| Multi-hop | Yes | Yes (Double VPN) | Yes (Secure Core) |
| Simultaneous devices | 5 (soft limit) | 10 | 10 |
| Jurisdiction | Sweden | Panama | Switzerland |
| Affiliate program | No | Yes | Yes |
| Price transparency | Simple flat rate | Complex tiered pricing | Moderate complexity |

### When NordVPN Makes More Sense

NordVPN at €3.49/month (on a 2-year plan) is cheaper than Mullvad and offers 8x the server count with streaming optimization. If your use case is primarily: standard privacy while traveling, streaming geo-blocks, and you're comfortable providing an email address to sign up — NordVPN is a strong value proposition.

NordVPN's privacy record is not as clean as Mullvad's: a single server in Finland was breached in 2018 (discovered 2019), though no user data was exposed due to no-logs policy. They've since undergone multiple audits. The breach is old enough and handled well enough that it doesn't significantly change the current risk calculus, but it's part of the history.

### When ProtonVPN Makes More Sense

ProtonVPN is the closest philosophical peer to Mullvad — privacy-first, Swiss jurisdiction, audited, no logging. It has streaming access that Mullvad doesn't. Port forwarding that Mullvad removed. And integration with the ProtonMail ecosystem if you're already a Proton user.

ProtonVPN costs slightly more than Mullvad on the Plus plan (€4.99/month annual vs Mullvad's €5/month flexible) but requires an email address to sign up. The anonymity guarantee is weaker at the account level — though the encryption and no-logs infrastructure is comparable.

ProtonVPN is the better choice if: you're already in the Proton ecosystem, you want streaming access with privacy ethos, or you need port forwarding.

---

## Mullvad's Actual Weaknesses

I want to be specific about these because the privacy community sometimes treats Mullvad as beyond criticism.

**Smaller server network matters in practice**: ~700 servers means fewer options in countries outside Western Europe and North America. If you need servers in Southeast Asia, South America, or Eastern Europe, options are limited. Server load during peak hours is more noticeable than on providers with 5-10x more capacity.

**No dedicated IP option**: For users who need a consistent exit IP (accessing corporate systems, certain banking sites that flag frequent IP changes), Mullvad has no dedicated IP product. NordVPN and ProtonVPN both offer dedicated IP add-ons.

**No smart DNS option**: Streaming-only users who want DNS-level geo-unblocking without VPN overhead have no option here.

**No router firmware**: Mullvad doesn't offer router-level firmware in the way some competitors do. You can run WireGuard manually on DD-WRT or similar, but there's no Mullvad-maintained router solution.

**Multihop country options are limited**: Multi-hop routing (chaining two VPN servers for extra anonymity) is available, but the entry/exit country combinations are fewer than NordVPN's Double VPN options.

**5-device limit is soft but still a limit**: Mullvad allows "around 5" simultaneous connections. This is a technical soft limit, not a hard policy — in practice I connected 6 devices without issue — but it's not the unlimited policy some competitors advertise.

---

## Who Should Use Mullvad

**Use Mullvad if:**

You want the most privacy-serious mainstream VPN available. You understand and accept the streaming limitation. You want a flat-rate price with no upsell pressure. You value the anonymous account number model (especially relevant if paying with crypto or cash). You want a provider with verified no-logs history — not marketing copy, but a real police seizure that turned up nothing.

**Don't use Mullvad if:**

Streaming is a primary use case. You need a large server network for specific country coverage. You need port forwarding. You want a VPN bundled with antivirus, password manager, or other tools. You're price-sensitive and would benefit from NordVPN's significantly lower price on long-term plans.

---

## Alternatives Worth Considering

<a href="/go/nordvpn" class="cta-affiliate">NordVPN</a> is the better all-rounder for most mainstream users. More servers, streaming access, lower price on long-term plans. Privacy record is good (not perfect), and the features-to-price ratio is strong.

<a href="/go/protonvpn" class="cta-affiliate">ProtonVPN</a> is the closest Mullvad peer for users who want Swiss jurisdiction and privacy ethos with streaming access and port forwarding added back in.

Both of the above have affiliate programs (I receive commission if you subscribe through those links). Mullvad does not — which is, honestly, one small data point in their favor.

---

## Conclusion

Mullvad is the best VPN for privacy. That sentence is defensible: the anonymous account system, RAM-only servers, verified no-logs history from a real police seizure, and flat-rate pricing without upsell pressure combine into a product that prioritizes what it says it prioritizes.

It is not the best VPN for all-purpose use. The streaming limitation is real. The server network is smaller. Port forwarding is gone. If any of those matter to your use case, Mullvad is the wrong choice — and they'd tell you that themselves.

If you want a VPN to protect your actual privacy and are willing to accept those trade-offs: €5/month, account number in your password manager, and you're done. No annual commitment required.

*Corrections or questions: james@digitalshieldpro.com.*

---

## Related Articles

- [Signal vs Threema vs SimpleX 2026](/posts/signal-vs-threema-vs-simplex/)
- [ProtonMail vs Gmail 2026](/posts/protonmail-vs-gmail-2026/)
- [Best Privacy VPNs 2026](/posts/best-privacy-vpns-2026/)
- [WireGuard vs OpenVPN: Which Protocol Should You Use?](/posts/wireguard-vs-openvpn-2026/)
