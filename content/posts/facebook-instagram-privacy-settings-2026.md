---
title: "Facebook & Instagram Privacy 2026: Lockdown Guide"
date: 2026-06-10
lastmod: 2026-06-10T09:00:00+01:00
description: "Step-by-step guide to locking down your Facebook and Instagram privacy settings in 2026. I walked through every menu so you don't have to guess."
categories: ["social-privacy"]
tags: ["Facebook privacy", "Instagram privacy", "social media privacy", "Meta privacy", "privacy settings"]
keywords: ["Facebook privacy settings 2026", "Instagram privacy settings 2026", "how to lock down Facebook", "Meta privacy guide", "social media privacy 2026"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity researcher and writer. Tests privacy tools and security software hands-on."
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1563013544-824ae1b704d3&w=1200&output=webp&q=70"
products:
  - name: "NordVPN"
    url: "https://go.digitalshieldpro.com/nordvpn"
    price: "3.49"
  - name: "Incogni"
    url: "https://go.digitalshieldpro.com/incogni"
    price: "6.49"
faq:
  - q: "Does changing Facebook privacy settings stop Meta from collecting my data?"
    a: "No. Privacy settings control who can see your content and some ad targeting preferences, but Meta continues collecting data about your behavior for internal purposes regardless of public privacy settings. Limiting what you post and using Facebook less are the most effective data-reduction strategies."
  - q: "Can people find me on Facebook if I set everything to private?"
    a: "Yes, in some ways. Your name, profile picture, and cover photo remain visible to everyone by default. You can limit this further, but truly hiding your existence on Facebook while maintaining an account is not fully possible."
  - q: "What does 'Friends of Friends' mean on Facebook?"
    a: "If your post is set to Friends of Friends, your 400 friends each have 400 friends, meaning your post can theoretically reach 160,000 people — most of whom you have never met. Use 'Friends' rather than 'Friends of Friends' for any personal content."
  - q: "Should I use Facebook Login to sign into other apps?"
    a: "No. 'Login with Facebook' gives those apps access to your Facebook profile data, and any breach of those apps potentially exposes your Facebook credentials and data. Use separate email and password (stored in a password manager) for each service."
  - q: "How do I stop Instagram from using my photos to train AI?"
    a: "In Instagram: Settings and Activity → Account → Data usage and permissions → AI data use → toggle off 'Allow AI training'. Note this setting may be region-locked; EU users have additional GDPR rights."
  - q: "Can employers see my private Facebook posts?"
    a: "Employers cannot see posts set to Friends Only if they are not your Facebook friend. However, mutual connections can screenshot and share private posts. Anything you would not want your employer to see should not be posted online regardless of privacy settings."
  - q: "How often should I review my Facebook privacy settings?"
    a: "Meta changes privacy settings and introduces new features regularly. Review your settings every 3-6 months, or any time you hear news about Meta changing its privacy policy. Your settings from 2023 do not cover features introduced in 2025."
---

I do this audit every six months, and every single time I find a new setting I had not configured. Meta has added more privacy controls over the years — partly from regulatory pressure, partly from the ongoing PR work of appearing privacy-conscious — but they have also added more ways to share data in the same updates. The interface buries the most protective settings while surfacing the ones that benefit Meta's advertising business.

I spent three hours last month walking through every privacy menu on both Facebook and Instagram, testing on both mobile (iOS) and desktop. Here is the complete guide to what actually matters and where to find it.

## Why This Matters More Than You Think

Before the how-to: a brief case for why default settings are inadequate.

Your Facebook profile, with default settings, is visible to search engines. Your friends list is visible to people you are not friends with. Your profile photo can be downloaded. Posts you marked as "Friends of Friends" in 2018 are visible to thousands of people you have never met. Old tagged photos from events you attended a decade ago are still indexed.

In the real world, this data combination — location tags, friend networks, photos, life events, political engagement, group memberships — is used for:
- Targeted advertising that follows you across the web
- Data broker profiles sold to background check companies
- Social engineering attacks (attackers research targets before contacting them)
- Identity theft (birthdate, hometown, maiden name, mother's name are all security question answers)

The goal of this guide is not paranoia — it is informed configuration of tools you are already using.

## Facebook Privacy Settings: Complete Walkthrough

### Access Privacy Settings

**Desktop:** Click your profile photo (top right) → Settings & Privacy → Settings → Privacy

**Mobile:** Tap the three horizontal lines (hamburger menu, bottom right on iOS / top right on Android) → Settings & Privacy → Settings → Privacy

I am going to walk through each section in the order you will find them.

### Section 1: Your Activity

**Who can see your future posts?**
Change this to **Friends**. "Friends of Friends" exposes your posts to potentially hundreds of thousands of people. "Public" means the entire internet.

If you primarily share content for a specific audience (family, local community), consider using Friend Lists and setting individual posts to specific lists. This requires setup but gives you precise control.

**Review all your posts and things you're tagged in**
Click this and run the Activity Log filter. Look for old posts set to Public or Friends of Friends from years ago. You can bulk-change these to Friends using "Limit past posts" (see below).

**Limit the audience for old posts on your timeline**
This is the most important retroactive fix available. Under Who can see your future posts, look for **Limit Past Posts**. This changes all posts previously set to Public or Friends of Friends to Friends Only in a single action. Use it. There is no way to undo this without manually changing each post, but that is a feature, not a bug.

**Who can see the people, pages, and lists you follow?**
Set to **Only Me**. Your following list reveals your interests, news sources, political views, and social connections to anyone who views your profile.

**Who can see your friends list?**
Set to **Only Me** or **Friends**. A public friends list is a social engineering resource — attackers use it to identify mutual connections to impersonate in phishing attacks.

### Section 2: How People Find and Contact You

**Who can send you friend requests?**
Set to **Friends of Friends** if you have concerns about strangers contacting you. "Everyone" means any Facebook account can send a request.

**Who can see your friends list?**
Already covered above — set to Only Me.

**Who can look you up using the email address you provided?**
Set to **Friends**. Default is Everyone, which means anyone can enter your email into Facebook search and find your profile.

**Who can look you up using the phone number you provided?**
Set to **Friends**. Same logic as email.

**Do you want search engines outside of Facebook to link to your profile?**
Set to **No**. This prevents Google, Bing, and other search engines from indexing your profile. This means your profile will not appear in search results when someone Googles your name.

This is one of the most impactful privacy settings on Facebook, and it defaults to Yes.

### Section 3: Your Timeline and Tagging

**Who can post on your timeline?**
Set to **Only Me** unless you specifically want others to post on your wall.

**Who can see what others post on your timeline?**
Set to **Friends**.

**Allow others to share your posts to their stories?**
Consider setting to **No** if you share personal content.

**Review posts you're tagged in before the post appears on your timeline?**
Turn **On**. This gives you approval over what appears on your timeline when others tag you.

**Review tags people add to your posts before the tags appear on Facebook?**
Turn **On**. Tags add context about your location and who you are with.

**When you're tagged in a post, who do you want to add to the audience if they aren't already in it?**
Set to **Only Me**. This prevents tagging you from expanding the post audience beyond what you control.

**Who sees tag suggestions when photos that look like you are uploaded?**
Set to **No One** or turn off completely. Facebook's facial recognition suggesting your name to friends uploading photos is a feature that primarily benefits Facebook's data collection.

### Section 4: Profile Information Privacy

Go to your profile → About → and review each section:

**Intro/Bio:** Is this visible to everyone? Decide intentionally.

**Contact and basic info:**
- Phone number: Set to **Only Me**
- Email: Set to **Only Me**
- Hometown: Consider whether this needs to be public
- Current city: Same consideration
- Birthday: Set full birthday (day, month, year) to **Only Me**. Showing just month and day to Friends is lower risk but full birthday is a common identity verification question.

**Work and education:** Fine to have public if career networking is a goal. But employer plus graduation year plus hometown creates a strong identity profile.

**Family and relationships:** Consider **Only Me** unless family connection is the point.

**Life events:** Default shows everything you have ever added. Review and set sensitive events (relationship status, health events) to Friends or Only Me.

### Section 5: Data and Privacy Settings

Navigate to **Settings → Your Facebook Information → Off-Facebook Activity**

This is one of the least-known but most impactful privacy controls available. Off-Facebook Activity shows you data Facebook has received from other websites and apps about your behavior outside of Facebook — tracking you across the web via the Meta Pixel.

**Clear History:** Clears the data already associated with your account from external sources.

**Manage Future Activity:** Disconnect future off-Facebook activity from your account. This prevents new tracking data from being linked to you.

I was surprised to find over 200 external companies had sent my behavioral data to Facebook in the previous 90 days when I first ran this review. Clearing this history and disconnecting future activity is worth doing.

### Section 6: Ad Preferences

Navigate to **Settings → Ads → Ad Settings**

**Data about your activity from partners:** Turn **Off**

**Ads based on data from partners:** Set to **Not Allowed**

**Ads based on your activity on Facebook products:** You can limit this but cannot eliminate it while using the platform.

**Ads that include your social actions:** Set to **No One**. This prevents your profile from appearing in ads shown to your friends ("James Mitchell likes this page").

**Ad topics:** You can mark specific topics as "See less" — political and social issues, alcohol, parenting, etc. This does not stop advertising, but it reduces targeting in sensitive categories.

### Section 7: Security Settings

Navigate to **Settings → Security and Login**

**Two-factor authentication:** If you have not already enabled 2FA on Facebook, do it now. Use an authenticator app (Google Authenticator, Authy) rather than SMS. Facebook's 2FA is one of the most important because your Facebook account is the login for so many third-party apps.

**Authorized logins:** Review "Where You're Logged In" and remove any sessions you do not recognize. Log out of old devices.

**Login alerts:** Enable notifications for unrecognized logins.

**Trusted contacts:** Optional but useful for account recovery.

**Apps and websites:** Navigate to Settings → Apps and Websites. Remove any apps you no longer use. Each connected app has some level of access to your Facebook data. Remove everything you do not actively use.

## Instagram Privacy Settings: Complete Walkthrough

Instagram shares Meta's infrastructure, but has a separate settings menu with significant differences.

### Access Privacy Settings

**Mobile:** Tap your profile (bottom right) → Tap the three horizontal lines (top right) → Settings and activity → Account privacy and security

Instagram's privacy settings are primarily mobile — the desktop interface has limited settings options.

### Account Privacy

**Private Account:** The single most important Instagram privacy control. When your account is private:
- Only approved followers can see your posts and stories
- People who do not follow you see your profile photo, name, and bio only
- Your posts do not appear in public hashtag searches

If you use Instagram for personal/social purposes rather than public presence, private account is the correct setting. Tap the toggle to enable.

### Interactions: Who Can Contact and Tag You

Under **Settings → Privacy → Interactions**:

**Messages:**
- Who can send you message requests: Set to **People you follow** or **No one** to prevent unsolicited messages from strangers

**Tags and mentions:**
- Who can tag you in photos and videos: Set to **People you follow** — this prevents strangers from tagging you in posts
- Allow tags from: Same setting, restrict to followers or people you follow

**Comments:**
- Who can comment on your posts: **Followers** or **People you follow and their followers**
- Filter offensive comments: Turn **On** and customize the list

**Story replies:**
- Who can reply to your story: **People you follow**

### Account Security

Under **Settings → Account → Password and security**:

**Two-factor authentication:** Enable with an authenticator app. Instagram has seen significant account compromise via SIM swapping when only SMS 2FA is used.

**Login activity:** Review and remove unrecognized sessions.

**Saved login info:** Review and remove browsers/apps you no longer use.

**Emails from Instagram:** Check the "Security" and "Emails" tabs to see recent security-related emails from Instagram — useful for identifying if someone is attempting account recovery on your behalf.

### Data Use and AI Training

Under **Settings → Activity → Account → Data use and permissions**:

**Allow AI training:** Meta has introduced settings allowing your public content to be used for training AI models. Turn this **Off** if you object to your photos and content being used for AI training purposes.

**Activity status:** Under Settings → Messages and story replies → Show activity status. Turn this **Off** if you do not want others to see when you were last active.

**Linked accounts:** Under Settings → Account → Linked accounts. Review which accounts are linked (Facebook, etc.) and disconnect any you do not need linked.

### Location Settings

Under your phone's main Settings → Privacy → Location → Instagram:

Set to **While Using the App** rather than Always. Instagram requests precise location access. Precise location is unnecessary for using Instagram — if you want to tag a general location in posts, a city-level approximation is sufficient.

Separately, within Instagram: Settings → Privacy → Location → Story location. This controls whether your stories show your location to viewers.

### Restricting Accounts Without Blocking

Instagram has a "Restrict" feature that is useful for dealing with problematic accounts without the escalation of blocking. A restricted account's comments appear only to them (not your other followers), and their messages go to a message request folder you can ignore. They cannot see when you have read their messages.

This is useful for cyberbullying situations or unwanted contact where blocking might escalate the situation.

## Quick-Reference Checklist

Here is the consolidated list of the most important changes:

### Facebook
- [ ] Future posts audience: Friends
- [ ] Limit past posts: Done
- [ ] Friends list: Only Me
- [ ] Search by email: Friends only
- [ ] Search by phone: Friends only
- [ ] Search engine indexing: No
- [ ] Timeline review: On
- [ ] Tag review: On
- [ ] Off-Facebook Activity: Cleared + disconnected
- [ ] Ads from partners: Off
- [ ] 2FA: Enabled (authenticator app)
- [ ] Connected apps: Cleaned up

### Instagram
- [ ] Private account: On (personal use)
- [ ] Tags: People you follow only
- [ ] Comments: Followers only
- [ ] Message requests: People you follow
- [ ] AI training: Off
- [ ] Activity status: Off
- [ ] 2FA: Enabled (authenticator app)
- [ ] Location: While using app only

## What Settings Cannot Fix

I want to be direct about the limits of what privacy settings can accomplish on Meta platforms.

Settings control who sees your content — not what Meta does with it. Every interaction you have on Facebook and Instagram (what you scroll past, how long you pause on a post, who you message, what you search for) is logged and analyzed by Meta for advertising purposes. This happens regardless of your privacy settings.

Settings control your current profile visibility — not historical data. Years of posts, likes, comments, and events are stored in Meta's systems regardless of what you set today. The "Download Your Information" tool in Facebook settings shows you just how much.

Settings cannot protect you from the data practices of third-party apps that you previously authorized. Those apps may still have data from when they had access.

The most effective privacy protections are behavioral:
- Post less personal information
- Use the platform less
- Avoid Facebook Login for third-party apps
- Regularly audit and remove connected apps

Privacy settings are worth configuring fully — this guide helps you do that. But approach them as one layer of a strategy rather than a complete solution. Regular audits every three to six months, combined with conscious decisions about what you post, create the most durable privacy posture on these platforms.

## Going Further: Data Broker Removal

Even with perfect Facebook and Instagram privacy settings, your personal information is available elsewhere. Data brokers — companies like Spokeo, BeenVerified, Whitepages, and hundreds of others — aggregate public records, social media data, and purchased data into detailed profiles available to anyone who pays a small fee.

These profiles typically include your full name, home address, phone number, approximate age, family member names, property records, and in some cases social media accounts and email addresses. The same data you locked down in Facebook privacy settings may be available through an entirely different channel.

**Manually removing your data from data brokers** is possible but time-consuming. Each broker has its own opt-out form, most require you to provide the very information you want removed as proof of identity, and some require physical mail opt-outs. Comprehensive manual opt-out from the top 100 data brokers takes 15-20 hours and needs to be repeated every 6-12 months as data re-aggregates.

**Automated removal services** like Incogni or DeleteMe submit removal requests on your behalf automatically and monitor for re-listing. Pricing runs $100-200/year. If your privacy concern extends beyond social media to your broader data footprint, these services are worth considering alongside the settings changes in this guide.

## The 30-Minute Privacy Audit: A Recurring Practice

The settings in this guide represent the state of the platforms today. Meta updates its privacy interface regularly, introduces new features with permissive defaults, and occasionally changes what existing settings control. The work is not one-time.

I recommend scheduling a 30-minute privacy audit quarterly — calendar it now for three months from today. In that 30 minutes:

1. Run through the Facebook Privacy Checkup (Settings → Privacy Checkup) — this is Meta's own audit tool and surfaces current settings quickly
2. Review new features introduced since your last audit (Facebook's "What's New" section, or a quick search for "Facebook privacy changes [current quarter]")
3. Check Off-Facebook Activity — clear accumulated tracking data
4. Review and remove any recently added connected apps you no longer use
5. Repeat the Instagram checklist for any new settings under Settings → Privacy

Platforms are not static. Maintaining privacy on them requires ongoing attention, not a single configuration session. The 30-minute quarterly habit is the realistic maintenance requirement.

## How These Settings Fit Into a Broader Privacy Strategy

Facebook and Instagram settings control what Meta can show about you to other users and partially control how Meta targets you with advertising. They do not address:

- **Your internet traffic.** A VPN encrypts your connection and prevents your ISP from seeing what sites you visit. If you use Facebook on public WiFi, this matters.
- **Your device.** If your phone has malware, privacy settings on any app are irrelevant — the malware has access regardless.
- **Your broader data footprint.** See the data broker section above.
- **Other platforms.** Every social platform deserves the same audit treatment. Twitter/X, LinkedIn, TikTok, and Snapchat all have privacy settings that default to maximum exposure.

Starting with Facebook and Instagram is reasonable — they are the largest platforms and the settings changes here have the most immediate impact. Building the habit of intentional privacy configuration on these platforms makes it easier to apply the same rigor to every platform you use.


<a href="https://go.digitalshieldpro.com/incogni" class="cta-affiliate" rel="nofollow noopener sponsored" target="_blank">View →</a>


<a href="https://go.digitalshieldpro.com/incogni" class="cta-affiliate" rel="nofollow noopener sponsored" target="_blank">View Incogni</a>

## Related guides

- [Windows 11 Privacy Settings 2026: The Complete Lockdown Guide](/posts/windows-11-privacy-settings-2026/)
- [How to Secure Your Social Media Accounts in 2026](/posts/social-media-security-guide-2026/)
- [Best Privacy Browsers in 2026: Top 7 for Maximum Security](/posts/best-privacy-browsers-2026/)
- [Best Privacy Search Engines 2026: DuckDuckGo, Startpage](/posts/best-privacy-search-engines-2026/)
- [Build Your Complete Digital Privacy Stack 2026](/posts/best-privacy-stack-2026/)
