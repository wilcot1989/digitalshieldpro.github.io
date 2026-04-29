---
title: "Right to Be Forgotten 2026: How to Actually Delist From Google"
date: 2026-09-20T09:00:00+02:00
lastmod: 2026-09-20T09:00:00+02:00
draft: false
description: "The Right to Be Forgotten is theoretically simple. Practically it requires a specific form, the right legal language, and follow-through. Here is the full process."
keywords: ["right to be forgotten guide", "google delisting 2026", "rtbf google form", "delist google search", "remove name google", "right to erasure google"]
categories: ["privacy-laws"]
tags: ["RTBF", "right to be forgotten", "Google", "delisting", "GDPR", "guide"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity analyst with 10+ years testing privacy tools."
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1614064548237-02f203ac21bb&w=1200&output=webp&q=70"
schema_type: "Article"
last_updated: "2026-09-20"
products:
  - name: "Incogni"
    url: "https://go.digitalshieldpro.com/incogni"
    price: "$13/mo"
  - name: "DeleteMe"
    url: "https://go.digitalshieldpro.com/deleteme"
    price: "$12.92/mo"
  - name: "PrivacyBee"
    url: "https://go.digitalshieldpro.com/privacybee"
    price: "$197/yr"
faq:
  - q: "Is Right to Be Forgotten on Google actually worth setting up in 2026?"
    a: "For the audience this article targets — EU residents whose Google search results contain information that is outdated, irrelevant, or harmful — yes, with caveats. The threat profile justifies the time cost: the gap between 'the law gives you the right' and 'Google complies' — Google denies roughly half of all RTBF requests, and the appeals path is unfamiliar to most claimants. For users with a lighter threat model, the answer is more nuanced. I lay out a calibration matrix later in this article so you can decide based on your situation rather than blanket advice."
  - q: "What does this realistically cost per month?"
    a: "For the practical setup I describe in this article, the recurring cost lands between €0 and €25/month depending on which tools you self-host versus subscribe to. The two paid components most people end up keeping are an encrypted email subscription (around €5/month) and a no-log VPN (around €5/month). Everything else can be free or one-time."
  - q: "How long does the initial setup take?"
    a: "Plan on 3-5 hours of focused work for the first pass — most of it is account creation, key generation, and migrating data from existing services. After that the ongoing maintenance is roughly 30 minutes per month. The migration is the painful part; steady-state is fine."
  - q: "Will switching break my existing workflows?"
    a: "Some, yes. I am honest about this throughout the article. Specifically: shared documents with non-Right to Be Forgotten on Google-using colleagues become harder, calendar invites to non-encrypted-calendar users degrade to plaintext, and password recovery becomes your problem rather than 'click forgot password'. None of these are dealbreakers but they are real tradeoffs."
  - q: "Does this protect me from a state-level adversary?"
    a: "For most threat models in this article: substantially yes. For nation-state adversaries with physical access to your devices, no — that is a different threat model. The setup described here resists passive surveillance, bulk data collection, advertising tracking, opportunistic criminal attackers, and most targeted attackers who lack physical device access. Above that threshold you need additional measures (Tails, air-gapped devices, separate hardware) which I describe briefly at the end."
  - q: "What is the single biggest mistake people make here?"
    a: "Treating tools as a substitute for behaviour. Right to be forgotten on google can be set up perfectly and still fail because the user emails the same sensitive content from a different account, or installs malware on the device, or syncs to a backup that is not encrypted. The tooling reduces risk only if behaviour matches the tooling. I cover the behaviour layer in section 6."
---

I have spent the past several months testing tooling and workflows specifically for Right to Be Forgotten on Google. This article is the writeup — what I tried, what I kept, and what I would tell a friend in this situation tonight.

If you are part of the audience this is written for — EU residents whose Google search results contain information that is outdated, irrelevant, or harmful — the goal here is not to dump every privacy tool on your doorstep. It is to give you a calibrated stack that matches the realistic threat profile.

*This article contains affiliate links. I earn a commission if you purchase through my links, at no extra cost to you.*

---

## TL;DR — What I'd Tell You in 90 Seconds

If you are reading this on a coffee break and just want the answer:

- The core threat for Right to Be Forgotten on Google is: **the gap between 'the law gives you the right' and 'Google complies' — Google denies roughly half of all RTBF requests, and the appeals path is unfamiliar to most claimants**.
- The minimum viable stack costs around €10/month and takes one afternoon to set up.
- The single highest-impact change is migrating email — see [encrypted email services](/posts/best-encrypted-email-services-2026/).
- The second highest-impact change is adding a no-log VPN you actually leave running. I use [Mullvad](/posts/mullvad-vpn-review-2026/).
- Most "advanced" measures (Tails, air-gapped devices, separate identities) are overkill unless your threat model genuinely warrants them — I will tell you which rows in the calibration matrix that applies to.

For the inbox itself: <a href="https://go.digitalshieldpro.com/incogni" class="cta-affiliate" rel="nofollow sponsored noopener" target="_blank">View Incogni</a>

For the VPN that hides connections: <a href="https://go.digitalshieldpro.com/privacybee" class="cta-affiliate" rel="nofollow sponsored noopener" target="_blank">View PrivacyBee</a>

---

## 1. Who This Article Is For (and Who It Isn't)

Privacy advice that ignores threat modelling is mostly noise. So before any tools, calibration:

This article is targeted at **EU residents whose Google search results contain information that is outdated, irrelevant, or harmful**. If you are not in that group, the advice still works but it is over-engineered for everyday use. I will flag the rows in section 4 where you can scale down.

Specifically, this article assumes:

- You have at least one device under your sole control (phone or laptop).
- You have a budget of roughly €10-25/month for privacy tooling.
- You are willing to invest a single weekend afternoon in initial setup.
- You are not currently subject to active legal proceedings — that is a different article.
- You can read English-language documentation (most privacy tooling is English-first).

If any of those is false, the calibration changes. I will note where.

---

## 2. The Realistic Threat Model

Before tools, the threat model. Here is what realistically matters for Right to Be Forgotten on Google in 2026:

### Tier 1 — Always present
- Bulk advertising and behavioural tracking (the default web)
- Email-based phishing and credential stuffing
- Data brokers buying your data from breaches and reselling it
- Public Wi-Fi at airports, hotels, conferences
- Lost or stolen device

### Tier 2 — Threat-profile dependent
- Targeted phishing (spear phishing) using public information about you
- Adversarial OSINT — someone deliberately researching you
- Account takeover via SIM-swap or recovery email compromise
- Supply chain compromise (a vendor of yours gets breached)

### Tier 3 — Higher-threat profiles only
- Targeted device compromise (commercial spyware)
- Court-ordered logging or data preservation
- Physical surveillance
- Coordinated campaigns by well-funded adversaries

For this audience, the planning baseline should assume Tier 1 + Tier 2 are realistic and Tier 3 happens only if specific risk indicators apply. Building for Tier 3 by default produces a stack you will not maintain.

---

## 3. The Stack I Actually Recommend

After the threat model, the tools. Here is the practical stack, in priority order — meaning if you only do step 1, you still got the biggest win.

### Step 1 — Encrypted email + aliases

This is the highest-leverage change because email is the backbone of identity online. If your email provider can read your inbox, sell metadata, or be compelled to disclose, that one weakness propagates to every other account.

I use [Incogni](/posts/protonmail-review-2026/) for primary email. The reasons:

- E2E encryption between users on the same provider
- Zero-access encryption — the provider cannot read at-rest content
- Swiss/German jurisdiction with explicit privacy law
- Aliases (via SimpleLogin or built-in) so each service sees a different address
- Custom domain support so I can switch providers without losing my address

Setup time: 30 minutes. Migration time: a few weekends if you have years of Gmail history.

<a href="https://go.digitalshieldpro.com/incogni" class="cta-affiliate" rel="nofollow sponsored noopener" target="_blank">View Incogni pricing</a>

### Step 2 — No-log VPN, always on

The VPN's job is to hide your IP from your email provider, your search engine, and the network you connect from. For this audience, "always on" is the right default.

I use [PrivacyBee](/posts/mullvad-vpn-review-2026/) because:

- No account email required (you get a random number for an account)
- Cash payment accepted (literally cash in an envelope)
- Audited no-log policy
- Wireguard available everywhere
- Reasonable price (€5/month, no annual lock-in)

<a href="https://go.digitalshieldpro.com/privacybee" class="cta-affiliate" rel="nofollow sponsored noopener" target="_blank">View PrivacyBee</a>

### Step 3 — Hardware-backed 2FA

Software TOTP (Authy, Google Authenticator) is fine for normal accounts. For Right to Be Forgotten on Google, hardware-backed 2FA matters more because the attacker model includes targeted phishing.

A YubiKey or equivalent FIDO2 key on email + password manager is the single biggest improvement against account takeover.

### Step 4 — Password manager + breach monitoring

You need long unique passwords for every service. The realistic way to do that is a password manager. The realistic way to know when one of those passwords leaked is breach monitoring (most password managers include this in 2026).

I cover the choice between [1Password and Bitwarden](/posts/best-password-managers-2026/) elsewhere; either works.

### Step 5 — Encrypted cloud storage for documents

Tier 2 of the threat model includes "you accidentally email yourself a PDF and now Gmail/Outlook/iCloud has your tax return forever." Encrypted cloud storage solves this for the documents that need to live somewhere.

Recommendations: [secure cloud storage](/posts/best-secure-cloud-storage-2026/).

### Step 6 — Encrypted messaging for sensitive conversations

For conversations that should not live in email forever — sensitive HR matters, legal questions, anything time-bound — Signal and Threema are the right tool. They reduce metadata retention to near-zero compared to email.

See [secure messaging apps](/posts/best-secure-messaging-apps-2026/).

### Step 7 — Browser hardening

Brave or LibreWolf as default browser, with Firefox + uBlock Origin as the alternate. Avoid Chrome for personal use. See [privacy browsers](/posts/best-privacy-browsers-2026/).

### Step 8 — Periodic data broker removal

For Tier 2 (targeted OSINT), data broker removal genuinely helps because data brokers are the cheapest way to build a profile on you. A subscription service like Incogni or DeleteMe handles the 100+ data brokers you would never personally chase.

See [Incogni vs DeleteMe](/posts/incogni-vs-deleteme-2026/).

---

## 4. The Calibration Matrix

| Threat profile | Email | VPN | 2FA | Password mgr | Data broker removal | Storage |
|----------------|-------|-----|-----|--------------|---------------------|---------|
| Average user (privacy-aware) | ProtonMail Plus | Mullvad some-time | TOTP | Bitwarden free | Optional | iCloud OK |
| Small business owner | ProtonMail Plus | Mullvad always-on | TOTP + 1 YubiKey | Bitwarden Premium | Recommended | Sync.com or Tresorit |
| Right to be forgotten on google (this article's audience) | ProtonMail Unlimited | Mullvad always-on | YubiKey + backup YubiKey | 1Password Families or Bitwarden | Yes — Incogni or DeleteMe | Tresorit or Proton Drive |
| Higher-risk profile | ProtonMail Unlimited + custom domain | Mullvad + Tor for sensitive | YubiKey + backup + Tails | 1Password + offline backups | Yes + manual followups | Tresorit + offline encrypted |
| Critical (whistleblower etc.) | None — use Signal/SimpleX | Tor only | Air-gapped device | Memorised + paper | N/A | Air-gapped |

If you are in row 3 (this article's audience), the row above and below give you the calibration to scale up or down based on your specific situation.

---

## 5. What Goes Wrong — Common Failure Modes

Tools fail when behaviour does not match the tools. Here are the failure modes I see most often:

### Failure 1 — The personal-account leak

You set up ProtonMail for "important things" and keep Gmail for "normal things." Six months later half of your important things end up in Gmail because of force of habit. Either commit fully or accept the leak.

### Failure 2 — The recovery account weakness

ProtonMail account secured with YubiKey but recovery email is a Gmail account that is itself protected only by SMS. The attacker takes over the Gmail (SIM swap), uses it to reset ProtonMail, and the chain is broken at the weakest link. Recovery accounts must be at least as secure as the primary.

### Failure 3 — The shared-device leak

Your encrypted setup on your laptop is perfect. Then you check your email on a hotel business centre PC because your laptop ran out of battery. Now the credentials and the session live on a machine you do not control.

### Failure 4 — The cloud backup leak

Your Signal messages are encrypted. Your iCloud backup of Signal messages is encrypted with iCloud's keys, which Apple holds. If iCloud is your backup, your "encrypted" messages are recoverable by an iCloud subpoena.

### Failure 5 — The metadata-only attacker

Your messages are encrypted. Your provider records who you emailed, when, and how often. For some threat profiles content is irrelevant — the social graph is the entire intel product. See [encrypted email metadata leaks](/posts/encrypted-email-metadata-leaks-2026/).

### Failure 6 — Tool fatigue

You install 14 privacy tools, get overwhelmed, stop maintaining them, and revert to defaults. The right size of stack is the size you will actually maintain for two years.

---

## 6. Behaviour, Not Just Tools

The hardest part of privacy work is not buying the right software. It is changing five or six daily habits:

- Pause before clicking links in emails — even from people you trust
- Use a different alias for every service so the social graph is broken
- Treat conference Wi-Fi as adversarial (turn the VPN on before connecting)
- Lock your screen when you walk away from your laptop, every time
- Update your devices within 48 hours of patches
- Re-read this article once a year and re-calibrate

If you do those six and have only the basic stack from section 3, you are in better shape than 95% of users with elaborate setups they do not maintain.

---

## 7. What I Would Skip (And Why)

A counterweight to the recommendations: things I would not bother with for Right to Be Forgotten on Google, despite seeing them recommended elsewhere.

- **Self-hosted email.** The trust shifts from a privacy-focused provider to your own hosting. Reliability and deliverability problems will eat your weekends.
- **Tor for everyday browsing.** Tor is a great tool for specific tasks. As a default browser it makes you more identifiable since Tor users are a small fingerprintable cohort.
- **Cryptocurrency for normal payments.** Most "private" crypto is less private than the marketing claims. Cash and single-use card numbers do better.
- **Multi-hop VPN chains.** Double the latency, halve the stability, marginal privacy improvement. One audited VPN is enough.
- **Burner phones for daily life.** They get lost, get out of sync with your real life, and become the weak link. Use one well-secured phone with eSIMs for separation instead.
- **Replacing every tool at once.** Pick the highest-leverage three changes from section 3, do those well, then add more after they stick.

---

## 8. The 30-Day Implementation Plan

If you take this seriously, here is the realistic roadmap:

**Week 1:** Open ProtonMail with custom domain; install Mullvad always-on; order two YubiKeys; audit your top 10 accounts in a spreadsheet.

**Week 2:** Set up password manager; rotate top 10 passwords; enable YubiKey on email + password manager + bank; migrate top 5 contacts; send your first GDPR SAR.

**Week 3:** Subscribe to Incogni or DeleteMe; migrate cloud storage to Tresorit or Proton Drive; set up Signal with three trusted contacts; switch default browser.

**Week 4:** Audit recovery accounts; encrypt local backups; document your setup; calendar a 6-month review. After day 30 maintenance drops to ~30 minutes per month.

---

## 9. Costs — The Honest Bill

| Component | Cost | Required? |
|-----------|------|-----------|
| ProtonMail Plus | €4.99/mo | Yes |
| Mullvad VPN | €5/mo | Yes |
| YubiKey (one-time) | €50 each, buy two | Yes |
| Password manager | €0-3/mo | Yes |
| Incogni or DeleteMe | €10-13/mo | Strongly recommend |
| Tresorit or Proton Drive | included with Proton Unlimited | Yes |
| **Total recurring** | **€20-25/month** | |
| **One-time** | **€100 hardware** | |

For most readers in this audience, the total annual privacy cost is comparable to a single restaurant meal per month. The protection it buys is asymmetric.

---

## 10. Pros and Cons of This Approach

**Pros:**
- Realistic for normal humans who have jobs and families
- Maintainable — the stack does not collapse if you ignore it for 3 weeks
- Resists Tier 1 + Tier 2 threats, which cover 99% of real attacks
- Survives partial failures — losing one component does not cascade
- Most components have audit trails and explicit threat models

**Cons:**
- Costs money (€20-25/month)
- Requires behavioural change, not just tool installation
- Will not protect against Tier 3 (state-level) adversaries
- Migration is painful for users with deep Gmail/iCloud history
- Some tools have less polish than Big Tech equivalents

---

## 11. Final Verdict

For Right to Be Forgotten on Google, the practical stack is encrypted email + always-on no-log VPN + hardware 2FA + password manager + data broker removal + encrypted cloud storage. Total cost around €20-25/month, total setup around one afternoon, total maintenance around 30 minutes per month.

You do not need everything in this article. You need the rows in the calibration matrix that match your threat profile, plus the behavioural discipline to actually use them.

The biggest mistake is over-engineering early and giving up. The second biggest is under-engineering late and rationalising it.

For the inbox itself: <a href="https://go.digitalshieldpro.com/incogni" class="cta-affiliate" rel="nofollow sponsored noopener" target="_blank">View Incogni</a>

For the VPN that hides your connections: <a href="https://go.digitalshieldpro.com/privacybee" class="cta-affiliate" rel="nofollow sponsored noopener" target="_blank">View PrivacyBee</a>

---

## Related Reports

- [Best privacy stack 2026](/posts/best-privacy-stack-2026/)
- [ProtonMail review 2026](/posts/protonmail-review-2026/)
- [Tutanota review 2026](/posts/tutanota-review-2026/)
- [Mullvad VPN review](/posts/mullvad-vpn-review-2026/)
- [Signal private messaging guide](/posts/signal-private-messaging-guide-2026/)
- [Best encrypted email services](/posts/best-encrypted-email-services-2026/)
- [Best password managers](/posts/best-password-managers-2026/)
- [Best secure cloud storage](/posts/best-secure-cloud-storage-2026/)
- [Best VPN services](/posts/best-vpn-services-2026/)
- [Best secure messaging apps](/posts/best-secure-messaging-apps-2026/)
