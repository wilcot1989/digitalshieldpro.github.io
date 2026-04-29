---
title: 'How to flash OpenWrt and set up a VPN router 2026: full walkthrough'
date: 2026-10-16 09:00:00+02:00
lastmod: 2026-10-16 09:00:00+02:00
description: A real, tested 2026 walkthrough for replacing your router firmware with OpenWrt and putting a VPN at the network level — covering hardware choice, flashing safely, WireGuard setup with Mullvad and Proton, kill switch, split tunneling and the privacy traps to avoid.
categories:
- privacy-guides
tags:
- openwrt
- vpn router
- wireguard
- mullvad
- proton vpn
- privacy
- networking
keywords:
- openwrt vpn router 2026
- flash openwrt
- wireguard router setup
- mullvad router
- proton vpn router
- vpn router guide
affiliate: false
author: James Mitchell
author_bio: Cybersecurity analyst with 10+ years of hands-on experience testing VPNs, antivirus software, and privacy tools.
featured_image: /images/categories/privacy-guides.svg
faq:
- q: 'Why put a VPN on the router instead of on each device?'
  a: 'Three reasons. First, every device is covered automatically — TVs, doorbells, smart bulbs that cannot run a VPN client are now behind one. Second, your real IP never leaks during VPN client reconnects on a phone. Third, guests on your Wi-Fi inherit your privacy posture without setup. The trade-offs: slightly lower throughput than a desktop client, single point of failure, less per-device control.'
- q: 'Can I use my ISP-supplied router for OpenWrt?'
  a: 'Almost never. ISP routers are locked, low-spec, and unsupported. Buy a separate router that is on the OpenWrt hardware list and use the ISP box only as a modem in bridge mode. The full hardware compatibility list is at openwrt.org. As of 2026, the GL.iNet Flint 2, Linksys WRT3200ACM, and Banana Pi BPI-R4 are common solid choices.'
- q: 'Will I lose internet access if I mess up the flash?'
  a: 'You can brick the router temporarily if you flash the wrong firmware. All recent routers have a recovery mode that lets you re-flash via TFTP or a vendor recovery utility. Read the device-specific OpenWrt wiki page in full before starting. Have your laptop wired to the router via Ethernet during the flash — never flash over Wi-Fi.'
- q: 'Is WireGuard or OpenVPN better on a router?'
  a: 'WireGuard, every time, in 2026. WireGuard saturates a gigabit link on a $100 router; OpenVPN typically caps at 100–200 Mbps because it is single-threaded. Every reputable VPN provider offers WireGuard. Use OpenVPN only if your provider does not support WireGuard (rare) or if you need WireGuard-incompatible features.'
- q: 'Does running a VPN on the router slow my internet down?'
  a: 'Yes, somewhat. Expect 60–80% of line speed for WireGuard on a modern router (e.g. Flint 2 saturating 700+ Mbps on a gigabit line). On older or weaker routers (anything from 2019 or earlier), expect 100–300 Mbps. If your line is fibre, get a router with hardware crypto offload — otherwise the CPU is the bottleneck.'
- q: 'Can I exclude specific devices or sites from the VPN tunnel?'
  a: 'Yes — this is split tunneling. OpenWrt supports it via Policy-Based Routing (PBR) packages. You can exclude specific MAC addresses (e.g. your work laptop), specific destination IPs (e.g. your bank), or specific domains. I always exclude streaming services that geofence VPN exits and any site that uses your home IP for fraud detection.'
- q: 'Do I lose the kill switch if the router is the VPN client?'
  a: 'No — actually, router-level kill switch is more reliable than per-device. With OpenWrt + a properly configured WireGuard interface and firewall rule, when the tunnel drops, all WAN traffic stops. Devices on the LAN simply lose internet until the tunnel is back up. This is the strongest possible kill switch because no device can route around it.'
- q: 'Is this legal in my country?'
  a: 'In every Western country, yes. VPN use is legal. Flashing your own router is legal. A few jurisdictions (China, Iran, UAE, Russia) restrict VPN use; check local rules. The FCC in the US has historically required vendors to lock down certain Wi-Fi parameters; OpenWrt complies in stock builds.'
