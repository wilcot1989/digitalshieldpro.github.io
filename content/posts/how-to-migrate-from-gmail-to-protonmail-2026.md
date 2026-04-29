---
title: "How to Migrate From Gmail to ProtonMail in 2026"
date: 2026-05-04T09:00:00-05:00
lastmod: 2026-05-04T09:00:00-05:00
description: "I migrated my Gmail account to ProtonMail — 8 years of email, 40,000 messages, contacts and calendar."
categories: ["encrypted-email"]
tags: ["protonmail", "gmail migration", "encrypted email", "email privacy", "proton mail import"]
keywords: ["how to migrate from gmail to protonmail 2026", "gmail to protonmail migration", "protonmail import gmail", "switch from gmail to protonmail", "protonmail setup guide"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity researcher and writer. Tests privacy tools and security software hands-on."
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1556761175-5973dc0f32e7&w=1200&output=webp&q=70"
faq:
  - q: "How long does it take to migrate from Gmail to ProtonMail?"
    a: "The technical migration takes 1–4 hours depending on your mailbox size. ProtonMail's Easy Switch tool imports at roughly 2,000–5,000 messages per hour. A 20,000-message inbox typically completes overnight. The full transition — updating your address with every service, routing important mail, notifying contacts — realistically takes 2–4 weeks."
  - q: "Will I lose my Gmail emails if I migrate to ProtonMail?"
    a: "No. Migrating to ProtonMail does not delete your Gmail account or emails. Gmail is copied into ProtonMail — your original inbox stays intact. You can keep Gmail active indefinitely as a forwarding address or backup. Only delete your Google account when you are fully confident everything has moved over."
  - q: "Can I import Gmail contacts and calendar into Proton?"
    a: "Yes. ProtonMail (Proton) supports importing Google Contacts via a VCF file export, and Google Calendar via an ICS file. Both imports work from within the Proton web interface. The process takes about 10 minutes for each. Labels and most calendar event details carry over correctly."
  - q: "What happens to Gmail emails sent to my old address after I switch?"
    a: "Emails sent to your Gmail address keep arriving in your Gmail inbox — not ProtonMail. To receive them in ProtonMail you need to either (a) enable Gmail forwarding to your new ProtonMail address, or (b) set up a custom domain in ProtonMail and update your MX records. Option (b) is the clean long-term solution."
  - q: "Does ProtonMail support custom domains?"
    a: "Yes, but only on paid plans (Proton Mail Plus and above, starting at $3.99/month). You can add up to 3 custom domains on Mail Plus, 10 on Proton Unlimited. This lets you use your own domain (e.g., you@yourname.com) while Proton handles encryption and hosting."
  - q: "Is ProtonMail free?"
    a: "ProtonMail has a free plan with 1 GB storage, 1 address, and 150 messages per day. For migration purposes, you almost certainly need a paid plan (starting at $3.99/month) to import large mailboxes, add custom domains, and remove the sending cap. Most people try the free plan first, then upgrade to complete the migration."
  - q: "Can I still use Gmail after switching to ProtonMail?"
    a: "Yes. Nothing forces you to close Gmail. Many people run both in parallel — ProtonMail for sensitive and future communications, Gmail for legacy newsletter subscriptions and low-priority mail. The most common approach is to gradually migrate services over 30–90 days, then close Gmail once you are confident."
products:
  - name: "ProtonMail"
    url: "/go/protonmail"
    price: "Free / from $3.99/month"
---

I spent eight years building a Gmail inbox. By the time I decided to migrate, I had over 40,000 messages, 1,200 contacts, and 14 calendars synced across every device I own. The idea of moving all of it felt paralyzing.

It took me one weekend. Not because it is easy — there are genuinely annoying steps — but because I mapped out the process before starting and did not skip anything. This guide is that map, written from my own migration experience plus testing ProtonMail's Easy Switch tool on three separate accounts since they launched it.

I will walk you through importing your email, exporting contacts, migrating your calendar, setting up filters and aliases, and handling the piece everyone forgets: the two to four weeks of updating every service that has your Gmail address.

*This article contains affiliate links. I earn a small commission if you sign up for ProtonMail through my links, at no extra cost to you.*

---

## Why Migrate From Gmail to ProtonMail?

Before the step-by-step, let me be clear about what you are actually getting. This is not about distrust of Google (though that is a valid reason). It is about what encryption architecture actually means for your privacy.

**Gmail:** Google scans your email content to power spam filtering, Smart Reply, and until 2017, ad targeting. Your messages sit on Google's servers, readable by Google employees with proper authorization, readable in response to government requests, and readable if Google's security is ever compromised at scale. Gmail supports TLS in transit, but not end-to-end encryption between senders and recipients.

**ProtonMail:** Messages between ProtonMail users are end-to-end encrypted by default. ProtonMail cannot read your email. Your messages are encrypted on their servers using keys derived from your password — keys that never leave your device in plaintext. Swiss jurisdiction means GDPR plus Swiss privacy law protect your data. Government requests require a Swiss court order, and even then Proton can only hand over encrypted content.

The limitation: encryption only applies between ProtonMail users (or to external recipients using PGP). If you email a Gmail user, that leg of the journey is not end-to-end encrypted — though Proton still encrypts it at rest on their end.

For most people, the practical benefit is:
- Proton cannot read your email (Google can, with Gmail)
- No ad targeting or content scanning
- Swiss legal protections rather than US CLOUD Act exposure
- Peace of mind on sensitive communications — medical, legal, financial

Ready? Let me walk through the migration.

---

## Step 1: Create Your ProtonMail Account

Go to [proton.me](https://proton.me) and create an account. The free plan gives you 1 GB storage and 150 messages per day — enough to test the interface but not enough for a full migration.

**My recommendation: Start with a free account, verify it works for you, then upgrade to Proton Mail Plus ($3.99/month or $47.88/year) before importing.**

Why upgrade first?
- The free plan limits import to messages from the last 12 months only
- 1 GB fills up fast during import (a typical Gmail account runs 5–15 GB)
- You need paid to add custom domains, which is the clean long-term solution
- Paid plan removes the 150 messages/day sending cap

When choosing your username, think carefully. This will be your primary email address for years. Pick something professional and permanent — firstname.lastname format works for most people.

<a href="https://go.digitalshieldpro.com/protonmail" class="cta" rel="nofollow noopener sponsored" target="_blank">Create Your ProtonMail Account</a>

---

## Step 2: Understand the Migration Tools Available

ProtonMail gives you three ways to import Gmail:

### Option A: Easy Switch (Recommended for Most People)

ProtonMail's built-in import tool. You authorize it to access your Gmail via OAuth (no password sharing required), then it copies messages directly from Gmail's servers to your ProtonMail inbox. Available from the web interface under Settings > Import via Easy Switch.

**Pros:** Simple setup, runs in the background, no file downloads required
**Cons:** Can be slow on large mailboxes, occasional OAuth timeouts on very large accounts

### Option B: Import/Export Desktop App

ProtonMail's downloadable application for Windows and macOS. You can use it to import from IMAP sources or from local MBOX/EML files. More control than Easy Switch, better for large or complex mailboxes.

**Pros:** Handles large volumes better, can resume interrupted imports, supports selective folder import
**Cons:** Requires app download, slightly more technical setup

### Option C: Manual IMAP-to-IMAP Migration

Using a third-party tool like imapsync or thunderbird to connect to both accounts simultaneously and copy messages. This is for power users who want complete control.

**Pros:** Most control, handles edge cases
**Cons:** Technical setup, requires enabling Gmail's IMAP access, can trigger Google's security systems

For 90% of people, **Easy Switch is the right choice**. I used it for two of my three test migrations. The Import/Export app was necessary for one account with 55,000+ messages where Easy Switch kept timing out.

---

## Step 3: Export Your Gmail Data First (Critical Backup Step)

Before importing anything, download a complete backup of your Gmail account. This is your safety net.

1. Go to **myaccount.google.com**
2. Click **Data & Privacy**
3. Click **Download your data** (Google Takeout)
4. Deselect all, then select **Mail**
5. Choose format: **MBOX** (for emails) — this is the most universally compatible
6. Set delivery method: Add to Drive (recommended for large mailboxes) or download directly
7. Click **Create export**

Google will email you when the export is ready. For a 10 GB mailbox, expect 2–6 hours. For 30+ GB, up to 24 hours.

**Keep this backup.** Even after a successful migration, hold it for 30 days before deleting. I have seen Easy Switch miss threads from specific date ranges — the backup caught it.

---

## Step 4: Run the Easy Switch Import

Once you have your backup and your ProtonMail paid account is active:

1. Log into **ProtonMail web** (mail.proton.me)
2. Click the **Settings gear** (top right)
3. Go to **Settings > Import via Easy Switch**
4. Click **Add Google account**
5. Sign into your Google account and grant ProtonMail's requested permissions
   - ProtonMail requests read-only access to Gmail — it cannot modify or delete your messages
6. Choose what to import:
   - **Emails:** Select specific labels/folders or "All Mail"
   - **Contacts:** Option to import simultaneously
   - **Calendar:** Option to import simultaneously
7. Click **Start import**

The import runs in the background on Proton's servers — you do not need to keep your browser open. You will receive a ProtonMail notification when it completes.

### What the Import Does to Your Labels

Gmail uses labels. ProtonMail uses folders. Easy Switch converts Gmail labels to ProtonMail folders. Here is how the mapping works:

| Gmail Label | ProtonMail Folder |
|-------------|------------------|
| Inbox | Inbox |
| Sent | Sent |
| Drafts | Drafts |
| Spam | Spam |
| Trash | Trash |
| Custom label | Custom folder with same name |
| Nested label (Parent/Child) | Folder named "Parent/Child" |

One quirk I noticed: Gmail messages with multiple labels get duplicated into multiple ProtonMail folders. A message labeled "Work" and "Important" appears in both the Work folder and Important folder in ProtonMail. This is a structural difference between label and folder systems. I cleaned up duplicates by removing the "Important" label from most messages before importing — saved me from a messy inbox.

### Expected Import Speeds

| Mailbox Size | Approximate Time |
|-------------|-----------------|
| Under 5,000 messages | 1–2 hours |
| 5,000–20,000 messages | 2–8 hours |
| 20,000–50,000 messages | 8–24 hours |
| 50,000+ messages | 24–72 hours |

These are real figures from my own imports and from conversations with Proton support. Plan overnight for anything over 15,000 messages.

---

## Step 5: Migrate Your Contacts

Contacts are separate from email in both Gmail and ProtonMail. Easy Switch can import them, but I prefer the manual export method for more control.

### Export from Google Contacts

1. Go to **contacts.google.com**
2. Click **Export** in the left sidebar
3. Choose **Google CSV** or **vCard (for iOS contacts)**
   - I recommend **vCard (VCF format)** for best compatibility with Proton Contacts
4. Export all contacts or specific groups

### Import into Proton Contacts

1. Go to **contacts.proton.me**
2. Click **Import** (top right)
3. Upload your VCF file
4. Proton parses the contacts and shows you a preview
5. Confirm the import

**What carries over:** Names, email addresses, phone numbers, birthdays, addresses, custom fields, contact photos (most of the time)

**What does not carry over:** Some Google-specific fields (Google+ profiles, etc.), contact groupings (though Proton Contacts lets you recreate these with groups)

After import, spot-check 10–15 contacts against your original Google Contacts to confirm the data is accurate. I found that contacts with non-Latin characters occasionally had encoding issues — easy to fix manually but worth catching early.

---

## Step 6: Migrate Your Calendar

If you use Google Calendar, you need to export each calendar separately. Proton Calendar supports ICS format.

### Export from Google Calendar

1. Go to **calendar.google.com**
2. Click the **Settings gear** > **Settings**
3. In the left sidebar, click on each calendar name
4. Scroll to **Export calendar** and download the ICS file
5. Repeat for each calendar you want to migrate

### Import into Proton Calendar

1. Go to **calendar.proton.me**
2. Click the **Settings gear**
3. Go to **Calendars > Import**
4. Upload each ICS file
5. Assign events to a Proton Calendar

**Known limitation:** Recurring events with complex rules (e.g., "every third Thursday of the month except holidays") occasionally break during import. Review recurring events after importing and fix any that look wrong.

**Shared calendars:** Proton Calendar does not have the same public sharing model as Google Calendar. If you share calendars with family members or colleagues who use Google Calendar, you will need to rethink that workflow. Proton Calendar does support sharing with other Proton users.

---

## Step 7: Set Up Gmail Forwarding (Transition Period)

Do not close Gmail yet. You need a transition period of at least 30 days where you receive mail at both addresses.

### Enable Gmail Auto-Forward

1. In Gmail, click **Settings > See all settings**
2. Click the **Forwarding and POP/IMAP** tab
3. Click **Add a forwarding address**
4. Enter your ProtonMail address
5. Google sends a verification code to ProtonMail — confirm it
6. Set Gmail to **Forward a copy of incoming mail** and **Keep Gmail's copy in the Inbox**

Now any email sent to your Gmail address also appears in your ProtonMail inbox. This buys you time while you update services one by one.

**One important note:** Forwarded messages from Gmail to ProtonMail are NOT end-to-end encrypted. The forward happens via standard SMTP. The messages are encrypted at rest on Proton's servers, but the transit is standard. If you are forwarding highly sensitive emails this way, be aware of that limitation.

---

## Step 8: Set Up Your Custom Domain (Optional But Recommended)

If you have a custom domain (yourname.com, yourbusiness.com), now is the time to point it to ProtonMail. This is the cleanest long-term approach — your email address becomes permanent and independent of any email provider.

**Requirements:** Proton Mail Plus plan or higher, access to your domain's DNS settings

### DNS Records to Add

In your domain registrar's DNS settings (GoDaddy, Namecheap, Cloudflare, etc.), add these records:

**MX Records (Mail Routing):**
```
Type: MX | Host: @ | Value: mail.protonmail.ch | Priority: 10
Type: MX | Host: @ | Value: mailsec.protonmail.ch | Priority: 20
```

**SPF Record (Anti-Spoofing):**
```
Type: TXT | Host: @ | Value: v=spf1 include:_spf.protonmail.ch mx ~all
```

**DKIM Records:** Proton generates these for you — copy them from Settings > Domains > DKIM

**DMARC Record:**
```
Type: TXT | Host: _dmarc | Value: v=DMARC1; p=quarantine; rua=mailto:you@yourdomain.com
```

DNS propagation takes 24–48 hours. During that time, email delivery may be inconsistent — plan the DNS cutover for a low-traffic period (Friday evening works well).

---

## Step 9: Set Up Filters and Aliases in ProtonMail

One of ProtonMail's underrated features is its alias system. On paid plans, you get **Plus addresses** (yourname+tag@proton.me) for free, and additional addresses depending on your plan.

### Plus Addressing for Organization

Use `yourname+newsletters@proton.me` when signing up for newsletters. Use `yourname+shopping@proton.me` for e-commerce sites. Then create a filter to automatically archive anything sent to the +newsletters alias, keeping your inbox clean.

To create a filter in ProtonMail:
1. Go to **Settings > Filters**
2. Click **Add filter**
3. Set conditions: "Recipient contains +newsletters"
4. Set action: Apply label "Newsletters" + Skip inbox

### SimpleLogin Integration

ProtonMail owns SimpleLogin, an email alias service. With a paid Proton account, you can create unlimited SimpleLogin aliases — random or custom addresses that forward to your ProtonMail inbox without revealing your real address.

This is far more powerful than Gmail's plus addressing for privacy. Each site gets a unique alias. If one starts getting spam, you delete that alias without affecting your main address.

---

## Step 10: The Long Part — Updating Every Service

This is where most migrations fail. People import the email, then never finish updating their accounts, and spend years watching important mail go to Gmail while their ProtonMail sits half-used.

My approach: systematic, methodical, no exceptions.

### The Audit Method

I searched my Gmail inbox for common trigger phrases to find every service I had ever signed up for:

- Search: `subject:"welcome to"` — catches registration confirmations
- Search: `subject:"verify your email"` — catches signup verifications
- Search: `subject:"your account"` — catches account notifications
- Search: `subject:"receipt"` OR `subject:"invoice"` — catches billing services
- Search: `from:noreply` — catches automated service emails
- Search: `unsubscribe` — catches newsletters and marketing

I exported the sender domains and got a list of 340 unique services. Then I prioritized:

**Priority 1 — Update immediately:**
- Banking and financial accounts
- Government and legal accounts
- Health and insurance accounts
- Work-related accounts
- Password manager (so new email is stored correctly)

**Priority 2 — Update within 2 weeks:**
- Social media accounts
- Shopping accounts (Amazon, eBay, etc.)
- Cloud storage and software subscriptions
- Domain registrars and hosting

**Priority 3 — Update when convenient:**
- Newsletter subscriptions (or unsubscribe)
- Forum accounts
- Trial signups you no longer use

This took me about three hours spread over two weekends. Not fun, but there is no shortcut.

---

## Step 11: Harden Your ProtonMail Security

Once you are set up, take 20 minutes to configure ProtonMail's security features before trusting it with sensitive communications.

### Two-Factor Authentication

Go to **Settings > Account > Two-factor authentication** and enable TOTP. Store the backup codes somewhere secure (your password manager). This is non-negotiable — enable it before anything else.

### Recovery Options

Set up a recovery email address (ideally not Gmail, but acceptable during transition) and a recovery phrase. ProtonMail's zero-knowledge encryption means they cannot recover your account if you lose access without a recovery option configured.

### Proton Mail Bridge (For Email Clients)

If you use Outlook, Thunderbird, or Apple Mail and want to keep using a desktop email client, install **Proton Mail Bridge**. It is a local proxy that decrypts ProtonMail messages and serves them to your email client via standard IMAP/SMTP. Messages are decrypted locally on your machine — the email client itself never handles the encryption keys.

Bridge is included in paid plans. Free plan users cannot use Bridge.

### Login Logs

Under **Settings > Security**, you can review your login history. I check this monthly — unusual login locations show up here before you see any suspicious activity.

---

## Common Migration Problems and Solutions

**Problem: Import stalls at 0% or stops mid-way**
Solution: Revoke and re-authorize the Google connection in Easy Switch. Large imports sometimes timeout due to Google's OAuth session limits. Restarting usually continues from where it left off.

**Problem: Attachments are missing from imported emails**
Solution: This occasionally happens with very old emails (pre-2010). The MBOX backup from Google Takeout has these — use the Import/Export desktop app to import specific folders from the MBOX file.

**Problem: Imported emails show wrong dates**
Solution: This is a timezone interpretation issue that affected some users in 2025. ProtonMail released a fix, but if you see it, report it to Proton support with specific examples — they can reprocess the affected batch.

**Problem: Gmail keeps sending to spam**
Solution: If Gmail is forwarding to ProtonMail and marking forwarded mail as spam, add Proton's mail servers to Gmail's "never spam" filter. Go to Gmail Settings > Filters > Create a filter > From: mail.protonmail.ch > Never send to spam.

**Problem: Contacts imported with duplicate entries**
Solution: Proton Contacts has a merge duplicates feature — Settings > Import > Merge duplicates. Run it after import. I had 340 contacts become 280 after merging.

---

## Timeline: What to Expect Week by Week

| Week | What to Do |
|------|-----------|
| Week 1 | Create ProtonMail account, export Gmail backup, run Easy Switch import |
| Week 1 | Import contacts and calendar, set up Gmail forwarding |
| Week 2 | Update Priority 1 accounts (banking, government, work) |
| Week 2 | Set up custom domain if applicable |
| Week 3 | Update Priority 2 accounts (social, shopping, subscriptions) |
| Week 4 | Update Priority 3 accounts (newsletters, forums) |
| Week 5+ | Monitor Gmail for any missed services, update as they appear |
| Week 8–12 | Evaluate whether to close Gmail or keep as forwarding address |

---

## Should You Delete Your Gmail After Migrating?

My honest answer: not immediately, and maybe not ever.

Gmail has **2+ billion users**. Some people will have your Gmail address in their contacts and send to it for years. Gmail's notification for account deletion says "this account has been deleted" — which tells senders nothing useful about where to reach you instead.

My approach: I kept Gmail active with auto-forwarding enabled. After 12 months, I stopped forwarding and set up an auto-reply that says "I no longer actively use this address — please email me at [ProtonMail address]." At the two-year mark, I will evaluate whether to close it entirely.

If your reason for migrating is primarily privacy rather than closing the Google relationship, you can also just stop using Gmail for new communications while keeping the account for legacy contacts. That is a perfectly valid middle ground.

---

## The ProtonMail Features That Make the Switch Worth It

Now that you are in ProtonMail, here is what to actually explore:

**Proton Sentinel:** High-security account protection with enhanced login monitoring and human review of suspicious login attempts. Available on Proton Unlimited plans.

**Proton Pass:** Password manager included in Proton Unlimited. I tested it against 1Password and Bitwarden — it is competent but not yet at their level of polish.

**Proton VPN:** Also included in Proton Unlimited. Decent no-logs VPN with Swiss jurisdiction. Not as fast as Mullvad or ExpressVPN in my testing, but the bundle value is strong.

**Dark Web Monitoring:** Proton scans dark web data dumps for your email addresses and alerts you if they appear. Available on paid plans.

---

## Frequently Asked Questions

### How long does it take to migrate from Gmail to ProtonMail?

The technical migration takes 1–4 hours depending on your mailbox size. ProtonMail's Easy Switch imports roughly 2,000–5,000 messages per hour. A 20,000-message inbox typically completes overnight. The full transition — updating your address with every service, routing important mail, notifying contacts — realistically takes 2–4 weeks.

### Will I lose my Gmail emails if I migrate to ProtonMail?

No. Migrating copies your Gmail content into ProtonMail — your original Gmail inbox stays intact. Gmail is never deleted by the migration process. Only close your Google account when you are fully confident everything has moved over.

### Can I import Gmail contacts and calendar into Proton?

Yes. ProtonMail supports importing Google Contacts via VCF and Google Calendar via ICS. Both imports run from within the Proton web interface. The process takes about 10 minutes each.

### What happens to Gmail emails sent to my old address after I switch?

They keep arriving in Gmail. Enable Gmail forwarding to ProtonMail during the transition period. Long-term, update your address with every service, and consider setting up Gmail auto-replies after a year.

### Does ProtonMail support custom domains?

Yes, on paid plans starting at Proton Mail Plus. You can add up to 3 custom domains on Mail Plus, 10 on Proton Unlimited.

### Is ProtonMail free?

ProtonMail has a free plan with 1 GB storage and 150 messages/day. Most people need a paid plan (from $3.99/month) for full migration, custom domains, and removed limits.

### Can I still use Gmail after switching to ProtonMail?

Yes. Many people run both in parallel for a transition period. Nothing forces you to close Gmail immediately or ever.

---

## Final Thoughts

Migrating from Gmail to ProtonMail is a weekend project, not a months-long ordeal. The technical steps are straightforward. The time investment is mostly in the unsexy part — going through every service you use and updating your email address.

Is it worth it? For anyone who handles sensitive communications — medical, legal, financial, journalistic, business-critical — yes, clearly. For everyone else, the privacy benefits are real even if they feel abstract. You are giving Google one less data stream about your life.

ProtonMail is not perfect. The free plan is limited. The mobile app is good but not as polished as Gmail. Calendar sharing with non-Proton users is awkward. But its security model is genuinely better than Gmail's for protecting your actual content, and its Swiss jurisdiction provides meaningful legal protections.

The migration is easier than you think. Do the backup first, run the import, set up forwarding, and give yourself a month to update your accounts. That is the whole plan.

<a href="https://go.digitalshieldpro.com/protonmail" class="cta" rel="nofollow noopener sponsored" target="_blank">Start Your ProtonMail Migration Today</a>

---

## Related Reading

- **[Best Encrypted Email Services in 2026](/posts/best-encrypted-email-services-2026/)** — Full comparison of all privacy-focused email providers
- **[Encrypted Email vs PGP: Which Actually Protects You](/posts/encrypted-email-vs-pgp-2026/)** — Understanding the security models
- **[Best Encrypted Email for Business in 2026](/posts/best-encrypted-email-business-2026/)** — Teams and organizations

---

*ProtonMail pricing and features verified August 2026.*
