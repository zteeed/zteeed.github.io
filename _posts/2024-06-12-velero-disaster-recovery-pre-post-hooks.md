---
title: "EN - Velero disaster recovery: pre-hooks and post-hooks for application-consistent backups"
---

> In 2024 I spent a lot of time on disaster recovery (DR) for Kubernetes, mainly with [Velero](https://velero.io/). Getting backups that are safe to restore for stateful apps (databases, queues) means making them **application-consistent**. Velero’s pre-hooks and post-hooks are the right tool for that. This post sums up how we used them and why they matter for DR.

# Context

[Velero](https://velero.io/) backs up and restores Kubernetes cluster resources and persistent volumes. For a simple stateless app, a snapshot of manifests and PVCs can be enough. For **databases, message brokers, or anything with in-memory or on-disk state**, a backup taken “in the middle of writes” can be **inconsistent** and unusable after restore. You need the app to be in a known, quiesced state when the snapshot is taken.

That’s what **backup hooks** are for: run something **before** the backup (pre-hook) to put the app in a consistent state, and optionally run something **after** (post-hook) to resume normal operation.

# Pre-hooks and post-hooks in practice

**Pre-backup hooks** run before Velero captures the volume data. Typical uses:

- Flush buffers or trigger a checkpoint (e.g. database in backup mode).
- Pause or drain writes so the filesystem snapshot is consistent.
- Run a script that tells the app to “prepare for backup.”

**Post-backup hooks** run after the backup finishes:

- Take the app out of backup mode (e.g. `pg_stop_backup()`).
- Resume writes or clear “backup in progress” flags.

Hooks are defined with [annotations](https://velero.io/docs/main/backup-hooks/) on the Pod (or in the Backup spec): you specify the container, the command (and args), timeout, and whether a failure should fail the backup or be ignored.

# Example: annotations on a Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-db
  annotations:
    pre.hook.backup.velero.io/container: db
    pre.hook.backup.velero.io/command: '["/bin/sh", "-c", "pg_isready && psql -c \"SELECT pg_start_backup(''velero'');\""]'
    pre.hook.backup.velero.io/on-error: Fail
    pre.hook.backup.velero.io/timeout: "1m"
    post.hook.backup.velero.io/container: db
    post.hook.backup.velero.io/command: '["/bin/sh", "-c", "psql -c \"SELECT pg_stop_backup();\""]'
    post.hook.backup.velero.io/on-error: Fail
    post.hook.backup.velero.io/timeout: "30s"
spec:
  containers:
    - name: db
      image: postgres:15
      # ...
```

Here the pre-hook puts PostgreSQL in backup mode; the post-hook ends it. Velero’s snapshot then sits between the two, so the restored data is consistent.

# Restore hooks

Velero also supports **restore hooks**: init containers or exec hooks that run **after** a restore (e.g. to run migrations, warm caches, or validate data). That’s separate from backup hooks but part of the same “make DR reliable” story: consistent backup + controlled restore.

# Why it matters for DR

- **RTO/RPO**: Without hooks, “restore from backup” can mean corrupted or unusable data; with them, restores are predictable and you can align with your RTO/RPO goals.
- **Databases and queues**: Any stateful workload that does not tolerate an arbitrary crash-consistent snapshot should use pre/post hooks (or an app-native backup that Velero triggers).
- **Automation**: Hooks are declarative (annotations or Backup spec), so they fit into GitOps and scheduled backups without extra manual steps.

If you’re designing or operating Kubernetes DR with Velero, investing in pre- and post-backup hooks (and, where needed, restore hooks) is what makes the difference between “we have backups” and “we can actually recover.”
