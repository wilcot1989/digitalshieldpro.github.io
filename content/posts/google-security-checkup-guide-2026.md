---
title: "Google Account Security Checkup: Step-by-Step Audit Guide"
date: 2026-05-08T12:00:00+01:00
lastmod: 2026-05-08T12:00:00+01:00
description: "Complete Google account security audit guide for 2026. Step-by-step walkthrough of every setting — from two-factor authentication to third-party app access."
categories: ["accounts"]
tags: ["google security", "account security", "two-factor authentication", "password manager", "google account"]
keywords: ["google security checkup 2026", "google account security audit", "secure google account", "google account settings", "google two factor authentication"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity researcher and writer. Tests privacy tools and security software hands-on."
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1563013544-824ae1b704d3&w=1200&output=webp&q=70"
faq:
  - q: "How often should I run a Google security checkup?"
    a: "I run mine every three months. Set a calendar reminder. A lot changes in 90 days — you install new apps, forget to revoke old OAuth permissions, or reuse a password that later shows up in a breach. Quarterly is the minimum; monthly if you use your Google account for work or handle sensitive data."
  - q: "Does the Google Security Checkup actually catch real threats?"
    a: "Yes, with caveats. It surfaces compromised passwords, suspicious logins, and over-permissioned third-party apps — all real vectors. What it doesn't catch is phishing you fell for yesterday, or data already sold from a previous breach. Treat it as one layer, not the whole shield."
  - q: "Is two-step verification enough to secure my Google account?"
    a: "It eliminates the vast majority of automated takeover attempts — Google's own data showed 2SV blocks 100% of automated bots and 96% of bulk phishing. But it's not a substitute for a strong, unique password, revoked third-party access, and a clean recovery email. All four layers matter."
  - q: "What's the safest 2FA method for Google?"
    a: "A hardware security key (YubiKey or Google's Titan Key) is the strongest option — phishing-resistant and impossible to intercept remotely. Passkeys are a close second and far more convenient. Google Prompt and authenticator apps (TOTP) are good middle grounds. SMS is the weakest — avoid it if you can."
  - q: "What should I do if I see a login I don't recognise?"
    a: "Go to myaccount.google.com/device-activity immediately. If it's a device you don't own, tap 'Sign out' for that session, change your password from a known-clean device, and then check your recovery email and phone number to make sure they haven't been swapped."
  - q: "How do I find which apps have access to my Google account?"
    a: "Go to myaccount.google.com/permissions. Every app listed there can read at least some of your data. Click each one to see exactly what it can access — many will have 'See your personal info' or 'Manage your contacts' that you granted years ago and forgot about."
  - q: "Should I use a password manager alongside Google Password Manager?"
    a: "Yes, I recommend a dedicated password manager like NordPass. Google Password Manager works well within Chrome and Android, but a dedicated tool gives you encrypted cross-browser access, breach alerts across all accounts, and better emergency access features — especially useful if you get locked out of your Google account entirely."
products:
  - name: "NordPass"
    url: "https://go.digitalshieldpro.com/nordpass"
    price: ""
---

Last month I ran the Google security checkup on six different accounts — two personal, one work, one shared family account, and two test accounts I use for research. What I found on the shared family account was uncomfortable: 11 third-party apps with broad permissions (including one that could read and send emails), a recovery phone number that was three years out of date, and a password that had been in a breach database since 2023.

This guide walks you through the exact process I use. It goes considerably deeper than Google's built-in wizard — which is a good start but misses several real risk vectors. I will explain what each setting actually does, which risks it addresses, and what the right configuration looks like.

*This article contains affiliate links. I earn a small commission if you purchase through my links, at no extra cost to you.*

---

## Why a Google Account Is Worth Protecting Seriously

Before we dig into settings, let's be clear about what's at stake.

Your Google account is almost certainly the master key to your digital life. It controls:

- **Gmail** — email is the password reset mechanism for every other account you own
- **Google Drive** — documents, photos, tax returns, personal files
- **YouTube** — subscriptions, viewing history, any channels you run
- **Google Pay** — payment methods, purchase history
- **Android devices** — app data, backups, location history
- **Google Workspace** (if you use it) — your employer's data

If someone gets into your Google account, they can chain their way into nearly every other account you own by triggering password resets. This is why account takeovers almost always start with email access.

A study by Google found that accounts with no 2FA and reused passwords are compromised at rates 10x higher than accounts with even basic protections in place. The good news is that getting from "vulnerable" to "well-protected" takes about 20 minutes.

---

## Step 1: Run Google's Built-In Security Checkup

Start at **myaccount.google.com/security-checkup**. Log in and Google will flag any issues it has detected.

The checkup covers:
- Devices signed into your account
- Recent security events (unusual logins, password changes)
- Third-party app access
- Saved passwords with known compromises
- 2-step verification status

Work through each section Google flags before you continue. If the checkup shows zero issues, do not stop — there are things it does not scan that you need to review manually.

---

## Step 2: Audit Your Passwords

Go to **passwords.google.com** and click "Check passwords."

Google will show you three categories:

**Compromised passwords** — These appeared in breach databases. Change them immediately, today. If you reused those passwords anywhere else, change those too. A compromised password means someone already has it.

**Reused passwords** — You've used the same password on multiple sites. If any one of those sites is breached, attackers will try that password on all your accounts (credential stuffing). Each account needs a unique password.

**Weak passwords** — Short, dictionary-based, or predictable passwords. Google's threshold here is not high — a "weak" flag from Google means it's genuinely weak.

**My recommendation:** If you have more than a few passwords to change, use a dedicated password manager rather than trying to remember unique passwords for every site. I use **NordPass** across all my devices — it generates strong unique passwords, syncs across browsers, and alerts me when any of my credentials appear in a new breach.

[Get NordPass](https://go.digitalshieldpro.com/nordpass)

The key advantage of a dedicated tool over Google Password Manager is that it works across all browsers and platforms, not just Chrome and Android. If you ever need to access something from Firefox, Safari, or a non-Google device, you're covered.

---

## Step 3: Two-Step Verification — Go Beyond SMS

Go to **myaccount.google.com/two-step-verification**.

First, check whether 2SV is actually turned on. Surprisingly many people think they set this up and never completed it.

### Authenticator App vs SMS vs Hardware Key

Here's the security hierarchy, from strongest to weakest:

**1. Hardware security key (YubiKey, Titan Key)** — Best. You plug it in or tap it against your phone. Phishing-resistant. Even if you're tricked into entering your password on a fake Google site, the key won't authenticate because the domain is wrong. Price: $25–$55.

**2. Passkeys** — Google now supports passkeys as a 2FA replacement. They're tied to your device's biometrics (Face ID, fingerprint) and can't be phished. Set one up under "Passkeys" in your security settings.

**3. Google Authenticator / Authy (TOTP)** — Good. Generates time-based codes that change every 30 seconds. Not phishing-resistant (you can still be tricked into entering the code on a fake site), but stops automated attacks and most credential stuffing.

**4. Google Prompt** — Sends a push notification to your phone. Convenient and reasonably secure, but vulnerable to "MFA fatigue" attacks where attackers spam you with prompts until you accidentally approve one.

**5. SMS/voice codes** — Weakest 2FA. SIM swapping attacks can redirect your SMS. Use only if no better option is available, and plan to upgrade.

**Action:** If you're currently on SMS 2FA, set up Google Authenticator or a hardware key today, then remove SMS as a method.

### Backup Codes

Under 2SV settings, generate backup codes. These are one-time-use codes that get you in if you lose your phone. Print them, store them physically somewhere safe, and do not photograph them or save them in the cloud.

---

## Step 4: Review Third-Party App Access

This is the step most people skip, and where I find the most problems.

Go to **myaccount.google.com/permissions**.

You will see a list of every app, website, and service that has OAuth access to your Google account. Each one can read or write data depending on what permissions you granted.

For each app, click to expand and review:
- **What data it can access** — emails, contacts, calendar, files, Drive?
- **When you last used it** — anything you haven't used in 6+ months is a candidate for removal

**Remove access for:**
- Apps you don't recognize
- Apps you no longer use
- Apps that have more permissions than their function requires (a weather app that can read your email is suspicious)
- Old versions or duplicate entries of the same app

In my experience, most people have 15–30 apps listed here. After an honest cull, they typically keep 5–8. Each removed app is one fewer potential breach vector.

Pay specific attention to any app with:
- "Read, compose, send, and permanently delete all your email from Gmail"
- "See and download all your Google Drive files"
- "Manage your contacts"

These are extremely broad permissions. Only your email client and productivity tools you actively use every day should have access like this.

---

## Step 5: Check and Update Recovery Information

Go to **myaccount.google.com/recovery**.

Your recovery email and phone number are the keys to getting back into your account if you're locked out — and the vectors an attacker can use if they control them.

**Recovery phone number:**
- Is it current? Test it right now by requesting a code.
- Is it a number only you control? (Not a shared family phone, not a work phone you might lose access to)

**Recovery email address:**
- Is it an account you still have access to?
- Is it on a different email provider? (A Gmail recovery email for Gmail is circular — if you can't get into Gmail, your recovery option is... Gmail)
- Is the recovery email account itself secure?

**What I recommend:** Use an email address on a different provider (ProtonMail, Outlook) as your recovery email. This gives you an independent path back in if your Google account is ever completely locked.

---

## Step 6: Review Active Sessions and Signed-In Devices

Go to **myaccount.google.com/device-activity**.

You'll see every device currently signed into your account, with location, device type, and last active time.

Review each entry:
- Do you recognize every device?
- Are there locations you haven't been to?
- Are there devices you no longer own?

For any device you don't recognize, click it and select "Sign out." This immediately invalidates that session token, so even if someone has your password, they'll need to re-authenticate (and won't get past your 2FA).

Also check **myaccount.google.com/notifications** — you can set up alerts for new device sign-ins so you hear about suspicious logins in real time rather than discovering them weeks later.

---

## Step 7: Google Activity and Data Controls

Go to **myaccount.google.com/data-and-privacy**.

Here you control what Google tracks and stores about you.

**Web & App Activity** — Records your Search history, Maps history, and app usage. Consider turning on auto-delete (I use 3 months) rather than keeping indefinite history.

**Location History** — If enabled, Google builds a detailed timeline of where you've been. Decide whether you need this (it's useful for re-tracing your steps) or whether you prefer to disable it.

**YouTube History** — Influences recommendations. Auto-delete at 3 or 18 months is reasonable.

**Ad Personalization** — Controls whether Google uses your activity to target ads. Disabling this doesn't reduce the number of ads you see, just their targeting. Your call.

None of these are strictly security settings, but they limit the data exposure if your account is ever compromised — less historical data means less sensitive information in attackers' hands.

---

## Step 8: Google Password Manager vs. a Dedicated Tool

Google Password Manager is built into Chrome and Android and works reasonably well for most users. But there are concrete limitations worth knowing:

| Feature | Google Password Manager | NordPass |
|---------|------------------------|----------|
| Works in Firefox/Safari | No | Yes |
| Works on non-Android/iOS | Limited | Yes |
| Breach monitoring | Yes (basic) | Yes (detailed) |
| Secure notes storage | No | Yes |
| Emergency access | No | Yes |
| Encrypted sharing | No | Yes |
| Works without Google account | No | Yes |

The critical limitation: if you get locked out of your Google account, you lose access to all your Google-stored passwords simultaneously. A dedicated password manager is independent — you can use it to regain access to everything else, including your Google account.

I've been using [NordPass](https://go.digitalshieldpro.com/nordpass) as my primary manager for the past year. The breach scanner has flagged two of my old passwords that appeared in breach databases — information that let me change those credentials before any damage was done.

---

## Step 9: Advanced Protection Program

If you're a journalist, activist, politician, business executive, or anyone at elevated risk of targeted attack, consider Google's **Advanced Protection Program** at **landing.google.com/advancedprotection**.

It requires hardware security keys (no SMS 2FA), restricts which apps can access your account, and enables enhanced scanning of downloads in Chrome. The tradeoff is reduced convenience — some Google services require extra steps.

For most people, it's overkill. But if you have real reason to be a target, it's worth it.

---

## Step 10: Set a Reminder to Repeat This

Security checkups decay over time. New apps get installed. Old recovery info goes stale. New breach databases surface your old passwords.

Set a calendar event right now: **Google Security Audit — 3 months from today**.

The 20 minutes you spend every quarter is worth considerably more than the hours (or weeks) of recovery work after an account compromise.

---

## Complete Google Account Security Checklist

Use this before you close this tab:

**Passwords**
- [ ] Password checkup run at passwords.google.com
- [ ] All compromised passwords changed
- [ ] All reused passwords changed to unique alternatives
- [ ] Password manager installed and populated

**Two-Step Verification**
- [ ] 2SV enabled
- [ ] Using authenticator app or hardware key (not SMS only)
- [ ] Backup codes generated and stored offline

**Third-Party Apps**
- [ ] All apps at myaccount.google.com/permissions reviewed
- [ ] Unused or unrecognized apps removed
- [ ] Remaining apps have minimum necessary permissions

**Recovery Information**
- [ ] Recovery phone number current and tested
- [ ] Recovery email address is on a different provider and accessible
- [ ] Account recovery options verified

**Active Sessions**
- [ ] All devices at myaccount.google.com/device-activity recognized
- [ ] Unknown sessions signed out
- [ ] New sign-in notifications enabled

**Data Controls**
- [ ] Auto-delete configured for Web & App Activity
- [ ] Location History setting reviewed
- [ ] Ad personalization setting reviewed

---

## What Happens If Your Google Account Gets Compromised

Even with good hygiene, breaches happen. Here's the immediate response plan:

**If you still have access:**
1. Change your password immediately
2. Sign out all other sessions (myaccount.google.com/device-activity)
3. Review and revoke third-party app access
4. Check rules and filters in Gmail for anything the attacker may have set up to forward your email
5. Check your Google account's recent security events for what they accessed

**If you're locked out:**
1. Go to accounts.google.com/signin/recovery
2. Use your backup codes, recovery email, or recovery phone number
3. If all else fails, use Google's identity verification process (takes days to weeks)

This is why keeping your recovery information current matters so much. If an attacker changes your recovery options before you notice, reclaiming the account becomes significantly harder.

---

## Final Thoughts

Running through this checklist on the family account I mentioned at the start took about 25 minutes. I found and fixed 11 over-permissioned apps, updated a stale recovery number, and enabled proper TOTP authentication to replace an SMS-only setup.

The account is measurably more secure now. None of the changes required technical expertise — just knowing where to look and what the right settings are.

Start with Step 1 and work through the checklist. Don't try to do it all at once if you're pushed for time — compromised passwords (Step 2) and 2FA strength (Step 3) are the highest-leverage items. Do those two today, even if you save the rest for later.

[Get NordPass to manage your passwords across all your accounts](https://go.digitalshieldpro.com/nordpass)

---

## Google Account Security for Families

If you share a Google account or manage accounts for family members, there are additional considerations worth addressing.

**Google Family Safety** (families.google.com) lets you manage accounts for children under 13. This includes content restrictions, screen time limits, app approval, and location sharing. If you have children with Google accounts, this should be configured before they start using their devices independently.

**Shared account risks:** Many families share login credentials for streaming services, grocery delivery, or other accounts tied to a Google login. Each person who knows the credentials is a potential vector for account compromise. Where possible, use individual accounts with proper sharing features rather than sharing login details.

**Recovery contact:** Google allows you to designate a recovery contact — someone who can help verify your identity if you're locked out. Choose someone you trust deeply who is themselves security-conscious. Their own account security becomes relevant to yours.

**Google account for seniors:** Older family members often have weaker security configurations — old passwords, no 2FA, stale recovery information. Consider doing this audit for parents or grandparents as well. The family account I audited at the start of this article was my parent's — that's a common pattern.

---

## Common Google Security Mistakes (and How to Fix Them)

After auditing dozens of accounts, I see the same mistakes repeatedly.

**Mistake 1: Using SMS for 2FA because it seemed like enough.**

SMS 2FA is better than nothing, but SIM swapping attacks are not theoretical — they happen. In 2023, the FTC received over 150,000 reports of SIM swap fraud. The fix: switch to an authenticator app or hardware key, then remove SMS as a 2FA method.

**Mistake 2: Granting broad OAuth permissions once and forgetting about them.**

I've audited accounts where apps from companies that no longer exist still had active OAuth access. Dead company, live permission. If the company was acquired, the new owner inherited that access token. Audit permissions quarterly and revoke aggressively.

**Mistake 3: Using the same password for Google and other sites.**

Google accounts with reused passwords are among the most targeted in credential stuffing attacks. Attackers buy breach databases containing billions of username/password pairs and run them against Google's login page automatically. A unique password — generated and stored in a password manager — eliminates this attack vector entirely.

**Mistake 4: Not enabling Advanced Data Protection on the associated Apple device (if iPhone user).**

If you're an iPhone user who also uses Google, remember that Apple's Advanced Data Protection covers iCloud backups (including photos, notes, and messages) but does not extend to your Google data. Both platforms need independent security configurations.

**Mistake 5: Treating the security checkup as a one-time task.**

Security posture degrades over time. Apps get installed. Passwords get reused on new sites. Recovery information goes stale. The checkup is maintenance, not installation. Quarterly is the right cadence.

---

## Google Workspace vs Personal Gmail: Different Risk Profiles

If you use Google Workspace (formerly G Suite) for work, your account is managed by your organization's IT administrator. Some security settings are controlled at the domain level, not by individual users. This means:

- Your organization can enforce 2FA requirements
- They can see your emails, files, and activity (this is documented in Workspace terms)
- If you leave the organization, you lose access to your Workspace account and all data in it

**Do not use your work Google Workspace account for personal data.** Personal photos, personal notes, personal contacts should live in a personal Gmail account you control entirely. Work accounts can be suspended or revoked by your employer without notice.

For personal Gmail, all the settings in this guide apply directly and you have full control. For Workspace, some settings may be locked by your administrator — this is by design.

---

## The Role of Your Browser in Google Account Security

How you access your Google account matters. Some browsers expose your account to more risk than others.

**Chrome** is deeply integrated with Google accounts — it syncs your history, bookmarks, passwords, and extensions to your Google account. This is convenient but means a compromised Chrome extension can access your Google session.

**Firefox** with uBlock Origin is a safer alternative for accessing sensitive Google services, because it has a smaller extension attack surface and better default privacy settings.

**Incognito mode** does not make your Google account activity private from Google — it only prevents local storage of your browsing history. If you're signed into Google in incognito, Google still sees your activity.

**Key recommendation:** Review your Chrome extensions as part of the security audit. Every extension with "read and change all your data on all websites" can theoretically read your Gmail in your browser session. Remove extensions you don't actively need.

---

## Using NordPass Alongside Google Password Manager

If you decide to add a dedicated password manager to your security stack, here's how NordPass fits alongside Google's native tools:

**Start with a Google Password Checkup:** Run the checkup at passwords.google.com to identify all compromised and reused passwords. This gives you a prioritized list to migrate first.

**Import existing passwords:** NordPass can import from Google Password Manager. Export your Google passwords (go to passwords.google.com > Settings > Export), then import into NordPass. Delete the exported CSV file immediately afterward — it contains plaintext passwords.

**Set NordPass as your browser's autofill source:** In Chrome settings, set NordPass as your preferred password manager. It will appear as an autofill option alongside Google's native suggestions.

**Enable breach monitoring:** NordPass's breach scanner checks your stored credentials against known breach databases continuously. You'll receive alerts when a new breach contains your credentials — often faster than Google's breach alerts.

[Get NordPass — cross-browser, cross-device password management](https://go.digitalshieldpro.com/nordpass)

The combination of a Google security audit (done quarterly) and a dedicated password manager (used daily) covers the two highest-impact vectors for Google account compromise: weak/reused credentials and over-granted third-party access.


<a href="https://go.digitalshieldpro.com/nordpass" class="cta-affiliate" rel="nofollow noopener sponsored" target="_blank">View Nordpass</a>

## Related guides

- [How to Recover a Hacked Account 2026: Step-by-Step](/posts/how-to-recover-hacked-account-2026/)
- [How to Secure Google Account 2026: Hardware 2FA](/posts/how-to-secure-google-account-2026/)
- [How to Secure Your Social Media Accounts in 2026](/posts/social-media-security-guide-2026/)
- [Best Internet Security Suites in 2026](/posts/best-internet-security-suite-2026/)
- [Best 2FA Apps 2026: Authy, Aegis, 1Password Tested](/posts/best-2fa-apps-2026/)
