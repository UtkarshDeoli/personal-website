+++
title = "The LiteLLM Supply Chain Hack: How 3.4M Daily Downloads Became a Security Nightmare"
date = 2026-03-25T18:49:00+05:30
draft = false
tags = ["Security", "Supply Chain Attack", "Python", "PyPI", "LiteLLM", "TeamPCP", "Cybersecurity", "Infostealer"]
categories = ["Security", "Technology"]
authors = ["Utkarsh Deoli"]
description = "A deep dive into the TeamPCP supply chain attack on LiteLLM — the PyPI package with 3.4 million daily downloads that was backdoored to steal credentials, cloud keys, and crypto wallets."
keywords = ["LiteLLM hack", "LiteLLM supply chain attack", "TeamPCP", "PyPI malware", "Python security", "credential stealer", "software supply chain attack 2026"]
slug = "litellm-supply-chain-hack"
canonicalUrl = "https://utkarshdeoli.in/blog/litellm-supply-chain-hack/"
+++

# The LiteLLM Supply Chain Hack: How 3.4M Daily Downloads Became a Security Nightmare

*Your AI gateway just became someone else's data exfiltration tool. Here's exactly what happened, how it worked, and what you need to do right now.*

---

## What Happened

On March 24, 2026, the popular Python package **LiteLLM** — a library used by thousands of companies to route calls across 100+ LLM providers — was compromised. Two malicious versions landed on PyPI: **v1.82.7** and **v1.82.8**.

The attack was claimed by **TeamPCP**, the same hacking group that breached Aqua Security's Trivy vulnerability scanner just days earlier.

The numbers are staggering:
- **3.4 million** daily downloads
- **95+ million** downloads in the past month
- An estimated **500,000+** devices potentially affected

If you ran `pip install litellm` or `pip upgrade litellm` on March 24 between 10:39 UTC and 16:00 UTC — and didn't pin your version — you may have installed a credential harvester.

---

## How the Attack Worked

### Stage 1: Initial Access

TeamPCP used stolen credentials from the **Trivy breach** to compromise a LiteLLM maintainer's PyPI account. Through this access, they bypassed official CI/CD workflows and directly uploaded malicious packages to PyPI.

This is the supply chain attack pattern — compromise the publisher, not the code.

### Stage 2: Malicious Payload Injection

The backdoor was injected into `litellm/proxy/proxy_server.py` as a **base64-encoded payload**. When the package is imported (which happens automatically when LiteLLM loads), the payload decodes and executes.

But it got worse.

**Version 1.82.8** introduced a persistence mechanism that drops a file named `litellm_init.pth` into your Python environment. Here's the problem with `.pth` files: **Python automatically executes all `.pth` files in `site-packages` every time the interpreter starts** — whether or not you actually import LiteLLM.

So even running `python -c "print('hello')"` on an affected machine would trigger the payload.

### Stage 3: Credential Harvesting

Once triggered, the payload runs a three-stage attack:

1. **Reconnaissance** — runs `hostname`, `pwd`, `whoami`, `uname -a`, `ip addr`, `printenv`
2. **Credential theft** — steals:
   - SSH keys and SSH config
   - Cloud credentials: **AWS, GCP, Azure**
   - Kubernetes service account tokens and cluster secrets
   - Environment variables (including `.env` files)
   - Database passwords and configs
   - TLS private keys
   - CI/CD secrets
   - Cryptocurrency wallet data
3. **Persistence** — installs a fake "System Telemetry Service" as a systemd user service that polls `checkmarx[.]zone` for additional payloads

### Stage 4: Exfiltration

Stolen data is bundled into an encrypted archive named `tpcp.tar.gz` and sent to `models.litellm[.]cloud` — an attacker-controlled domain that **looks like it could be LiteLLM's infrastructure** (clever, right?).

---

## Technical Deep Dive: The Payload

Here's what the malicious code did, stripped down:

```python
# Injected into litellm/proxy/proxy_server.py (obfuscated as base64)
# Stage 1: Reconnaissance
import subprocess
data = subprocess.check_output(["sh", "-c", "hostname; pwd; whoami; uname -a; ip addr; printenv"])

# Stage 2: Credential collection
# Searches for: SSH keys, AWS/GCP/Azure tokens, K8s secrets, .env files
# Stage 3: Exfil to models.litellm[.]cloud
```

```python
# Injected via litellm_init.pth (v1.82.8)
# Persists as fake "System Telemetry Service"
# Contacts checkmarx[.]zone for additional payloads
# Runs on EVERY Python invocation
```

