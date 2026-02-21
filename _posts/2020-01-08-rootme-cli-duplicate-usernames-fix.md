---
title: EN - Fixing the Root-Me CLI when multiple accounts share a username
---

> The Root-Me CLI ([sagittarius-a/rootme](https://github.com/sagittarius-a/rootme)) looks up users by username. When several accounts share the same display name, the API returns multiple matches and the tool assumed a single user ID, which led to a 404. Here’s the fix that was contributed and merged.

# What is Root-Me?

[Root-Me](https://www.root-me.org/) is a platform for security and CTF challenges. The [rootme](https://github.com/sagittarius-a/rootme) Python CLI lets you query your score, rank, and other info from the command line (e.g. `rootme rank -u zTeeed`).

# The bug

When **several accounts share the same username** (display name), the Root-Me API returns a list of authors, for example:

```json
{"0": {"id_auteur": "108022", "nom": "zTeeed"}, "1": {"id_auteur": "115405", "nom": "zTeeed"}}
```

The CLI was written under the assumption that a username maps to a single user. It took the first ID (e.g. `108022`) and requested user info for that ID only. For duplicate usernames, the API can return 404 for one of the IDs while another ID is valid, so the command failed with:

```
ValueError: ('Cannot get info about user %s. Error %s', '108022', 404)
```

even though another account with the same name (e.g. `115405`) was valid and had the expected score/rank.

# The fix

The fix was to **handle multiple accounts with the same username**: when the API returns several authors for a given name, the code tries each returned `id_auteur` until one request succeeds. That way `rootme rank -u zTeeed` works even when several users share that display name.

- **PR:** [sagittarius-a/rootme#1](https://github.com/sagittarius-a/rootme/pull/1): *Fix issue of several accounts with same usernames*
- **Status:** Merged (Jan 2020)

# Result

Before:

```
rootme rank -u zTeeed
Traceback (most recent call last):
  ...
ValueError: ('Cannot get info about user %s. Error %s', '108022', 404)
```

After:

```
rootme rank -u zTeeed
Cannot get info about user 108022. Error 404
[+] zTeeed Score: 5875 Position: 297
```

So the CLI now tolerates duplicate usernames and still returns the correct score and rank when at least one of the matching accounts is valid.
