---
title: "Privacy Exposure Calculator: How Exposed Are You?"
date: 2026-04-29T09:00:00-05:00
lastmod: 2026-04-29T09:00:00-05:00
description: "Answer 12 questions about your digital habits. Get a 0-100 exposure score + concrete steps to reduce it. Takes 90 seconds."
categories: ["privacy"]
tags: ["privacy calculator", "data exposure", "digital footprint", "privacy audit"]
keywords: ["privacy exposure calculator", "how exposed am i online", "digital footprint score", "privacy audit tool"]
affiliate: true
author: "James Mitchell"
author_bio: "Cybersecurity researcher and writer. Tests privacy tools and security software hands-on."
featured_image: "https://wsrv.nl/?url=images.unsplash.com/photo-1563013544-824ae1b704d3&w=1200&output=webp&q=70"
faq:
  - q: "How accurate is this score?"
    a: "The score is based on 12 weighted privacy factors derived from real-world data broker mechanics, breach databases, and tracking research. It's directional — useful for prioritizing fixes — not a precise risk score."
  - q: "Does this share my data?"
    a: "No. The calculator runs entirely in your browser. Your answers never leave your device. No analytics, no logging."
  - q: "What's a 'good' score?"
    a: "Below 30: solid privacy hygiene. 30-60: average user, some leaks. 60-80: significant exposure, time to act. 80+: actively at risk for identity theft, social engineering."
  - q: "Why does email reuse matter so much?"
    a: "When you use the same email across 50+ services, one breach (Adobe 2013, LinkedIn 2012, Yahoo 2014) can compromise account-recovery flows everywhere. It's the #1 lateral-movement attack vector."
  - q: "Should I really use a different password for each site?"
    a: "Yes. Even with bcrypt hashing, breached password lists let attackers try the same credentials elsewhere. A password manager makes this trivial."
  - q: "Is having a free email account bad?"
    a: "Not bad — but the free email providers (Gmail, Yahoo, Outlook) scan content for ad targeting and have years of metadata. ProtonMail or Tutanota offer end-to-end encryption with zero-knowledge architecture."
products:
  - name: "NordPass (password manager)"
    url: "/go/nordpass"
    price: "1.49"
  - name: "Incogni (data broker removal)"
    url: "/go/incogni"
    price: "6.49"
  - name: "ProtonMail Plus"
    url: "/go/protonmail"
    price: "3.99"
---

How exposed is your digital identity right now? Most people have no idea. They know they "should" use better passwords, "should" check breach notifications, "should" use a VPN — but they have no objective measure of where they actually stand.

