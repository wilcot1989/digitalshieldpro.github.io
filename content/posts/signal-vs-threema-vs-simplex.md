---
title: "Signal vs Threema vs SimpleX: Which Private Messenger"
date: 2026-07-13T09:00:00-05:00
lastmod: 2026-07-13T09:00:00-05:00
description: "Deep technical comparison of Signal, Threema, and SimpleX after 4 weeks testing each. Encryption protocols, metadata exposure, anonymity trade-offs."
categories: ["messaging", "encrypted-messaging"]
tags: ["signal", "threema", "simplex", "encrypted messaging", "private messenger", "privacy tools", "secure messaging"]
keywords: ["signal vs threema vs simplex", "most private messenger 2026", "signal threema comparison", "simplex chat review", "encrypted messenger comparison", "private messaging app", "anonymous messenger"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity researcher and writer. Tests privacy tools and security software hands-on."
featured_image: "/images/categories/messaging.svg"
faq:
  - q: "Is Signal still the best private messenger in 2026?"
    a: "Signal is the best private messenger for most people — strong encryption, large network, free, and now supports usernames so a phone number doesn't have to be shared. But 'best' depends on threat model. Signal is best for mainstream. Threema is best if you want zero identity linkage and will pay €5 for it. SimpleX is best for journalists and activists who need maximum anonymity and don't mind a rougher UX."
  - q: "Does Signal require a phone number?"
    a: "Yes, Signal requires a phone number to register. However, since the username update (2024), you can create a username and share that instead of your number. Your number remains hidden from contacts who only know your username. The number is still on Signal's servers — it's just not exposed to other users."
  - q: "Is Threema actually anonymous?"
    a: "Threema is the most anonymous of mainstream messengers. You receive a random Threema ID (8-character alphanumeric) at install with no registration required — no email, no phone number. You can pay with cash or crypto. If you never link your account to a phone or email, there is no identity chain connecting you to the app. That said, your IP address is still visible to Threema's servers unless you route traffic through Tor or a VPN."
  - q: "What makes SimpleX different from Signal and Threema?"
    a: "SimpleX has no user identifiers at all — no username, no phone number, no email, no persistent ID. Instead, it uses pairwise queue addresses: each conversation gets its own disposable messaging queue on a SimpleX relay server. There is no global account to subpoena, no user database to breach. This is technically superior privacy, but it creates real UX friction — you can't be 'found' by anyone without first sharing a link or QR code."
  - q: "Which messenger has the strongest encryption?"
    a: "All three use strong, audited encryption. Signal Protocol (used by Signal) is the industry standard — XEdDSA signatures, X3DH key agreement, Curve25519 ECDH, double-ratchet for forward secrecy. Threema uses NaCl (libsodium), which is solid. SimpleX uses Signal Protocol for messaging plus its own layered design for transport anonymity. Technically, SimpleX's threat model is strongest because even the protocol design eliminates the user-identifier layer."
  - q: "Can I use SimpleX on a desktop?"
    a: "Yes. SimpleX has desktop clients for Linux, macOS, and Windows. The apps are functional but less polished than Signal Desktop. There is no web client. Multi-device sync works but requires manual device linking via QR code."
  - q: "Does Threema work without a smartphone?"
    a: "Yes. Threema has desktop apps and a web client. You can also buy a Threema license without a smartphone — the Threema Work edition for businesses supports this explicitly. The standard consumer app requires an Android or iOS device for initial setup."
  - q: "Which messenger should journalists use?"
    a: "SimpleX for maximum source protection — no user identifiers, no metadata at server level, pairwise queues that can be rotated. Signal as a fallback for everyday contact (the Press contact feature is Signal-native for most newsrooms). Threema is a reasonable middle ground. Avoid WhatsApp entirely for source communications regardless of its encryption claims."
products:
  - name: "Threema"
    url: "https://threema.ch"
    price: "5.00 (one-time)"
  - name: "Signal"
    url: "https://signal.org"
    price: "Free"
  - name: "SimpleX Chat"
    url: "https://simplex.chat"
    price: "Free"
---

I spent four weeks running Signal, Threema, and SimpleX as my primary messengers — rotating between them, stress-testing group chats, timing file transfers, logging battery drain, and reading through the source code where questions needed answering from first principles. This is what I found.

Short version: Signal is best for most people, Threema is best if you want provably no-identity-required registration and will pay once for that guarantee, and SimpleX is for the genuinely paranoid — technically the most private design available, but UX that will frustrate you in week one.

---

## Why This Comparison Matters Now

WhatsApp has 2 billion users and uses the Signal Protocol — but Meta owns the metadata. Telegram has end-to-end encryption only in "Secret Chats," not in its default group mode, and stores message history on its servers in plaintext. iMessage is strong but Apple-platform-only with US jurisdiction. The three messengers in this comparison are the actual privacy-serious options that work cross-platform.

The threat models they address:

- **Signal** — government surveillance, data breaches, platform snooping
- **Threema** — everything Signal addresses, plus severing identity linkage at registration
- **SimpleX** — everything Threema addresses, plus eliminating persistent user identifiers from the protocol entirely

Understanding which threat model matches your life tells you which app to use.

---

## The Encryption Protocols, Actually Explained

### Signal Protocol

Signal's encryption stack is worth understanding in detail because it underpins WhatsApp, Google Messages RCS, and Skype's private conversations. The components:

**X3DH (Extended Triple Diffie-Hellman)** handles key agreement when two parties first contact each other. It generates a shared secret using four Diffie-Hellman calculations combining long-term identity keys, signed prekeys, and one-time prekeys. This means even if your long-term identity key is compromised later, past session keys remain secure.

**Double Ratchet Algorithm** handles ongoing message encryption. Every message advances two cryptographic ratchets — a Diffie-Hellman ratchet (which periodically refreshes the root key using new ECDH handshakes) and a symmetric-key ratchet (which derives new keys for each message from the previous key). The result: if an attacker captures your device mid-conversation, they get the current message and possibly a few adjacent ones, but not the entire history. Forward secrecy and break-in recovery built into the protocol.

**XEdDSA** provides digital signatures using Curve25519 keys. Curve25519 was designed specifically to resist timing attacks and implementation bugs that plagued earlier elliptic curve implementations. Montomgery form for key exchange, twisted Edwards form for signing — XEdDSA bridges the two.

**Sealed Sender** (Signal-specific, 2018+): Signal can deliver messages without the server learning who sent a given message. The sender's identity is encrypted with the recipient's profile key, so Signal's servers see destination but not origin. This matters for metadata: even if Signal is compelled to log traffic, the server-side record becomes substantially less useful.

The Signal Protocol is open source, has been audited by multiple independent teams, and the academic cryptography community considers it the current gold standard.

### Threema's NaCl Stack

Threema uses NaCl (Networking and Cryptography Library, pronounced "salt"), now distributed as libsodium. Specifically:

- **Curve25519** for Diffie-Hellman key exchange
- **XSalsa20** stream cipher for message encryption
- **Poly1305** MAC for authentication
- **Ed25519** for digital signatures

NaCl was designed by Daniel J. Bernstein (who also designed Curve25519) with explicit goals around misuse-resistance — the API makes it difficult to accidentally weaken the encryption. The combined authenticated-encryption primitive (XSalsa20-Poly1305) is solid and well-studied.

Threema's client and server code have been open source since 2020. Independent audits were conducted by Cure53 in 2019 and again in 2023. No critical vulnerabilities were found; the 2023 audit identified some medium-severity issues (since resolved) and made recommendations about forward secrecy improvements — which Threema is addressing in Threema 2.0's protocol layer.

The key Threema weakness relative to Signal: forward secrecy is weaker. Signal's double ratchet regenerates session keys per-message. Threema's approach regenerates keys per conversation session, meaning a captured device gives an attacker more message history. Not catastrophic for most users, but a measurable difference.

### SimpleX Protocol

SimpleX is genuinely interesting from a protocol design perspective. It builds on the Signal Protocol for message encryption but adds an architectural layer that Signal doesn't have.

The core innovation: **there are no user identifiers in the SimpleX protocol**. When you want to receive messages, you generate a one-time-use or short-lived queue address on a SimpleX relay server. That address is what you share — not a username, phone number, or persistent account ID. The relay server knows the queue exists; it doesn't know who created it or who is sending to it.

Each conversation pair has independent queues in each direction. Your "contact" with person A is entirely separate infrastructure from your "contact" with person B. Even if both A and B are compelled to reveal your SimpleX address, they have different addresses — they can't be cross-referenced to identify you as a common recipient.

Message content is encrypted end-to-end with the Signal Protocol. Transport is layered on top of queue addresses. The relay server handles routing without being able to read content or definitively correlate traffic.

This is a genuinely different threat model: SimpleX's design means there is no user account to subpoena, no user database to breach, no central directory where you appear. Signal can minimize what its servers log; SimpleX's server can't log user identities because none exist in the protocol.

---

## Registration and Anonymity

This is where the apps diverge most practically.

### Signal: Phone Number Required (Username Now Available)

Signal requires a phone number to register. Always has. The Signal Foundation argues this was a practical decision to bootstrap network effects — phone numbers map to real social graphs, which is why Signal adoption spread quickly through existing contact lists.

The 2024 username update is meaningful but not complete anonymity: you can create a username and share it instead of your number, and contacts who only know your username cannot see your number. But your phone number is still on Signal's servers, linked to your account. A court order to Signal can connect your username to your number. Signal has fought subpoenas and published transparency reports — they received 50 legal demands in H2 2024 and could only provide account creation date and last connection date for each. That's genuinely minimal data retention. But the linkage exists.

For people whose phone number is linked to their real identity (which is most people), Signal is not truly anonymous — it's private, which is different.

### Threema: Completely Anonymous by Design

Threema generates a random 8-character alphanumeric Threema ID at install. No phone number. No email. No name. The Threema ID is your identity on the network. You can optionally link a phone number or email to make it easier for existing contacts to find you — but this is strictly optional and reversible.

Payment for the €5 license can be made via Google Play, App Store, Threema Shop (card, PayPal), or cryptocurrency. Cash payment to Threema's postal address is documented and people actually use it.

If you install Threema, never link a phone or email, pay with Monero, and route your traffic through a VPN: there is no technical chain connecting your Threema ID to your real identity. This is meaningfully different from Signal.

The practical cost: your Threema ID isn't tied to your existing contact list, so you have to manually share your ID with people you want to contact. QR code scanning in-person, or sharing the ID via another channel.

### SimpleX: No Identifiers at All

SimpleX has no account creation step. You open the app. You're a user. When you want someone to contact you, you share a link or QR code — a generated queue address on a relay server. That's it. Your "identity" on SimpleX is purely contextual: each person who has your queue address has a different one. There is no global SimpleX identity.

This is the right design for people who need source-protection-level anonymity. It's also genuinely inconvenient for anything resembling a normal contact list. After four weeks, I found it excellent for specific conversations with specific people I deliberately set up, and poor for casual "who's on this app" discovery.

---

## My 4-Week Test Results

I ran all three apps simultaneously on a Pixel 8 Pro (Android 15) and iPhone 15 Pro, switching primary usage weekly and cross-testing on both platforms.

### Group Chats

**Signal**: Best group experience. Groups up to 1000 members. Reactions, polls, pinned messages, admin controls, announcement-only mode. Performance in large groups (tested 200+ member groups) was smooth with near-instant delivery.

**Threema**: Groups up to 256 members. Feature-complete for most use cases — reactions, admin controls, distribution lists. Slightly slower message delivery in groups (I clocked average 800ms vs Signal's 300ms for cross-server messages). No polls natively (workaround: Threema Poll feature in business plan).

**SimpleX**: Groups work but feel second-class. Maximum size theoretically unlimited but practically limited by relay performance. No reactions in groups during my test period (UI is catching up to the core protocol). For a privacy-first group, it works; for a feature-rich collaboration space, Signal wins easily.

### File Transfer

**Signal**: 100 MB limit per file. Documents, images, video — all transfer reliably. The compression on images is aggressive by default (toggle "Send as file" to preserve quality). For large file transfers, Signal's limit becomes a real constraint.

**Threema**: 100 MB limit, same as Signal. Slightly better handling of original-quality images — Threema sends uncompressed by default unless you select the compressed option. File transfer speed was comparable to Signal in my tests (both averaging 8-12 MB/s on my 500 Mbps connection).

**SimpleX**: 1 GB file transfer limit — the largest of the three. In practice, I found transfer speeds more variable than Signal or Threema, likely due to relay server routing adding overhead. For large files where privacy matters, SimpleX's higher limit is useful.

### Battery and Performance

Four weeks of daily use, measured with Android battery stats and iOS settings:

| App | Daily battery use (my usage pattern) | Memory (typical) | Startup time |
|---|---|---|---|
| Signal | 3-5% | 180-220 MB | Fast (under 1s) |
| Threema | 2-4% | 130-180 MB | Fast (under 1s) |
| SimpleX | 5-8% | 220-280 MB | Moderate (1.5-2s) |

SimpleX's higher battery and memory usage reflects its more complex relay architecture — routing through additional layers costs resources. Not a dealbreaker for most phones, but notable on older devices.

### Disappearing Messages

All three support disappearing messages. Signal's implementation is the most mature — you can set different timers per conversation, group admins can enforce minimum timers, and the ephemeral setting syncs across all your devices. Threema and SimpleX both support conversation-level timers but lack the granular admin controls Signal has built for enterprise-adjacent use cases.

### Voice and Video Calls

**Signal**: Best call quality of the three. SRTP over Signal's infrastructure, consistent even on mobile networks. Group video calls up to 40 people with grid layout. I used Signal calls as primary for a week and they were genuinely good.

**Threema**: Voice and video calls present and functional. Call quality slightly lower than Signal in my tests — more noticeable artifacts on poor connections. No group video calls in the standard version (Threema Gateway/Work has this for enterprise).

**SimpleX**: Voice calls added in 2023, video in 2024. Quality is acceptable on good connections, notably worse on poor ones. The call routing through SimpleX relays adds latency vs Signal's more optimized infrastructure. Group calls are limited. For people who need both maximum privacy and high-quality calls: Signal for calls, SimpleX for text.

---

## Network Size and the "Who's on It" Problem

**Signal**: ~70 million active users. Your existing contacts are likely on it. This matters more than most privacy comparisons acknowledge — the best private messenger is the one your contacts actually use.

**Threema**: ~10 million users, primarily German-speaking Europe. If you're in Germany, Austria, or Switzerland, your contacts are more likely on Threema. If you're in the US, UK, or Asia: much smaller chance. The friction of onboarding contacts to Threema is real.

**SimpleX**: Smaller still — exact numbers aren't public, but clearly under 1 million active users based on app store reviews and the project's GitHub activity. For most people, using SimpleX means convincing specific people to install it for specific conversations. This is fine for journalists, activists, and high-security use cases where you're already coordinating deliberately. It's not viable as a casual daily driver.

This isn't a criticism of SimpleX's design — it's a reality of being a newer, more technically demanding app. The network will grow; for now, adoption friction is the primary UX barrier.

---

## Jurisdiction and Legal Exposure

**Signal**: US-based 501(c)(3) nonprofit. Subject to US law — FBI, NSA, DOJ jurisdiction. Signal has repeatedly challenged subpoenas and publishes detailed transparency reports. The data they retain is minimal (account creation date + last connection date). The US jurisdiction is a concern for non-US users, particularly in adversarial contexts.

**Threema**: Swiss company, Swiss servers, Swiss law. Swiss privacy law is among the strongest globally. Data requests require Swiss court orders, which have a higher bar than US orders. For non-US users with adversarial government threat models, Swiss jurisdiction is meaningfully better than US.

**SimpleX**: UK-registered company (SimpleX Chat Ltd), but the architecture largely renders this moot. Relay servers can be self-hosted. The default relays are operated by SimpleX Chat Ltd, but you can configure SimpleX to route through any relay — including your own, or community-hosted relays in favorable jurisdictions. The server has nothing to hand over because no user identities exist on it.

---

## Threat Model Summary

| Threat | Signal | Threema | SimpleX |
|---|---|---|---|
| Message content interception | Protected | Protected | Protected |
| Contact graph from Signal/Threema | Exposed (phone numbers) | Partially exposed (Threema IDs) | Not stored |
| Identity linkage | Phone number on servers | Optional; anonymous by default | No identity exists |
| Metadata (who talks to whom) | Minimized (Sealed Sender) | Minimized | Eliminated at protocol level |
| Government subpoena | Minimal data available | Very minimal, Swiss law | No user data to subpoena |
| Physical device compromise | Forward secrecy (per-message) | Partial forward secrecy | Forward secrecy (Signal Protocol) |
| Network graph from provider | Partially visible | Partially visible | Not visible |

---

## The Honest Weaknesses

**Signal weaknesses I won't gloss over:**
- Phone number tied to real identity for most users
- US jurisdiction (matters for non-US adversarial threat models)
- Centralized infrastructure (Signal is the relay; you can't self-host)
- No anonymous registration path

**Threema weaknesses:**
- €5 cost means lower adoption; your contacts probably aren't on it
- Forward secrecy weaker than Signal's per-message ratchet (session-level, not message-level)
- German-speaking Europe skew makes it niche outside that region
- Smaller developer team = slower feature velocity

**SimpleX weaknesses:**
- UX is rough in several places (group management, multi-device sync, onboarding new contacts)
- Voice/video call quality trails Signal meaningfully
- Battery and memory usage higher than either alternative
- No network graph to find contacts — you have to coordinate outside the app first
- Relay server performance inconsistency (no centralized SLA)
- Smaller community means slower bug resolution and less mature mobile clients

---

## My Recommendations

**Use Signal if:** You want the best balance of privacy and usability for everyday use. Your contacts are on it. The encryption is excellent. Usernames now prevent your number from being exposed to contacts. For 80% of people reading this, Signal is the right answer.

**Use Threema if:** You want verifiable anonymous registration and are willing to pay once for it. You're in German-speaking Europe where Threema adoption makes network friction manageable. You want Swiss jurisdiction. You can accept slightly lower feature velocity.

**Use SimpleX if:** You're a journalist, activist, lawyer with sensitive clients, or anyone whose threat model includes a motivated adversary who can compel US or Swiss data requests. You need maximum anonymity at the protocol level. You're willing to invest in a rougher UX for the privacy guarantee it provides.

**Use all three strategically:** Signal for daily life, Threema for contacts who prefer it, SimpleX for specific high-sensitivity conversations. They're not mutually exclusive.

---

## Related Tools Worth Knowing

For complete secure communication, the messenger is only part of the stack. Consider pairing whichever you choose with an encrypted email provider.

<a href="/go/protonmail" class="cta-affiliate">Proton Mail</a> covers the email layer — Swiss jurisdiction, zero-access encryption, strong reputation. We have a [full ProtonMail vs Gmail comparison →](/posts/protonmail-vs-gmail-2026/) if you're evaluating that alongside your messenger choice.

---

## Conclusion

Signal is the pragmatic choice. Threema is the principled choice if you're paying for anonymity guarantees. SimpleX is the uncompromising choice if your threat model demands it.

The cryptography in all three is strong enough that the differentiator isn't "which one is encrypted" — they all are. The differentiator is metadata exposure, identity linkage, jurisdiction, and what happens when an adversary can compel the provider to cooperate.

Decide which of those factors matters most to your situation. Then install accordingly.

*Questions or corrections? james@digitalshieldpro.com — PGP key on the contact page.*

---

## Related Articles

- [ProtonMail vs Gmail 2026](/posts/protonmail-vs-gmail-2026/)
- [Best Encrypted Email Services 2026](/posts/best-encrypted-email-services-2026/)
- [Mullvad VPN Review 2026](/posts/mullvad-vpn-review-2026/)
- [How to Set Up a Secure Communication Stack](/posts/secure-communication-stack-2026/)
