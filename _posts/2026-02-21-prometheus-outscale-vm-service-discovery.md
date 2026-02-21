---
title: "EN - Prometheus: Outscale VM service discovery (new feature)"
---

> Prometheus can discover scrape targets from cloud APIs (EC2, Azure, GCE, etc.). This post describes a new discovery integration for **Outscale Cloud**: `outscale_sd_configs`, contributed upstream.

# What is Outscale?

[Outscale](https://outscale.com/) is a cloud provider offering an AWS-compatible API (among others). If you run workloads on Outscale and use Prometheus, you want to discover VMs (and their metadata) the same way you do for EC2, without maintaining static target lists.

# New feature: Outscale VM service discovery

A new discovery type **`outscale_sd_configs`** was added to Prometheus. It talks to the Outscale Cloud API, discovers VMs in the configured region, and produces scrape targets with the usual labels (instance, region, availability zone, etc.), so you can use the same scraping and relabeling patterns as with EC2 SD.

# Configuration

In your `prometheus.yml`, add a scrape job that uses `outscale_sd_configs`:

```yaml
scrape_configs:
  - job_name: outscale
    outscale_sd_configs:
      - region: eu-west-2
        access_key: YOUR_ACCESS_KEY
        secret_key: YOUR_SECRET_KEY
```

If you need a custom endpoint (e.g. for a specific Outscale region or gateway):

```yaml
scrape_configs:
  - job_name: outscale
    outscale_sd_configs:
      - region: eu-west-2
        endpoint: https://api.eu-west-2.outscale.com/api/v1
        access_key: YOUR_ACCESS_KEY
        secret_key: YOUR_SECRET_KEY
```

Credentials can also be provided via environment variables or IAM roles where supported, similar to other SD integrations.

# Upstream PR

- **PR:** [prometheus/prometheus#18139](https://github.com/prometheus/prometheus/pull/18139): *feat(discovery): add Outscale VM service discovery*
- **Branch:** `feat/outscale-sd`

Once merged and released, you can use `outscale_sd_configs` in Prometheus to discover Outscale VMs automatically and keep your scrape targets in sync with your cloud inventory.
