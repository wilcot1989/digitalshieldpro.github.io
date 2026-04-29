---
title: 'Pi-hole + encrypted DNS home setup guide 2026'
date: 2026-10-18 09:00:00+02:00
lastmod: 2026-10-18 09:00:00+02:00
description: A real, tested 2026 guide to running Pi-hole with encrypted DNS upstream — including hardware choice, Docker vs bare-metal, the upstream resolver decision, and how to combine Pi-hole''s ad-blocking with NextDNS or Quad9 without losing either layer.
categories:
- privacy-guides
tags:
- pi-hole
- encrypted dns
- ad blocking
- home network
- privacy
- raspberry pi
- doh
keywords:
- pi-hole encrypted dns 2026
- pi-hole setup guide
- pi-hole nextdns
- pi-hole over doh
- raspberry pi ad blocker
- home network ad blocking
affiliate: false
author: James Mitchell
author_bio: Cybersecurity analyst with 10+ years of hands-on experience testing VPNs, antivirus software, and privacy tools.
featured_image: /images/categories/privacy-guides.svg
faq:
- q: 'What does Pi-hole actually do that encrypted DNS does not?'
  a: 'Pi-hole runs locally on your network and blocks ads, trackers, and unwanted domains by intercepting DNS lookups. Encrypted DNS (NextDNS, Quad9) does similar work in the cloud. The difference: Pi-hole gives you full local control, runs without subscription, has a beautiful per-device dashboard showing exactly which domain made which lookup, and works even when your internet is offline. The trade-off is operational responsibility — you run a small box on your network.'
- q: 'Should I run Pi-hole instead of, or in addition to, encrypted DNS?'
  a: 'In addition. Pi-hole sits on your LAN and handles all local DNS. Pi-hole then forwards what it cannot block to your encrypted DNS upstream (NextDNS, Quad9, Cloudflare). You get local ad blocking + encrypted upstream + visibility — three benefits in one box. Running only one of the two is leaving value on the table.'
- q: 'What hardware should I run Pi-hole on?'
  a: 'A Raspberry Pi 4 (2GB) is the canonical answer at $45. A Raspberry Pi Zero 2 W is fine and cheaper. A Synology NAS with Docker works. An old laptop running Linux works. Anything that runs 24/7 with reasonable uptime works. CPU and RAM requirements are tiny — DNS is not heavy.'
- q: 'Will Pi-hole break websites?'
  a: 'Sometimes. Out-of-the-box block-lists are conservative and rarely break sites. As you add more aggressive lists (anti-tracking-aggressive, social-media-blocking) you will eventually break a checkout flow somewhere. The fix is the per-domain whitelist, which Pi-hole shows you immediately when you check the query log. Reckon on five whitelist edits in the first month, then near-zero after that.'
- q: 'How does Pi-hole talk to encrypted DNS upstream?'
  a: 'Pi-hole itself does plain DNS to its upstream. To get encrypted DNS, install a small "DNS-over-HTTPS proxy" alongside Pi-hole — `cloudflared`, `dnscrypt-proxy`, or NextDNS''s own CLI all work. Pi-hole sends queries to localhost:5053 (or similar), the proxy encrypts them and forwards to your chosen upstream. Plain DNS only happens inside the box; nothing leaves the LAN unencrypted.'
- q: 'Can Pi-hole serve my whole house?'
  a: 'Yes. Set your router''s DHCP to hand out the Pi-hole IP as the DNS server for all clients. Every device on the network — phone, TV, doorbell, kid''s tablet, smart bulb — uses Pi-hole automatically. The only exceptions are devices that hardcode their own DNS (some Chromecasts, some smart TVs); these need separate handling.'
- q: 'What about IoT devices that hardcode 8.8.8.8?'
  a: 'Two options. Easy: use your router''s firewall to redirect all outbound DNS (port 53) to the Pi-hole. Devices that try to reach 8.8.8.8 silently get Pi-hole instead. Slightly harder: set up a separate VLAN for IoT and force their DNS at the router level. The redirect approach catches 95% of cases and takes five minutes.'
