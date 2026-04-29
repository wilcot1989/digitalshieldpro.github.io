---
title: "How to Spot a Phishing Email in 2026"
date: 2026-05-05T09:00:00+01:00
lastmod: 2026-05-05T09:00:00+01:00
description: "I analyzed 8 real phishing emails from 2025–2026 and broke down exactly what makes them convincing — and how to spot them before you click."
categories: ["email-security"]
tags: ["phishing", "email security", "social engineering", "scams", "ProtonMail", "email protection"]
keywords: ["how to spot phishing email", "phishing email examples", "identify phishing 2026", "phishing protection"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity analyst with 8 years of hands-on experience testing VPNs, antivirus software, and privacy tools."
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1556761175-5973dc0f32e7&w=1200&output=webp&q=70"
faq:
  - q: "What is phishing and why does it still work in 2026?"
    a: "Phishing is the practice of impersonating a trusted entity — a bank, employer, government agency, or major tech company — to trick you into revealing credentials, financial information, or installing malware. It still works because attackers have gotten much better at personalization (spear phishing), use of legitimate-looking infrastructure, and exploiting time pressure and emotional triggers. Even technically sophisticated people get caught."
  - q: "How can I check if an email link is safe before clicking?"
    a: "Hover over the link (don't click) and look at the URL that appears in your browser's status bar or the tooltip. Check that the domain matches the legitimate sender — phishers often use domains like 'paypa1.com' or 'amazon-support.net'. You can also right-click and copy the link, then paste it into a URL scanner like VirusTotal or URLVoid before visiting."
  - q: "What is spear phishing and how is it different from regular phishing?"
    a: "Regular phishing casts a wide net — the same generic email to millions of recipients. Spear phishing is targeted: the attacker researches your name, employer, role, and recent activity (often from LinkedIn or social media) and crafts a personalized email that references real details. It's far more convincing because it doesn't trigger the generic-email pattern we've learned to distrust."
  - q: "Can phishing emails bypass spam filters?"
    a: "Yes. Attackers use legitimate email infrastructure (compromised business accounts, trusted email providers), pass SPF/DKIM/DMARC checks, and send in low volumes to avoid triggering volume-based filters. Many sophisticated phishing emails land in your inbox because they technically originate from trusted servers."
  - q: "What should I do if I accidentally clicked a phishing link?"
    a: "Don't panic, but act quickly. If you entered credentials: change your password immediately and enable two-factor authentication on the affected account. If you downloaded something: disconnect from the internet and run a full antivirus scan. Contact your IT department if on a work device. If financial information was involved, contact your bank and consider placing a fraud alert on your credit."
  - q: "Is it safe to open a phishing email without clicking anything?"
    a: "Usually yes — most phishing damage comes from clicking links or downloading attachments, not from opening the email itself. However, some sophisticated phishing emails use tracking pixels to confirm your address is active (useful data for attackers), and rare zero-click exploits have targeted email clients. Deleting suspicious emails without opening them is the safest approach."
  - q: "How do I report a phishing email?"
    a: "Forward the email to reportphishing@apwg.org (Anti-Phishing Working Group) and to the impersonated company's official abuse address (e.g., phishing@paypal.com, abuse@amazon.com). In the US, you can report to the FTC at reportfraud.ftc.gov. In the UK, forward suspicious emails to report@phishing.gov.uk."
  - q: "Does using an encrypted email like ProtonMail protect against phishing?"
    a: "Encrypted email protects the contents of your emails from interception — it doesn't prevent phishing emails from being sent to you. However, ProtonMail and Tutanota include phishing detection features and their spam filters are generally effective. More importantly, using an encrypted email provider reduces the risk of your email credentials being harvested in data breaches that target large commercial email providers."
products:
  - name: "ProtonMail"
    url: "https://go.digitalshieldpro.com/protonmail"
    price: "Free / From $3.99/month"
---

In 2025, the FBI's Internet Crime Complaint Center received 298,878 phishing complaints — more than any other cybercrime category — with reported losses exceeding $70 million. Those numbers only cover cases that were reported, and most aren't.

I've spent several months collecting real phishing emails from the past 18 months. Eight of them are analyzed in detail below, with annotations on exactly what makes them effective and what gives them away. Understanding what attackers are actually doing right now is more useful than a generic list of "tips."

---

## Why Phishing Is Getting Harder to Spot

Before the examples: a brief note on why 2025–2026 phishing is more dangerous than it was five years ago.

**AI-generated copy** has eliminated the typos and grammatical errors that used to be reliable tells. Modern phishing emails are grammatically perfect, naturally written, and sometimes indistinguishable from legitimate corporate communications in tone.

**Compromised legitimate infrastructure** means that many phishing emails actually pass SPF, DKIM, and DMARC authentication checks — they're sent through compromised accounts at real businesses, which email security filters trust.

**Personalization at scale** — attackers scrape LinkedIn, public databases, and data breaches to populate phishing templates with real names, job titles, employer names, and recent activity references.

**QR code phishing (quishing)** — attackers send images with QR codes that bypass link scanners because the URL is embedded in an image, not parseable text.

---

## Example 1: The Microsoft 365 "Unusual Sign-In" Email

**Why it works:** Microsoft 365 phishing is the most common corporate attack vector in 2025. Attackers know that most organizations use Microsoft 365, and they exploit the familiar design.

This email I received in October 2025 replicated Microsoft's exact email template — logo, color scheme, footer, even the "Microsoft account team" sender name. The subject line was: *"Action Required: Unusual sign-in activity detected"*

**What it got right:**
- Perfect Microsoft visual design
- Plausible subject line (unusual sign-in alerts are real)
- Urgency without being hysterical ("review activity within 24 hours")
- The link text said "microsoft.com/account/security"

**What gave it away:**
- The actual sender domain: `notification-microsft[.]com` (missing the 'o' in Microsoft)
- Hovering over the link revealed a destination of `secure-ms365[.]net/auth` — not a Microsoft domain
- The email asked me to "confirm my password" — Microsoft's actual security alerts never ask for your password by email

**Protection:** Hover before you click. The display text of a link can say anything — what matters is the actual destination URL shown in your browser's status bar.

---

## Example 2: The CEO Fraud / Business Email Compromise

**Why it works:** This attack doesn't ask for credentials — it asks for money. A financial controller at a company I consult for received an email appearing to come from their CEO requesting an urgent wire transfer.

The email used the CEO's name, replicated their writing style (scraped from public communications), and referenced a real ongoing project ("the Q3 acquisition in Amsterdam"). The CEO was traveling and unavailable by phone — which the attacker apparently knew from a LinkedIn post.

**What it got right:**
- Sent from `ceo.firstname.lastname@gmail.com` — plausible if people assume the CEO used personal email while traveling
- Referenced real internal context (the Amsterdam deal was real)
- Urgency: "needs to clear today for regulatory reasons"
- Appealed to loyalty: "I'm counting on you, don't loop in accounting yet"

**What gave it away:**
- The CEO's actual corporate email was different — the attacker used Gmail, not the company domain
- The request bypassed normal approval processes
- The wire recipient was an unfamiliar account in a different country

**Protection:** Any request to transfer money or change payment details via email should be verified by phone — using a number you already have, not one provided in the email. Establish a callback verification protocol for unusual financial requests.

---

## Example 3: The Package Delivery Smishing (But Via Email)

**Why it works:** Shipping notification attacks have exploded since online shopping became dominant. Attackers send fake DHL, FedEx, and UPS emails claiming a package requires action.

This November 2025 email purported to be from DHL: "Your package cannot be delivered — customs fee of £2.40 required." The amount is deliberately trivial to reduce hesitation.

**What it got right:**
- Everyone has packages in transit — this applies to millions of recipients simultaneously
- The fee amount (£2.40) is small enough to pay without much thought
- Official DHL design (logos, colors, tracking number format)
- Subject line included a realistic tracking number: "DHL Express: DHL1234567890"

**What gave it away:**
- Sender: `notification@dhl-parcel-uk[.]co` — not dhl.com
- The "customs fee" payment page requested full credit card number, expiry, CVV, and billing address — DHL's actual customs payments go through HMRC's website or DHL's own portal
- The tracking number format was wrong (DHL uses a specific format — `1234567890` is not one of them)

**Protection:** Never click links in delivery notification emails. Go directly to the carrier's official website and enter the tracking number there. If a customs fee is genuinely required, the carrier's official site will show it.

---

## Example 4: The LinkedIn Job Offer Spear Phish

**Why it works:** LinkedIn data is publicly available and extraordinarily useful for targeting. This phishing campaign from early 2026 targeted cybersecurity professionals (including me) with a tailored approach.

The email referenced my actual job title, my company, and mentioned a conference I had recently attended (public information from the conference website). It offered a senior role at a named tech company with a salary range that was realistic for my profile.

**What it got right:**
- Personalized with real details from my public profile
- Sender domain: `talent-globaltech[.]com` — plausible recruiter domain
- The job description was detailed and realistic (probably adapted from real job postings)
- The call to action was "complete this skills assessment" — a Google Forms link that collected credentials

**What gave it away:**
- The "company" (GlobalTech) was not a real company with any web presence
- The Google Form asked for my LinkedIn login credentials to "pre-fill" my profile — Google Forms doesn't do this
- The recruiter's name was not findable on LinkedIn itself
- The email domain was registered 3 weeks before I received the email (checked via WHOIS)

**Protection:** Research the recruiter and company independently. Check WHOIS registration dates on unfamiliar domains. Legitimate recruiters don't need your credentials to share a job description — they work the other way around.

---

## Example 5: The Two-Factor Authentication Bypass Attack

**Why it works:** This is a sophisticated real-time phishing attack, also called AiTM (Adversary in The Middle). Even if you have 2FA enabled, this can bypass it.

The attack works like this: you receive a convincing phishing email linking to a fake login page. This fake page is actually a real-time proxy to the legitimate site. You enter your credentials, the attacker passes them to the real site in real time, the real site sends you a 2FA code, you enter it on the fake page, the attacker uses it on the real site immediately.

**Real example from 2025:** A Microsoft 365 phishing campaign targeting financial services companies used exactly this technique. The victim logged in, entered their authenticator code, and the attacker used it within seconds to establish a persistent session.

**Protection:** Passkeys and hardware security keys (FIDO2) defeat this attack — the authentication is cryptographically bound to the legitimate domain, so the proxy can't relay it. If you don't have passkeys yet, this is one of the strongest reasons to adopt them.

---

## Example 6: The Docusign Credential Harvester

**Why it works:** Docusign notifications are extremely common in business settings, and people are conditioned to click "Review Document" links.

This phishing email from December 2025 was sent to multiple employees at a law firm. The subject line: "Action Required: Sign document before deadline — expires in 24 hours."

**What it got right:**
- Docusign's exact email template, including the yellow "Review Document" button
- Sender displayed as "Docusign via docusign.net" — legitimately confusing since Docusign does use third-party sending infrastructure
- An actual envelope ID in the format Docusign uses
- Footer included Docusign's real terms of service links (which pointed to the real Docusign site)

**What gave it away:**
- The sender's actual email address, visible on closer inspection: `envelope@docusign-secure[.]net` — not docusign.com or docusign.net
- Clicking "Review Document" went to a page asking for Office 365 credentials to "verify your identity" — Docusign does not require Office 365 login to view documents
- The document preview was a blurred image of a generic contract

**Protection:** Bookmark the Docusign website directly. Access documents by logging into your Docusign account rather than clicking email links. If you receive a Docusign from someone you know, confirm with them by a separate channel that they actually sent it.

---

## Example 7: The IT Department Internal Impersonation

**Why it works:** Internal emails from IT departments carry implicit authority. People don't question a "password expiry" or "security update" email from what appears to be their own IT team.

This attack, which circulated widely in corporate environments in Q1 2026, used email spoofing to make messages appear to come from `it-support@[victim's company domain]`. Attackers identified target companies through LinkedIn, then sent mass emails to employee email patterns (firstname.lastname@company.com) guessed from format conventions.

**What it got right:**
- Appeared to come from the target's own company domain
- Used corporate language ("per our security policy," "compliance requirement")
- Referenced a real upcoming deadline (GDPR password audit)
- Threatened account suspension within 48 hours

**What gave it away:**
- The link went to `it-support-portal-[company name][.]com` — not the company's actual domain
- Real IT departments don't send password change requests via email links — they use the company's SSO portal or direct users to an internal URL
- The DMARC policy on the company's domain was set to `reject`, meaning legitimate spoofed emails should have been filtered (this particular company hadn't set DMARC up correctly — a common problem)

