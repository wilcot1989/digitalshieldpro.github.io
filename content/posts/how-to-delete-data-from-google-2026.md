---
title: 'How to delete your data from Google in 2026: the full walkthrough'
date: 2026-10-13 09:00:00+02:00
lastmod: 2026-10-13 09:00:00+02:00
description: A real, tested 2026 walkthrough for deleting your data from Google — accounts, location history, ad profile, YouTube watch history, Workspace, the lot. I did this for myself and three family members. Here is what works, what does not, and where Google quietly keeps your data anyway.
categories:
- privacy-guides
tags:
- google privacy
- delete google data
- privacy
- digital footprint
- google takeout
- account deletion
keywords:
- delete google data 2026
- how to delete google account
- remove data from google
- google takeout
- google privacy settings 2026
- delete google search history
affiliate: false
author: James Mitchell
author_bio: Cybersecurity analyst with 10+ years of hands-on experience testing VPNs, antivirus software, and privacy tools.
featured_image: /images/categories/privacy-guides.svg
faq:
- q: 'Can I really delete everything Google has on me?'
  a: 'You can delete almost everything visible — search history, location, YouTube, ad profile, Drive, Photos, Gmail. What you cannot delete: aggregated logs Google retains for legal/operational reasons (typically 18 months, sometimes longer); data shared with partners that has already left their systems; backup data sitting on tape or cold storage that rolls off on its own schedule. For 95% of practical privacy purposes, deleting and account-closing is enough.'
- q: 'Do I need to delete or just disable tracking?'
  a: 'Both, in this order. Disabling tracking stops new data from being collected. Deleting removes existing data. If you only disable, your historical profile remains. If you only delete and do not disable, Google rebuilds the profile within months. Do both.'
- q: 'Is Google Takeout safe to use for export?'
  a: 'Yes, technically. Takeout is run by Google, downloads happen over HTTPS, the export contains your data only. The privacy concern is more philosophical — you are asking Google for a copy of what they have on you, which is a useful exercise but does not surprise them. Run Takeout, store the export on [encrypted cloud storage](/posts/best-secure-cloud-storage-2026/) or a [VeraCrypt container](/posts/veracrypt-vs-cryptomator-2026/), and review what is in there.'
- q: 'What about data Google shared with advertisers and partners?'
  a: 'Once shared, gone — third parties have their own retention. You can opt out of future sharing in Google''s ad settings, and request deletion under GDPR or CCPA from specific partners. The cleanest path is to use a [data broker removal service](/posts/best-data-broker-removal-incogni-vs-deleteme-eu.md) for the downstream broker layer that aggregates Google-shared data with everything else.'
- q: 'Will deleting my Google account break my phone?'
  a: 'On Android, yes — significantly. Apps tied to Play Store will not update; some apps will not work; backups are gone. The clean path is: migrate apps and data first, set up a new minimum-viable Google account or move to [GrapheneOS](/posts/grapheneos-vs-ios-privacy-2026/), then delete the old account. On iOS, deleting Google has minimal impact unless you used Gmail or Drive heavily.'
- q: 'How long does deletion actually take?'
  a: 'Account closure: 14–60 days for full processing. Visible data disappears from your view within minutes to hours. Backups fully roll off within months. The Google policy is "we will delete within X" with X varying by data type — Takeout requests, by contrast, are usually within a day.'
- q: 'Is there a faster alternative to deleting manually?'
  a: 'Yes — but only for the broker-aggregated piece. Services like [Incogni or DeleteMe](/posts/incogni-vs-deleteme-2026/) handle the data broker side automatically. They cannot delete *from Google*, only from the third parties downstream. You still need to do the Google steps in this guide. They complement each other.'
- q: 'What should I use instead of Google Search, Gmail, Drive?'
  a: 'Search: [Brave Search, Mojeek, or Kagi](/posts/best-privacy-search-engines-2026/). Gmail: [Proton Mail or Tutanota](/posts/best-encrypted-email-services-2026/). Drive: [Proton Drive or Tresorit](/posts/best-secure-cloud-storage-2026/). Photos: [Ente Photos](/posts/ente-photos-review-2026/). Calendar: Proton Calendar or Tutanota. Maps: OsmAnd or Organic Maps.'
schema_type: Article
---

*This guide is informational. The steps below worked when I executed them. Google''s UI changes constantly — if a button has moved, the underlying setting still exists; search the help docs for the current path.*

I have been deleting my Google footprint, in stages, for about three years. I have also walked three family members through the same exercise. Every time I learn something new — Google quietly added a new product, retention setting, or "auto-delete after 18 months" toggle that did not exist before.

This is the 2026 version. It is the order I would do it in if I were starting from scratch. Do as many of these steps as feel right for you — none of them is irreversible until the very last "delete account" button.

---