products:
- name: GL.iNet Flint 2
  url: https://www.gl-inet.com/products/gl-mt6000
  price: $169
- name: Mullvad VPN
  url: https://mullvad.net
  price: €5/mo
- name: Proton VPN
  url: https://protonvpn.com
  price: €4.99/mo
schema_type: Article
---

*This article contains affiliate links. I earn a commission if you purchase through some of my links, at no extra cost to you.*

Putting a VPN on your router is one of the higher-leverage privacy moves available, but it has a reputation for being scary. Bricking a router does not actually happen often if you follow the right steps, and the result — every device on your network silently behind a VPN with a real kill switch and no per-device fiddling — is genuinely great.

I have flashed OpenWrt onto five different routers over the years, set up VPN tunnels with Mullvad, Proton VPN and IVPN, and lived with the result as my home network. Here is the 2026 walkthrough for doing it right.

---

## What you actually want to achieve

The end-state setup:

1. ISP modem in bridge mode — does layer 2 only, no routing
2. OpenWrt router doing routing, DHCP, DNS, firewall, VPN tunnel
3. Wi-Fi from the OpenWrt router covering the house
4. WireGuard tunnel to a [reputable VPN](/posts/best-vpn-services-2026/) up at all times
5. Kill switch enforced by firewall — if tunnel drops, no traffic leaves
6. [Encrypted DNS](/posts/best-encrypted-dns-providers-2026/) on top of the tunnel
7. Optionally: split tunneling for specific devices that need bare-IP exit

This setup means every device in the house — Apple TV, smart speakers, kids' tablets, IoT things you cannot run a VPN client on — is behind the VPN automatically. Guests get the same protection. You stop thinking about it.

---

## Stage 1: Pick the right hardware

This is where most people fail. The wrong router will be slow, unstable, or unsupported.

**Things that matter in 2026:**

- **CPU:** Multi-core ARM at 1.5GHz+ is the floor for gigabit WireGuard
- **Hardware crypto offload:** Helps WireGuard performance significantly
- **RAM:** 256MB minimum, 512MB+ comfortable
- **Storage:** 128MB+ flash
- **OpenWrt support:** Officially listed on `openwrt.org/toh`

**My current recommendations:**

- **GL.iNet Flint 2 (GL-MT6000):** Ships with OpenWrt out of the box. Quad-core, 1GB RAM, 8GB storage. Saturates gigabit. Easiest path. ~$169.
- **Linksys WRT3200ACM:** Older, well-supported, 512MB RAM. Saturates ~500 Mbps WireGuard. Good if you find one used.
- **Banana Pi BPI-R4:** Powerful, 2.5GbE, more advanced. For people who want to also run other services on it.

The GL.iNet route is by far the easiest because it ships with a fork of OpenWrt already, with a friendlier UI on top. You can flash full vanilla OpenWrt later if you want — but most people are happy with what GL.iNet ships.

---

## Stage 2: Flash OpenWrt (vanilla path)

If you bought a Flint 2, skip this stage — it ships with OpenWrt-derived firmware. If you bought a router that ships with vendor firmware:

1. **Read the device-specific page** at `openwrt.org/toh/<vendor>/<model>` end to end. Stop and read everything before doing anything.
2. **Download the right firmware image.** Two types: `factory` (for first install over vendor firmware) and `sysupgrade` (for subsequent OpenWrt-to-OpenWrt updates). Get `factory.bin` for now.
3. **Connect via Ethernet.** Disable Wi-Fi on your laptop. The router's web UI lives at `192.168.1.1` (or vendor-specific).
4. **Reset router to factory.** Hold the reset button per device docs.
5. **Open the vendor admin UI.** Find "Firmware update" and upload the OpenWrt `factory.bin`.
6. **Wait.** Lights blink. Do not power off. Five minutes minimum. Some devices reboot once, twice, three times.
7. **Re-connect.** OpenWrt's default IP is `192.168.1.1`, default user `root`, no password.
8. **Set a strong root password immediately.** Then enable SSH key auth and disable password SSH.

