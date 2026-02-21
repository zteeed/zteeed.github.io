---
title: "EN - Filecoin ecosystem: Lotus miner, Farcaster, and CID Gravity"
---

> In 2023 I worked in the [Filecoin](https://filecoin.io/) ecosystem, mainly around [Lotus](https://github.com/filecoin-project/lotus) (miner and node) and tooling for storage providers. This post is a short overview of that context and of [CID Gravity](https://www.cidgravity.com/), a gateway and management layer that makes it easier to work with Filecoin storage and retrieval.

# Context

Filecoin is a decentralized storage network: clients pay storage providers to store data, and the network guarantees persistence and retrievability via proofs and consensus. Building or operating storage infrastructure means dealing with **Lotus** (the reference node and miner implementation), deal-making, and the broader ecosystem (indexers, gateways, monitoring).

# Lotus miner and node

[Lotus](https://github.com/filecoin-project/lotus) is the main Go implementation of a Filecoin node and miner. As a **miner**, you run Lotus to:

- Publish storage and retrieval capacity.
- Make deals with clients and store their data.
- Run the sealing pipeline and submit proofs to the chain.

Operationally, that involves configuring sectors, managing deal flow, handling sealing and proving, and keeping the node in sync with the network. In 2023, a lot of the work in the ecosystem was around stability, performance, and tooling around Lotus (e.g. [lotus-farcaster](https://github.com/s0nik42/lotus-farcaster) for monitoring and analytics).

# Farcaster (lotus-farcaster)

[Farcaster](https://github.com/s0nik42/lotus-farcaster) (lotus-farcaster) is a **Prometheus exporter and visualization stack** for Filecoin Lotus nodes. It’s the monitoring and analytics tool many storage providers use instead of watching Lotus in the terminal.

- **Prometheus exporter**: Exposes Lotus miner and node metrics (sector state, deal flow, sealing, chain sync) for scraping.
- **Grafana dashboards**: Pre-built dashboards for realtime monitoring and historical analytics (e.g. average sealing time, sector lifecycle).
- **Stack**: Prometheus, Grafana, and Python; developed in cooperation with Protocol Labs.

Documentation and setup are on [Twin Quasar’s Farcaster page](https://twinquasar.io/farcaster.html). If you’re running Lotus miners, Farcaster gives you the visibility you need to operate them reliably (sector health, deal states, sealing pipeline, and chain sync).

# CID Gravity

[CID Gravity](https://www.cidgravity.com/) sits on the other side of the pipeline: it’s a **gateway and management platform** for Filecoin storage. From the [Filecoin Foundation ecosystem](https://fil.org/ecosystem-explorer/cidgravity) and [docs](https://docs.cidgravity.com/):

- **For clients**: Upload and manage data on Filecoin (and IPFS) through a simple interface; data is replicated across providers with verification and retrieval probes.
- **For storage providers**: CID Gravity acts as a **pricing and client management tool**: manage storage and retrieval deals, pricing, and client onboarding through a UI instead of raw Lotus or custom scripts.

So while Lotus miner is “run the chain and store the data,” CID Gravity is “offer and sell storage in a manageable way” and “consume storage without touching Lotus directly.” That’s useful when you want to integrate Filecoin into existing workflows (backups, archives, content delivery) or when you operate as a provider and need deal and pricing visibility.

# Why it matters

- **Lotus**: The core of running a Filecoin miner or node; understanding sealing, proving, and deal flow is essential for anyone building on the supply side.
- **Farcaster (lotus-farcaster)**: Prometheus exporter and Grafana dashboards for Lotus miner and node, so you can run miners reliably with realtime and historical visibility.
- **CID Gravity**: A practical onramp for both storing data on Filecoin and (for providers) managing deals and clients without building everything from scratch.

If you’re looking at the Filecoin ecosystem from a miner or infrastructure angle, the combination of Lotus + monitoring (e.g. [Farcaster](https://github.com/s0nik42/lotus-farcaster)) + a gateway or management layer (e.g. CID Gravity) is a common stack worth knowing.
