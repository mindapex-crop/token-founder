# 🌐 Comprehensive Free AI Model API Report (June 2026)

> Compiled by 智谱2号战士 | Last updated: June 2026
> This report covers ALL known free AI model APIs worldwide.

---

## Table of Contents

1. [Chinese AI Providers with Free Tiers](#1-chinese-ai-providers-with-free-tiers)
2. [International Providers with Free Tiers](#2-international-providers-with-free-tiers)
3. [Cloud Providers Offering Free AI Credits](#3-cloud-providers-offering-free-ai-credits)
4. [Aggregator Platforms with Free Models](#4-aggregator-platforms-with-free-models)
5. [Special/Hidden Free Tiers](#5-specialhidden-free-tiers)
6. [Quick Comparison Table](#6-quick-comparison-table)
7. [Best Practices & Tips](#7-best-practices--tips)

---

## 1. Chinese AI Providers with Free Tiers

### 1.1 硅基流动 SiliconCloud (SiliconFlow)

| Item | Detail |
|------|--------|
| **Provider** | 硅基流动 (SiliconFlow) |
| **Website** | https://siliconflow.cn |
| **API Base URL** | `https://api.siliconflow.cn/v1` |
| **Free Models** | DeepSeek-V3, Qwen3 series (235B/30B/Coder), ChatGLM series, Llama series, and many more |
| **Free Tier** | New user registration gives generous free tokens (up to 20M tokens); many models permanently free |
| **Rate Limits** | Varies by model; free models typically 10-30 RPM |
| **Registration** | Email + phone (Chinese number); optional real-name verification for more quota |
| **OpenAI Compatible** | ✅ Yes (OpenAI SDK compatible) |
| **How to Get Key** | Sign up → Console → API Keys → Create |

**Notes:** One of the most generous Chinese platforms. Multiple popular open-source models available for free. OpenAI-compatible API format makes switching easy.

---

### 1.2 智谱AI BigModel.cn (GLM Series)

| Item | Detail |
|------|--------|
| **Provider** | 智谱AI (Zhipu AI) |
| **Website** | https://open.bigmodel.cn |
| **API Base URL** | `https://open.bigmodel.cn/api/paas/v4` (custom) or use SiliconFlow's OpenAI-compatible endpoint |
| **Free Models** | **GLM-4.7-Flash** (free & open source), GLM-4.6, GLM-4.5 series |
| **Free Tier** | GLM-4.7-Flash: **Permanently free** with 40 RPM limit; other models have daily/hourly token quotas |
| **Rate Limits** | ~40 requests/min for GLM-4.7-Flash |
| **Registration** | Email + phone; real-name verification (身份证) required for full access |
| **OpenAI Compatible** | ✅ Yes (compatible format, but custom base URL) |
| **How to Get Key** | Register → Console → API Keys |

**Notes:** GLM-4.7-Flash replaced GLM-4.5-Flash as the free flagship. Excellent Chinese language understanding. Permanently free tier for Flash models.

---

### 1.3 阿里云百炼 (Alibaba Cloud Bailian / Qwen)

| Item | Detail |
|------|--------|
| **Provider** | 阿里云 (Alibaba Cloud) |
| **Website** | https://bailian.console.aliyun.com |
| **API Base URL** | `https://dashscope.aliyuncs.com/compatible-mode/v1` (OpenAI compatible) |
| **Free Models** | Qwen3.5 series, Qwen3 series (235B, 30B, Coder), **DeepSeek series**, Kimi series, MiniMax series, GLM series |
| **Free Tier** | Each model: **500,000 tokens free (permanently valid)**; auto-claim 500K tokens on activation |
| **Rate Limits** | Varies by model tier |
| **Registration** | Alibaba Cloud account required (email + phone); real-name verification needed |
| **OpenAI Compatible** | ✅ Yes |
| **How to Get Key** | Alibaba Cloud console → Bailian → Get API Key (DashScope) |

**Notes:** Permanently valid free tokens are unique. Supports a massive variety of models including third-party ones. Collaboration reward plan gives additional daily tokens.

---

### 1.4 百度千帆 (Baidu Qianfan / ERNIE)

| Item | Detail |
|------|--------|
| **Provider** | 百度 (Baidu) |
| **Website** | https://cloud.baidu.com/product/wenxinworkshop |
| **API Base URL** | `https://aip.baidubce.com` (custom format) |
| **Free Models** | ERNIE-4.5 series, DeepSeek R1/V3/V3.1 (with Think), Qwen3 series, Kimi-K2-Instruct, bge-large (embedding) |
| **Free Tier** | **1,000,000 tokens per model** (per 3 months); covers DeepSeek, Qwen, Kimi, and more |
| **Rate Limits** | Varies; ~3 month validity per model quota |
| **Registration** | Baidu account + real-name verification |
| **OpenAI Compatible** | ⚠️ Partial (custom format, some models via compatible endpoint) |
| **How to Get Key** | Qianfan console → Auto-issued upon platform activation |

**Notes:** Huge model selection. Each model gets independent free quota. 3-month validity means you need to use it before it expires.

---

### 1.5 火山引擎 / 字节豆包 (Volcengine / ByteDance Doubao)

| Item | Detail |
|------|--------|
| **Provider** | 字节跳动 (ByteDance) / 火山引擎 (Volcengine) |
| **Website** | https://console.volcengine.com/ark |
| **API Base URL** | `https://ark.cn-beijing.volces.com/api/v3` (OpenAI compatible) |
| **Free Models** | Doubao (豆包) series, Qwen series, DeepSeek series, Kimi series, MiniMax series, GLM series |
| **Free Tier** | 安心体验模式: **500K tokens per model**; 协作奖励计划: **2,000,000 tokens per day** (resets daily!) |
| **Rate Limits** | Daily-reset quota |
| **Registration** | Volcengine account (phone); real-name verification needed |
| **OpenAI Compatible** | ✅ Yes |
| **How to Get Key** | Volcengine console → Ark → Free quota auto-applied |

**Notes:** **Best for daily-reset quotas.** The 2M tokens/day collaboration plan is outstanding for automated scripts. Tokens reset every day so you never run out.

---

### 1.6 腾讯云混元 (Tencent Cloud Hunyuan)

| Item | Detail |
|------|--------|
| **Provider** | 腾讯云 (Tencent Cloud) |
| **Website** | https://cloud.tencent.com/product/hunyuan |
| **API Base URL** | `https://hunyuan.tencentcloudapi.com` (custom) |
| **Free Models** | Hunyuan-large-role, Hunyuan-translation, Vision 1.5 Instruct, Hunyuan-embedding |
| **Free Tier** | **1,000,000 tokens/year** for Hunyuan series models |
| **Rate Limits** | Annual quota; one of the most generous among Chinese providers for total volume |
| **Registration** | Tencent Cloud account; real-name verification needed |
| **OpenAI Compatible** | ⚠️ Partial |
| **How to Get Key** | Activate Hunyuan service → Free quota auto-applied |

---

### 1.7 月之暗面 Moonshot (Kimi)

| Item | Detail |
|------|--------|
| **Provider** | 月之暗面 (Moonshot AI) |
| **Website** | https://platform.moonshot.cn |
| **API Base URL** | `https://api.moonshot.cn/v1` |
| **Free Models** | Kimi K2 series (kimi-latest, moonshot-v1-8k/32k/128k) |
| **Free Tier** | New user free credits + daily quota; amount varies |
| **Rate Limits** | ~3 RPM for free tier |
| **Registration** | Phone number (Chinese) |
| **OpenAI Compatible** | ✅ Yes |
| **How to Get Key** | Register → API Keys → Create |

**Notes:** Exceptional long-context handling (128K+). Kimi K2 is excellent for document processing.

---

### 1.8 DeepSeek 官方

| Item | Detail |
|------|--------|
| **Provider** | DeepSeek (幻方量化) |
| **Website** | https://platform.deepseek.com |
| **API Base URL** | `https://api.deepseek.com/v1` |
| **Free Models** | DeepSeek-V3, DeepSeek-R1 series, DeepSeek-Coder |
| **Free Tier** | **5,000,000 free tokens** for new accounts (~$8-10 value); no credit card required |
| **Rate Limits** | Free models (`:free` suffix on some platforms): 20 RPM |
| **Registration** | Email (international OK); phone optional |
| **OpenAI Compatible** | ✅ Yes (fully compatible) |
| **How to Get Key** | Sign up → Platform → Create API key |

**Notes:** One of the most powerful open models available. Also accessible for free via OpenRouter (`deepseek/deepseek-r1:free`) and SiliconFlow.

---

### 1.9 MiniMax

| Item | Detail |
|------|--------|
| **Provider** | MiniMax |
| **Website** | https://www.minimaxi.com / https://platform.minimaxi.com |
| **API Base URL** | `https://api.minimax.chat/v1` |
| **Free Models** | **MiniMax-M2** (continuing free), MiniMax-Text-01 |
| **Free Tier** | **M2 model: completely free** (temporarily/permanently); generous free credits for new users |
| **Rate Limits** | M2: Unlimited (but may throttle during peak); other models: limited free credits |
| **Registration** | Email or phone |
| **OpenAI Compatible** | ✅ Yes |
| **How to Get Key** | Platform registration → API Keys |

**Notes:** M2 is specifically strong at coding and agent tasks. Continued free access despite resource pressure.

---

### 1.10 讯飞星火 (iFlytek Spark)

| Item | Detail |
|------|--------|
| **Provider** | 科大讯飞 (iFlytek) |
| **Website** | https://xinghuo.xfyun.cn |
| **API Base URL** | Custom format |
| **Free Models** | Spark-lite, Spark-Ultra, Spark-Max, Spark-Pro |
| **Free Tier** | spark-lite: free; higher models: free quota with limits |
| **Rate Limits** | Limited for free tier |
| **Registration** | Phone number (Chinese) |
| **OpenAI Compatible** | ⚠️ Partial (requires wrapper) |
| **How to Get Key** | Register → Console → API Key |

---

### 1.11 小米 MiMo

| Item | Detail |
|------|--------|
| **Provider** | 小米 (Xiaomi) |
| **Website** | https://platform.xiaomimimo.com |
| **API Base URL** | Custom |
| **Free Models** | MiMo series (focus on reasoning) |
| **Free Tier** | **Currently free** (limited-time promotion) |
| **Rate Limits** | Limited during beta |
| **Registration** | Xiaomi account |
| **OpenAI Compatible** | ⚠️ Check documentation |
| **How to Get Key** | Platform registration |

**Notes:** Focused on mathematical reasoning and code generation. Limited-time free access.

---

### 1.12 零一万物 (01.AI / Yi)

| Item | Detail |
|------|--------|
| **Provider** | 零一万物 (01.AI) |
| **Website** | https://platform.lingyiwanwu.com |
| **API Base URL** | Custom |
| **Free Models** | Yi series |
| **Free Tier** | Limited free credits for new users |
| **Registration** | Email + phone |
| **OpenAI Compatible** | ⚠️ Partial |

---

## 2. International Providers with Free Tiers

### 2.1 Google Gemini API / AI Studio

| Item | Detail |
|------|--------|
| **Provider** | Google |
| **Website** | https://aistudio.google.com / https://ai.google.dev |
| **API Base URL** | `https://generativelanguage.googleapis.com/v1beta` or `https://generativelanguage.googleapis.com/v1beta/openai/` (OpenAI compatible) |
| **Free Models** | Gemini 2.5 Flash, Gemini 2.0 Flash, Gemini 1.5 Flash, Gemini 1.5 Pro (limited), Gemini 3.1 Flash Lite |
| **Free Tier Limits** | |
| | Gemini 2.5 Flash: **10 RPM**, 250K TPM, **1,500 RPD** |
| | Gemini 1.5 Flash: **15 RPM**, **1,500 RPD** (most generous) |
| | Gemini 2.0 Flash: **10 RPM**, 250K TPM, ~1,000 RPD |
| | Gemini 3.1 Flash Lite: High RPD limits |
| **Registration** | Google account only; no credit card |
| **OpenAI Compatible** | ✅ Yes (via `/openai/` endpoint) |
| **How to Get Key** | AI Studio → Get API Key → One click |

**Notes:** ⭐ **HIGHEST free tier among international providers.** 1,500 RPD for Flash models is enormous. No credit card, no phone, just Google account. **RECOMMENDED #1.**

---

### 2.2 Groq

| Item | Detail |
|------|--------|
| **Provider** | Groq |
| **Website** | https://groq.com |
| **API Base URL** | `https://api.groq.com/openai/v1` |
| **Free Models** | Llama 3.3 70B, Llama 4 Scout/Maverick, Mixtral, Gemma 2, DeepSeek, Qwen3 32B, Kimi K2, Whisper, GPT-OSS |
| **Free Tier** | **All models free** with rate limits; no credit card required |
| **Rate Limits** | ~30 RPM, ~6,000 RPM (requests per minute across all models); TPM caps vary |
| **Registration** | Email only; no credit card |
| **OpenAI Compatible** | ✅ Yes (natively OpenAI SDK compatible) |
| **How to Get Key** | Console → Create API key → Instant |

**Notes:** ⭐ **ULTRA-FAST inference** using custom LPU hardware. All models accessible for free. Excellent for real-time applications. **RECOMMENDED #2.**

---

### 2.3 Cerebras

| Item | Detail |
|------|--------|
| **Provider** | Cerebras Systems |
| **Website** | https://cerebras.ai |
| **API Base URL** | `https://api.cerebras.ai/v1` |
| **Free Models** | Llama 3.3 70B, Llama 3.1 8B (and more) |
| **Free Tier** | **Up to 1,000,000 tokens per day** free; no credit card |
| **Rate Limits** | 1M TPD for free; developer tier: 10x higher |
| **Registration** | Email only |
| **OpenAI Compatible** | ✅ Yes |
| **How to Get Key** | Sign up → Get API key |

**Notes:** World's fastest AI inference (wafer-scale chip). 1M tokens/day free is very generous.

---

### 2.4 Mistral AI

| Item | Detail |
|------|--------|
| **Provider** | Mistral AI |
| **Website** | https://mistral.ai / https://console.mistral.ai |
| **API Base URL** | `https://api.mistral.ai/v1` |
| **Free Models** | Mistral Small, Mistral NeMo, Codestral, Mistral Large (limited), Pixtral (limited) |
| **Free Tier** | Free mode enabled by default with limited rate limits; 1 request/second global limit |
| **Rate Limits** | Free: 1 RPS, limited RPM; Scale plan for higher limits |
| **Registration** | Email |
| **OpenAI Compatible** | ✅ Yes |
| **How to Get Key** | La Plateforme → Sign up → API key |

**Notes:** French AI company. Free tier includes latest models (Vibe access). Great for prototyping.

---

### 2.5 Cohere

| Item | Detail |
|------|--------|
| **Provider** | Cohere |
| **Website** | https://cohere.com |
| **API Base URL** | `https://api.cohere.ai/v1` |
| **Free Models** | Command R+, Command R7B, Embed v3, Rerank v3.5 |
| **Free Tier** | **Trial key: all API calls FREE**; ~1,000 calls/month across all models |
| **Rate Limits** | Trial key: limited but free; Production key: pay-as-you-go |
| **Registration** | Email |
| **OpenAI Compatible** | ⚠️ Partial (custom format, but has OpenAI-compatible wrapper) |
| **How to Get Key** | Dashboard → Create Trial API key |

**Notes:** Trial key gives free access to ALL models including embeddings and reranking. Command R7B is extremely cost-effective.

---

### 2.6 NVIDIA NIM APIs

| Item | Detail |
|------|--------|
| **Provider** | NVIDIA |
| **Website** | https://build.nvidia.com |
| **API Base URL** | `https://integrate.api.nvidia.com/v1` |
| **Free Models** | **80+ AI models** including Llama, Mistral, Google, Meta models, Nemotron, etc. |
| **Free Tier** | **Free serverless APIs for development**; accelerated by DGX Cloud |
| **Rate Limits** | Development tier limits; higher for paid |
| **Registration** | NVIDIA Developer account (free) |
| **OpenAI Compatible** | ✅ Yes |
| **How to Get Key** | build.nvidia.com → Sign in → Get API key |

**Notes:** 80+ models all accessible for free during development. Accelerated by NVIDIA DGX Cloud infrastructure.

---

### 2.7 Anthropic Claude (Limited Free Access)

| Item | Detail |
|------|--------|
| **Provider** | Anthropic |
| **Website** | https://www.anthropic.com |
| **API Base URL** | `https://api.anthropic.com/v1` |
| **Free Models** | Claude Opus 4.x, Claude Sonnet 4.x, Claude Haiku |
| **Free Tier** | ⚠️ **No permanent free tier**; but offers: |
| | • Startup credits: $25,000–$100,000 (application required) |
| | • Occasional promotions ($100 credits via partners like Lovable.dev) |
| | • Claude.ai: free web access (not API) with limits |
| **Registration** | Email; credit card required for API |
| **OpenAI Compatible** | ❌ No (custom Anthropic format; but has OpenAI-compatible wrapper) |
| **How to Get Key** | Console → Create API key (requires payment method) |

**Notes:** No permanent free API tier. Look for promotions and startup programs.

---

### 2.8 OpenAI

| Item | Detail |
|------|--------|
| **Provider** | OpenAI |
| **Website** | https://platform.openai.com |
| **API Base URL** | `https://api.openai.com/v1` |
| **Free Models** | GPT-4o, GPT-4o-mini, o1/o3/o4-mini (all require credits) |
| **Free Tier** | ⚠️ **No automatic free credits** for new accounts since 2025 |
| | • Must add payment method |
| | • Some tool builders get daily complimentary credits (application required) |
| | • Students: check for educational credits |
| **Registration** | Email + payment method |
| **OpenAI Compatible** | ✅ Yes (they ARE the standard) |
| **How to Get Key** | Platform → API Keys → Create |

**Notes:** No free trial credits anymore. You must pay to play. However, GPT-4o-mini is extremely cheap.

---

### 2.9 SambaNova

| Item | Detail |
|------|--------|
| **Provider** | SambaNova Systems |
| **Website** | https://sambanova.ai |
| **API Base URL** | `https://api.sambanova.ai/v1` |
| **Free Models** | Llama 3.x, DeepSeek, and more |
| **Free Tier** | Free inference API available |
| **Registration** | Email |
| **OpenAI Compatible** | ✅ Yes |
| **How to Get Key** | Sign up → API key |

**Notes:** Fast inference with custom chip architecture. Free tier available for development.

---

## 3. Cloud Providers Offering Free AI Credits

### 3.1 Google Cloud Platform (GCP)

| Item | Detail |
|------|--------|
| **Offer** | **$300 in free credits** + 20+ free products |
| **AI Services** | Vertex AI (Gemini models), Cloud AI APIs |
| **Validity** | 90 days after credit claim |
| **Registration** | Google account + credit card (required but not charged) |
| **How to Get** | https://cloud.google.com/free → Start Free Trial |
| **Bonus** | Always Free tier includes limited Vertex AI usage after trial ends |

**Notes:** $300 credits go far with Gemini pricing. Always Free tier gives sustained access to some AI features.

---

### 3.2 AWS (Amazon Web Services)

| Item | Detail |
|------|--------|
| **Offer** | **AWS Free Tier** (12 months) + ongoing free tier |
| **AI Services** | Amazon Bedrock (Claude, Titan, Llama, Mistral), Amazon SageMaker |
| **Validity** | 12 months for some services; some always free |
| **Registration** | Email + credit card + phone verification |
| **How to Get** | https://aws.amazon.com/free → Create account |
| **Bonus** | Bedrock offers limited free invocations for some models |

**Notes:** Bedrock free tier gives limited access to Anthropic Claude, Meta Llama, and Amazon Titan models.

---

### 3.3 Azure (Microsoft)

| Item | Detail |
|------|--------|
| **Offer** | **$200 in free Azure credits** (popular promotions) |
| **AI Services** | Azure OpenAI Service (GPT-4o, GPT-4o-mini, etc.) |
| **Validity** | 30 days typical |
| **Registration** | Microsoft account |
| **How to Get** | https://azure.microsoft.com/free → Various promotions |

**Notes:** Azure OpenAI gives access to GPT-4 series. Look for promotional credits.

---

### 3.4 Oracle Cloud (OCI)

| Item | Detail |
|------|--------|
| **Offer** | **Always Free tier** with substantial compute |
| **AI Services** | OCI Generative AI, limited free capacity |
| **Validity** | Always Free (permanent) |
| **Registration** | Email + phone + credit card |
| **How to Get** | https://cloud.oracle.com/free → Start for free |
| **Bonus** | Up to 4 ARM Ampere instances + GPU instances available |

**Notes:** Very generous Always Free tier. Some GPU compute available for running your own models.

---

### 3.5 Cloudflare Workers AI

| Item | Detail |
|------|--------|
| **Provider** | Cloudflare |
| **Website** | https://developers.cloudflare.com/workers-ai/ |
| **API Base URL** | Via Cloudflare Workers |
| **Free Models** | **78+ models** including Llama 4, Qwen, Kimi K2.6, Whisper, Mistral, etc. |
| **Free Tier** | **10,000 Neurons/day** for free; Workers Free plan included |
| **Rate Limits** | 10K neurons/day on free plan |
| **Registration** | Cloudflare account (free) |
| **OpenAI Compatible** | ⚠️ Partial (use Workers AI bindings) |
| **How to Get** | Cloudflare dashboard → Workers AI → Enable |

**Notes:** 78+ models including frontier models. Integrated with edge computing (Workers). Great for building AI features into web apps.

---

## 4. Aggregator Platforms with Free Models

### 4.1 OpenRouter

| Item | Detail |
|------|--------|
| **Website** | https://openrouter.ai |
| **API Base URL** | `https://openrouter.ai/api/v1` |
| **Free Models** (constantly updated) | |
| | 🔥 **Qwen 3.6 Plus** (`qwen/qwen3.6-plus:free`) — completely free, 1M context |
| | 🔥 **Qwen3 Coder** (`qwen/qwen3-coder:free`) — code generation focused |
| | **DeepSeek R1** (`deepseek/deepseek-r1:free`) |
| | **DeepSeek V3** (`deepseek/deepseek-chat:free`) |
| | **Llama 4 Maverick** (`meta-llama/llama-4-maverick:free`) |
| | **Llama 3.3 70B** (`meta-llama/llama-3.3-70b-instruct:free`) |
| | **Gemma 3** (`google/gemma-3-27b-it:free`) |
| | **Mistral Small** (`mistralai/mistral-small-24b-instruct-2501:free`) |
| | Plus hundreds more with very low pricing |
| **Free Tier** | Multiple models at **$0.00** (both input and output); some with shared community pool |
| **Rate Limits** | Free models: ~20 RPM; paid: higher |
| **Registration** | Email; no credit card for free models |
| **OpenAI Compatible** | ✅ Yes |
| **How to Get Key** | Sign up → Keys → Create |

**Notes:** ⭐ **BEST aggregator for free models.** Unified API across hundreds of models. Qwen 3.6 Plus being completely free is huge. Automatically routes to cheapest provider. **RECOMMENDED #3.**

---

### 4.2 HuggingFace Inference API

| Item | Detail |
|------|--------|
| **Website** | https://huggingface.co/inference-api |
| **API Base URL** | `https://api-inference.huggingface.co/models/` |
| **Free Models** | Thousands of community models (Llama, Mistral, Qwen, etc.) |
| **Free Tier** | Free inference for most models; rate limited |
| **Rate Limits** | Varies; ~1000 requests/day for popular models |
| **Registration** | HuggingFace account (free, email) |
| **OpenAI Compatible** | ⚠️ Partial (has OpenAI-compatible Text Generation Inference) |
| **How to Get Key** | HF account → Settings → Access Tokens |

---

### 4.3 Together AI

| Item | Detail |
|------|--------|
| **Website** | https://together.ai |
| **API Base URL** | `https://api.together.xyz/v1` |
| **Free Models** | Many open-source models |
| **Free Tier** | **$5–$100 free credits** for new accounts (varies by promotion); 30-90 day expiration |
| **Registration** | Email |
| **OpenAI Compatible** | ✅ Yes |
| **How to Get Key** | Sign up → Credits auto-applied → API Key |

**Notes:** Watch for promotions that give higher credits. Good for fine-tuning experiments.

---

### 4.4 Fireworks AI

| Item | Detail |
|------|--------|
| **Website** | https://fireworks.ai |
| **API Base URL** | `https://api.fireworks.ai/inference/v1` |
| **Free Models** | Llama, Qwen, Mistral, and more |
| **Free Tier** | Free credits for new accounts; some models have free tier |
| **Registration** | Email |
| **OpenAI Compatible** | ✅ Yes |
| **How to Get Key** | Sign up → API Keys |

---

## 5. Special/Hidden Free Tiers

### 5.1 Google AI Studio (Web Interface)

- **URL:** https://aistudio.google.com
- **Free access** to Gemini Pro/Ultra models via web chat interface
- Can export prompts as API calls
- No rate limiting on web interface (generous limits)
- Great for testing before API integration

### 5.2 Google Colab

- **URL:** https://colab.research.google.com
- **Free GPU** (T4) access for running local models
- Can also use Gemini API within Colab notebooks
- Free tier: ~12 hours of GPU usage per session

### 5.3 Chatbot Arena / LMSYS

- Free access to compare models side-by-side
- Access to GPT-4, Claude, Gemini Pro, and more via web
- Not API but useful for testing

### 5.4 GitHub Copilot Free Tier

- GitHub Copilot now has a free tier for personal use
- Limited completions per month
- Access to Claude and GPT models via IDE

### 5.5 AI/ML API (aimlapi.com)

- 400+ models with one API key
- Free tier includes GPT-5, Claude 4, Gemini, DeepSeek, Llama
- No credit card required
- Website: https://aimlapi.com

### 5.6 Price Per Token (pricepertoken.com)

- Useful comparison site tracking free tiers
- Shows exact RPM, RPD, TPM, TPD for every model
- URL: https://pricepertoken.com

### 5.7 GitHub Collections

- **cheahjs/free-llm-api-resources:** https://github.com/cheahjs/free-llm-api-resources
- **mnfst/awesome-free-llm-apis:** https://github.com/mnfst/awesome-free-llm-apis
- **guihuashaoxiang/FreeLLM-API-KeyHub:** https://github.com/guihuashaoxiang/FreeLLM-API-KeyHub (Chinese providers focus)

---

## 6. Quick Comparison Table

| Provider | Free Tier | Best Free Model | OpenAI Compat | Credit Card | Best For |
|----------|-----------|----------------|---------------|-------------|----------|
| **Google Gemini** | 1,500 RPD | Gemini 2.5 Flash | ✅ | ❌ No | Generous daily quota |
| **Groq** | All models free | Llama 4 Scout | ✅ | ❌ No | Speed / real-time |
| **Cerebras** | 1M TPD | Llama 3.3 70B | ✅ | ❌ No | Max speed |
| **OpenRouter** | Multiple $0 models | Qwen 3.6 Plus:free | ✅ | ❌ No | Model variety |
| **SiliconFlow** | 20M tokens | DeepSeek-V3 | ✅ | ❌ No | Chinese models |
| **DeepSeek** | 5M tokens | DeepSeek-V3/R1 | ✅ | ❌ No | Reasoning |
| **智谱AI** | Permanent free | GLM-4.7-Flash | ✅ | ❌ No | Chinese language |
| **阿里百炼** | 500K/model (perm) | Qwen3.5-235B | ✅ | ❌ No | Permanent tokens |
| **火山引擎** | 2M tokens/day | Doubao series | ✅ | ❌ No | Daily reset |
| **百度千帆** | 1M/model (3mo) | ERNIE-4.5 | ⚠️ | ❌ No | Multi-model testing |
| **腾讯混元** | 1M tokens/year | Hunyuan-large | ⚠️ | ❌ No | Annual budget |
| **Kimi/Moonshot** | Daily quota | Kimi K2 | ✅ | ❌ No | Long context |
| **MiniMax** | M2 free | MiniMax-M2 | ✅ | ❌ No | Coding agents |
| **Mistral** | Free mode | Mistral Small | ✅ | ❌ No | EU-based / French |
| **Cohere** | Trial key free | Command R7B | ⚠️ | ❌ No | Embeddings/Rerank |
| **NVIDIA NIM** | 80+ models free | Llama 3.3 70B | ✅ | ❌ No | Model variety |
| **Cloudflare** | 10K neurons/day | 78+ models | ⚠️ | ❌ No | Edge AI / web apps |
| **HuggingFace** | Free inference | Thousands | ⚠️ | ❌ No | Community models |
| **Together AI** | $5-100 credits | Various | ✅ | ❌ No | Fine-tuning |
| **SambaNova** | Free tier | Llama 3.x | ✅ | ❌ No | Fast inference |
| **Anthropic** | ❌ No free tier | Claude Opus 4.8 | ❌ | ✅ Yes | (paid only) |
| **OpenAI** | ❌ No free tier | GPT-4o | ✅ | ✅ Yes | (paid only) |

---

## 7. Best Practices & Tips

### 🏆 Top 3 Recommendations for Different Use Cases

| Use Case | Recommended | Why |
|----------|-------------|-----|
| **Maximum free quota** | Google Gemini (1,500 RPD) | Highest daily limit, no card needed |
| **Ultra-fast inference** | Groq or Cerebras | Custom hardware, all models free |
| **Model variety (free)** | OpenRouter | 100+ models, multiple at $0.00 |
| **Chinese language** | 智谱AI GLM-4.7-Flash or 阿里百炼 Qwen | Permanently free, excellent Chinese |
| **Daily reset (automation)** | 火山引擎 (2M/day) | Resets daily, never expires |
| **Production prototyping** | SiliconFlow (20M tokens) | One-time large quota |
| **Long context** | Kimi K2 (128K+) | Best for document processing |
| **Coding** | MiniMax M2 (free) | Strong coding/agent capabilities |
| **Edge AI / web apps** | Cloudflare Workers AI | Integrated with edge platform |
| **Embeddings/Reranking** | Cohere (trial free) | Trial key gives all models free |

### 💡 Pro Tips

1. **Combine multiple providers**: Use rate limit rotation across Google Gemini, Groq, and OpenRouter for 3x+ the free throughput
2. **Use OpenAI-compatible SDK**: All major providers support it — just change `base_url` and `api_key`
3. **Sign up early**: Some platforms reduce free tiers over time
4. **Watch for promotions**: OpenRouter, Together AI, Anthropic occasionally offer promotional credits
5. **Use free tiers for development, paid for production**: Free tiers are great for prototyping
6. **Monitor rate limits**: Use exponential backoff and key rotation
7. **Chinese providers require real-name verification**: Most need 身份证; some accept international registration

### 🔑 Quick Start Code (Python)

```python
from openai import OpenAI

# Google Gemini
client_gemini = OpenAI(
    api_key="YOUR_GEMINI_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Groq
client_groq = OpenAI(
    api_key="YOUR_GROQ_KEY",
    base_url="https://api.groq.com/openai/v1"
)

# SiliconFlow (Chinese)
client_silicon = OpenAI(
    api_key="YOUR_SILICONFLOW_KEY",
    base_url="https://api.siliconflow.cn/v1"
)

# OpenRouter
client_openrouter = OpenAI(
    api_key="YOUR_OPENROUTER_KEY",
    base_url="https://openrouter.ai/api/v1"
)

# Cerebras
client_cerebras = OpenAI(
    api_key="YOUR_CEREBRAS_KEY",
    base_url="https://api.cerebras.ai/v1"
)

# All use the same interface:
response = client_groq.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

---

## 📊 Summary Statistics

- **Total providers with free tiers: 25+**
- **Chinese providers: 12+** (SiliconFlow, 智谱, 阿里, 百度, 字节, 腾讯, 月之暗面, DeepSeek, MiniMax, 讯飞, 小米, 零一万物)
- **International providers: 10+** (Google, Groq, Cerebras, Mistral, Cohere, NVIDIA, SambaNova, Together, Fireworks, HuggingFace)
- **Cloud providers: 5** (GCP, AWS, Azure, Oracle, Cloudflare)
- **Aggregators: 4** (OpenRouter, HuggingFace, Together, Fireworks)
- **Models accessible for free: 300+**

---

*This report was compiled through extensive web research in June 2026. Free tier details change frequently — always verify current limits on provider websites. Last verified: June 2026.*