## Stage 0: Plan before you delete

Before clicking anything destructive:

1. **List the Google services you actually use.** Gmail, Drive, Photos, YouTube, Calendar, Maps, Android sign-in, third-party logins via "Sign in with Google" — write them all down.
2. **List the dependencies.** Anything that uses your Google login, anything that emails to your Gmail, anything that backs up to your Drive.
3. **Pick replacements.** [Encrypted email](/posts/best-encrypted-email-services-2026/), [encrypted cloud](/posts/best-secure-cloud-storage-2026/), [encrypted photos](/posts/ente-photos-review-2026/), [privacy search engine](/posts/best-privacy-search-engines-2026/), [privacy maps](/posts/privacy-respecting-alternatives-google-services-2026/).
4. **Set up a long-term forwarding address.** The Gmail-forwarding feature lets you keep receiving mail at the old address (forwarded to your new encrypted email) for as long as the account exists. Useful as a transition layer.

You will spend more time on this stage than on the actual deletions. That is fine. Skipping it is the most common reason people abandon the migration halfway.

---

## Stage 1: Run Google Takeout

Before deleting anything, get a copy.

1. Go to <a href="https://takeout.google.com" target="_blank" rel="noopener">takeout.google.com</a>.
2. Click "Deselect all," then select only the services you care about (Gmail, Drive, Photos, Contacts, Calendar — start with these).
3. Choose `.zip` format (or `.tgz` if your data is over 50GB).
4. Choose "Send download link via email" or "Add to Drive/Dropbox/OneDrive."
5. Wait. Small accounts come back in minutes. Mine took six hours.

Store the resulting archive on encrypted storage. A [VeraCrypt container](/posts/veracrypt-vs-cryptomator-2026/) on a USB drive is the simplest answer; [encrypted cloud storage](/posts/best-secure-cloud-storage-2026/) works too. Do not leave a Takeout zip in your Downloads folder.

---

## Stage 2: Disable future tracking

Now stop new data from being collected. This buys you time to migrate.

### Activity controls

Go to <a href="https://myaccount.google.com/data-and-privacy" target="_blank" rel="noopener">myaccount.google.com/data-and-privacy</a> and turn off:

- **Web & App Activity** — turn off, AND set "Auto-delete after 3 months"
- **Location History** — turn off, set auto-delete
- **YouTube History** — turn off, set auto-delete

Setting auto-delete on top of "off" is belt-and-braces — if you accidentally turn the toggle back on later, the auto-delete still applies.

### Ad personalisation

Go to <a href="https://myadcenter.google.com" target="_blank" rel="noopener">myadcenter.google.com</a>:

- Turn off "Personalised ads"
- Turn off every individual category (gender, age, languages, demographics)
- Turn off "Personalised ads on partner sites"

This stops Google selling your profile to advertisers and stops them building one in the first place.

### Sign-in security and third-party access

Go to <a href="https://myaccount.google.com/permissions" target="_blank" rel="noopener">myaccount.google.com/permissions</a>:

- Review every third-party app with access to your Google data
- Revoke any you do not actively use
- Especially revoke "Sign in with Google" for sites where you can switch to email-and-password login

Now is also the time to make sure your Google account has [strong 2FA](/posts/how-to-set-up-two-factor-authentication-2026/), ideally a [hardware security key](/posts/best-hardware-security-keys-2026/), so the migration window itself is safe.

---

## Stage 3: Delete the existing data

You can do this from the same `data-and-privacy` page or service-by-service. The service-by-service path is more reliable — Google has a per-service "delete all" button that is faster than the consolidated UI.

### Search history

`myactivity.google.com` → "Delete activity by" → "All time" → confirm.

### Location history

`maps.google.com/timeline` → settings cog → "Delete all Location History."

### YouTube watch and search history

`myactivity.google.com/product/youtube` → delete all.

### Voice and audio

`myactivity.google.com/voice` → delete all (most relevant if you ever used Assistant).

### Gmail

If you are not yet ready to delete the entire account: select all → delete. Then empty Trash. This removes the visible content but leaves the account intact.

If you are ready to delete the whole account, skip — the account deletion handles it.

### Drive

`drive.google.com` → select all → delete → empty trash.

### Photos

`photos.google.com` → settings → "Delete all photos." Note: this is irreversible, and Photos retention separate from Drive.

### Contacts

`contacts.google.com` → select all → delete.

---

## Stage 4: Migrate to alternatives

Now that the old data is gone and tracking is off, set up replacements:

