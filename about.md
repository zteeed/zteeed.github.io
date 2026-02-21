---
layout: page
title: About
---

# About me

![](/images/pics/github.png){:style="float: left;margin-right: 15px;margin-bottom: 10px; width: 150px"}

Hi 👋, I'm Aurélien

**DevOps/SRE & cybersecurity enthusiast.** I design and automate cloud-native infrastructure (Kubernetes, observability, secrets management) and try to stay sharp as much as possible on the security side: web and application security, internal CTFs, and hands-on offensive challenges.

I work as a **freelance DevOps/SRE engineer**, with a focus on building and hardening infrastructures, CI/CD, and monitoring. I’ve contributed to production-grade tooling and I run my own systems end-to-end, from servers and automation to observability.

**Security** is a core part of my profile. I was **president of [HackademINT](https://www.hackademint.org)**, the InfoSec club of [Télécom SudParis](https://www.telecom-sudparis.eu/). I regularly take part in **Capture The Flag** events with [T35H](https://ctftime.org/team/45998) and [HackademINT](https://ctftime.org/team/30462). In **Carrefour’s internal CTF 2025** I placed **1st out of 102** Carrefour internal employees worldwide (🇧🇷 Brazil, 🇫🇷 France, 🇪🇸 Spain, 🇷🇴 Romania, etc.), and I’ve placed in the top tiers at BreizhCTF 🏴, InsHack, Mars@Hack, and others (see [awards](/awards)). I enjoy web vulnerability research (e.g. SSRF, GraphQL, modern API security), binary exploitation, and Android security, and I write technical [blog posts](/articles) on DevOps and security when I run into problems worth sharing.

I also have deep experience in **large-scale web scraping** and **bypassing anti-bot protections** (e.g. 🔍 Google, ▶️ YouTube, 🛡️ Cloudflare, …).

Outside work: Linux daily driver 💻 🐧, table tennis 🏓, and my own homelab (24U rack, servers, home automation).

<br>
**Next steps:** [Resume](/resume) · [Projects (GitHub)](https://github.com/zteeed) · [Awards](/awards) · [Articles](/articles)
<br><br>

<link rel="stylesheet" href="{{ '/css/fontawesome-6-all.css' | prepend: site.baseurl | replace: '//', '/' }}">
<style>
  /* HTB badge replica - from labs.hackthebox.com/achievement/badge/190724/215 */
  .htb-replica { width: 320px; background: #1B2027; border-radius: 12px; overflow: hidden; box-sizing: border-box; font-family: system-ui, -apple-system, sans-serif; }
  .htb-replica .htb-banner { height: 90px; background-color: #151820; background-image: radial-gradient(ellipse 120% 100% at 0% 0%, rgba(159, 239, 0, 0.25) 0%, transparent 55%), url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24'%3E%3Ccircle fill='%23333' cx='4' cy='4' r='0.8'/%3E%3Ccircle fill='%23333' cx='12' cy='4' r='0.8'/%3E%3Ccircle fill='%23333' cx='20' cy='4' r='0.8'/%3E%3Ccircle fill='%23333' cx='4' cy='12' r='0.8'/%3E%3Ccircle fill='%23333' cx='12' cy='12' r='0.8'/%3E%3Ccircle fill='%23333' cx='20' cy='12' r='0.8'/%3E%3Ccircle fill='%23333' cx='4' cy='20' r='0.8'/%3E%3Ccircle fill='%23333' cx='12' cy='20' r='0.8'/%3E%3Ccircle fill='%23333' cx='20' cy='20' r='0.8'/%3E%3C/svg%3E"); }
  .htb-replica .htb-icon-wrap { width: 80px; height: 80px; margin: -42px auto 0; border-radius: 50%; border: 2px dashed #9fef00; background: #1B2027; display: flex; align-items: center; justify-content: center; position: relative; z-index: 1; }
  .htb-replica .htb-icon-wrap i { color: #9FEF00; font-size: 80px; width: 100%; height: 100%; text-align: center; line-height: 80px; display: block; }
  .htb-replica .htb-icon-wrap .htb-hoodie-svg { width: 48px; height: 48px; fill: #9FEF00; position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); pointer-events: none; }
  .htb-replica .htb-icon-wrap i { position: relative; z-index: 1; }
  .htb-replica .htb-content { padding: 12px 20px 20px; text-align: center; }
  .htb-replica .htb-content h2 { color: #fff; font-size: 1.5rem; font-weight: 700; margin: 0 0 10px 0; }
  .htb-replica .htb-content hr { border: none; border-top: 1px solid #2d3548; margin: 0 0 12px 0; }
  .htb-replica .htb-user { display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 16px; }
  .htb-replica .htb-user img { width: 28px; height: 28px; border-radius: 50%; background: #2d3548; flex-shrink: 0; }
  .htb-replica .htb-user span { color: #fff; font-size: 0.9rem; text-align: left; }
  .htb-replica .htb-stats { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
  .htb-replica .htb-stat { background: #0d1117; border-radius: 8px; padding: 12px; }
  .htb-replica .htb-stat .val { color: #9fef00; font-size: 1rem; font-weight: 400; margin: 0 0 2px 0; }
  .htb-replica .htb-stat .lbl { color: #6b7280; font-size: 0.65rem; text-transform: uppercase; letter-spacing: 0.05em; margin: 0; }
  .htb-replica .htb-footer { width: 100%; min-height: 70px; background-color: #111927; text-align: center; box-sizing: border-box; padding-top: 20px; padding-bottom: 20px; }
  .htb-replica .htb-footer .htb-bottom-text { color: #A4B1CD; font-size: 0.9rem; margin: 0; }
  .htb-replica .htb-footer .htb-logo-img { height: 26px; width: auto; vertical-align: middle; margin-bottom: 1px; }
  .rootme-badge-wrap { display: inline-block; transform: scale(1.35); transform-origin: center top; }
  .badges-col, .badges-col-htb { min-width: 0; display: flex; flex-direction: column; align-items: center; }
  .rootme-last-update { font-size: 0.8rem; color: #6b7280; margin-top: 0.75rem; padding-top: 0.25rem; }
  .badges-wrapper { display: grid; grid-template-columns: minmax(30%, auto) 1fr; gap: 2rem; align-items: center; justify-content: start; max-width: 100%; }
  .personal-info-spacer { margin-bottom: 2rem; }
  .personal-info-heading { margin-top: 30px; margin-bottom: 20px; }
  .personal-info-table a { word-break: break-all; overflow-wrap: break-word; }
  @media (max-width: 770px) { .badges-wrapper { grid-template-columns: 1fr; } .badges-col-htb { min-width: 0; } }
</style>
<div class="badges-wrapper">
  <div class="badges-col">
    <div class="rootme-badge-wrap">
      <script src="https://root-me-badge.cloud.duboc.xyz/storage_clients/5c75b02f7d81874f8fc17adc0b7bc9ab/badge.js"></script>
    </div>
    <p class="rootme-last-update">Last update 11/2019</p>
  </div>
  <div class="badges-col badges-col-htb">
    <div class="htb-replica">
        <div class="htb-banner"></div>
        <div class="htb-icon-wrap">
          <i class="fa-solid fa-user-hoodie green icon" aria-hidden="true"></i>
          <svg class="htb-hoodie-svg" viewBox="0 0 448 512" aria-hidden="true"><path d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512H418.3c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304H178.3z"/></svg>
        </div>
        <div class="htb-content">
          <h2>Hacker</h2>
          <hr>
          <div class="htb-user">
            <img src="https://account.hackthebox.com/storage/users/9ae50a89-9521-4b01-a9ac-cded6ecc2552-avatar.png" alt="" onerror="this.style.display='none'">
            <span>zTeeed115405 has reached the Hacker rank.</span>
          </div>
          <div class="htb-stats">
            <div class="htb-stat">
              <p class="val">1.92% of users</p>
              <p class="lbl">RARITY</p>
            </div>
            <div class="htb-stat">
              <p class="val">11 Sep 2024</p>
              <p class="lbl">EARNED DATE</p>
            </div>
          </div>
        </div>
        <div class="htb-footer">
          <div class="htb-bottom-container">
            <span class="htb-bottom-text">Powered by</span>&nbsp;&nbsp;<img class="htb-logo-img" src="/images/pics/logo-htb.svg" alt="Hack The Box" height="26" style="vertical-align:middle; margin-bottom: 1px;">
          </div>
        </div>
      </div>
  </div>
</div>

# Personal information
{: .personal-info-heading }

|:-------------------|:---|
| Mail 📫 | [aurelien@duboc.xyz](mailto:aurelien@duboc.xyz)|
| LinkedIn 🌐 | [https://www.linkedin.com/in/aurelien-duboc/](https://www.linkedin.com/in/aurelien-duboc/)|
| Services 🚩 | [https://status.duboc.xyz/status/public](https://status.duboc.xyz/status/public)|
| Github 🌐 | [https://github.com/zteeed](https://github.com/zteeed)|
| RootMe ☠ | [https://www.root-me.org/zTeeed-115405](https://www.root-me.org/zTeeed-115405)|
| HackTheBox ☠ | [https://labs.hackthebox.com/achievement/badge/190724/215](https://labs.hackthebox.com/achievement/badge/190724/215)|
{: .personal-info-table }

<div class="personal-info-spacer"></div>