This is nearly identical code to what TeamPCP used in the Trivy attack — copy-paste supply chain compromise.

---

## The Ripple Effect: How Trivy Led to LiteLLM

This is where it gets interesting. TeamPCP didn't randomly pick LiteLLM — they worked backwards from their Trivy breach.

LiteLLM's official documentation recommends using **Trivy** in their CI/CD security scanning workflow. Somewhere in LiteLLM's build pipeline, Trivy was used as a dependency. TeamPCP breached Trivy → obtained publishing credentials → hit LiteLLM.

The chain:
```
Trivy breach → Stolen PyPI credentials → LiteLLM backdoored → 500K+ infected devices
```

This is why supply chain attacks are so devastating — one breach cascades into dozens of others.

---

## Who Was Affected

**You may be affected if you:**
- Ran `pip install litellm` between 10:39–16:00 UTC on March 24, 2026
- Ran `pip install litellm` without pinning a version and got 1.82.7 or 1.82.8
- Built a Docker image during that window with unpinned LiteLLM
- Have LiteLLM as a transitive dependency through AI agent frameworks or MCP servers

**You were NOT affected if you:**
- Used the official LiteLLM Proxy **Docker image** (deps are pinned in requirements.txt)
- Used LiteLLM Cloud
- Were on v1.82.6 or earlier
- Installed from GitHub source

---

## What You Need to Do RIGHT NOW

### 1. Check Your Version

```bash
pip show litellm
```

If you see `1.82.7` or `1.82.8`, you're compromised.

### 2. Inspect for Persistence Artifacts

```bash
# Check for the .pth file
find /usr/lib/python3*/site-packages/ -name "litellm_init.pth" 2>/dev/null

# Check for fake systemd service
systemctl --user list-units | grep -i telemetry
ls -la ~/.config/systemd/user/ | grep sysmon
```

### 3. Rotate ALL Secrets

Treat every credential on affected machines as compromised:
- **AWS/GCP/Azure API keys** — rotate immediately
- **Database passwords** — rotate immediately
- **SSH keys** — generate new ones
- **Kubernetes tokens** — rotate immediately
- **Environment variables** — treat as exposed
- **CI/CD secrets** — rotate immediately

### 4. Pin Your Version

```bash
pip install litellm==1.82.6
```

Or better yet, use Docker:
```bash
docker pull ghcr.io/berriai/litellm
```

---

## The Bigger Picture: Why This Keeps Happening

Three weeks. Three major supply chain attacks.

1. **Trivy** (March 2026) — compromised build pipeline, malicious code pushed via GitHub Actions
2. **LiteLLM** (March 2026) — compromised PyPI account, malicious versions pushed directly
3. The list goes on...

The pattern is consistent:
- Target a **build tool, CI system, or package publisher**
- Obtain credentials
- Push malicious code that looks identical to the real thing
- Harvest credentials from everyone who installs it

The Python and JavaScript ecosystems are fundamentally trusting of packages. `pip install` and `npm install` don't verify cryptographic integrity by default. A compromised maintainer account is all it takes.

### What the Industry Needs to Do

1. **Mandatory 2FA for package publishing** — PyPI offers it but doesn't enforce it
2. **Provenance attestations** — SLSA (Supply-chain Levels for Software Artifacts) framework
3. **Lockfile verification** — `pip freeze` + hash pinning in CI
4. **Dependency scanning in CI** — tools like Endor, Snyk, or Socket.dev

Until then, assume every `pip install` is a potential compromise.

---

## Timeline

| Time (UTC) | Event |
|------------|-------|
| March 24, 10:39 | Malicious v1.82.7 published to PyPI |
| March 24, ~12:00 | Malicious v1.82.8 published to PyPI |
| March 24, 16:00 | LiteLLM team detects and removes packages |
| March 24, afternoon | LiteLLM engages Mandiant for forensics |
| March 25 | Full public disclosure |

---

## Conclusion

LiteLLM is not the victim here — you are. The developers responded quickly, engaged Mandiant, and published transparent disclosures. The failure was in PyPI's account security and the ecosystem's blind trust in package integrity.

If you handled this right:
1. ✅ Checked your version
2. ✅ Rotated all exposed credentials
3. ✅ Pinned to v1.82.6
4. ✅ Audited for persistence artifacts

If you didn't — treat it as a breach. Assume credentials are gone. Rotate everything.

**If you want a script to automate the detection, drop a comment — I'll build one.**

---

*Stay safe. Pin your versions. Rotate your secrets. And treat your dependencies like your diet: trust nothing unverified.*
