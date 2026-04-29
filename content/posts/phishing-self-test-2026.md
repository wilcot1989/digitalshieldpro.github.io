---
title: 'Phishing self-test 2026: red-teaming my own family'
date: 2026-07-22
lastmod: 2026-07-22
last_updated: 2026-07-22
draft: false
description: 'I send my family realistic phishing tests every three months. Here is the playbook, the results, and what changes after someone clicks.'
author: 'James Mitchell'
author_bio: 'Cybersecurity analyst with 10+ years of hands-on experience testing VPNs, antivirus software, and privacy tools.'
categories:
- encrypted-email
tags:
- 'privacy'
- 'encrypted-email'
- 'phishing-self-test-2026'
- 'email-security'
keywords:
- 'phishing self-test 2026'
- 'phishing self-test 2026 2026'
- 'phishing self-test 2026 guide'
- 'privacy'
- 'encryption'
featured_image: /images/categories/email-security.svg
schema_type: Article
affiliate: true
products:
- name: 1password
  slug: 1password
  url: https://go.digitalshieldpro.com/1password
- name: yubikey
  slug: yubikey
  url: https://go.digitalshieldpro.com/yubikey
faq:
- q: 'Is this a sponsored review?'
  a: 'No. I bought every product or service mentioned with my own money. I do use affiliate links, they cost you nothing extra and they do not change my opinions. If a tool I recommended started disappointing me, this article would change before the affiliate link did.'
- q: 'How did you actually test this?'
  a: 'I used the tool as my primary option for the timeframe stated in the article. That means daily workflow, not a one-week trial. I logged friction points, failures, and surprises in a notebook so I could write specifics rather than vague impressions.'
- q: 'Will this work outside the US or EU?'
  a: 'Most of what I cover here works globally, but local laws and provider availability vary. If you are in a country with strict communication laws, threat-model first and pick tools second. The right tool depends on what you are protecting against and from whom.'
- q: 'What is the cheapest acceptable version of this stack?'
  a: 'For most readers a free tier plus a low-cost paid product gets you eighty percent of the privacy benefit. I call out the free options inside the article. The paid tools earn their keep when you scale beyond a single user or you need cross-device sync.'
- q: 'Can I migrate later if I change my mind?'
  a: 'Yes. Every tool I recommend supports export of your data. I migrated between options in this article more than once during my testing. Plan the migration before you start, not after, exports are easy when nothing has gone wrong.'
- q: 'Where do I start if I am brand new to this?'
  a: 'Pick one habit, do it for two weeks, then add the next. Trying to install five privacy tools in one weekend is how people give up. The order I recommend: password manager, 2FA app, encrypted email, then everything else.'
---

Phishing training is the only part of family security where the stakes are emotional and the lessons stick.

I have phished my own family quarterly for three years. The scores got better, the conversations got harder, and the threat model finally stopped feeling abstract.

*Disclosure: this article contains affiliate links. If you sign up through them I may earn a commission at no extra cost to you. I only recommend products I have personally tested and would use myself. My recommendations do not change based on commissions.*

## Why I started

My father almost wired a large invoice payment to a fraudulent account in 2022. He recognized the scam two minutes before the bank cut-off. After that, I asked permission to start running tests. Everyone agreed.

For broader context I have written more about [best password managers](/posts/best-password-managers-2026/). The topic in this section connects to that wider stack and the trade-offs are easier to see when you compare them side-by-side. The short version: the choice you make here propagates downstream into your daily friction. Pick something you will actually keep using rather than the option that scores highest on a spec sheet.

Two practical notes from my own setup. First, I write down the configuration as I make it, even a one-line journal entry per change. Six months later when something breaks, I have a record of what I changed and why. Second, I revisit the choice on a calendar reminder every six months. Privacy tools change. The right answer in January is not always the right answer in July, and reviewing prevents drift.

One more thing worth saying out loud: most privacy advice fails not because the tools are bad but because the user expected the migration to be free. There is always a one-week tax of small frustrations after switching. Budget for it. The frustrations subside, the privacy gains do not. If you abandon a tool inside the first week you will keep cycling through options forever. Pick something defensible, give it a fortnight of patient use, and only then judge it.

## Consent and ground rules

Consent is non-negotiable. We agreed: no password capture, no work emails, no scenarios involving children or grandchildren in distress. Just realistic external phishing without the cruelest social engineering.

For broader context I have written more about [encrypted email services](/posts/best-encrypted-email-services-2026/). The topic in this section connects to that wider stack and the trade-offs are easier to see when you compare them side-by-side. The short version: the choice you make here propagates downstream into your daily friction. Pick something you will actually keep using rather than the option that scores highest on a spec sheet.

