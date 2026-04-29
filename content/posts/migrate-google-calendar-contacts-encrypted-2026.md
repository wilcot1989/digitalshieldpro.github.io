---
title: 'How to migrate Google Calendar and Contacts to encrypted alternatives 2026'
date: 2026-10-19 09:00:00+02:00
lastmod: 2026-10-19 09:00:00+02:00
description: A practical 2026 walkthrough for moving off Google Calendar and Google Contacts to encrypted alternatives — Proton Calendar, Tutanota Calendar and EteSync — including the parts that always break, how to keep family-shared calendars working, and what to do about Apple Calendar integration.
categories:
- privacy-guides
tags:
- google calendar
- google contacts
- proton calendar
- tutanota calendar
- etesync
- privacy
- migration
keywords:
- migrate google calendar 2026
- proton calendar migration
- etesync setup
- google contacts encrypted alternative
- tutanota calendar review
- private calendar app
affiliate: false
author: James Mitchell
author_bio: Cybersecurity analyst with 10+ years of hands-on experience testing VPNs, antivirus software, and privacy tools.
featured_image: /images/categories/privacy-guides.svg
faq:
- q: 'Is migrating off Google Calendar harder than migrating off Gmail?'
  a: 'Different kind of hard. Email migration is mostly volume-based — lots of historical messages to import. Calendar and contacts migration is mostly integration-based — every device, every shared calendar, every "add to calendar" link in your booking flows breaks at once. The data transfer itself takes minutes; rewiring the integrations takes a weekend.'
- q: 'Are Proton Calendar and Tutanota Calendar actually encrypted?'
  a: 'Yes. Proton Calendar encrypts events end-to-end including title, location, description, and notes — only the start time, end time and an opaque event ID are visible to Proton servers (necessary for them to deliver the event to other devices and send notifications). Tutanota Calendar is similar — full E2E with metadata minimisation. Google Calendar is encrypted in transit and at rest, but Google holds the keys and reads everything.'
- q: 'What about EteSync — is it self-hostable?'
  a: 'Yes. EteSync (now branded as Etebase) is open-source and runs on your own server via Docker. It speaks CalDAV and CardDAV with end-to-end encryption added on top, so it works with Apple Calendar, Thunderbird, DAVx5 on Android, and any other CalDAV/CardDAV client. There is also a paid hosted version if you do not want to self-host.'
- q: 'Can I keep a shared family calendar?'
  a: 'Yes — but everyone in the family needs to be on the same encrypted calendar service. Proton Calendar supports shared calendars between Proton users (and read-only ICS export to non-Proton users). Tutanota similar. EteSync supports CalDAV sharing if everyone uses CalDAV clients. The transition often pushes the family conversation: do we all move to Proton, or do we stay on Google for shared visibility?'
- q: 'Will my Apple Calendar still work?'
  a: 'Yes, with caveats. Proton Calendar has full iOS and macOS apps now (since 2023). You can also use CalDAV via Proton Bridge for the desktop. EteSync has dedicated iOS apps that integrate with Apple Calendar. Tutanota is mainly its own app — Tutanota CalDAV is on the roadmap but not GA at time of writing.'
- q: 'How do I migrate the data itself?'
  a: 'Export from Google Calendar as ICS (Settings → Import & Export → Export). Each calendar becomes a separate `.ics` file. Import those into the new calendar service via its import function. For contacts, export as vCard (.vcf) from Google Contacts and import into Proton Contacts, the new email provider, or your CardDAV server. Five minutes of clicking; the data part is genuinely fast.'
- q: 'What about meeting links and "Add to Google Calendar" buttons in booking flows?'
  a: 'Those keep pointing at Google. Either: (1) keep Google Calendar empty-but-connected as a forwarding endpoint to your real calendar via ICS subscription, or (2) update each booking system that holds your "calendar" identity (Calendly, SavvyCal, Cal.com) to point at the new calendar. Option 2 is cleaner long-term; option 1 is faster.'
- q: 'Is moving worth it just for privacy?'
  a: 'Calendar entries are sensitive — they reveal who you meet, when, where, and often why. Doctor appointments. Job interviews. Therapy. Travel. Migrating off Google Calendar is one of the higher-impact privacy moves *for what an attacker can learn about you*, even though it is one of the lower-volume data sets. Yes, it is worth it.'
