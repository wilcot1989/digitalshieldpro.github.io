---
title: 'Self-hosted notes apps for privacy 2026: Joplin Server vs Logseq vs SilverBullet'
date: 2026-10-11 09:00:00+02:00
lastmod: 2026-10-11 09:00:00+02:00
description: I self-hosted Joplin Server, Logseq Sync, and SilverBullet on my own VPS for six months each. Here is the honest 2026 comparison of which one actually keeps your notes private, syncable, and recoverable when things go wrong.
categories:
- privacy-tools
tags:
- self-hosted
- joplin
- logseq
- silverbullet
- notes
- privacy
- markdown
keywords:
- self hosted notes app 2026
- joplin server review
- logseq self host
- silverbullet notes
- private notes sync
- markdown notes self hosted
affiliate: false
author: James Mitchell
author_bio: Cybersecurity analyst with 10+ years of hands-on experience testing VPNs, antivirus software, and privacy tools.
featured_image: /images/categories/privacy-tools.svg
faq:
- q: 'Why self-host notes instead of using Standard Notes or Cryptee?'
  a: 'Three reasons. First, no vendor lock-in — your notes are markdown files on your server, readable by any text editor forever. Second, no monthly subscription. Third, the sync server runs on hardware you control, so even if a vendor is compelled or compromised, your notes are not exposed. The trade-off is operational responsibility — you back it up, you patch it, you fix it when it breaks.'
- q: 'Is self-hosting notes safer than a zero-knowledge SaaS?'
  a: 'Not automatically. A poorly secured VPS with weak SSH passwords is *less* safe than [Standard Notes](/posts/best-encrypted-notes-apps-2026/). Self-hosting is safer only if you keep up with patches, run a firewall, use SSH keys not passwords, enable [encrypted DNS](/posts/best-encrypted-dns-providers-2026/), and back up encrypted snapshots off-site. If that sounds like work — it is. SaaS is fine.'
- q: 'Does Joplin Server actually encrypt my notes end-to-end?'
  a: 'Joplin clients can encrypt notes end-to-end before upload (E2EE setting in Joplin, off by default). Joplin Server only ever sees ciphertext when E2EE is on. Turn it on. The server itself is not encrypted at rest by default — that is your responsibility on the host (full-disk encryption, encrypted volume).'
- q: 'Is Logseq Sync available self-hosted?'
  a: 'Logseq has a paid hosted Sync product, but for self-hosting most people use Git, Syncthing, or rsync over SSH to sync the markdown files between devices. This works very well. The downside: there is no real-time multi-device collaboration; you sync between sessions.'
- q: 'What is SilverBullet and why do people like it?'
  a: 'SilverBullet is a relatively new (2023+) open-source notes-as-code app that runs as a single binary or Docker container. It treats your notes as a queryable knowledge base — you write markdown with embedded queries that surface tasks, links, and structured data. It is the most "programmer-flavoured" of the three but it is fast, clean, and the self-hosting story is the simplest.'
- q: 'Can I use my phone with self-hosted notes?'
  a: 'Yes for all three. Joplin has full iOS/Android apps that connect to Joplin Server. Logseq has mobile apps that read from a Git repo or sync folder (works best with iCloud + manual Git). SilverBullet works in mobile browsers as a web app and supports installable PWA — you do not get a native app, but you get full functionality.'
- q: 'How much does it cost to self-host?'
  a: 'A $4/month VPS (Hetzner CX11, Vultr regular, OVH starter) handles all three with room to spare for other services. A $5/month domain. Total: under $60/year, plus your time. Compared to $96/year for Standard Notes Productivity, the savings are real if your time is cheap. The savings disappear if you have to debug at 11pm.'
- q: 'Which one should a beginner pick?'
  a: 'Joplin Server. It has the best documentation, the most mature mobile apps, and the most active community when something goes wrong. Logseq is a stronger thinking tool but has the most awkward sync story. SilverBullet is the most fun but the smallest community — fine for tinkerers, less fine if you just want it to work.'
products:
- name: Joplin
  url: https://joplinapp.org
  price: 'Free (self-host) / €2.99 hosted'
- name: Logseq
  url: https://logseq.com
  price: 'Free / $5 Sync'
- name: SilverBullet
  url: https://silverbullet.md
  price: 'Free'
schema_type: Article
---

*This article describes self-hosting setups I have personally run. None of these projects has an affiliate program. They are all free and open source.*

Self-hosting your own notes server is the kind of thing that sounds like a chore until you realise you have been paying $96 a year for an app that occasionally goes down anyway. The math gets clearer in 2026 with VPS prices flat, Docker images trivial to deploy, and the open-source notes ecosystem genuinely competitive with the commercial options.

I ran Joplin Server, Logseq, and SilverBullet on my own VPS for roughly six months each as my daily notes app. Different jobs, different strengths. Here is the honest comparison.

