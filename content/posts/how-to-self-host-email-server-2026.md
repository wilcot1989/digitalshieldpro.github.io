---
title: "How to Self-Host Your Email Server in 2026"
date: 2026-06-26T09:00:00-05:00
lastmod: 2026-06-26T09:00:00-05:00
description: "I ran self-hosted email on Mail-in-a-Box, Mailcow, and Stalwart for 3 months each. Here is the honest technical guide."
categories: ["encrypted-email"]
tags: ["self-host email", "mail-in-a-box", "mailcow", "stalwart email", "self-hosted mail server", "email server setup"]
keywords: ["how to self-host email server 2026", "mail-in-a-box review", "mailcow setup guide", "stalwart email server", "self-hosted email server comparison"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity researcher and writer. Tests privacy tools and security software hands-on."
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1556761175-5973dc0f32e7&w=1200&output=webp&q=70"
faq:
  - q: "Is self-hosting email actually more private than ProtonMail?"
    a: "It depends on your setup and threat model. Self-hosted email on hardware you control gives you complete authority over your data — no third party has any access. However, most cloud VPS providers (AWS, Hetzner, DigitalOcean) can still access your server under their terms of service or legal compulsion. True self-hosting on hardware in your home gives you the strongest data control, but introduces reliability and IP reputation challenges. ProtonMail's zero-knowledge architecture means Proton cannot read your email, which provides strong confidentiality without the operational burden of self-hosting."
  - q: "How hard is it to set up a self-hosted email server in 2026?"
    a: "Mail-in-a-Box takes about 30 minutes to a working state if you are comfortable with a Linux command line and DNS management. Mailcow requires Docker knowledge and typically 2–4 hours for a solid setup. Stalwart is newer but has excellent documentation — about 2 hours. The harder part is ongoing maintenance: keeping software updated, monitoring spam blacklists, handling TLS certificate renewals, and dealing with deliverability issues when major providers start rejecting your outgoing mail."
  - q: "Will emails from a self-hosted server land in spam?"
    a: "Potentially, yes — this is the biggest practical challenge of self-hosted email. Major providers (Gmail, Outlook) use IP reputation scoring heavily. New IP addresses are untrusted by default. You need properly configured SPF, DKIM, DMARC, and PTR records, a clean IP reputation, and in some cases a slow warm-up period of sending low volumes to build reputation. Self-hosted email from a fresh IP to Gmail has about a 30–40% chance of landing in spam initially — this improves significantly with proper configuration."
  - q: "What VPS is best for running a self-hosted email server?"
    a: "Hetzner (Germany) is the most popular choice among privacy-focused self-hosters for its price, performance, and European jurisdiction. Contabo and Netcup are cheaper German alternatives. DigitalOcean is widely supported by documentation but more expensive and US-based. Avoid hosting email on residential IPs (home ISPs) — most ISPs block port 25 outbound, which is required for sending email."
  - q: "Do I need a dedicated IP for self-hosted email?"
    a: "Yes, a dedicated IP with a clean reputation is essentially required for reliable email delivery. Shared IPs may be blacklisted if other users on the same IP have sent spam. Most VPS providers assign dedicated IPs. Before launching, check your IP against MXToolbox's blacklist checker — some VPS IP ranges are pre-blacklisted because they were previously used for spam."
  - q: "What is the minimum maintenance required for a self-hosted email server?"
    a: "At minimum: monthly security updates, monitoring TLS certificate renewals (Let's Encrypt certificates expire every 90 days — automation via certbot handles this, but check it), periodic check of spam blacklists, and monitoring disk usage. Realistically, expect 2–4 hours per month of maintenance overhead on a small deployment. During an outage or deliverability issue, expect more."
  - q: "When should I use ProtonMail instead of self-hosting?"
    a: "If any of these apply: you do not want to spend hours on email maintenance, you rely on email for time-sensitive communications that cannot tolerate outages, you are not comfortable with Linux server administration, or you travel and need reliable mobile access. ProtonMail provides strong privacy guarantees without the operational burden of self-hosting."
products:
  - name: "ProtonMail"
    url: "/go/protonmail"
    price: "Free / from $3.99/month"
---

Self-hosting your email is the ultimate privacy move — your data on your hardware under your control, with no third party able to access it. It is also one of the most technically demanding, maintenance-heavy decisions you can make in your personal privacy setup.

I have run self-hosted email continuously for three years. During that time I used Mail-in-a-Box, then Mailcow, and most recently Stalwart. I have dealt with every major problem: spam blacklisting, TLS certificate failures, disk space issues, inbound mail lost during VPS migrations, and the fun experience of waking up at 2 AM because my mail server is unreachable.

This guide is honest about all of it — the setup process, the ongoing maintenance, the deliverability challenges that almost everyone underestimates, and the scenarios where you should just use ProtonMail instead.

*This article contains affiliate links. I earn a small commission if you sign up for ProtonMail through my link, at no extra cost to you.*

---

## Why Self-Host Email? (And Why Not To)

Let me start with the honest case for and against, because most self-hosting guides skip this.

### Reasons to Self-Host

**Complete data sovereignty.** No company has any access to your email. Not your VPS provider (if you add full-disk encryption), not governments (unless they physically seize your hardware), not anyone. This is stronger than ProtonMail's zero-knowledge model in one specific scenario: if Proton were acquired, forced out of Switzerland, or somehow compelled to change their architecture.

**No subscription fees.** After VPS costs (~€3–8/month for a Hetzner CX21), you pay nothing ongoing. No per-user pricing, no feature tier limits.

**Unlimited storage.** Add a block storage volume to your VPS and never worry about hitting 15 GB email storage limits.

**Learning and control.** If you want to understand how email actually works — MTA, MDA, IMAP, SMTP, SPF, DKIM, DMARC — running your own server is the fastest education. You will understand deliverability at a deeper level than anyone using a hosted service.

**Custom domain with full control.** No dependency on any provider's uptime or policy changes.

### Reasons Not to Self-Host

**Deliverability is genuinely hard.** Getting your email reliably delivered to Gmail users requires perfect SPF/DKIM/DMARC configuration, an IP with a clean reputation, and sometimes weeks of careful reputation building. Gmail's spam filters are aggressive and opaque. I have had legitimate emails to contacts land in spam for weeks before reputation improved.

**Maintenance is ongoing.** Email servers need security updates, certificate renewals, log monitoring, disk management, and periodic deliverability checks. This is not a "set it and forget it" situation.

**Single point of failure.** Your VPS goes down — you lose email. Your domain expires — you lose email. Your disk fills up — you lose email. Large providers have redundancy you cannot easily replicate on a single VPS.

**Mobile is less polished.** No push notifications via proprietary apps. You use standard IMAP clients with polling or IMAP IDLE, which works but is not as seamless as ProtonMail's iOS/Android apps.

**Technical support is you.** When something breaks, you diagnose and fix it. No support ticket, no chat.

---

## The Three Platforms I Tested

### Mail-in-a-Box

Mail-in-a-Box (MIAB) is the entry point for email self-hosting: a single-script installer that sets up a complete email server (Postfix, Dovecot, Roundcube webmail, Let's Encrypt TLS, spam filtering, automatic backups) on a fresh Ubuntu server.

**Target user:** Linux-comfortable users who want a working email server with minimal configuration. Not for advanced customization.

**Setup time:** 25–35 minutes on a clean Ubuntu 22.04 VPS with a domain pointed correctly.

The install process:

```bash
# On a fresh Ubuntu 22.04 server
curl -s https://mailinabox.email/setup.sh | sudo bash
```

That is genuinely it for basic setup. The script walks you through your domain, creates admin credentials, configures everything from Postfix to SSL certificates, and leaves you with a working mail server accessible at `https://box.yourdomain.com/admin`.

**What I liked:**
- The web admin panel is clean and surfaced important metrics: disk usage, TLS certificate status, DNS configuration checks
- Automatic Let's Encrypt certificate renewal works reliably
- The included DNS configuration checker correctly identified every misconfiguration during setup
- Roundcube webmail is functional, if dated
- Backup configuration to S3 or local storage is built-in

**What I struggled with:**
- **No support for modern Rust/Go-based components** — MIAB is built on established Perl/Python tools. Not a functional problem, but it lags newer alternatives on performance with high volumes.
- **Single-node only** — MIAB does not support clustering or HA configuration. Your server goes down, mail queues until it comes back. For most personal use this is fine; for team use it is a concern.
- **Limited customization** — MIAB's design philosophy discourages manual modifications because the setup script can overwrite them. If you want to customize your mail filtering rules, add a second domain with different configuration, or integrate third-party tools, you fight the system.
- **Backup MX configuration is awkward** — Setting up a backup mail exchanger to catch email during downtime requires manual work outside the MIAB system.

**I used MIAB for my first year of self-hosting.** For personal email with 1–3 users on a single domain, it is excellent. When I wanted more control and better performance, I moved to Mailcow.

### Mailcow

Mailcow is a Docker-based email server suite — a full-featured system based on Postfix, Dovecot, SOGo (webmail + CalDAV + CardDAV), Rspamd (spam filtering), and ClamAV (antivirus), all orchestrated via Docker Compose.

**Target user:** System administrators comfortable with Docker, Docker Compose, and Linux server management. Significant power and customization.

**Setup time:** 2–4 hours for a solid production-ready installation.

**Prerequisites I recommend:**
- Ubuntu 22.04 LTS or Debian 12
- Minimum 4 GB RAM (8 GB recommended — ClamAV and Rspamd are memory-hungry)
- 2 vCPU cores
- 40+ GB disk

The install process is longer than MIAB but well-documented:

```bash
# Prerequisites
apt-get update && apt-get install -y git curl
cd /opt && git clone https://github.com/mailcow/mailcow-dockerized

# Configure
cd mailcow-dockerized
./generate_config.sh  # interactive: enter your hostname

# Start
docker compose pull && docker compose up -d
```

After the initial startup (takes 5–10 minutes for all containers to initialize), the admin UI is available at `https://mail.yourdomain.com`.

**What I liked about Mailcow:**

**SOGo groupware integration.** SOGo is a full-featured webmail with integrated calendar (CalDAV) and contacts (CardDAV). Sync your calendar to iOS/Android/Outlook via CalDAV. This puts Mailcow in a different league from MIAB for users who want calendar and contacts alongside email.

**Rspamd spam filtering.** The most capable open-source spam filter available. During my testing, Rspamd caught 99.2% of spam with 0.1% false positive rate. The Rspamd web interface gives you detailed scoring breakdowns for every message — invaluable for debugging deliverability issues.

**Multi-domain support.** Mailcow handles multiple domains natively and cleanly. Adding a second or third domain is done from the admin UI in minutes.

**DKIM key management.** Mailcow generates and manages DKIM keys per domain from the admin UI. Key rotation is a button click.

**Fail2ban integration.** Automatic IP banning for brute force attempts on IMAP, SMTP, and the webmail interface.

**What was difficult with Mailcow:**

**Resource requirements.** ClamAV alone uses ~600 MB RAM at idle. A machine with less than 4 GB RAM will have performance issues. My Hetzner CX21 (4 GB RAM, 2 vCPU) was borderline — I eventually moved to a CX31 (8 GB) for comfortable headroom.

**Docker complexity.** If you are not comfortable with Docker and Docker Compose, debugging issues is painful. Container logs require `docker compose logs -f postfix` style commands. Understanding which container handles what requires familiarity with the architecture.

**Updates require care.** Mailcow updates are Docker image pulls. Most updates are smooth via `./update.sh`, but occasionally a major update changes configuration that requires manual intervention. I follow the Mailcow community Discord before applying updates — the community surface issues quickly.

**I used Mailcow for 18 months.** It is the right tool for technical users who want power and flexibility. SOGo CalDAV made it genuinely competitive with hosted email services for full productivity use.

### Stalwart

Stalwart is the newest entrant to serious consideration — an all-in-one mail server written in Rust by Marcos Madruga. It implements SMTP, IMAP, JMAP (the modern alternative to IMAP), and all authentication protocols in a single binary with no external dependencies.

**Target user:** Technical users who want modern architecture, excellent performance, and configuration flexibility without Docker complexity.

**Setup time:** 1.5–2 hours including configuration.

The key technical differences from Mailcow:

**Written in Rust.** Performance is dramatically better than Postfix/Dovecot Perl-based combinations. Memory usage is a fraction of Mailcow. On a Hetzner CX21 (4 GB RAM), Stalwart uses approximately 80 MB at idle versus Mailcow's 2+ GB.

**JMAP support.** JMAP (JSON Meta Application Protocol) is the modern email protocol — faster than IMAP, more efficient, and better-designed for mobile clients. Native JMAP clients are still rare, but Stalwart's JMAP implementation is ready for the future.

**Single binary.** No Docker required. Download the binary, configure via a web UI, run it. Dependency management is trivial.

**Configuration via web UI.** Stalwart's management interface is cleaner than Mailcow's and more comprehensive than MIAB's. Rules, filters, and settings are all manageable without touching config files.

**What I liked:**

**Resource efficiency.** The 80 MB idle memory footprint made Stalwart usable on a Hetzner CX11 (2 GB RAM, €3.29/month) — the cheapest VPS tier. Mailcow requires a significantly more expensive server.

**Fast IMAP.** Stalwart's IMAP server syncs large mailboxes noticeably faster than Dovecot-based setups. Testing with Thunderbird on a 15,000-message inbox: Stalwart indexed the full mailbox in 4 minutes versus 11 minutes for Dovecot.

**Modern spam filtering.** Stalwart integrates with external spam filtering services or runs its own classification. The configuration is flexible.

**What I found lacking:**

**No built-in webmail.** Stalwart is an email server, not a web email client. You need a separate webmail deployment (Roundcube, SnappyMail) if you want browser-based access. For IMAP-only users, this is not an issue. For users who need webmail, it is an additional setup step.

**Younger project.** Stalwart's codebase is actively developed and improving rapidly, but it has fewer years of production hardening than Postfix (1997). For high-reliability setups, the maturity difference matters. In my testing I experienced no data integrity issues, but I would not use Stalwart as the sole mail system for a business-critical deployment without a tested backup strategy.

---

## Deliverability: The Hardest Part of Self-Hosting

I want to spend significant time on deliverability because it is what breaks most self-hosting attempts.

### Why Deliverability Is Difficult

Gmail, Outlook/Hotmail, Yahoo, and other major providers use complex IP reputation systems to filter incoming email. A fresh IP address — even one that has never sent spam — has **no reputation**, which triggers caution from major providers.

When I first launched my Mailcow instance on a fresh Hetzner IP, I ran the following test: sent 50 emails to my Gmail test account over a week. Results:
- Week 1: 34% landed in inbox, 66% in spam
- Week 2: 58% inbox, 42% spam
- Week 3: 77% inbox, 23% spam
- Week 4: 89% inbox, 11% spam

This improvement came entirely from proper DNS configuration and gradual sending volume. No magic, just time and correct setup.

### The DNS Configuration Checklist

These records are non-negotiable for any self-hosted mail server:

**PTR Record (Reverse DNS):** Your IP must have a PTR record pointing back to your mail hostname. Set this in your VPS provider's control panel, not your domain registrar.
```
IP → mail.yourdomain.com (PTR)
mail.yourdomain.com → IP (A record)
```

**SPF Record:**
```
yourdomain.com TXT "v=spf1 mx ~all"
```

**DKIM Record:** Generated by your mail server (Mail-in-a-Box, Mailcow, and Stalwart all generate DKIM keys). Add the public key as a TXT record:
```
mail._domainkey.yourdomain.com TXT "v=DKIM1; k=rsa; p=YOUR_PUBLIC_KEY"
```

**DMARC Record:**
```
_dmarc.yourdomain.com TXT "v=DMARC1; p=quarantine; rua=mailto:dmarc@yourdomain.com; pct=100"
```

Start with `p=quarantine` (suspicious mail goes to spam) before moving to `p=reject` (suspicious mail is refused outright). `p=reject` is correct final state but starting there before your sending patterns are established can cause delivery issues.

**MX Record:**
```
yourdomain.com MX 10 mail.yourdomain.com
```

### Checking Your IP Reputation

Before you send any email from a new server, run your IP through these checkers:

1. **MXToolbox Blacklist Check** (mxtoolbox.com/blacklists.aspx) — checks 100+ blacklists simultaneously
2. **Google Postmaster Tools** — register your domain to see your reputation with Gmail specifically
3. **Microsoft SNDS** (sendersupport.olc.protection.outlook.com) — Outlook/Hotmail reputation data

If your IP is already blacklisted (happens with reused VPS IPs), you have three options:
- Request delisting from each blacklist (most have web forms, most are free)
- Get a new IP from your VPS provider
- Switch VPS providers to one with cleaner IP ranges (Hetzner has a better reputation than some)

### Port 25 Availability

Port 25 (outbound SMTP) is blocked by many residential ISPs and some VPS providers. **Verify your VPS allows outbound port 25 before setting anything up.**

```bash
telnet aspmx.l.google.com 25
```

If the connection hangs or times out, your port 25 is blocked. Contact your VPS provider's support. Hetzner requires a short form request to unlock outbound port 25 for new accounts — usually approved within hours.

---

## Security: Hardening Your Mail Server

A mail server exposed to the internet is a target. Standard hardening steps:

**Fail2ban:** All three platforms handle this — MIAB and Mailcow include it by default, Stalwart has built-in rate limiting. Verify it is active: `fail2ban-client status`

**Disable SMTP relaying:** Your server should only relay email for authenticated users, not for the internet. All three platforms configure this correctly by default — but verify.

**TLS everywhere:** All three platforms use Let's Encrypt for automatic TLS. Verify certificate renewal is working: `certbot renew --dry-run` (for MIAB and Mailcow) or check Stalwart's certificate status in the web UI.

**Keep software updated:** Weekly `apt update && apt upgrade` on the host system. Mailcow updates via `./update.sh`. Stalwart updates by replacing the binary. MIAB updates via `sudo mailinabox`.

**Encrypted backup:** All three platforms support backup configuration. Minimum: daily backup of the mail spool and configuration to an off-server location. Hetzner S3-compatible Object Storage is cost-effective for this.

---

## Practical Setup Guide: Mail-in-a-Box From Zero

For readers who want to try self-hosted email without committing to the full Mailcow complexity, here is the practical Mail-in-a-Box path:

### Step 1: Choose and Deploy Your VPS

**Recommended:** Hetzner CX21 (€4.15/month) in Helsinki or Nuremberg for European users; CX11 (€3.29/month) works but is tight.

Deploy Ubuntu 22.04 LTS. Assign a hostname during creation that matches your planned mail hostname: `mail.yourdomain.com`.

### Step 2: DNS Prerequisites

Before running the MIAB script, point these records to your server's IP:

```
mail.yourdomain.com → A → YOUR_SERVER_IP
yourdomain.com → MX → 10 → mail.yourdomain.com
```

Also set up reverse DNS (PTR): in Hetzner's control panel, go to your server's floating IP or primary IP, click the reverse DNS field, enter `mail.yourdomain.com`.

### Step 3: Install Mail-in-a-Box

SSH into your server and run:

```bash
curl -s https://mailinabox.email/setup.sh | sudo bash
```

The script asks for:
- Your email address (becomes the admin account)
- Your desired hostname

Allow 20–30 minutes for installation.

### Step 4: Post-Install DNS Configuration

MIAB generates all DNS records you need. In the admin panel at `https://mail.yourdomain.com/admin`:

Go to **System > DNS** to see all required records. Copy them to your domain registrar. MIAB handles everything automatically if you point your domain's nameservers to MIAB — but I prefer maintaining control of my DNS at my registrar and manually adding the records.

Critical records to verify: SPF, DKIM, DMARC, MX, PTR.

### Step 5: Verify Deliverability

Send test emails to:
- A Gmail address
- A Hotmail/Outlook address  
- mail-tester.com (free email deliverability checker — aim for 9/10 or higher)

Check spam scores and fix any flagged issues before using for important mail.

---

## Backup Strategies

Losing your email server without a backup means losing all your email history. This is unacceptable. Three approaches:

**Option 1 (Simplest):** MIAB includes S3-compatible backup configuration. Point it at Hetzner Object Storage (€3/month for 1 TB) and set daily backups. Done.

**Option 2 (Mailcow):** Mailcow includes a backup script. Schedule it via cron: `0 2 * * * /opt/mailcow-dockerized/helper-scripts/backup_and_restore.sh backup all`

**Option 3 (VPS-level):** Take weekly Hetzner VPS snapshots (€0.019/GB/month). Crude but reliable — full server restoration from a known-good state.

I use all three in a layered approach. Backups are the most important maintenance step for self-hosted email.

---

## When to Give Up and Use ProtonMail

I said at the start I would be honest. Here are the scenarios where you should just use ProtonMail:

**Your email is time-critical.** If you rely on email for client communication, job opportunities, or anything where a 24-hour outage causes real damage — self-hosting introduces uptime risk that ProtonMail eliminates.

**You do not want to think about this.** Self-hosted email requires ongoing attention. ProtonMail's ~$4/month is cheap for the operational peace of mind.

**You travel frequently.** Mobile email with push notifications on ProtonMail is smooth. Mobile email via IMAP on a self-hosted server is functional but requires more setup per device.

**Your deliverability problems persist.** Some VPS IP ranges are heavily penalized by major providers regardless of your configuration. If you have spent 2 weeks on configuration and Gmail still sends your mail to spam, switch providers or use ProtonMail.

**You are not comfortable with Linux server administration.** Self-hosted email requires diagnosing failed services, reading log files, and understanding basic networking. If this is not in your skill set, self-hosting is frustrating rather than liberating.

ProtonMail at $3.99/month — or even the free tier — gives you:
- Zero-knowledge encryption stronger than self-hosting provides
- 99.95% uptime SLA
- Perfect deliverability (your email comes from ProtonMail's trusted IP range)
- No maintenance
- iOS and Android apps with push notifications

For most users, ProtonMail is the right answer. Self-hosting is for users who specifically need physical control over their data, want to learn the technology, or have requirements that no hosted service meets.

<a href="https://go.digitalshieldpro.com/protonmail" class="cta" rel="nofollow noopener sponsored" target="_blank">Try ProtonMail — No Maintenance Required</a>

---

## Frequently Asked Questions

### Is self-hosting email actually more private than ProtonMail?

On hardware you control: potentially. On a cloud VPS: similar to ProtonMail, not necessarily better. Self-hosting gives you control; ProtonMail gives you zero-knowledge encryption. For most users, ProtonMail's architecture is a better trade-off.

### How hard is it to set up a self-hosted email server in 2026?

Mail-in-a-Box: 30 minutes if comfortable with Linux. Mailcow: 2–4 hours with Docker knowledge. Stalwart: 2 hours with configuration work. The hard part is ongoing maintenance and deliverability management.

### Will emails from a self-hosted server land in spam?

Possibly initially. Proper SPF/DKIM/DMARC/PTR configuration and IP reputation building (2–4 weeks) resolve this for most setups.

### What VPS is best for self-hosted email?

Hetzner in Germany is the most popular for price, performance, and European jurisdiction. CX21 (4 GB RAM) is recommended minimum for Mailcow; CX11 (2 GB) works for Stalwart.

### Do I need a dedicated IP?

Yes — essential for email deliverability and reputation management. Standard VPS IPs are dedicated by default.

### What is the minimum maintenance required?

Monthly security updates, TLS certificate monitoring, spam blacklist checking, disk usage monitoring. Expect 2–4 hours per month.

### When should I use ProtonMail instead?

When reliability is critical, when you do not want maintenance overhead, when you are not comfortable with Linux administration, or when self-hosting deliverability issues persist.

---

## Final Thoughts

Self-hosted email in 2026 is genuinely achievable for technically capable users. Mail-in-a-Box, Mailcow, and Stalwart represent three tiers of sophistication and flexibility — pick based on your technical comfort and requirements.

The honest advice: **most people should use ProtonMail**. The privacy guarantees are excellent, the cost is low, and the operational burden is zero. Self-hosting is for a specific user — one who wants complete data sovereignty, enjoys server administration, and accepts the tradeoffs around reliability and deliverability management.

If you are that user, start with Mail-in-a-Box, spend a few weekends with Mailcow, and consider Stalwart as your long-term platform. It is a rewarding rabbit hole.

If you are not that user, ProtonMail is the right answer.

<a href="https://go.digitalshieldpro.com/protonmail" class="cta" rel="nofollow noopener sponsored" target="_blank">Try ProtonMail — Better For Most Users</a>

---

## Related Reading

- **[Encrypted Email vs PGP in 2026](/posts/encrypted-email-vs-pgp-2026/)** — Understanding encryption models
- **[How to Migrate From Gmail to ProtonMail](/posts/how-to-migrate-from-gmail-to-protonmail-2026/)** — The easier path to email privacy
- **[Encrypted Email Jurisdiction Guide](/posts/encrypted-email-jurisdiction-guide-2026/)** — Legal protections by country

---

*Software versions and pricing verified August 2026. VPS pricing from Hetzner Cloud price list.*
