---
title: "EN - Prometheus AWS EC2 service discovery: fixing the custom endpoint (regression fix)"
---

> After the migration to AWS SDK v2, Prometheus AWS EC2 service discovery stopped applying the configured `endpoint` option. This post summarizes the regression and the fix contributed upstream.

# Context

Prometheus [EC2 service discovery](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#ec2_sd_config) lets you discover scrape targets from AWS EC2. Some setups use a **custom endpoint** (e.g. for localstack, MinIO, or an API-compatible alternative) by setting the `endpoint` option in `ec2_sd_configs`.

With the move from AWS SDK v1 to v2, the code that builds the AWS client was refactored. In the v1 implementation, the configured `endpoint` was passed into the session config and was actually used. In the v2 version, that wiring was dropped, so the `endpoint` field in the config was **ignored** and the client always used the default AWS endpoints. That’s a regression for anyone relying on a custom endpoint.

Additionally, the availability zone handling did not guard against `DescribeAvailabilityZones` returning nil or structs with nil `ZoneName`/`ZoneId`, which could lead to panics.

# The fix

A small change restores the intended behavior and hardens the code:

1. **Apply the configured endpoint** when building the AWS client for EC2 discovery, so `endpoint` in `ec2_sd_configs` is respected again.
2. **Add nil-safety** in the availability zone handling so that nil responses or nil `ZoneName`/`ZoneId` no longer cause panics.

# Upstream PR

- **PR:** [prometheus/prometheus#18133](https://github.com/prometheus/prometheus/pull/18133): *fix(discovery): apply EC2 SD endpoint and guard refreshAZIDs*
- **Branch:** `fix/ec2-sd-custom-endpoint`

Example config that benefits from this fix (custom endpoint for compatibility layers or private AWS-compatible APIs):

```yaml
scrape_configs:
  - job_name: ec2
    ec2_sd_configs:
      - region: eu-west-1
        endpoint: https://my-ec2-compatible-api.example.com
        access_key: YOUR_ACCESS_KEY
        secret_key: YOUR_SECRET_KEY
```

Once the fix is merged and released, this `endpoint` will again be used when building the EC2 client.
