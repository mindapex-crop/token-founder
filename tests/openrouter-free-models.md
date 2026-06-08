# OpenRouter 免费模型完整列表

**测试时间**：2026-06-08 10:25 UTC+8  
**测试人**：智谱战士1号  
**数据来源**：OpenRouter API (`/api/v1/models`)

## 概况

- 总模型数：341
- **免费模型数：27**
- 路由模型：`openrouter/free`（自动选择最优免费模型）

## 完整列表（按上下文长度排序）

| # | 模型 ID | 上下文长度 | 备注 |
|---|---------|-----------|------|
| 1 | `openrouter/owl-alpha` | 1,048,756 | ~1M 上下文 |
| 2 | `google/lyria-3-pro-preview` | 1,048,576 | Google 音频模型 |
| 3 | `google/lyria-3-clip-preview` | 1,048,576 | Google 音频模型 |
| 4 | `qwen/qwen3-coder:free` | 1,048,576 | 通义千问代码模型，1M上下文 |
| 5 | `nvidia/nemotron-3-ultra-550b-a55b:free` | 1,000,000 | NVIDIA 超大模型 |
| 6 | `nvidia/nemotron-3-super-120b-a12b:free` | 1,000,000 | NVIDIA 大模型 |
| 7 | `poolside/laguna-xs.2:free` | 262,144 | Poolside 代码模型 |
| 8 | `poolside/laguna-m.1:free` | 262,144 | Poolside 中型模型 |
| 9 | `moonshotai/kimi-k2.6:free` | 262,144 | Kimi 最新版 |
| 10 | `google/gemma-4-26b-a4b-it:free` | 262,144 | Google Gemma 4 MoE |
| 11 | `google/gemma-4-31b-it:free` | 262,144 | Google Gemma 4 |
| 12 | `qwen/qwen3-next-80b-a3b-instruct:free` | 262,144 | 通义千问3 |
| 13 | `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` | 256,000 | NVIDIA 推理模型 |
| 14 | `nvidia/nemotron-3-nano-30b-a3b:free` | 256,000 | NVIDIA Nano |
| 15 | `openrouter/free` | 200,000 | **自动路由**（推荐） |
| 16 | `openai/gpt-oss-120b:free` | 131,072 | OpenAI 开源 120B |
| 17 | `openai/gpt-oss-20b:free` | 131,072 | OpenAI 开源 20B |
| 18 | `z-ai/glm-4.5-air:free` | 131,072 | **智谱 GLM-4.5 Air** |
| 19 | `meta-llama/llama-3.3-70b-instruct:free` | 131,072 | Meta Llama 3.3 70B |
| 20 | `meta-llama/llama-3.2-3b-instruct:free` | 131,072 | Meta Llama 3.2 3B |
| 21 | `nousresearch/hermes-3-llama-3.1-405b:free` | 131,072 | Nous Hermes 405B |
| 22 | `nvidia/nemotron-3.5-content-safety:free` | 128,000 | 内容安全模型 |
| 23 | `nvidia/nemotron-nano-12b-v2-vl:free` | 128,000 | NVIDIA 视觉语言模型 |
| 24 | `nvidia/nemotron-nano-9b-v2:free` | 128,000 | NVIDIA Nano 9B |
| 25 | `liquid/lfm-2.5-1.2b-thinking:free` | 32,768 | Liquid 推理模型 |
| 26 | `liquid/lfm-2.5-1.2b-instruct:free` | 32,768 | Liquid 指令模型 |
| 27 | `cognitivecomputations/dolphin-mistral-24b-venice-edition:free` | 32,768 | Dolphin Mistral |

## 重点推荐

### 通用对话
- `openrouter/free` — 自动路由，最省心
- `nvidia/nemotron-3-ultra-550b-a55b:free` — 550B 参数
- `moonshotai/kimi-k2.6:free` — Kimi 最新，262K 上下文
- `qwen/qwen3-coder:free` — 1M 上下文，代码能力强

### 代码生成
- `qwen/qwen3-coder:free` — 1M 上下文代码专用
- `poolside/laguna-xs.2:free` — 代码专用模型

### 推理
- `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free` — 推理增强
- `liquid/lfm-2.5-1.2b-thinking:free` — 轻量推理

### 我们自己的模型
- `z-ai/glm-4.5-air:free` — 智谱 GLM-4.5 Air 也在 OpenRouter 免费提供

---

*下次更新：添加实际推理测试结果*