If something goes wrong: do not panic. Search "model name OpenWrt recovery" — every supported device has a documented recovery flow. I have recovered three "bricked" routers via TFTP recovery modes; takes 20 minutes.

---

## Stage 3: Set up the basics

Before the VPN, you want a working OpenWrt:

1. **Set timezone, hostname, language** (System → System).
2. **WAN interface** — pull DHCP from ISP modem (default is fine if your ISP supplies an IPv4 DHCP).
3. **LAN interface** — pick a non-default subnet (e.g. `192.168.50.1/24`) to reduce conflicts.
4. **Wi-Fi** — turn on, set strong WPA3-Personal (or WPA2 if devices need it), set sensible channel.
5. **DHCP** — enable on LAN.
6. **Software update** — `opkg update`.

At this point you have a working OpenWrt router. Test from a device — should get DHCP, should browse normally.

---

## Stage 4: Install WireGuard

```sh
opkg update
opkg install wireguard-tools luci-app-wireguard kmod-wireguard
```

Reboot the router or restart the LuCI service.

---

## Stage 5: Get a VPN config

You need a WireGuard config from a privacy-respecting [VPN provider](/posts/best-vpn-services-2026/). My recommendations:

- **Mullvad:** No-account-needed flat €5/mo, audited, in [my full Mullvad review](/posts/mullvad-vpn-review-2026/). They have a config generator at mullvad.net/account/wireguard-config.
- **Proton VPN:** €4.99/mo with Plus, audited, see my [Proton VPN review](/posts/protonvpn-review-2026/). Config generator in account dashboard.
- **IVPN:** Strong privacy posture, more expensive. See [IVPN vs Mullvad](/posts/ivpn-vs-mullvad-2026/).

Whichever you pick, generate a WireGuard config for the router. The config file looks like:

```ini
[Interface]
PrivateKey = <your-private-key>
Address = 10.66.x.x/32, fc00:bbbb::/128
DNS = 10.64.0.1

[Peer]
PublicKey = <server-public-key>
Endpoint = <server>:51820
AllowedIPs = 0.0.0.0/0, ::/0
```

Save this. You will paste the values into LuCI.

---

## Stage 6: Configure the WireGuard interface in OpenWrt

In LuCI:

1. **Network → Interfaces → Add new interface.**
2. **Name:** `wg0`. Protocol: WireGuard VPN.
3. **General:** paste your `PrivateKey`. Add the `Address` from your config.
4. **Peers tab:** Add peer. Paste `PublicKey`, set `AllowedIPs` to `0.0.0.0/0,::/0`, set `Endpoint Host` and `Endpoint Port`, set `Persistent Keepalive` to 25.
5. **Save & Apply.**

Then:

6. **Network → Firewall.** Edit zone `lan` to forward to a new zone. Create a new zone `wg`, attach interface `wg0`, set Input/Forward/Output to ACCEPT, set Masquerading on. Forwarding from `lan` → `wg`.
7. **Network → Routing.** Confirm the WireGuard interface has its default route.

Reboot. Check `Status → Interfaces` — `wg0` should show "Connected" and a peer endpoint.

Test from a client device: `https://am.i.mullvad.net` should show a Mullvad IP (or whichever provider you used). If it shows your ISP IP, the firewall zone is wrong.

---

## Stage 7: Kill switch (the firewall version)

The whole reason to do this on the router is the kill switch. Configure it now:

1. **Network → Firewall → General Settings.**
2. **Edit `lan` zone forwarding.** Remove forwarding to `wan`. Keep forwarding only to `wg`.
3. **Save & Apply.**

Now if `wg0` is down, `lan` has no path to the internet. No leakage. No "for thirty seconds my real IP exited."

Test it: bring the WireGuard peer down (`ifdown wg0` over SSH or via LuCI). All client devices should lose internet within a few seconds. Bring it back (`ifup wg0`); internet returns.

---

## Stage 8: Encrypted DNS on top