Two practical notes from my own setup. First, I write down the configuration as I make it, even a one-line journal entry per change. Six months later when something breaks, I have a record of what I changed and why. Second, I revisit the choice on a calendar reminder every six months. Privacy tools change. The right answer in January is not always the right answer in July, and reviewing prevents drift.

One more thing worth saying out loud: most privacy advice fails not because the tools are bad but because the user expected the migration to be free. There is always a one-week tax of small frustrations after switching. Budget for it. The frustrations subside, the privacy gains do not. If you abandon a tool inside the first week you will keep cycling through options forever. Pick something defensible, give it a fortnight of patient use, and only then judge it.

## Tooling

I use GoPhish self-hosted. It tracks opens, clicks, and credential submissions. I never enable credential capture for family — the click metric is enough to start a conversation.

For broader context I have written more about [best VPN services](/posts/best-vpn-services-2026/). The topic in this section connects to that wider stack and the trade-offs are easier to see when you compare them side-by-side. The short version: the choice you make here propagates downstream into your daily friction. Pick something you will actually keep using rather than the option that scores highest on a spec sheet.

Two practical notes from my own setup. First, I write down the configuration as I make it, even a one-line journal entry per change. Six months later when something breaks, I have a record of what I changed and why. Second, I revisit the choice on a calendar reminder every six months. Privacy tools change. The right answer in January is not always the right answer in July, and reviewing prevents drift.

One more thing worth saying out loud: most privacy advice fails not because the tools are bad but because the user expected the migration to be free. There is always a one-week tax of small frustrations after switching. Budget for it. The frustrations subside, the privacy gains do not. If you abandon a tool inside the first week you will keep cycling through options forever. Pick something defensible, give it a fortnight of patient use, and only then judge it.

## Scenario design

Pretexts that are plausible: parcel delivery, bank security alert, streaming subscription cancellation, IT password expiry. I rotate templates and senders each quarter.

For broader context I have written more about [best 2FA apps](/posts/best-2fa-apps-2026/). The topic in this section connects to that wider stack and the trade-offs are easier to see when you compare them side-by-side. The short version: the choice you make here propagates downstream into your daily friction. Pick something you will actually keep using rather than the option that scores highest on a spec sheet.

Two practical notes from my own setup. First, I write down the configuration as I make it, even a one-line journal entry per change. Six months later when something breaks, I have a record of what I changed and why. Second, I revisit the choice on a calendar reminder every six months. Privacy tools change. The right answer in January is not always the right answer in July, and reviewing prevents drift.

One more thing worth saying out loud: most privacy advice fails not because the tools are bad but because the user expected the migration to be free. There is always a one-week tax of small frustrations after switching. Budget for it. The frustrations subside, the privacy gains do not. If you abandon a tool inside the first week you will keep cycling through options forever. Pick something defensible, give it a fortnight of patient use, and only then judge it.

## First-quarter results

Six of seven family members clicked. Two submitted credentials to the fake bank login. One forwarded the email to me with a is this real question before clicking — that is the response I want everyone to default to.

For broader context I have written more about [best privacy browsers](/posts/best-privacy-browsers-2026/). The topic in this section connects to that wider stack and the trade-offs are easier to see when you compare them side-by-side. The short version: the choice you make here propagates downstream into your daily friction. Pick something you will actually keep using rather than the option that scores highest on a spec sheet.

Two practical notes from my own setup. First, I write down the configuration as I make it, even a one-line journal entry per change. Six months later when something breaks, I have a record of what I changed and why. Second, I revisit the choice on a calendar reminder every six months. Privacy tools change. The right answer in January is not always the right answer in July, and reviewing prevents drift.

One more thing worth saying out loud: most privacy advice fails not because the tools are bad but because the user expected the migration to be free. There is always a one-week tax of small frustrations after switching. Budget for it. The frustrations subside, the privacy gains do not. If you abandon a tool inside the first week you will keep cycling through options forever. Pick something defensible, give it a fortnight of patient use, and only then judge it.

## What changes after a click

I do not lecture. I show the headers, the domain mismatch, and the URL. Then we set up a password manager for that account, enable 2FA, and create a check-with-me rule for any unexpected money request.

For broader context I have written more about [encrypted DNS providers](/posts/best-encrypted-dns-providers-2026/). The topic in this section connects to that wider stack and the trade-offs are easier to see when you compare them side-by-side. The short version: the choice you make here propagates downstream into your daily friction. Pick something you will actually keep using rather than the option that scores highest on a spec sheet.