- q: 'Do I lose Pi-hole privacy by sending upstream to NextDNS?'
  a: 'You move the trust point. Without an upstream encrypted resolver, your ISP sees DNS. With Pi-hole + NextDNS, NextDNS sees DNS instead. The difference: NextDNS does not log by default, has stronger privacy commitments than ISPs, and you can opt for Quad9 or Mullvad if you trust them more than NextDNS. Pi-hole itself keeps the local query log on your hardware, where you can choose to keep or wipe it.'
products:
- name: Pi-hole
  url: https://pi-hole.net
  price: 'Free'
- name: Raspberry Pi 4
  url: https://www.raspberrypi.com/products/raspberry-pi-4-model-b/
  price: $45
- name: NextDNS
  url: https://nextdns.io
  price: $1.99/mo
schema_type: Article
---

*This article describes setups I run on my own home network. Pi-hole is free and open source. NextDNS, Quad9, and other upstream DNS providers have their own pricing.*

Pi-hole is one of the highest-leverage privacy upgrades you can make at home, and it pairs beautifully with [encrypted DNS](/posts/best-encrypted-dns-providers-2026/). Most guides cover one or the other. The combo — local Pi-hole for ad blocking + encrypted upstream for ISP shielding + a single dashboard to see what every device on your network is actually requesting — is what I run, and it is what I would recommend to anyone who is comfortable plugging a small Linux box into their network.

Here is the 2026 walkthrough.

---

## Why Pi-hole + encrypted DNS is the right combination

Pi-hole alone:
- Blocks ads and trackers locally
- Per-device query log (great for visibility)
- Local control of block-lists
- BUT: queries to the upstream resolver still go in plain DNS to whatever you set (usually 8.8.8.8 or your ISP)

Encrypted DNS alone (e.g. NextDNS):
- Encrypts the query in transit
- Cloud-side ad blocking
- Privacy-respecting log policy
- BUT: no per-device LAN-level dashboard, no offline operation

Pi-hole + encrypted DNS upstream:
- Local ad blocking with visibility
- Upstream encrypted to a trusted resolver
- ISP cannot snoop the queries (they leave your house already encrypted)
- Pi-hole catches anything the cloud filter misses, and vice-versa

This is the right architecture for a home network in 2026.

---

## Stage 1: Hardware

Anything that runs Linux 24/7 with reasonable uptime works. My order of preference for a fresh setup:

- **Raspberry Pi 4 (2GB):** $45, low-power, the canonical choice. Get a real PSU (not a cheap one) and a quality SD card or boot from USB SSD if you can.
- **Raspberry Pi Zero 2 W:** $15. Wi-Fi only is a downside for DNS — wired is more reliable. Use it if you have an Ethernet adapter.
- **Old laptop or thin client:** Free if you have one. More power than needed but it works.
- **Synology / TrueNAS / Unraid container:** If you already have a NAS, Docker container is the no-extra-hardware path.
- **VM on a home server / Proxmox:** If you already run Proxmox, an LXC container with Pi-hole is the cleanest path.

The Pi 4 with a good PSU and an SSD has been rock-solid for me for years. SD cards die eventually; either accept that you will rebuild it occasionally or boot from USB SSD.

---

## Stage 2: Install Pi-hole

The official one-liner installer works great:

```bash
curl -sSL https://install.pi-hole.net | bash
```

The interactive installer asks for:

1. **Upstream DNS provider** — pick *anything* for now; we will replace it with the encrypted DoH proxy in stage 3.
2. **Block lists** — accept the defaults; you can add more later.
3. **Web admin interface** — say yes.
4. **Web server** — say yes (lighttpd is fine).
5. **Log queries** — yes, to start. You can disable later if storage is tight.
6. **Privacy mode** — "Show everything" for setup; lock down later.

At the end you get a randomly generated admin password — save it in [your password manager](/posts/best-password-managers-2026/) immediately.

You can now reach the dashboard at `http://<pi-ip>/admin`. Log in. You will see queries flowing the moment any device on the network points DNS at the Pi.

