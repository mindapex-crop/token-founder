# Kimi WebBridge & Kimi API - Complete Setup Guide

> **Last Updated**: 2026-06 (智谱2号战士 research)
> **Company**: Moonshot AI (月之暗面)
> **Product**: Kimi (智能助手)

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Clarification: WebBridge vs Kimi API](#2-clarification-webbridge-vs-kimi-api)
3. [Kimi WebBridge - Browser Automation Plugin](#3-kimi-webbridge---browser-automation-plugin)
4. [Kimi API Platform - LLM API Access](#4-kimi-api-platform---llm-api-access)
5. [Registration & Getting an API Key](#5-registration--getting-an-api-key)
6. [API Details](#6-api-details)
7. [Supported Models](#7-supported-models)
8. [Pricing](#8-pricing)
9. [Free Tier](#9-free-tier)
10. [Kimi CLI / Kimi Code](#10-kimi-cli--kimi-code)
11. [Quick Start Code Examples](#11-quick-start-code-examples)
12. [Third-Party Free Access Options](#12-third-party-free-access-options)
13. [Summary & Recommendations](#13-summary--recommendations)

---

## 1. Executive Summary

**Kimi WebBridge** is NOT an API key provider. It is a **browser extension** (Chrome/Edge) that lets AI agents (like Kimi Work, Claude Code, Cursor) control your browser remotely.

The **Kimi API Platform** (by Moonshot AI) is the separate service that provides LLM API access with OpenAI-compatible endpoints. Registration gives you **free credits** and an API key.

---

## 2. Clarification: WebBridge vs Kimi API

| Feature | Kimi WebBridge | Kimi API Platform |
|---------|---------------|-------------------|
| **What** | Browser extension (Chrome/Edge) | LLM API (OpenAI-compatible) |
| **Purpose** | Let AI agents control your browser | Programmatic access to Kimi LLM |
| **URL** | https://www.kimi.com/zh-cn/features/webbridge | https://platform.moonshot.ai / https://platform.kimi.ai |
| **API Key** | No API key needed | Yes, API key required (SK-xxx) |
| **Cost** | Free (with Kimi subscription) | Free credits + pay-as-you-go |
| **SDK** | N/A | OpenAI Python/Node.js SDK compatible |

---

## 3. Kimi WebBridge - Browser Automation Plugin

### What It Does
- A Chrome/Edge browser extension that acts as a bridge between AI agents and your browser
- Agents can: open web pages, click buttons, fill forms, extract information, take screenshots
- Runs **locally** on your device - login state and page content never leave your machine
- Uses Chrome DevTools Protocol for browser automation

### System Requirements
- **OS**: macOS or Windows
- **Browser**: Chrome or Edge
- **Network**: Stable internet connection
- **Companion**: Kimi Work desktop app OR a local agent (Claude Code, Codex, Cursor, Kimi Code, Hermes Agent)

### Installation

#### Option 1: Chrome Web Store / Edge Add-ons
- Chrome: Go to Chrome Web Store, search for "Kimi WebBridge"
- Edge: Go to Edge Add-ons, search for "Kimi WebBridge"

#### Option 2: Manual Installation
1. Download the plugin installation package from https://www.kimi.com/zh-cn/features/webbridge
2. Extract the downloaded file
3. For Chrome: go to `chrome://extensions/`, enable "Developer mode", click "Load unpacked", select the extracted folder
4. For Edge: go to `edge://extensions/`, enable "Developer mode", click "Load unpacked", select the extracted folder

#### Option 3: Quick Install for Local Agents (One-liner)
```bash
# macOS
curl -fsSL https://kimi-web-img.moonshot.cn/webbridge/install_skill.sh | bash -s -- -y

# Windows (PowerShell)
irm https://kimi-web-img.moonshot.cn/webbridge/install.ps1 | iex
```

### Usage
After installation, send prompts to your AI agent like:
```
使用Kimi WebBridge 帮我打开小红书，搜索关于 Kimi K2.6 发布的帖子
```

### How It Works
1. Agent sends instructions to a **local bridge service**
2. The browser extension executes the actions via Chrome DevTools Protocol
3. Results (screenshots, page content) are sent back to the agent
4. Everything runs locally - no data leaves your device

---

## 4. Kimi API Platform - LLM API Access

### Platform URLs
| Platform | URL | Language |
|----------|-----|----------|
| Moonshot AI (Global) | **https://platform.moonshot.ai** | English |
| Kimi AI (Global) | **https://platform.kimi.ai** | English |
| Moonshot AI (China) | **https://platform.moonshot.cn** | Chinese |
| Kimi Main Site | **https://www.kimi.com** | Chinese |

### API Documentation
- English: https://platform.kimi.ai/docs/guide/start-using-kimi-api
- Chinese: https://platform.moonshot.cn/blog/posts/kimi-api-quick-start-guide
- API Reference: https://platform.kimi.ai/docs/api-reference
- Pricing: https://platform.kimi.ai/docs/pricing/chat

### API Base URLs
```
Global:  https://api.moonshot.ai/v1
China:   https://api.moonshot.cn/v1
```

---

## 5. Registration & Getting an API Key

### Step 1: Create Account

**Option A - Global Platform (Google Sign-in)**:
1. Go to https://platform.moonshot.ai
2. Click "Get Started"
3. Sign in with Google account
4. Requires a payment method for API access

**Option B - China Platform (Phone Number)**:
1. Go to https://platform.moonshot.cn
2. Register with phone number (same as Kimi app account)
3. Platform gives you **15 RMB free credits** upon registration

### Step 2: Generate API Key
1. Go to: https://platform.moonshot.ai/console/api-keys (global) or https://platform.moonshot.cn/console/api-keys (China)
2. Click "Create API Key" / "新建 API Key"
3. Enter a name for your key
4. **Copy the key immediately** - it is only shown once!
5. Store it securely (password manager, .env file, secrets manager)
6. API keys start with `sk-` prefix

### Step 3: Recharge (if needed)
- The global platform requires a minimum recharge of **$1 USD** to activate API access
- The China platform gives **15 RMB free credits** for testing
- Reddit users report **500K free tokens per day** on the free tier

---

## 6. API Details

### Authentication
- **Method**: Bearer Token (HTTP Authorization header)
- **Header**: `Authorization: Bearer sk-YOUR_API_KEY`

### OpenAI Compatibility
The Kimi API is **fully compatible** with the OpenAI API format. You can use the official OpenAI SDK directly.

### Key Endpoints
```
POST /v1/chat/completions    - Chat completion (main API)
POST /v1/completions          - Text completion
POST /v1/embeddings           - Text embeddings
GET  /v1/models               - List available models
POST /v1/files                - Upload files
POST /v1/chat/completions (stream) - Streaming responses
```

### Request Format (OpenAI-compatible)
```json
{
  "model": "kimi-k2.6",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  "temperature": 0.7,
  "max_tokens": 1024
}
```

### Key Features
- **256K context window** (double most competitors)
- **Multimodal** (text + vision/image input)
- **Tool Calling** / Function Calling
- **Streaming** responses
- **File-based Q&A** (upload documents for analysis)
- **Web Search Tool** integration
- **Thinking Models** support
- **Batch API** for bulk inference

---

## 7. Supported Models

### Current Models (as of 2026-06)

| Model | ID | Context | Description |
|-------|-----|---------|-------------|
| **Kimi K2.6** | `kimi-k2.6` | 256K | Latest multimodal model with vision + text |
| **Kimi K2.5** | `kimi-k2.5` | 256K | Multimodal model with vision + text |
| Moonshot V1 (128K) | `moonshot-v1-128k` | 128K | Original generation model |
| Moonshot V1 (32K) | `moonshot-v1-32k` | 32K | Original generation model |
| Moonshot V1 (8K) | `moonshot-v1-8k` | 8K | Original generation model |

### Available on Third-Party Platforms
- **OpenRouter**: `moonshotai/kimi-k2.6` (free tier available!)
- **NVIDIA NIM**: `moonshotai/kimi-k2.6`
- **Together AI**: `moonshotai/kimi-k2-instruct`
- **Puter**: `kimi-k2.5`, `kimi-k2.6`

---

## 8. Pricing

### Official Kimi API Pricing (per million tokens)

| Model | Cache Hit | Input | Output |
|-------|-----------|-------|--------|
| **Kimi K2.6** | $0.16/MTok | $0.95/MTok | $4.00/MTok |
| **Kimi K2.5** | $0.10/MTok | $0.60/MTok | $3.00/MTok |
| **Moonshot V1** | - | $2.00/MTok | $2.00/MTok |

> Note: 1 token ≈ 3-4 English characters

### Estimated Monthly Costs
| Usage Level | Estimated Cost |
|-------------|---------------|
| Light use | $5-40/month |
| Medium use | $40-200/month |
| Heavy use | $200-800/month |

---

## 9. Free Tier

### Official Kimi Platform
- **China platform**: 15 RMB (~$2 USD) free credits upon registration
- **Global platform**: Requires minimum $1 recharge to activate
- Reddit reports: **500K tokens per day** free tier allowance

### Third-Party Free Access

#### OpenRouter (Recommended for Free Access)
- URL: https://openrouter.ai/moonshotai/kimi-k2.6:free
- Offers a **free variant** of Kimi K2
- Works with Claude Code and other tools
- Rate limited but great for testing

#### NVIDIA NIM
- URL: https://build.nvidia.com/moonshotai/kimi-k2.6
- Free API endpoint for developer testing
- OpenAI-compatible

#### Puter
- URL: https://puter.com
- Single auth token for hundreds of models including Kimi
- Free tier available

---

## 10. Kimi CLI / Kimi Code

### Kimi CLI (now transitioning to Kimi Code)
- **GitHub**: https://github.com/MoonshotAI/kimi-cli
- **Stars**: 8.9k+, Forks: 1.1k+
- **Latest version**: 1.47.0 (June 2026)
- **Language**: Python/Node.js/Rust
- **Description**: AI agent that runs in the terminal, helping with software development and terminal operations

### Installation
```bash
# Via npm (Node.js)
npm install -g @anthropic-ai/claude-code  # Alternative: check kimi-cli docs

# Check GitHub for latest installation instructions:
# https://github.com/MoonshotAI/kimi-cli
```

### Features
- Read and edit code in the terminal
- Execute terminal commands
- AI-powered code generation and debugging
- Compatible with Kimi API
- Transitioning to "Kimi Code" branding

---

## 11. Quick Start Code Examples

### Python (OpenAI SDK)
```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-YOUR_KIMI_API_KEY",  # Replace with your API Key
    base_url="https://api.moonshot.ai/v1",  # or https://api.moonshot.cn/v1
)

completion = client.chat.completions.create(
    model="kimi-k2.6",
    messages=[
        {
            "role": "system",
            "content": "You are Kimi, an AI assistant provided by Moonshot AI."
        },
        {
            "role": "user",
            "content": "Hello! What can you do?"
        }
    ],
    temperature=0.7,
)

print(completion.choices[0].message.content)
```

### Node.js (OpenAI SDK)
```javascript
const OpenAI = require("openai");

const client = new OpenAI({
    apiKey: "sk-YOUR_KIMI_API_KEY",
    baseURL: "https://api.moonshot.ai/v1",
});

async function main() {
    const completion = await client.chat.completions.create({
        model: "kimi-k2.6",
        messages: [
            { role: "system", content: "You are Kimi, an AI assistant provided by Moonshot AI." },
            { role: "user", content: "Hello! What can you do?" }
        ],
    });
    console.log(completion.choices[0].message.content);
}

main();
```

### cURL
```bash
curl https://api.moonshot.ai/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-YOUR_KIMI_API_KEY" \
  -d '{
    "model": "kimi-k2.6",
    "messages": [
      {"role": "system", "content": "You are Kimi, an AI assistant."},
      {"role": "user", "content": "Hello!"}
    ]
  }'
```

### Using with Claude Code / Cursor / Other AI Tools
```json
{
  "model": "kimi-k2.6",
  "baseURL": "https://api.moonshot.ai/v1",
  "apiKey": "sk-YOUR_KIMI_API_KEY"
}
```

---

## 12. Third-Party Free Access Options

### Option 1: OpenRouter (Easiest Free Access)
1. Go to https://openrouter.ai
2. Create a free account
3. Generate an API key from the dashboard
4. Use the free Kimi K2.6 endpoint:
```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-or-YOUR_OPENROUTER_KEY",
    base_url="https://openrouter.ai/api/v1",
)

response = client.chat.completions.create(
    model="moonshotai/kimi-k2.6:free",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

### Option 2: NVIDIA NIM
1. Go to https://build.nvidia.com/moonshotai/kimi-k2.6
2. Create a free NVIDIA developer account
3. Get API key from dashboard
4. Use NVIDIA's OpenAI-compatible endpoint

### Option 3: Puter
1. Go to https://puter.com
2. Create a free account
3. Get auth token from https://puter.com/dashboard
4. Use Puter's OpenAI-compatible endpoint:
```javascript
import OpenAI from "openai";

const client = new OpenAI({
    baseURL: "https://api.puter.com/puterai/openai/v1/",
    apiKey: "YOUR_PUTER_AUTH_TOKEN",
});

const response = await client.chat.completions.create({
    model: "kimi-k2.6",
    messages: [{ role: "user", content: "Hello!" }],
});
```

---

## 13. Summary & Recommendations

### For API Access
1. **Cheapest entry**: Register at https://platform.moonshot.cn (China) for 15 RMB free credits
2. **Global access**: Register at https://platform.moonshot.ai with Google account, minimum $1 recharge
3. **Completely free**: Use OpenRouter's `moonshotai/kimi-k2.6:free` endpoint
4. **Best for developers**: Kimi API is fully OpenAI-compatible - just change `base_url` and `api_key`

### For WebBridge (Browser Automation)
1. Install Kimi desktop app from https://www.kimi.com
2. Install the WebBridge browser extension (Chrome/Edge)
3. Use with Kimi Work, Claude Code, Cursor, or other agents
4. All operations are local - your login state stays on your device

### For CLI/IDE Integration
1. Check out **Kimi CLI** at https://github.com/MoonshotAI/kimi-cli (now becoming Kimi Code)
2. Configure any OpenAI-compatible tool to point to `https://api.moonshot.ai/v1`
3. Works with Dify, NextChat, OpenAI Translator, and many other tools

### Key URLs
| Resource | URL |
|----------|-----|
| Kimi API Platform (Global) | https://platform.moonshot.ai |
| Kimi API Platform (China) | https://platform.moonshot.cn |
| Kimi API Docs | https://platform.kimi.ai/docs |
| WebBridge Feature Page | https://www.kimi.com/zh-cn/features/webbridge |
| WebBridge Help | https://www.kimi.com/zh-cn/help/kimi-webbridge |
| Kimi CLI GitHub | https://github.com/MoonshotAI/kimi-cli |
| OpenRouter Free Kimi | https://openrouter.ai/moonshotai/kimi-k2.6:free |
| API Keys Management | https://platform.moonshot.ai/console/api-keys |
| Playground | https://platform.kimi.ai/playground |

---

*This document was compiled by 智谱2号战士 through web research. No API key was obtained as registration requires a phone number (China) or Google account (global) with payment method. For testing, the OpenRouter free tier is recommended.*
