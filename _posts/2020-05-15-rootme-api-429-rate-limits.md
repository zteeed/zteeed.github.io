---
title: "EN - Root-Me API: dealing with 429 rate limits when there was no public API"
---

> [Root-Me](https://www.root-me.org/) is a platform for security challenges and CTF. At the time this project was built, **there was no official public API**. I wrote an unofficial API ([Root-Me-API](https://github.com/zteeed/Root-Me-API)) that exposed user stats, challenges, and scores. The main difficulty was dealing with **rate-limiting** on the server side (HTTP 429 and temporary IP bans). This post describes the restrictions encountered and the techniques used to bypass or work around them, without disclosing private endpoints or encouraging abuse.

# Context

Root-Me’s website is the only official way to consult rankings, user profiles, and challenge validations. For bots, badges, or dashboards, you need either an official API (which exists today at [api.www.root-me.org](https://api.www.root-me.org/?lang=en)) or an unofficial layer that talks to the same backend the web UI uses. Back then, the only option was to **reverse-engineer the site’s requests** and replicate them from a service. Doing that naively (e.g. many requests in a short time) quickly led to **429 Too Many Requests** and **temporary IP bans**.

# What we hit: 429 and rate limits

- **429 Too Many Requests**  
  The server returned **429** when Root-Me detected too much traffic from one IP (see the [Root-Me-API](https://github.com/zteeed/Root-Me-API) README). In practice, 429 appeared when we crossed an implicit rate or concurrency limit.

- **Connection and rate limits**  
  The site’s firewall (or backend) enforced limits along the lines of: no more than a certain number of **connections per second**, and no more than a certain number of **simultaneous TCP connections** from the same client. Exceeding these triggered temporary bans (on the order of several minutes). Retrying during the ban could extend it.

So the goal was to **stay under those limits**, **spread load across multiple IPs**, and **recover from 429** so that the unofficial API could serve multiple clients (e.g. a Discord bot, a badge generator) without getting blocked.

# Bypass and mitigation techniques

What “bypass” meant here was not breaking the server, but **designing the client and the API layer** so that we stayed within the site’s tolerance and handled 429/errors gracefully.

## 1. Throttling and request spacing

The most important measure was **strict client-side throttling**: cap the number of requests per second and the number of concurrent requests. For example:

- A single global rate limiter (e.g. token bucket or sliding window) so that **all** outgoing requests to Root-Me pass through one bottleneck.
- A **minimum delay** between two requests (e.g. hundreds of milliseconds), even when the API had multiple queued callers.

That way, a burst of traffic to *our* API (e.g. 10 users asking for their rank at once) was translated into a **serialized, spaced stream** of requests to the upstream site, avoiding spikes that triggered 429 or bans.

## 2. Redis-backed job queue and workers

To scale the API beyond a single process and still respect a global rate limit, we used **Redis** as a central queue:

- Incoming API requests (e.g. “get user X”) were turned into **jobs** pushed into a Redis stream (or list).
- **Worker processes** consumed the stream and performed the actual HTTP requests to the site, with a **single, shared rate limit** (e.g. one request every N ms, or at most M concurrent). Only the workers talked to Root-Me; the REST API only talked to Redis and the workers.

So staying under rate limits at the scale level meant: **never letting the upstream see more concurrency or rate than it allows**. The queue absorbed bursts and let workers drip requests at an acceptable pace.

## 3. Retry with backoff on 429

When a request returned **429** or **5xx**, we did not fail the user request immediately. We:

- **Retried** the request a small number of times (e.g. 2-3).
- Used **exponential backoff** (e.g. 1 s, then 2 s, then 4 s) before each retry, to give the server time to release the ban.

That turned many transient 429s into successful responses after a short delay, without hammering the server.

## 4. Caching

We **cached** responses (e.g. per user ID or per challenge ID) for a short TTL (e.g. tens of seconds or a few minutes). So:

- Repeated requests for the same user or the same challenge were served from cache instead of hitting the site again.
- Request volume to the upstream dropped sharply for popular queries (e.g. “my rank”, “top 10”), which further reduced the chance of 429 and bans.

## 5. Session and headers

We reused a small pool of **sessions** (cookies, and optionally consistent headers) so that requests looked like a small set of “browsers” rather than hundreds of anonymous connections. That didn’t remove the need for throttling but helped avoid being classified as obvious scraping.

## 6. Docker macvlan and public IP pool

To **scale the number of workers** while staying under the per-IP limit, the [Root-Me-API](https://github.com/zteeed/Root-Me-API) repository documents an **advanced configuration** using [Docker macvlan](https://docs.docker.com/network/macvlan/) and a **public IP pool**. Root-Me blocks requests when it sees too many connections from a single public IP (429); with one worker per IP, each worker is subject to its own limit and the total throughput increases.

- **Setup:** The `advanced_configuration/docker-compose.yml` defines a macvlan network (`bridge_worker`) attached to a physical interface (e.g. `parent: eth1`) that has multiple public IPv4 addresses. The backend (API, Redis, workers' internal communication) uses a separate **internal** bridge with no internet access; only workers are attached to the macvlan so they egress with their assigned public IP.

- **IP pool:** The `ipam.config` specifies a **subnet** and an **ip_range** (e.g. `157.159.191.56/29`), so Docker assigns one address from that range to each worker container (e.g. six workers get `.56`-`.61`). Root-Me therefore sees requests from six different source IPs; the per-IP rate limit applies per worker instead of to the whole API.

- **Why not proxies:** The README states that proxy rotation was not used for data privacy reasons; the macvlan + public IP pool gives multiple egress IPs without sending traffic through third-party proxies.

Details (subnet, gateway, `ip_range`, `parent` interface) are in the [advanced_configuration/docker-compose.yml](https://github.com/zteeed/Root-Me-API/blob/master/advanced_configuration/docker-compose.yml) and the [Docker macvlan documentation](https://docs.docker.com/network/macvlan/). Note: with macvlan, containers typically cannot reach the Docker host's default namespace IP; the backend network is used so API, Redis, and workers still communicate.

# Summary

| Restriction        | Approach                                                |
|--------------------|----------------------------------------------------------|
| 429 / rate limit   | Global throttling, min delay between requests            |
| Burst traffic      | Redis job queue + workers with a single rate limiter      |
| Per-IP limit       | Docker macvlan + public IP pool (one IP per worker)        |
| Transient 429      | Retry with exponential backoff                           |
| Repeated queries   | Short-TTL cache per user/challenge                       |
| Detection          | Stable sessions and realistic headers                    |

So “handling 429” here meant **staying under the server’s limits and degrading gracefully** when we hit them, not exploiting a bug. Today, Root-Me provides an [official API](https://api.www.root-me.org/?lang=en); for new projects, prefer that and respect its terms and rate limits. The patterns above (queue, throttle, retry, cache, and when possible macvlan + public IP pool) still apply to any client that must talk to a rate-limited HTTP API.