---

## Stage 3: Add encrypted DNS upstream

Pi-hole talks plain DNS to its upstream. To make that upstream encrypted, install a DNS-over-HTTPS proxy on the same Pi.

Easiest path — `cloudflared`:

```bash
sudo mkdir -p /etc/apt/keyrings
curl -L https://pkg.cloudflare.com/cloudflare-main.gpg | sudo tee /etc/apt/keyrings/cloudflare-main.gpg > /dev/null
echo "deb [signed-by=/etc/apt/keyrings/cloudflare-main.gpg] https://pkg.cloudflare.com/cloudflared $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/cloudflared.list
sudo apt update && sudo apt install cloudflared
```

Configure cloudflared to listen on localhost:5053 and forward to Cloudflare or Quad9 over DoH. Create `/etc/cloudflared/config.yml`:

```yaml
proxy-dns: true
proxy-dns-port: 5053
proxy-dns-upstream:
  - https://1.1.1.1/dns-query
  - https://1.0.0.1/dns-query
```

Or for Quad9:

```yaml
proxy-dns-upstream:
  - https://9.9.9.9/dns-query
  - https://149.112.112.112/dns-query
```

Run as a service:

```bash
sudo cloudflared service install
sudo systemctl enable --now cloudflared
```

Then in the Pi-hole admin UI:

- **Settings → DNS → Upstream DNS Servers** — uncheck the public ones, add custom upstream `127.0.0.1#5053`.
- **Save.**

Pi-hole now sends all upstream queries to localhost:5053, which forwards them encrypted via DoH. Test from a client: `dig @<pi-ip> example.com` should resolve. `tcpdump` on the Pi shows DoH on port 443 leaving — no plain DNS on port 53.

If you prefer NextDNS specifically (better filtering than Cloudflare, per-device profiles), the NextDNS CLI is even simpler:

```bash
sh -c "$(curl -sL https://nextdns.io/install.sh)"
sudo nextdns install --config <your-config-id>
sudo nextdns config set listen 127.0.0.1:5053
```

Same Pi-hole upstream change — point at `127.0.0.1#5053`.

---

## Stage 4: Make every device use Pi-hole

Two paths:

### Easy path — DHCP DNS

In your router admin UI:

- DHCP settings → DNS server 1 → set to the Pi-hole IP (e.g. `192.168.1.10`)
- DNS server 2 → leave blank (NOT the ISP — clients fail over to it under load and you lose blocking)
- Save and renew DHCP leases on a test device

Devices that pull a fresh DHCP lease now use Pi-hole. To force-refresh every device, reboot the router.

### Harder path — let Pi-hole BE the DHCP server

Disable DHCP on your router. Enable it on Pi-hole (Settings → DHCP). Pi-hole is now the authoritative DHCP server, hands itself as DNS, and gets per-client hostnames in the dashboard (which is genuinely valuable — "Apple TV is requesting analytics.netflix.com").

I run the harder path. The reason: hostnames in the dashboard make ad-blocking lists meaningful. "Some device is hammering doubleclick.net 600 times an hour" is unhelpful; "Bedroom TV is hammering doubleclick.net 600 times an hour" tells you something.

---

## Stage 5: Block IoT devices that hardcode DNS

Smart TVs, Chromecasts, and some doorbells hardcode 8.8.8.8 (Google) or 1.1.1.1 (Cloudflare) and ignore your DHCP DNS setting. Pi-hole cannot block what does not ask Pi-hole.

Fix: redirect all outbound DNS at the router. In OpenWrt:

```
Network → Firewall → Traffic Rules → Add
- Name: Force-DNS-redirect
- Source zone: lan
- Destination zone: wan
- Destination port: 53
- Action: redirect to <pi-hole-IP>:53
```

In other router firmwares, the equivalent is "Port forwarding for outbound DNS" or "DNS hijacking." Most consumer routers do not expose this; another reason to use OpenWrt — see my [OpenWrt VPN router guide](/posts/how-to-flash-openwrt-vpn-router-2026/) for the full setup.

