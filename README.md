# Token Founder 🔑

> Free AI Model API Discovery & Testing — 免费大模型API发掘、注册、测试与验证

**由 MindApex 团队智谱2号战士维护** | Last Updated: 2026-06-07

---

## 项目目标

发掘、注册、测试并验证所有可用的免费AI模型API，为团队构建零成本AI能力提供完整方案。

## 核心发现

- **25+ 提供商**提供免费AI API
- **300+ 模型**可免费使用
- **12+ 中国提供商** + **10+ 国际提供商**
- 覆盖文本、图像、视频、语音全模态

## 目录结构

```
token-founder/
├── README.md                    # 本文件
├── docs/
│   ├── comprehensive-free-models.md   # 全球免费模型完整报告
│   ├── kimi-webbridge-setup.md        # Kimi API 完整指南
│   ├── zhihu-article-notes.md         # 知乎文章笔记
│   ├── wechat-article-notes.md        # 微信文章笔记
│   └── feishu-doc-summary.md          # 飞书文档摘要
├── scripts/
│   ├── test_free_apis.py              # API 测试脚本
│   └── api_keys.example.env           # API Key 模板
├── test_results/
│   └── test_results_20260607.json     # 最新测试结果
└── verified-providers.md              # 已验证通过的提供商
```

## Tier 0：真正无限免费（无需信用卡）

| 提供商 | 免费额度 | 最佳模型 | OpenAI兼容 | API Base URL |
|--------|---------|---------|-----------|-------------|
| Google Gemini | 1,500 RPD | Gemini 2.5 Flash | ✅ | `generativelanguage.googleapis.com/v1beta/openai/` |
| Groq | 30 RPM | Llama 4 Scout | ✅ | `api.groq.com/openai/v1` |
| Cerebras | 1M TPD | Llama 3.3 70B | ✅ | `api.cerebras.ai/v1` |
| OpenRouter | 27+ $0模型 | Qwen 3.6 Plus | ✅ | `openrouter.ai/api/v1` |
| SiliconFlow | 20M tokens | DeepSeek-V3 | ✅ | `api.siliconflow.cn/v1` |
| DeepSeek | 5M tokens | DeepSeek-V3/R1 | ✅ | `api.deepseek.com/v1` |
| 智谱AI | 永久免费 | GLM-4.7-Flash | ✅ | `open.bigmodel.cn/api/paas/v4` |
| Mistral | Free mode | Mistral Small | ✅ | `api.mistral.ai/v1` |
| NVIDIA NIM | 80+ 模型 | Llama 3.3 70B | ✅ | `integrate.api.nvidia.com/v1` |
| SambaNova | Free tier | Llama 3.x | ✅ | `api.sambanova.ai/v1` |
| Agnes AI | 无限期免费 | Agnes-2.0-Flash | ✅ | `apihub.agnes-ai.com/v1` |
| 讯飞MaaS | 无限Token(6月底) | Qwen3.6-35B | ✅ | `maas-api.cn-huabei-1.xf-yun.com/v2` |
| Cloudflare | 10K neurons/day | 78+ 模型 | ⚠️ | workers.cloudflare.com |
| HuggingFace | Free inference | 10万+ 模型 | ⚠️ | `api-inference.huggingface.co/` |

## Tier 1：大额免费积分（无需信用卡）

| 提供商 | 免费额度 | 有效期 | 最佳模型 |
|--------|---------|-------|---------|
| Together AI | $5-100 | 30-90天 | 200+开源模型 |
| xAI Grok | $25 + $150/月 | 月度刷新 | Grok-3系列 |
| Fireworks AI | $1 | 注册即送 | Llama 3.3等 |
| Cohere | Trial key free | 速率限制 | Command R+ |
| DeepInfra | $5 | 注册即送 | Llama 3.1 405B |
| Cerebrium | $30 | 注册即送 | 任意HF模型 |
| AI21 Labs | $10 | 3个月 | Jamba系列 |
| Friendli AI | $10 | 注册即送 | Llama 3.1 70B |

## 聚合平台（一个Key调所有）

| 平台 | 免费模型数 | 特点 |
|------|----------|------|
| OpenRouter | 35+ | 一个API Key调几十种模型，推荐首选 |
| NVIDIA NIM | 120+ | 全部免费开发使用 |
| Pollinations.ai | 全模态 | 一个API覆盖文本/图像/音频/视频，无需Key |
| GitHub Models | 8 | GitHub账号直接可用 |

## 特殊发现

### 1. Agnes AI — 全球首个全模态免费API
- 来源: [知乎文章](https://zhuanlan.zhihu.com/p/2044805921726100061)
- 文本: Agnes-2.0-Flash
- 图像: Agnes-Image-2.0-Flash  
- 视频: Agnes-Video-2.0 (含音频)
- 注册: platform.agnes-ai.com

### 2. 讯飞MaaS — 无限Token白嫖Qwen3.6
- 来源: [微信公众号](https://mp.weixin.qq.com/s/PlxEXAhaJFtqe4t9WSH40A)
- 地址: https://maas.xfyun.cn/modelSquare?ch=maas-cg-kol-102
- 免费模型: Qwen3.6-35B-A3B、Qwen3.5-35B-A3B
- 截止: 2026年6月30日
- 工具: [CC Switch](https://ccswitch.io/zh/) 可直接配置到 Claude Code

### 3. Noiz.ai — AI语音克隆平台
- 网址: https://noiz.ai/
- 功能: TTS (文本转语音)、Voice Clone (语音克隆)
- 免费额度: 需注册确认

## 已验证端点（无需Key即可访问）

以下端点确认在线且返回模型列表:

| 端点 | /models | 状态 |
|------|---------|------|
| OpenRouter | 27 free models | ✅ 200 |
| NVIDIA NIM | 120 models | ✅ 200 |
| SambaNova | 8 models | ✅ 200 |
| GitHub Models | 8 models | ✅ 200 |
| AIMLAPI | 617 models | ✅ 200 |

## 快速开始

### 1. 获取API Key（推荐顺序）

1. **OpenRouter** → openrouter.ai → 注册 → 获取Key (最推荐，27+免费模型)
2. **Google Gemini** → aistudio.google.com → 获取API Key (1,500 RPD)
3. **Groq** → console.groq.com → 注册 → 获取Key (极速推理)
4. **DeepSeek** → platform.deepseek.com → 注册 → 获取Key (5M tokens)

### 2. 配置

```bash
cp scripts/api_keys.example.env .env.keys
# 编辑 .env.keys 填入你的API Keys
```

### 3. 测试

```bash
python3 scripts/test_free_apis.py
```

### 4. 使用（OpenAI兼容格式）

```python
from openai import OpenAI

# OpenRouter - 27+ free models
client = OpenAI(
    api_key="sk-or-YOUR_KEY",
    base_url="https://openrouter.ai/api/v1"
)

# Google Gemini
client = OpenAI(
    api_key="YOUR_GEMINI_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Groq
client = OpenAI(
    api_key="YOUR_GROQ_KEY",
    base_url="https://api.groq.com/openai/v1"
)

# 所有使用统一接口
response = client.chat.completions.create(
    model="MODEL_NAME",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

## 贡献

欢迎提交新的免费API发现！请包含:
- 提供商名称和网址
- 免费额度详情
- API Base URL和认证方式
- 测试验证结果

## 许可

MIT License

---

*MindApex Team | 智谱2号战士 | 2026-06*