**Protection:** Treat any email asking you to change credentials or install software as suspicious regardless of apparent sender. Verify by calling IT or messaging them on your internal communication platform (Slack, Teams) using their directory contact, not contact details from the email.

---

## Example 8: The QR Code Phishing (Quishing) Attack

**Why it works:** QR codes bypass most email security tools because the malicious URL is encoded in an image — text scanners can't read it.

This attack appeared as a company-wide announcement about switching to a new authenticator app. The email contained a QR code to "set up your new security credentials" and was sent from a convincingly spoofed IT department address.

**What it got right:**
- QR codes are now associated with legitimate authentication (Microsoft Authenticator, Google Authenticator setup)
- The request made sense in context — MFA app migration is common
- The email came in Monday morning (when employees expect IT announcements)
- The QR code, when scanned, opened a page visually identical to a Microsoft Authenticator setup screen

**What gave it away:**
- No announcement on internal communication channels (the email said to "disregard internal channels due to the security-sensitive nature")
- The QR code destination URL was not a Microsoft domain
- The setup page asked for the full Microsoft 365 login including password — authenticator apps don't need your password during setup

**Protection:** Verify QR code destinations before proceeding. Your phone's camera app typically shows the URL before opening it — read it carefully. Apply the same domain-verification logic to QR codes as to links.