- **Email:** Sign up for [Proton Mail or Tutanota](/posts/best-encrypted-email-services-2026/). Set up Gmail forwarding so the old address keeps catching mail during transition.
- **Cloud storage:** [Proton Drive, Tresorit, or Sync.com](/posts/best-secure-cloud-storage-2026/).
- **Photos:** [Ente](/posts/ente-photos-review-2026/) — Takeout your Google Photos, import into Ente.
- **Search:** Set [Brave, Mojeek, or Kagi](/posts/best-privacy-search-engines-2026/) as your default search engine in every browser.
- **Calendar:** Proton Calendar or Tutanota Calendar.
- **Maps:** OsmAnd (Android), Organic Maps (iOS), or Apple Maps if you are in the Apple ecosystem.
- **Browser:** [Brave or Librewolf](/posts/best-privacy-browsers-2026/) instead of Chrome.
- **Login:** Use [a password manager](/posts/best-password-managers-2026/) to generate strong passwords for each site, instead of "Sign in with Google."

This stage takes the longest because it is the part where you actually change your habits. Plan a weekend.

---

## Stage 5: The "Inactive Account" trap

Google has an Inactive Account Manager — if your account is unused for 6–18 months, Google can email a designated contact and/or delete it for you. This is *not* the deletion you want for active migration, but it is worth setting it up before you delete, because:

- If you forget the password later, you have a recovery contact
- If you change your mind mid-migration, you have time

`myaccount.google.com/inactive` → set up.

---

## Stage 6: Delete the account

Only when you have:

- Migrated email and set up forwarding
- Migrated Drive, Photos, Contacts, Calendar
- Updated every site that uses "Sign in with Google" to use email-and-password
- Notified anyone who emails you regularly of your new address
- Run a final Google Takeout for the archive

…go to `myaccount.google.com/deleteaccount`, work through the confirmation flow, and click delete.

The account enters a recovery period (typically 30 days) during which you can restore it. After that, the account is gone. Your username (the part before `@gmail.com`) is *never* reused — Google will not let anyone else have it.

---

## Stage 7: The downstream cleanup

Google has shared data with thousands of advertisers, analytics partners, and data brokers over the years. Deleting your Google account does not delete that downstream copy.

Use a [data broker removal service](/posts/best-data-broker-removal-incogni-vs-deleteme-eu.md) — Incogni, DeleteMe, or Optery — to handle this layer. They send GDPR/CCPA deletion requests to several hundred brokers. The Google account deletion handles Google; the broker removal handles the downstream copy.

For the publicly visible Google search results that contain your name (LinkedIn, news articles, old forum posts), use Google's "Personal info removal" form. It is surprisingly effective for things like phone numbers and home addresses.

---

## What Google still keeps

Even after full deletion, Google retains some data:

- **Server logs** for security and operational purposes — typically 18 months
- **Aggregate stats** that include anonymised data from your usage
- **Legal hold data** if there is an active subpoena or investigation
- **Backup tapes** that roll off on their own schedule, often months

This is the same posture as most cloud providers. It does not mean you are still being profiled — the active profile is gone. It means deletion has a long tail.

---

## What about Android and ChromeOS

If you delete your primary Google account and you have an Android phone signed in with it:

- Apps will keep running until they need an auth refresh
- Google Play Store will stop working
- App data backed up to Google will be deleted
- Find My Device, Google Pay, etc., stop working

Path of least pain:

1. Migrate to a fresh minimum-viable Google account (email-only, no real name, no real phone if possible) just for Play Store; OR
2. Move to [GrapheneOS](/posts/grapheneos-vs-ios-privacy-2026/) and use the sandboxed Play Services flow

ChromeOS is harder — the entire OS is signed-in. If you are using ChromeOS and want to leave Google, you are really moving to Linux.

---

## Common mistakes

1. **Deleting before migrating.** You will lose access to every site that only knows your old Gmail address. Migrate first.
2. **Forgetting "Sign in with Google."** Every site you signed into via Google now has a broken account. Switch each one to email-and-password before deleting.
3. **Skipping Takeout.** You may want your old emails or photos later. Keep an encrypted archive.
4. **Not telling people.** Friends and family will keep emailing the old address. Use Gmail forwarding for at least 12 months as a transition.
5. **Deleting and immediately re-creating.** Google flags this; sometimes blocks it. Wait if you need a new account.

---

## Bottom line

Deleting your Google footprint is one of the highest-impact privacy moves available in 2026. It also takes work. The realistic timeline:

- Weekend 1: Plan, run Takeout, disable tracking, delete history
- Weeks 2–4: Migrate email, cloud, photos, calendar
- Weekend 5: Update third-party logins, set up forwarding, run final Takeout
- Day 31+: Delete the account

Six weeks of part-time effort to remove yourself from Google's training data, ad profile, and downstream broker network. Compare that to the cost of leaving the data in place — every year for the rest of your life — and it is the easiest privacy ROI you can get.

Pair this guide with your full [privacy stack](/posts/best-privacy-stack-2026/) and you are well ahead of where most internet users will ever be.