---

## What you get and what you give up

Self-hosted notes have three properties that paid services often do not match:

1. **Notes are plain markdown files** — readable in any editor on any OS, forever
2. **Sync is on your infrastructure** — no vendor logs, no compelled disclosure of *which* notes you have
3. **No subscription** — one-time time cost, ongoing $4/mo VPS

What you give up:

1. **Polish.** All three are usable. None has the iOS-native feel of Apple Notes or the design refinement of Standard Notes.
2. **Time.** You will spend an evening setting it up. You will spend another evening when something goes wrong six months later.
3. **The "I just paid them" excuse.** When notes vanish, it is on you.

If those trade-offs sound bad, [Standard Notes or Cryptee](/posts/best-encrypted-notes-apps-2026/) are excellent SaaS alternatives.

---

## The three contenders

### Joplin Server

- **Type:** Markdown notes app with notebooks, tags, tasks
- **Sync:** Joplin Server (Docker), or third-party (Dropbox, OneDrive, Nextcloud, S3, WebDAV)
- **Mobile:** iOS, Android (full-featured)
- **Desktop:** macOS, Windows, Linux
- **E2E encryption:** Yes, optional, opt-in
- **Maturity:** Very mature — first release 2017
- **Plugin ecosystem:** Strong — outlines, math, mermaid, kanban, etc.

Joplin is the boring-but-it-works option. Markdown, notebooks, attachments, tags, web clipper, search, tasks. The desktop app is Electron (memory-hungry but cross-platform). The mobile apps are genuinely good. E2E encryption is a checkbox.

The killer feature for self-hosters is Joplin Server: a small Docker container (about 200MB RAM) that handles sync over HTTPS. You run it behind nginx or Caddy with a Let's Encrypt cert and you have your own private notes cloud.

### Logseq

- **Type:** Outliner / knowledge graph (Roam-style)
- **Sync:** Git, Syncthing, iCloud, or paid Logseq Sync ($5/mo)
- **Mobile:** iOS, Android
- **Desktop:** macOS, Windows, Linux
- **E2E encryption:** Yes via Logseq Sync; varies for self-host setups
- **Maturity:** Mature — first release 2020
- **Plugin ecosystem:** Strong — calendar, tasks, references, etc.

Logseq is the thinking tool. Daily journals, bidirectional links, block references, queries. If you have ever loved Roam Research or Obsidian's graph view but wanted full-fat open source with a self-hosted sync option, Logseq is the answer.

The catch is sync. Logseq does not have a native self-hosted sync server (unlike Joplin). Most self-hosters sync via Git: each device commits and pulls from a private Gitea or self-hosted Forgejo. This is bulletproof but introduces merge conflicts when two devices edit the same file. For solo users it is fine. For multi-device active users it is awkward.

### SilverBullet

- **Type:** Markdown + queries + scripts (notes-as-code)
- **Sync:** Single server, all devices connect to it
- **Mobile:** Web/PWA only — no native apps
- **Desktop:** Web/PWA + Electron wrapper
- **E2E encryption:** Server-side via TLS; not E2E in the zero-knowledge sense
- **Maturity:** Newer — first release 2022
- **Plugin ecosystem:** Plugs (TypeScript), small but growing

SilverBullet is the most fun of the three. It runs as a single Docker container or even a single Deno binary. Notes are markdown files in a folder on your server. The web UI is genuinely fast and clean. It supports embedded queries — you write markdown that includes `query: tasks where state="todo"` and the page surfaces matching content from your other notes.

It is also the youngest and the smallest community. If you hit a bug, you are reading the GitHub issues yourself. For tinkerers, this is part of the appeal.

---

## Setup: roughly what each takes

### Joplin Server

```bash
docker run -d --name joplin-server \
  -p 22300:22300 \
  -e APP_BASE_URL=https://notes.example.com \
  -e DB_CLIENT=sqlite \
  joplin/server:latest
```

Then put it behind Caddy with auto-HTTPS:

```caddy
notes.example.com {
  reverse_proxy localhost:22300
}
```

Create the admin account at `https://notes.example.com`, add users, log into Joplin desktop and mobile clients, point them at your server, enable E2E encryption, set a strong key, you are done. About 30 minutes total.

### Logseq + Git

1. Stand up a Forgejo or Gitea on your VPS (or use a private repo on a self-hosted source-forge).
2. Create a private repo, e.g. `logseq-graph`.
3. On each device, clone the repo into a Logseq graph folder.
4. Use Git directly or a tool like Working Copy (iOS) to sync.

About 60 minutes — most of it Forgejo setup, which is reusable for other things.

### SilverBullet

