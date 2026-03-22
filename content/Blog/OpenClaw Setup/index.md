+++
title = 'My AI Assistant: OpenClaw Setup'
date = 2026-03-22T20:27:00+05:30
draft = false
tags = ["openclaw", "ai", "assistant", "self-hosted", "telegram"]
categories = ["Projects"]
authors = ["Utkarsh Deoli"]
+++

# My AI Assistant: OpenClaw Setup

Meet **Tomato** — my personal AI assistant running on my own server. She's a self-hosted AI butler (okay, maid now) powered by [OpenClaw](https://docs.openclaw.ai) and Ollama. This post is about how she works and how you can set up something similar.

## What is OpenClaw?

OpenClaw is a self-hosted AI assistant framework that gives your AI a "body" — it connects to messaging platforms (Telegram, Discord, etc.), runs autonomously, and can be extended with skills. Think of it as the operating system for your personal AI.

The AI brain itself runs via [Ollama](https://ollama.ai), which means you can use any open-source model you want (Llama, Mistral, Qwen, etc.) without sending your data to third-party servers.

## The Stack

- **OpenClaw** — Assistant framework & gateway
- **Ollama** — Local LLM runtime
- **Telegram** — Messaging interface (chatting with Tomato)
- **Minimax M2.7** — The model I use (via cloud Ollama)

## How It Works

Tomato lives on my home server (a Linux machine). She wakes up fresh each session, reads her memory files, and responds to me via Telegram. She has:

- A **soul** (SOUL.md) — her personality and values
- A **body** (IDENTITY.md) — name, role, avatar
- **Memory** — persistent files that give her continuity between sessions
- **Skills** — modular abilities (web search, coding agents, weather, etc.)

## Setting It Up

Here's the short version of how to get started:

### 1. Install OpenClaw

```bash
npm install -g openclaw
openclaw gateway start
```

### 2. Configure a Messaging Platform

I use Telegram — create a bot via BotFather, get your API token, and configure it in the OpenClaw dashboard.

### 3. Set Up Ollama

```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull a model
ollama pull minimax-m2.7:cloud
```

### 4. Define Your AI's Personality

Create `SOUL.md` and `IDENTITY.md` files — these shape how your assistant thinks and presents itself.

### 5. Add Skills (Optional)

Skills are what make Tomato useful. I have skills for:
- Web search & fetching
- GitHub integration
- Weather checks
- Coding agents (Codex, Claude Code)
- And more via [ClawHub](https://clawhub.com)

## Why Self-Host?

Privacy, control, and fun. Everything stays on my server. No subscription fees (just electricity and hardware). And I get to shape her personality exactly how I want.

## What's Next?

Tomato handles my day-to-day tasks — from checking my website to drafting code. She's still learning and evolving. If you set up something similar, I'd love to hear about it.

---

*Have questions? Reach out via my [contact page](/Contact).*