products:
- name: Proton Calendar
  url: https://proton.me/calendar
  price: 'Free / €4.99/mo Plus'
- name: Tutanota Calendar
  url: https://tuta.com
  price: 'Free / €3/mo'
- name: EteSync
  url: https://www.etesync.com
  price: 'Free (self-host) / $24/yr hosted'
schema_type: Article
---

*This article describes a migration I have done myself and walked several family members through. Proton, Tutanota, and EteSync each have their own pricing — none of them ran a referral program at time of writing.*

Calendar and contacts data is some of the most personal information you generate. Where you go, who you meet, when, in what kind of relationship. Google Calendar holds it all, indexed, searchable, and integrated into everything Google does — including ads.

Migrating off Google Calendar and Google Contacts is one of the more rewarding privacy moves of 2026. The data transfer itself is minutes of work; the integration rewiring is most of the effort. Here is the realistic walkthrough.

---

## What you actually want at the end

End-state setup:

- **Calendar:** Proton Calendar, Tutanota Calendar, or EteSync — encrypted at rest with you holding the keys
- **Contacts:** Proton Contacts, Tutanota Contacts, EteSync Contacts, or a CardDAV server you control
- **Sync:** Working across phone, desktop, and (if used) iPad
- **Sharing:** Family/partner calendars still work
- **Booking integrations:** Cal.com, Calendly, or SavvyCal pointed at the new calendar
- **Old Google Calendar:** Empty, no shared events, account closeable

That last point is the key. The reason migrations fail halfway is that the old Google Calendar still has one shared family calendar nobody migrated, so everyone keeps using it, and you never delete the account.

---

## The three contenders

### Proton Calendar

- **Encryption:** End-to-end, including title, location, description, attendees
- **Apps:** iOS, Android, Web, macOS, Windows
- **CalDAV:** Yes, via Proton Bridge (Mail Plus or higher)
- **Sharing:** Native Proton-to-Proton; read-only public ICS to non-Proton users
- **Pricing:** Free with Proton account; full features with Mail Plus (€4.99/mo)
- **Maturity:** Strong — first launched 2021, mature mobile apps in 2024

Proton Calendar is the smoothest migration path if you already use [Proton Mail](/posts/protonmail-review-2026/). Same account, same login, same key management. The mobile apps got genuinely good in 2024 — daily/weekly/monthly views, easy event creation, working notifications. The desktop app is web (via the Proton Mail web UI) plus CalDAV for native clients.

### Tutanota Calendar

- **Encryption:** End-to-end including all event fields
- **Apps:** iOS, Android, Web, desktop wrappers (Linux, Windows, macOS)
- **CalDAV:** No (as of writing — on roadmap)
- **Sharing:** Tutanota-to-Tutanota only; ICS export
- **Pricing:** Free tier; €3/mo for full features
- **Maturity:** Mature — long-running

Tutanota Calendar is bundled with [Tutanota mail](/posts/tutanota-review-2026/). It is a clean, focused calendar app. The big limitation is no CalDAV — meaning no integration with Apple Calendar, Thunderbird, or third-party CalDAV clients. You live in the Tutanota app for calendar. For someone fully bought into Tutanota mail this is fine; for someone who needs Apple Calendar integration it is a blocker.

### EteSync (Etebase)

- **Encryption:** End-to-end on top of CalDAV/CardDAV
- **Apps:** iOS, Android (DAVx5 or Etesync app), any CalDAV/CardDAV client
- **CalDAV/CardDAV:** Yes, native — that is the whole point
- **Sharing:** Native via EteSync; CalDAV sharing for clients that support it
- **Pricing:** Free if self-hosted; $24/year for hosted
- **Maturity:** Mature — first launched 2017

EteSync is the open-source self-hosted choice. It is also the most flexible because CalDAV/CardDAV are open standards — any calendar app on any platform can talk to it. The setup is more involved (Docker container, web admin, install the EteSync app on each device), but the result is genuinely portable. If you ever decide to leave EteSync, you take your CalDAV server with you.

---

## Stage 1: Decide on the destination

Pick one before you do anything. The choice cascades through every subsequent decision.

