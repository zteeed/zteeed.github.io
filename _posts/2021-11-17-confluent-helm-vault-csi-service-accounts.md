---
title: EN - Kubernetes service accounts for Vault CSI with Confluent Helm charts
---

> When using the Vault CSI driver to inject secrets or certificates into pods, each pod needs a dedicated Kubernetes service account. This post describes a contribution to Confluent’s Kafka Helm charts to make those service accounts configurable.

# Context

The [Vault CSI provider](https://developer.hashicorp.com/vault/docs/platform/k8s/csi) lets Kubernetes pods get secrets (or certificates) from Vault at mount time. In many setups, **each pod that uses the driver must run with a specific service account** so that Vault can identify it (e.g. via Kubernetes auth) and issue the right tokens.

Confluent’s [cp-helm-charts](https://github.com/confluentinc/cp-helm-charts) deploy Kafka and related components (Zookeeper, etc.) on Kubernetes. By default, the charts don’t allow you to override the service account used by each deployment. If you want those pods to use the Vault CSI driver with a custom service account (e.g. one per component or per namespace), you had no clean way to do it.

# The change

A pull request was opened to **make the service account used by deployments configurable** in the Helm values, so you can point each component (e.g. Kafka, Zookeeper) at a service account that has the right Vault policies and Kubernetes auth role.

- **PR:** [confluentinc/cp-helm-charts#567](https://github.com/confluentinc/cp-helm-charts/pull/567): *Manage service account in deployments*
- **Status:** Open (repository may be in maintenance mode; consider [Confluent for Kubernetes](https://docs.confluent.io/operator/current/overview.html) for newer setups.)

# How it was tested

Install/upgrade with a custom `values.yaml` that sets the service account(s) for the components you need:

```bash
helm upgrade --install \
  -f values.yaml \
  --timeout 600s \
  --create-namespace \
  --namespace my-namespace \
  my-namespace-cp-helm-charts \
  .
```

In `values.yaml` you would define the service account name(s) that your Vault Kubernetes auth is configured for, so pods started by the chart use those accounts and can authenticate to Vault via the CSI driver.

# Why it matters

- **Vault CSI**: Pods need a dedicated service account for Kubernetes auth; without configurable service accounts in the chart, you have to patch deployments manually or fork the chart.
- **Multi-tenant or multi-namespace**: Different namespaces or tenants can use different service accounts (and thus different Vault roles/policies) for the same Confluent components.

If you use cp-helm-charts with Vault CSI, the PR shows one way to wire service accounts in; for new deployments, Confluent for Kubernetes (CFK) may offer more native options.
