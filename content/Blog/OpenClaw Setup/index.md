+++
title = 'My AI Assistant: OpenClaw Setup'
date = 2026-03-22T20:27:00+05:30
draft = false
tags = ["openclaw", "ai", "assistant", "self-hosted", "telegram"]
categories = ["Projects"]
authors = ["Utkarsh Deoli"]
description = "How I set up Tomato — a personal AI assistant powered by OpenClaw and Ollama. Includes Telegram integration, automated workflows, and self-hosting guide."
keywords = ["openclaw", "ai assistant", "self-hosted ai", "ollama", "telegram bot", "personal ai", "automation"]
slug = "openclaw-setup"
canonicalUrl = "https://utkarshdeoli.in/blog/openclaw-setup/"
+++

# My AI Assistant: OpenClaw Setup

Meet **Tomato** — my personal AI assistant running on my own server. She's a self-hosted AI maid (long story) powered by [OpenClaw](https://docs.openclaw.ai) and [Ollama](https://ollama.ai). This post is about how she works and how you can set up something similar.

## What is OpenClaw?

[OpenClaw](https://docs.openclaw.ai) is a self-hosted AI assistant framework that gives your AI a "body" — it connects to messaging platforms (Telegram, Discord, WhatsApp, etc.), runs autonomously, and can be extended with skills. Think of it as the operating system for your personal AI.

The AI brain runs via [Ollama](https://ollama.ai), which means you can use any open-source model (Llama, Mistral, Qwen, etc.) without sending your data to third-party servers.

**Official Docs:** https://docs.openclaw.ai

## The Stack

- **OpenClaw** — Assistant framework & gateway
- **Ollama** — Local LLM runtime
- **Telegram** — Messaging interface (chatting with Tomato)
- **Minimax M2.7** — The model I use (via cloud Ollama)

## How It Works

Tomato lives on my home server (a Linux laptop). She wakes up fresh each session, reads her memory files, and responds to me via Telegram. She has:

- A **soul** (`SOUL.md`) — personality and values
- A **body** (`IDENTITY.md`) — name, role, avatar
- **Memory** — persistent files that give her continuity between sessions
- **Skills** — modular abilities (web search, coding agents, weather, etc.)

## Setting It Up

Here's how to get started:

### 1. Install OpenClaw

OpenClaw is installed via the official installer script:

```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

For Windows, use PowerShell:

```powershell
iwr -useb https://openclaw.ai/install.ps1 | iex
```

Other install methods (npm, Docker, etc.) are available at [https://docs.openclaw.ai/install](https://docs.openclaw.ai/install).

### 2. Run the Onboarding Wizard

After installation, run:

```bash
openclaw onboard --install-daemon
```

This wizard configures auth, gateway settings, and optional channels (Telegram, Discord, etc.).

### 3. Check the Gateway

Once onboarded, your gateway should be running:

```bash
openclaw gateway status
```

To run the gateway manually (foreground):

```bash
openclaw gateway --port 18789
```

### 4. Open the Control UI

Access your AI via the browser dashboard:

```bash
openclaw dashboard
```

Or open directly at `http://127.0.0.1:18789/` on the gateway machine.

### 5. Connect a Messaging Channel (Optional)

The Control UI works without any channel setup. But if you want to chat via Telegram:

1. Create a bot via [BotFather](https://t.me/BotFather) on Telegram
2. Get your bot token
3. Configure the Telegram channel via the wizard or `openclaw configure`

Full channel setup docs: [https://docs.openclaw.ai/channels](https://docs.openclaw.ai/channels)

### 6. Set Up Ollama

OpenClaw needs an LLM backend. Install Ollama:

```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull a model
ollama pull minimax-m2.7:cloud
```

Or use any model you prefer — Llama, Mistral, Qwen, etc.

### 7. Define Your AI's Personality (Optional)

Create these files in your workspace:

- `SOUL.md` — your AI's personality, values, and vibe
- `IDENTITY.md` — name, role, appearance
- `MEMORY.md` — long-term memory for continuity between sessions

## Adding Skills

Skills extend what Tomato can do. I have skills for:

- Web search & fetching
- GitHub integration (`gh` CLI)
- Weather checks
- Coding agents (OpenCode, Claude Code)
- And more via [ClawHub](https://clawhub.com)

Install new skills with:

```bash
clawhub install <skill-name>
```

## Why Self-Host?

Privacy, control, and fun. Everything stays on my server. No subscription fees (just electricity and hardware). And I get to shape her personality exactly how I want.

## My Experience with OpenClaw

After running Tomato for a while, here's what I've learned:

### It's a Workhorse for Automation

OpenClaw isn't just a chatbot — it's a legitimate automation powerhouse. I run **sub-agents** that work in the background on a schedule:

- 📰 **Daily news reports** — a sub-agent scans the web and sends me a briefing every morning
- 📧 **Email monitoring** — another sub-agent reads my emails and alerts me only when something important arrives
- 💼 **LinkedIn automation** — I have a sub-agent that searches LinkedIn for the latest jobs matching my interests, using the browser tool to scrape search results

The main agent stays free to handle direct conversations while sub-agents do the heavy lifting in the background. The best part? I can edit the prompt inside the schedule whenever I want — no code changes needed.

### Cheap AI Models Are Surprisingly Good Enough

Here's an unpopular opinion: **you don't need Claude Sonnet or GPT-4 for most tasks**. I run smaller, cheaper models (like Minimax M2.7 via Ollama) and they handle 90% of what I need — at a fraction of the cost. The heavy models are impressive, but for automation scripts, scheduling, and background tasks, a fast cheap model gets the job done just as well.

### Where Can You Run It?

OpenClaw is flexible about where it lives:

- 🖥️ **Old laptop or desktop** — perfect for a home setup, low power draw
- 🍓 **Raspberry Pi** — lightweight and cheap, great for轻量级任务
- 🖥️ **VPS/Cloud server** — if you want it accessible from anywhere

### A Word on Security

⚠️ **Don't run it on your main machine.** AI is unreliable by nature — it can glitch, hallucinate, or behave unexpectedly. I've seen enough odd outputs to know that giving an AI unrestricted access to your primary system is a bad idea. Keep it sandboxed, keep it isolated, and treat it like a helpful but somewhat chaotic intern.

### What I'm Still Exploring

I'm actively experimenting with OpenClaw and learning as I go. Right now I'm:

- Building custom skills for social media automation
- Setting up scheduled workflows that run on cron
- Exploring more sub-agent patterns for different use cases

I'll share more in a follow-up post once I've found the best skills worth recommending. Stay tuned!

## Useful Commands

| Command | Description |
|---------|-------------|
| `openclaw status` | Check gateway status |
| `openclaw doctor` | Diagnose config issues |
| `openclaw dashboard` | Open browser UI |
| `openclaw gateway restart` | Restart the gateway |
| `openclaw help` | List all commands |

Full CLI reference: [https://docs.openclaw.ai/start/getting-started](https://docs.openclaw.ai/start/getting-started)

## What's Next?

Tomato handles my day-to-day tasks — from checking my website to drafting code. She's still learning and evolving. If you set up something similar, I'd love to hear about it.

---

*Have questions? Reach out via my [contact page](/contact).*