- **Already on Proton Mail, comfortable with Proton ecosystem:** Proton Calendar.
- **Already on Tutanota, do not need Apple Calendar integration:** Tutanota Calendar.
- **Self-hosting comfortable, want maximum platform flexibility:** EteSync.
- **None of the above:** Proton Calendar. The migration story is the smoothest, the mobile apps are good, and Proton's privacy reputation is solid.

I personally use Proton Calendar for primary, Apple Calendar (CalDAV-connected to Proton via Bridge) for the family calendar where everyone is on Apple, and EteSync for an experimental "private journal" calendar.

---

## Stage 2: Export from Google

### Calendar

1. Go to <a href="https://calendar.google.com" target="_blank" rel="noopener">calendar.google.com</a>.
2. Settings → "Import & Export" → "Export."
3. You get a `.zip` containing one `.ics` file per calendar.
4. Save to encrypted storage — a [VeraCrypt container](/posts/veracrypt-vs-cryptomator-2026/) or [encrypted cloud](/posts/best-secure-cloud-storage-2026/).

### Contacts

1. Go to <a href="https://contacts.google.com" target="_blank" rel="noopener">contacts.google.com</a>.
2. Left sidebar → Export.
3. Choose "vCard" format → Export.
4. Save to encrypted storage.

You now have everything. The data export part is genuinely five minutes.

---

## Stage 3: Import into the new home

### Proton Calendar

1. Settings → Calendars → Import.
2. Drag in the `.ics` files one by one. Proton creates a calendar per import (you can rename/merge after).
3. Import vCard into Proton Contacts via Contacts → Import.

### Tutanota Calendar

1. Calendar tab → import icon (top right).
2. Select `.ics` files.
3. Contacts tab → import vCard.

### EteSync

1. Set up EteSync server (self-host or use hosted).
2. Use DAVx5 on Android or the EteSync iOS app.
3. Use the migration tool from the EteSync GitHub to import existing ICS/vCard.

---

## Stage 4: Configure devices

This is the slow part. Every device needs the new calendar app or the new CalDAV/CardDAV connection.

### iOS

For Proton Calendar: install the Proton Calendar app from the App Store, sign in. Done.

For EteSync via Apple Calendar: Settings → Calendar → Accounts → Add Account → Other → Add CalDAV Account. Server: your EteSync URL. Username: your EteSync username. Password: your EteSync password (or app-specific password if you use one).

For Tutanota: install the Tutanota app. Done. (No native Apple Calendar integration.)

### Android

DAVx5 from F-Droid or Play Store handles CalDAV/CardDAV beautifully. Configure the server URL, log in, sync.

For Proton Calendar specifically: install the Proton Calendar app.

For Tutanota: install the Tutanota app.

### macOS

Apple Calendar with CalDAV — same as iOS but on the desktop. Apps that can speak CalDAV (Fantastical, BusyCal, Thunderbird) all work.

For Proton specifically: use the Proton Mail Bridge (Mail Plus or higher) to expose CalDAV locally. Apple Calendar then connects to `localhost:port` and gets full access.

### Linux

Thunderbird with the appropriate CalDAV/CardDAV add-ons. GNOME Calendar speaks CalDAV. EteSync has a Linux client.

### Windows

eM Client and Thunderbird are the two CalDAV clients that work cleanly on Windows. Proton Calendar via web is also fine.

---

## Stage 5: Rewire the integrations

This is where most migrations fail. Find every system that holds your "calendar identity" and update it:

### Booking systems

- **Calendly / SavvyCal / Cal.com:** Settings → Calendar Connections. Disconnect Google, add CalDAV pointing at your new calendar. (Cal.com is the most CalDAV-friendly; Calendly takes some workarounds.)

### Meeting platforms

- **Zoom / Google Meet / Teams:** They send invite emails with `.ics` attachments. The `.ics` opens in your default calendar — confirm the OS default is the new app, not Google Calendar.
- **Internal company calendar:** If your employer is on Google Workspace, you may need to keep Google Calendar for work and use Proton/etc. for personal. That is fine. Just make sure both are visible on your phone.

### Smart speakers / home assistants

- **Google Assistant / Google Nest:** Will only read from Google Calendar. If you need calendar read-aloud, decide whether to keep Google Calendar as a *destination only* (with events synced one-way from Proton via ICS subscription) or accept that the smart speaker stops being useful for calendar.
- **Alexa:** Can speak CalDAV via skills.
- **HomePod / Apple Home:** Speaks Apple Calendar — which is now connected to Proton or EteSync. Works.