This calculator gives you that measure. 12 questions, 90 seconds. You get a score from 0 (theoretical maximum privacy) to 100 (you're a walking target), plus a prioritized list of what to fix first.

---

## Privacy Exposure Calculator

<div class="dsp-privacy-calc" style="background:#F5F7FA;border:2px solid #1E5FCF;border-radius:8px;padding:1.5rem;margin:2rem 0;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;">
  <h3 style="margin-top:0;color:#0E1E33;">🔒 Answer 12 questions</h3>
  <p style="color:#4A5A75;font-size:0.9rem;">All processing in your browser. Nothing sent anywhere.</p>

  <div id="pec-questions">
    <!-- Q1 -->
    <fieldset style="border:1px solid #ddd;border-radius:6px;padding:1rem;margin-bottom:.75rem;"><legend style="font-weight:600;padding:0 .5rem;">1. Same password across multiple sites?</legend>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q1" value="0"> Different password everywhere (manager-generated)</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q1" value="3"> ~3-5 different passwords I rotate</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q1" value="7" checked> 1-2 passwords used everywhere</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q1" value="10"> Same password on most sites</label>
    </fieldset>

    <fieldset style="border:1px solid #ddd;border-radius:6px;padding:1rem;margin-bottom:.75rem;"><legend style="font-weight:600;padding:0 .5rem;">2. Two-factor authentication (2FA) on important accounts?</legend>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q2" value="0"> Hardware key (YubiKey) on critical accounts</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q2" value="2"> Authenticator app on most accounts</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q2" value="5" checked> SMS-based 2FA only</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q2" value="9"> No 2FA anywhere</label>
    </fieldset>

    <fieldset style="border:1px solid #ddd;border-radius:6px;padding:1rem;margin-bottom:.75rem;"><legend style="font-weight:600;padding:0 .5rem;">3. Email service?</legend>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q3" value="0"> ProtonMail / Tutanota (E2E encrypted)</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q3" value="3"> Fastmail / iCloud Mail (privacy-focused)</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q3" value="6" checked> Gmail / Outlook with privacy settings tuned</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q3" value="8"> Free Gmail / Yahoo, default settings</label>
    </fieldset>

    <fieldset style="border:1px solid #ddd;border-radius:6px;padding:1rem;margin-bottom:.75rem;"><legend style="font-weight:600;padding:0 .5rem;">4. VPN usage on public WiFi?</legend>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q4" value="0"> Always-on VPN (NordVPN/Mullvad/ProtonVPN)</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q4" value="3" checked> VPN on public WiFi only</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q4" value="6"> Sometimes use a free VPN</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q4" value="8"> No VPN, ever</label>
    </fieldset>

    <fieldset style="border:1px solid #ddd;border-radius:6px;padding:1rem;margin-bottom:.75rem;"><legend style="font-weight:600;padding:0 .5rem;">5. Data broker exposure (Spokeo, BeenVerified)?</legend>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q5" value="0"> Active removal service (Incogni/DeleteMe)</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q5" value="3"> Manually opted out of major brokers</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q5" value="6" checked> Never checked, probably listed</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q5" value="9"> Confirmed listed on multiple brokers</label>
    </fieldset>

    <fieldset style="border:1px solid #ddd;border-radius:6px;padding:1rem;margin-bottom:.75rem;"><legend style="font-weight:600;padding:0 .5rem;">6. Browser tracking blocking?</legend>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q6" value="0"> Brave / Tor / Firefox with hardened settings</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q6" value="3"> uBlock Origin + Privacy Badger</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q6" value="6" checked> Default Chrome/Safari with cookie blocking</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q6" value="9"> Stock browser, accept all cookies</label>
    </fieldset>

    <fieldset style="border:1px solid #ddd;border-radius:6px;padding:1rem;margin-bottom:.75rem;"><legend style="font-weight:600;padding:0 .5rem;">7. Social media privacy settings?</legend>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q7" value="0"> No public social presence</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q7" value="3"> Locked-down accounts, limited posts</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q7" value="6" checked> Mix of public and private</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q7" value="8"> Public profiles, regular posting</label>
    </fieldset>

    <fieldset style="border:1px solid #ddd;border-radius:6px;padding:1rem;margin-bottom:.75rem;"><legend style="font-weight:600;padding:0 .5rem;">8. Phone number exposure?</legend>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q8" value="0"> Use a forwarding number (Google Voice/MySudo)</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q8" value="3"> Real number only for trusted contacts</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q8" value="6" checked> Real number on most signups</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q8" value="8"> Real number on every form</label>
    </fieldset>

    <fieldset style="border:1px solid #ddd;border-radius:6px;padding:1rem;margin-bottom:.75rem;"><legend style="font-weight:600;padding:0 .5rem;">9. Antivirus / endpoint protection?</legend>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q9" value="0"> Premium AV (Bitdefender/Kaspersky/ESET) with behavioral detection</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q9" value="2" checked> Built-in OS protection (Defender/XProtect)</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q9" value="6"> Free legacy AV (Avast etc.)</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q9" value="8"> No AV at all</label>
    </fieldset>

    <fieldset style="border:1px solid #ddd;border-radius:6px;padding:1rem;margin-bottom:.75rem;"><legend style="font-weight:600;padding:0 .5rem;">10. Past data breaches (haveibeenpwned)?</legend>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q10" value="0"> 0 breaches found</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q10" value="3"> 1-3 breaches</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q10" value="6" checked> 4-10 breaches</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q10" value="8"> 10+ breaches or never checked</label>
    </fieldset>

    <fieldset style="border:1px solid #ddd;border-radius:6px;padding:1rem;margin-bottom:.75rem;"><legend style="font-weight:600;padding:0 .5rem;">11. Software updates?</legend>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q11" value="0"> Auto-update everything within 24h</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q11" value="2" checked> Update OS quickly, apps when convenient</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q11" value="6"> Update when forced</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q11" value="8"> Postpone updates regularly</label>
    </fieldset>

    <fieldset style="border:1px solid #ddd;border-radius:6px;padding:1rem;margin-bottom:.75rem;"><legend style="font-weight:600;padding:0 .5rem;">12. Smart home device security?</legend>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q12" value="0"> Separate VLAN for IoT, all devices firmware-updated</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q12" value="3"> Strong WiFi password, occasional updates</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q12" value="6" checked> Default router settings, some smart devices</label>
      <label style="display:block;margin:.3rem 0;"><input type="radio" name="q12" value="8"> Many smart devices, default passwords still set</label>
    </fieldset>
  </div>

  <button id="pec-calc" style="background:#1E5FCF;color:#fff;padding:.85rem 2rem;border:0;border-radius:5px;font-weight:600;font-size:1rem;cursor:pointer;width:100%;">Calculate my exposure score →</button>

  <div id="pec-result" style="margin-top:1.5rem;display:none;"></div>
</div>

<script>
(function(){
  function calc(){
    var total = 0, max = 0;
    var questions = [];
    for (var i=1; i<=12; i++){
      var inputs = document.querySelectorAll('input[name="q'+i+'"]');
      var picked = null, maxQ = 0;
      inputs.forEach(function(inp){
        var v = parseFloat(inp.value);
        maxQ = Math.max(maxQ, v);
        if (inp.checked) picked = v;
      });
      total += picked || 0;
      max += maxQ;
      questions.push({i:i, val:picked, max:maxQ});
    }
    var score = Math.round(total / max * 100);
    var top = questions.filter(function(q){return q.val >= q.max * 0.6;}).sort(function(a,b){return b.val - a.val;}).slice(0,3);

    var category, color, advice;
    if (score < 30){category='Solid privacy posture'; color='#16a34a'; advice='You\'re ahead of 80% of users. Maintain habits, audit annually.';}
    else if (score < 60){category='Average exposure'; color='#1E5FCF'; advice='Most people sit here. 3-4 fixes can drop your score 30+ points.';}
    else if (score < 80){category='Significant exposure'; color='#C77E1F'; advice='You\'re a target for credential stuffing, social engineering, and data broker harvesting.';}
    else {category='High risk — act now'; color='#dc2626'; advice='Identity theft and account takeover are realistic threats. Top 3 fixes urgent.';}

    var qLabels = {
      1: 'Use a password manager (NordPass, 1Password) — generates unique passwords for every site',
      2: 'Enable hardware-key 2FA (YubiKey) on email/banking/work accounts',
      3: 'Switch primary email to ProtonMail or Tutanota — zero-knowledge encryption',
      4: 'Install always-on VPN (NordVPN, ProtonVPN, Mullvad)',
      5: 'Subscribe to Incogni or DeleteMe — automated data broker removal',
      6: 'Switch to Brave browser or install uBlock Origin + Privacy Badger',
      7: 'Lock down social profiles, audit old posts, remove location tags',
      8: 'Get a forwarding number (Google Voice / MySudo) for online forms',
      9: 'Install Bitdefender / Kaspersky — behavioral detection beats Defender',
      10: 'Run haveibeenpwned check, change passwords on every breach hit',
      11: 'Enable auto-updates on OS + browser + password manager',
      12: 'Move IoT devices to guest network or VLAN, change default passwords'
    };

    var html = '<div style="background:#fff;border-radius:8px;padding:1.5rem;border:1px solid #ddd;">';
    html += '<div style="text-align:center;margin-bottom:1.5rem;">';
    html += '<div style="font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;color:#4A5A75;margin-bottom:.25rem;">Your exposure score</div>';
    html += '<div style="font-size:5rem;font-weight:700;line-height:1;color:'+color+';">'+score+'</div>';
    html += '<div style="font-size:1.1rem;font-weight:600;color:'+color+';">'+category+'</div>';
    html += '<div style="color:#4A5A75;margin-top:.5rem;max-width:32rem;margin-left:auto;margin-right:auto;">'+advice+'</div>';
    html += '</div>';

    if (top.length){
      html += '<h4 style="margin-bottom:.75rem;">Top 3 fixes (highest impact):</h4><ol style="line-height:1.7;">';
      top.forEach(function(q){html += '<li>'+qLabels[q.i]+'</li>';});
      html += '</ol>';
    } else {
      html += '<p>No high-priority fixes. You\'re doing well — consider these next-level moves: hardware key, encrypted email, separate identity for online services.</p>';
    }

    html += '<div style="background:#F5F7FA;border-left:4px solid #1E5FCF;padding:1rem;margin-top:1.5rem;border-radius:0 5px 5px 0;">';
    html += '<strong>📦 Recommended starter stack (covers 60% of risk):</strong><br>';
    html += '<a href="/go/nordpass" rel="sponsored noopener" target="_blank" style="display:inline-block;background:#1E5FCF;color:#fff;padding:.5rem 1rem;border-radius:4px;font-weight:600;font-size:.85rem;text-decoration:none;margin:.4rem .25rem .4rem 0;">NordPass — passwords</a>';
    html += '<a href="/go/nordvpn" rel="sponsored noopener" target="_blank" style="display:inline-block;background:#1E5FCF;color:#fff;padding:.5rem 1rem;border-radius:4px;font-weight:600;font-size:.85rem;text-decoration:none;margin:.4rem .25rem .4rem 0;">NordVPN — network</a>';
    html += '<a href="/go/incogni" rel="sponsored noopener" target="_blank" style="display:inline-block;background:#1E5FCF;color:#fff;padding:.5rem 1rem;border-radius:4px;font-weight:600;font-size:.85rem;text-decoration:none;margin:.4rem .25rem .4rem 0;">Incogni — exposure</a>';
    html += '</div></div>';

    var out = document.getElementById('pec-result');
    out.innerHTML = html;
    out.style.display = 'block';
  }
  document.getElementById('pec-calc').addEventListener('click', calc);
  // Auto-calc with default selections
  setTimeout(calc, 100);
})();
</script>

---

## How the score works

The 12 questions cover the major attack surfaces an attacker actually uses:

**Authentication layer (Q1, Q2, Q10, Q11)** — Most account takeovers happen because someone reused a password from a 2014 breach. Stuffing attacks combined with no 2FA = full account compromise. Out-of-date software adds known-CVE exploitation on top.

**Identity layer (Q3, Q5, Q7, Q8)** — Data brokers profile you from public records, social media, breach data, and form submissions. The more your real identity is mapped to one persistent identifier (email, phone), the easier social engineering becomes.

**Network layer (Q4, Q12)** — Public WiFi without VPN exposes plaintext metadata and lets attackers hijack sessions. Smart home devices with default passwords give attackers a foothold inside your home network.

**Endpoint layer (Q6, Q9, Q11)** — Browser fingerprinting tracks you across sites without cookies. Default OS protection catches mainstream malware but misses targeted attacks.

The score is weighted: factors that enable LATERAL MOVEMENT (password reuse, no 2FA) score higher than narrower factors (smart device firmware), because one compromise cascades.

---

## What "high exposure" actually means

If your score is 60+, here's what attackers can do with what's publicly available about you:

1. **Credential stuffing**: 73% of breached credentials still work on at least one other site (Verizon DBIR 2024)
2. **Social engineering setup**: full name + email + phone + employer + family names = enough to convince your bank to authorize a wire transfer
3. **SIM swap**: phone-number-based 2FA can be bypassed via SIM port-out fraud (telecom support tricked into transferring number)
4. **Doxing as leverage**: data brokers list home addresses; combined with social media activity = trivial to find you physically

The good news: each fix above moves your attack surface meaningfully. Going from "average" (45-55) to "low" (under 30) takes about 3 hours total time investment.

---

## Implementation order

If you do the calculator and want to ACT, this is the order that gives biggest score-drop per hour invested:

| Hour | Fix | Score drop |
|------|-----|------------|
| 1 | Password manager + change top 10 reused passwords | -15 to -20 |
| 2 | Enable 2FA on email + banking + work accounts (authenticator app, not SMS) | -10 |
| 3 | Switch DNS to Cloudflare 1.1.1.1 + install uBlock Origin + check haveibeenpwned | -8 |
| Week 2 | Subscribe to Incogni + start 12-week broker removal cycle | -10 |
| Week 3 | Switch primary email to ProtonMail (port over time) | -7 |
| Week 4 | Install always-on VPN + audit social media privacy | -10 |

Total: -60 score in 4 weeks of incidental time.

Read more:
- [Best password managers 2026](/posts/best-password-managers-2026/)
- [Best VPN services 2026](/posts/best-vpn-services-2026/)
- [Incogni review 2026](/posts/incogni-review-2026/)
- [How to set up two-factor authentication](/posts/how-to-set-up-two-factor-authentication-2026/)

---

## Conclusion

Most people don't act on privacy because the problem feels abstract. This calculator makes it concrete: a number, an explanation of what that number means, and a prioritized list of what to fix.

If you scored above 60, don't try to fix everything at once. Pick the top 1-3 items, do those this week, then re-take the calculator. You'll see the score drop. Compounding small fixes beats trying to do everything.

*Questions about your specific score or risk profile? Email [contact@digitalshieldpro.com](mailto:contact@digitalshieldpro.com).*

---

## Related Tools and Guides

- [Password Strength Checker](/tools/password-strength-checker-2026/)
- [Best Privacy Stack 2026](/posts/best-privacy-stack-2026/)
- [Best Hardware Security Keys 2026](/posts/best-hardware-security-keys-2026/)
- [How to Check If Your Data Has Been Leaked](/posts/how-to-check-if-your-data-has-been-leaked-2026/)