---

## Stage 6: Block-lists — what to actually subscribe to

Default Pi-hole block-lists are conservative. To get serious blocking without breaking sites, add:

- StevenBlack's "Unified Hosts" — the standard, regularly updated, broad
- OISD Big — well-maintained, low false-positive rate
- HaGeZi's Pro list — aggressive but curated

Avoid stacking everything. More is not better. Three carefully chosen lists outperform fifteen overlapping lists with nothing curated.

Refresh schedule: weekly is fine. Pi-hole's `gravity` updater handles this — `pihole -g` runs nightly by default.

---

## Stage 7: Watch the dashboard for a week

For the first week, watch the dashboard daily. You will:

- See which devices request which domains
- Spot one or two false-positive blocks (legitimate sites breaking) — whitelist them
- Discover that your TV, your fridge, or your doorbell is making thousands of "phone home" requests to vendor analytics
- Decide whether you care

This visibility is the part that no cloud-only encrypted DNS provider can give you. Per-device, per-domain, per-hour, on a dashboard you control.

---

## Stage 8: Lock it down

Once it is running smoothly:

- **Privacy levels:** Settings → Privacy → "Anonymous mode" if you do not need per-client visibility
- **Local-only admin:** Set the admin UI to listen only on the LAN
- **Strong web password:** rotate the random one to one in [your password manager](/posts/best-password-managers-2026/)
- **SSH:** key-only login, disable password auth
- **Backups:** `pihole -a -t` exports settings; cron a weekly export to [encrypted cloud storage](/posts/best-secure-cloud-storage-2026/)

---

## How this fits with the rest of your stack

Pi-hole + encrypted DNS upstream is the LAN-level filtering and visibility layer. It pairs well with:

- [A VPN router](/posts/how-to-flash-openwrt-vpn-router-2026/) — Pi-hole inside the VPN tunnel for max privacy
- [Encrypted email](/posts/best-encrypted-email-services-2026/) — phishing domains often get blocked at the DNS level too
- [A privacy browser](/posts/best-privacy-browsers-2026/) on each device — defence in depth, both layers help
- [Disposable phone numbers](/posts/best-disposable-phone-numbers-2026/) and [email aliases](/posts/email-aliasing-simplelogin-vs-anonaddy-vs-relay-2026/) — for the identifier layer
- [Hardware security keys](/posts/best-hardware-security-keys-2026/) — for the auth layer

This is what defence in depth looks like in practice. No single layer is perfect; collectively they are very strong.

---

## Common mistakes

1. **Pointing devices to 8.8.8.8 in addition to Pi-hole.** They fall back, you lose blocking. Pi-hole only.
2. **Running Pi-hole without an upstream encrypted resolver.** ISP still sees the queries leaving. Set up cloudflared or nextdns CLI.
3. **Subscribing to 30 block-lists.** Breaks too many sites; whitelist hell. Three good lists is the right answer.
4. **Forgetting to back up.** Pi-hole config is small but rebuilding from scratch is annoying. Weekly export.
5. **Single point of failure.** If the Pi dies, the whole house has no DNS. Either run a second Pi as failover, or accept that DNS outages happen and you reboot the box.

---

## Bottom line

Pi-hole + encrypted DNS upstream is the home-network privacy upgrade that pays back the most on the smallest budget. About $50 of hardware, an evening of setup, and the result runs for years.

If you want one specific recommendation for the upstream encrypted resolver: <a href="https://nextdns.io" target="_blank" rel="nofollow sponsored noopener">NextDNS</a> on the $1.99/mo plan layered behind Pi-hole gives you the best of both — local visibility from Pi-hole, cloud-grade filtering from NextDNS, encrypted egress from your network. <a href="https://quad9.net" target="_blank" rel="nofollow sponsored noopener">Quad9</a> is the no-account-needed free alternative that covers 80% of the value.

Pair this with the rest of your [privacy stack](/posts/best-privacy-stack-2026/) and you will have the kind of home network that the average internet user does not know is possible.