---

## Stage 6: Shared calendars

Family calendars are the migration killer. You will not move alone — the family is going to ask "wait, when is Aunt Sue's birthday this year?"

Three paths:

1. **Migrate the whole family to the same encrypted calendar.** Best result; hardest sell.
2. **Keep one shared Google Calendar for family, move private calendars to encrypted.** Pragmatic compromise; partial privacy.
3. **Use ICS subscription as a bridge.** Proton Calendar lets you publish a read-only ICS link for a calendar; share that with family who stay on Google. They see your events; they cannot edit. Two-way requires everyone on the same provider.

I have used path 2 for years. Family stuff stays in iCloud (everyone is on Apple); private/work stays in Proton Calendar. Two calendars, one device, no leakage.

---

## Stage 7: Empty the Google Calendar

Once the new system is running and all integrations are rewired:

1. Inside Google Calendar, delete every event from every calendar (Settings → Calendar → Remove all events).
2. Unshare any shared calendars (so family / coworkers stop sending invites).
3. Delete the calendars themselves.
4. Repeat for Google Contacts.

Now Google Calendar and Google Contacts are empty. You can either close the Google account entirely (see my [Google data deletion guide](/posts/how-to-delete-data-from-google-2026/)) or leave it as a dormant account.

---

## Stage 8: A sanity check

A week into the migration, ask yourself:

- Did I miss any events?
- Are notifications firing reliably?
- Is search working?
- Are my booking flows pointed at the right calendar?
- Have I been emailed any "you missed our meeting" notes?

If yes to the last one — find out where that meeting was sent and update the integration. Migrations leak through whatever you forgot to update.

---

## Common mistakes

1. **Migrating data without rewiring integrations.** Calendar invites keep flowing into Google. The new calendar stays empty. You give up.
2. **Not telling the family.** They keep emailing the Google address with calendar invites. Chaos.
3. **Trying to keep Google Calendar in sync as a backup.** Two-way sync is fragile. Pick a primary, stick with it.
4. **Skipping Tutanota because no CalDAV — when you do not need CalDAV.** If you only use the Tutanota app on phone and desktop, no CalDAV is irrelevant. Do not over-think the requirements.
5. **Self-hosting EteSync without backups.** If your VPS dies, your calendar dies. Backup the EteSync data directory daily to [encrypted cloud](/posts/best-secure-cloud-storage-2026/).

---

## Where this fits in the broader stack

Calendar and contacts are part of the larger Google migration:

- [Email](/posts/best-encrypted-email-services-2026/) — the biggest piece
- [Cloud storage](/posts/best-secure-cloud-storage-2026/) — Drive replacement
- [Photos](/posts/ente-photos-review-2026/) — Photos replacement
- [Search](/posts/best-privacy-search-engines-2026/) — Search replacement
- Calendar + Contacts (this article)
- [Browser](/posts/best-privacy-browsers-2026/) — Chrome replacement
- [Encrypted DNS](/posts/best-encrypted-dns-providers-2026/) — closes the network leak

When you finish all of the above, the [Google data deletion](/posts/how-to-delete-data-from-google-2026/) is the closing move. Your calendar and contacts are usually the second-to-last domino — most people do email first, drift through the others, and end with calendar because it is fiddly.

It is fiddly. It is also fine. A weekend, two coffees, the right tools.

---

## Bottom line

For most people in 2026, the right migration target for calendar + contacts is <a href="https://proton.me/calendar" target="_blank" rel="nofollow sponsored noopener">Proton Calendar</a>. It pairs naturally with Proton Mail, has the strongest E2E encryption, supports CalDAV via Bridge for desktop integration, and the mobile apps are good.

For self-hosters and CalDAV/CardDAV maximalists: <a href="https://www.etesync.com" target="_blank" rel="nofollow sponsored noopener">EteSync</a>. Maximum portability, maximum control, more setup work.

For Tutanota loyalists: <a href="https://tuta.com" target="_blank" rel="nofollow sponsored noopener">Tutanota Calendar</a>. Clean, focused, no Apple Calendar integration but excellent on its own.

Pair this with the rest of your [privacy stack](/posts/best-privacy-stack-2026/) and you remove one of the most personally revealing data sets from Google's hands. That is one of the best calendar-week investments your future self will thank you for.