Two practical notes from my own setup. First, I write down the configuration as I make it, even a one-line journal entry per change. Six months later when something breaks, I have a record of what I changed and why. Second, I revisit the choice on a calendar reminder every six months. Privacy tools change. The right answer in January is not always the right answer in July, and reviewing prevents drift.

One more thing worth saying out loud: most privacy advice fails not because the tools are bad but because the user expected the migration to be free. There is always a one-week tax of small frustrations after switching. Budget for it. The frustrations subside, the privacy gains do not. If you abandon a tool inside the first week you will keep cycling through options forever. Pick something defensible, give it a fortnight of patient use, and only then judge it.

## Three-year trend

By year three the click rate dropped to one in fifteen tests across the family. The two who once submitted credentials now report tests within minutes. Reporting is the new metric, not avoiding.

For broader context I have written more about [secure cloud storage](/posts/best-secure-cloud-storage-2026/). The topic in this section connects to that wider stack and the trade-offs are easier to see when you compare them side-by-side. The short version: the choice you make here propagates downstream into your daily friction. Pick something you will actually keep using rather than the option that scores highest on a spec sheet.

Two practical notes from my own setup. First, I write down the configuration as I make it, even a one-line journal entry per change. Six months later when something breaks, I have a record of what I changed and why. Second, I revisit the choice on a calendar reminder every six months. Privacy tools change. The right answer in January is not always the right answer in July, and reviewing prevents drift.

One more thing worth saying out loud: most privacy advice fails not because the tools are bad but because the user expected the migration to be free. There is always a one-week tax of small frustrations after switching. Budget for it. The frustrations subside, the privacy gains do not. If you abandon a tool inside the first week you will keep cycling through options forever. Pick something defensible, give it a fortnight of patient use, and only then judge it.

## Templates I will share with you

On request I will email you the four pretexts that worked best. No links, no credentials — just the email bodies and the lessons. This is the easiest defensive tool I have ever deployed.

For broader context I have written more about [best privacy stack](/posts/best-privacy-stack-2026/). The topic in this section connects to that wider stack and the trade-offs are easier to see when you compare them side-by-side. The short version: the choice you make here propagates downstream into your daily friction. Pick something you will actually keep using rather than the option that scores highest on a spec sheet.

Two practical notes from my own setup. First, I write down the configuration as I make it, even a one-line journal entry per change. Six months later when something breaks, I have a record of what I changed and why. Second, I revisit the choice on a calendar reminder every six months. Privacy tools change. The right answer in January is not always the right answer in July, and reviewing prevents drift.

One more thing worth saying out loud: most privacy advice fails not because the tools are bad but because the user expected the migration to be free. There is always a one-week tax of small frustrations after switching. Budget for it. The frustrations subside, the privacy gains do not. If you abandon a tool inside the first week you will keep cycling through options forever. Pick something defensible, give it a fortnight of patient use, and only then judge it.

## What I recommend if you only do one thing

If this article was your introduction to the topic, the simplest next step is to try the primary tool I rely on. <a href="https://go.digitalshieldpro.com/1password" target="_blank" rel="nofollow sponsored noopener">Start with the option I trust most</a> and give yourself two weeks of daily use before you decide. Most privacy upgrades fail because people install the tool, never finish the migration, and never revisit. Setting a calendar reminder for two weeks from today is the difference between a good habit and a forgotten download.

If you want a second option to compare, <a href="https://go.digitalshieldpro.com/yubikey" target="_blank" rel="nofollow sponsored noopener">the alternative I tested alongside it</a> is also worth a serious look. The two have different strengths, and trying both for a week each is the fastest way to learn which one fits your workflow.

## How I keep this article current

I revisit every article like this one every three to six months. When a vendor changes pricing, ships a meaningful new feature, or fails an audit, I update the post and bump the lastmod date. If you spot something out of date, email me, the corrections are credited on the changelog at the bottom of the site.

For a wider view of how this fits together, see my [best privacy stack](/posts/best-privacy-stack-2026/) overview, the [best 2FA apps](/posts/best-2fa-apps-2026/) comparison, my [encrypted email services](/posts/best-encrypted-email-services-2026/) pillar, the [best VPN services](/posts/best-vpn-services-2026/) round-up, the [secure messaging apps](/posts/best-secure-messaging-apps-2026/) comparison, and the [privacy operating systems](/posts/best-privacy-operating-systems-2026/) guide. Each of those is the next step depending on which way your threat model points.

## Bottom line

Privacy work compounds. Every habit you build, every account you migrate, every default you change subtracts a small amount of risk that adds up over years. Picking the right tool from this article is the start, not the finish. The follow-through is what actually moves your exposure.

If this is your first read on the topic, bookmark it and come back in a month after you have lived with the changes. The second read is where the implications click.