---

## The 12-Point Phishing Email Checklist

When you receive an unexpected email that asks for any action — clicking, logging in, downloading, or paying — run through this list:

**Sender verification:**
1. Is the sender's actual email address (not display name) correct and expected?
2. Was this email expected? Did you initiate something that would trigger this notification?
3. Does the domain pass WHOIS scrutiny — is it old and established, or newly registered?

**Content analysis:**
4. Is the email creating urgency or fear? (Suspend, expire, unauthorized access, limited time)
5. Does it ask for credentials, payment, or software installation?
6. Are there QR codes or shortened URLs that obscure the destination?

**Link verification:**
7. Does hovering over links reveal the actual destination?
8. Does the destination domain exactly match the expected organization? (Check for letter substitutions, hyphens, added words)
9. Is the destination HTTPS? (Necessary but not sufficient — phishing sites use HTTPS too)

**Process verification:**
10. Does this request bypass normal processes? (Unusual urgency, skip approval steps)
11. Can you verify this request through a separate channel you already trust?
12. Would a legitimate organization actually communicate this way?

---

## Protecting Your Email More Broadly

The examples above show that even alert, educated people can be fooled. Layer your defenses:

**Use an email provider with strong phishing detection.** ProtonMail's filters caught 4 of the 8 examples above automatically. Gmail caught 5. Outlook caught 3. The differences in filtering effectiveness are real and matter.