```bash
docker run -d --name silverbullet \
  -v $(pwd)/notes:/space \
  -p 3000:3000 \
  -e SB_USER=me:strong-password-here \
  zefhemel/silverbullet:latest
```

Caddy reverse proxy to port 3000 with HTTPS. Open the URL on your phone, "Add to Home Screen," and you have a notes app. About 15 minutes — the simplest of the three.

---

## How they handle the privacy questions

### "Does the server see my notes?"

- **Joplin with E2EE on:** No. Server stores ciphertext only.
- **Joplin with E2EE off:** Yes. Server stores plain markdown.
- **Logseq + Git:** The Git server (yours) stores plain markdown unless you encrypt the repo (e.g. git-crypt).
- **SilverBullet:** Yes. Server stores plain markdown. Privacy is via the fact that you control the server, not via E2E.

For threat models that include "an attacker takes my VPS," Joplin with E2EE is the strongest. For threat models that are mostly "do not let SaaS vendors mine my notes," any of these works.

### "Where does the metadata leak?"

- **Joplin desktop:** Calls home for plugin updates and version checks. Can be disabled.
- **Logseq desktop:** Calls home for similar. Can be disabled.
- **SilverBullet:** No telemetry I have observed.

### "What about Web Clipper / mobile screenshots?"

All three support web clipping. Joplin's is a browser extension that posts to your server. Logseq has a quick-capture flow via Drafts (iOS) or the Logseq web clipper. SilverBullet has a simple "save URL" plug.

The privacy-respecting flow is: clipper sends straight to your server over HTTPS. No third party in the middle. All three meet this bar.

---

## Mobile experience

This is where the three split:

- **Joplin mobile:** Genuinely excellent. Full-featured, syncs with E2EE, web clipper share extension works. iOS and Android.
- **Logseq mobile:** Good for reading and editing. Syncing requires either paid Logseq Sync or some manual Git workflow on phone (Working Copy is the typical answer on iOS).
- **SilverBullet mobile:** Web-only PWA. Works fine in Safari/Chrome, installable to home screen, no offline mode by default. If your VPS is down you cannot read your notes.

For a phone-heavy workflow, Joplin wins. For a desktop-heavy workflow, all three are fine.

---

## How they compare for security hardening

Whichever you pick, harden the host:

- SSH keys only, no password auth
- UFW or iptables firewall, expose only 80/443 publicly
- [Encrypted DNS](/posts/best-encrypted-dns-providers-2026/) on the host
- Fail2ban on SSH
- Automatic security updates (`unattended-upgrades` on Debian/Ubuntu)
- Off-site encrypted backups to [secure cloud storage](/posts/best-secure-cloud-storage-2026/) — restic + B2 is the standard
- TLS via Let's Encrypt (Caddy makes this automatic)
- Watchtower or manual Docker image updates

The notes app is the easy part. The host is the part you can mess up.

---

## Backups: the part nobody talks about

Self-hosted notes without backups is a worse situation than SaaS notes. Standard Notes will not lose your data; your VPS provider will, eventually, on a hard-drive failure.

What I run:

- Daily `restic` snapshot of `/data` to a [Backblaze B2 bucket](/posts/best-secure-cloud-storage-2026/)
- Weekly snapshot to a second provider (Wasabi)
- Monthly download-to-laptop drill (proof you can actually restore)
- Restic password in a [password manager](/posts/best-password-managers-2026/) and on paper in a fire safe

Total cost: about $1/month for the storage. Total work: 30 minutes once.

---

## Common mistakes

1. **Skipping E2EE on Joplin Server.** Always turn it on. The ten seconds of setup pays off forever.
2. **Forgetting the encryption password.** No recovery. Lost is lost. Use a strong but memorable passphrase and write it down in two places.
3. **Self-hosting on a residential connection.** Dynamic IPs, ISP TOS issues, NAT pain. Use a $4 VPS instead.
4. **No off-site backup.** Your VPS provider can lose data. Backup to a *different* provider.
5. **Treating it like a hobby.** If you are not going to patch it, you should not run it. Stick with Standard Notes or Cryptee.

---

## Bottom line

If you want it to just work and your phone matters: **Joplin Server**. Polished mobile, strong E2EE, mature ecosystem.

If you want a thinking tool with a graph: **Logseq** with Git sync. The best for daily journals and connected thinking.

If you want the simplest deploy and you live in a browser: **SilverBullet**. Most fun, smallest moving parts.

All three are real alternatives to commercial encrypted notes apps. None of them is as polished as a paid SaaS. All of them respect your data because they run on hardware you own. Pair any of them with the rest of your [privacy stack](/posts/best-privacy-stack-2026/) — encrypted email, [encrypted cloud](/posts/best-secure-cloud-storage-2026/), [hardware security keys](/posts/best-hardware-security-keys-2026/) — and you are doing better than 99% of internet users.