Without explicit DNS config, your DNS now goes through whatever the VPN provider supplies. Mullvad provides 10.64.0.1 (their internal DNS). Proton has its own. This is fine.

For belt-and-braces, install `https-dns-proxy` and route DNS to a third-party encrypted DNS like NextDNS or Quad9 — see my [encrypted DNS guide](/posts/best-encrypted-dns-providers-2026/) for the per-router setup. The argument for layering: if the VPN provider has a DNS hiccup, your router still resolves; if you want NextDNS-style filtering, you pick it up here.

---

## Stage 9: Split tunneling (optional)

You will want some traffic to bypass the VPN — typically:

- Banking sites that flag VPN exits as "suspicious"
- Streaming services that block VPN IPs
- Specific work devices

Install Policy-Based Routing:

```sh
opkg install vpn-policy-routing luci-app-vpn-policy-routing
```

Then in LuCI, create rules:

- "Source IP 192.168.50.42 → use WAN" (a specific device bypasses the VPN)
- "Destination domain *.netflix.com → use WAN" (Netflix bypasses VPN)
- "Destination IP your-bank-cidr → use WAN" (banking bypasses VPN)

Be careful: rules are evaluated in order. Test each rule.

---

## Stage 10: Performance tuning

If you are not getting the speed you expected:

- Confirm WireGuard is using the right MTU (default 1420; sometimes lower works better on flaky links)
- Confirm you do not have IPv6 leaking around the tunnel (test at `https://ipv6leak.com`)
- Check CPU load during a speed test (`top` over SSH). If a single core pegs at 100%, you are CPU-limited and need a faster router.
- For the Flint 2, enable hardware NAT offload in firewall settings — gives a measurable boost.

Realistic numbers I see on a Flint 2 over Mullvad:

- Wired client: ~720 Mbps down on a 1 Gbps line
- Wi-Fi client (Wi-Fi 6, close to AP): ~600 Mbps
- Wi-Fi client (Wi-Fi 5, distant): ~250 Mbps

---

## Common mistakes

1. **Flashing over Wi-Fi.** Always Ethernet during the flash.
2. **Leaving the default password.** Set a strong root password and enable SSH key auth before exposing anything.
3. **Forgetting to disable IPv6 on the WAN if your provider does not handle it.** IPv6 leaks around the tunnel are common.
4. **Trusting the WireGuard interface to come up on boot without testing.** Reboot the router during setup and confirm `wg0` comes up automatically.
5. **Not backing up the config.** `System → Backup` exports a tarball of your full config. Save it before changes and after each working state.

---

## Pairing with the rest of the privacy stack

A VPN router is the network-layer protection. You still want:

- [Encrypted DNS](/posts/best-encrypted-dns-providers-2026/) on top
- [A hardened browser](/posts/best-privacy-browsers-2026/) per device
- [Encrypted email](/posts/best-encrypted-email-services-2026/) for the message layer
- [Hardware security keys](/posts/best-hardware-security-keys-2026/) for important accounts
- [Encrypted cloud storage](/posts/best-secure-cloud-storage-2026/) for documents
- [Disposable phone numbers](/posts/best-disposable-phone-numbers-2026/) for the identifier layer

The router protects the network; the rest of the stack protects the layers above. Together, this is a serious posture.

---

## Bottom line

A VPN router with OpenWrt is not as scary as the internet makes it sound. The critical bits:

- Buy <a href="https://www.gl-inet.com/products/gl-mt6000" target="_blank" rel="nofollow sponsored noopener">GL.iNet Flint 2</a> if you want the easy path
- Use <a href="https://mullvad.net" target="_blank" rel="nofollow sponsored noopener">Mullvad</a> or <a href="https://protonvpn.com" target="_blank" rel="nofollow sponsored noopener">Proton VPN</a> for the tunnel
- Configure the firewall correctly to enforce the kill switch
- Install policy-based routing for the inevitable "this site does not like VPN" exceptions

Total cost: ~$170 hardware, ~€5/month service, one Saturday afternoon. The result is a network that works exactly the way you want, with zero per-device VPN drama, for years.