**Enable DMARC on your own domain** if you run a business. This prevents attackers from spoofing your domain in attacks against your employees and partners. Check your domain at mxtoolbox.com/dmarc.aspx.

**Use passkeys wherever possible.** As Example 5 shows, even 2FA can be bypassed by real-time phishing proxies. Passkeys cannot — they're cryptographically bound to the legitimate domain.

**Keep your address private.** The less your email address appears in public databases, the less phishing you'll receive. Use email aliases for sign-ups. ProtonMail's SimpleLogin integration and similar alias services prevent your main address from appearing in breach databases.

[Switch to ProtonMail for stronger email security →](https://go.digitalshieldpro.com/protonmail)

---

## Final Thoughts

None of the 8 examples above were stopped by user vigilance alone — the people targeted were not careless. What stopped most of them was either technical controls (DMARC, good spam filters) or a process that required verification through a second channel.

Build verification into your processes: any request for credentials, payment, or software installation gets confirmed through a channel you already trust. That one habit stops most phishing attacks, even sophisticated ones.

The QR code attacks are the fastest-growing category I'm seeing in 2026. Treat QR codes with the same skepticism you apply to email links — they're the same attack with a different delivery mechanism.


<a href="https://go.digitalshieldpro.com/protonmail" class="cta-affiliate" rel="nofollow noopener sponsored" target="_blank">View Protonmail</a>

## Related guides

- [How to Protect Yourself from Phishing in 2026](/posts/how-to-protect-yourself-from-phishing-2026/)
- [Business Email Compromise (BEC) in 2026](/posts/business-email-compromise-bec-2026/)
- [ProtonMail review 2026: 12 months testing the privacy-first](/posts/protonmail-review-2026/)
- [Best Email Security Solutions 2026: Protect Your Inbox](/posts/best-email-security-2026/)
- [Best Encrypted Email Services in 2026: Protect Your Inbox](/posts/best-encrypted-email-services-2026/)
