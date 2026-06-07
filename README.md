# Token Founder - 免费 AI 模型 API 资源调研

> **创新型项目** | Madapex 团队维护
> 
> 全面调研、测试验证各大免费 AI 模型 API 资源，为智谱战士集群提供多模型备选方案。

## 📋 项目目标

1. 整理所有可用的免费 AI 模型 API 资源
2. 测试验证每个 API 的连通性和可用性
3. 提供统一的接入代码示例
4. 建立 token 管理和轮换机制
5. 为智谱战士集群降低对单一平台的依赖

---

## 🗂️ 目录结构

```
token-founder/
├── README.md              # 本文件 - 项目总览
├── docs/
│   └── free-api-guide.md  # 免费API完整指南（详细文档）
├── tests/
│   ├── connectivity-test.sh    # API连通性测试脚本
│   └── test-results.md         # 测试结果记录
└── scripts/
    └── unified-call.py     # 统一调用示例（OpenAI兼容格式）
```

---

## 🚀 免费 API 速查表

### 国内平台

| 平台 | 免费模型 | 免费额度 | Base URL | 注册获取 Key |
|------|---------|---------|----------|-------------|
| **智谱AI (GLM)** | GLM-4-Flash, GLM-4.7-Flash | 永久免费，新用户送2000万Token | `https://open.bigmodel.cn/api/paas/v4` | https://open.bigmodel.cn |
| **DeepSeek** | DeepSeek-V3, DeepSeek-R1 | 新用户送500万Token | `https://api.deepseek.com/v1` | https://platform.deepseek.com |
| **硅基流动 (SiliconCloud)** | DeepSeek-V3, Qwen3, GLM等100+ | 新人免费额度 | `https://api.siliconflow.cn/v1` | https://cloud.siliconflow.cn |
| **阿里百炼** | 通义千问全系列 | 每月100万Token免费 | `https://dashscope.aliyuncs.com/compatible-mode/v1` | https://bailian.console.aliyun.com |
| **Kimi (Moonshot)** | Moonshot-v1, Kimi-K2.5 | 新用户送15元 | `https://api.moonshot.cn/v1` | https://platform.moonshot.cn |
| **腾讯混元** | 混元系列 | 有限免费额度 | `https://api.hunyuan.cloud.tencent.com/v1` | https://console.cloud.tencent.com/hunyuan |
| **MiniMax** | MiniMax-Text-01 | 有限免费 | `https://api.minimax.chat/v1` | https://www.minimaxi.com |
| **Agnes AI** | Agnes-2.0-Flash, Agnes-Image-2.0-Flash, Agnes-Video-V2.0 | **无限期全免费**（文本+图片+视频） | `https://apihub.agnes-ai.com/v1` | https://platform.agnes-ai.com |
| **零一万物** | Yi系列 | 有限免费 | `https://api.lingyiwanwu.com/v1` | https://platform.lingyiwanwu.com |

### 海外平台

| 平台 | 免费模型 | 免费额度 | Base URL | 注册获取 Key |
|------|---------|---------|----------|-------------|
| **Google Gemini** | Gemini Flash, Pro | **永久免费**，1500次/天 | `https://generativelanguage.googleapis.com/v1beta` | https://aistudio.google.com |
| **Groq** | Llama 4 Scout, Qwen3 32B, DeepSeek R1 | 30K tokens/min, 14400 req/day | `https://api.groq.com/openai/v1` | https://console.groq.com |
| **OpenRouter** | 28个免费模型（openrouter/free 路由） | 永久免费 | `https://openrouter.ai/api/v1` | https://openrouter.ai |
| **Together AI** | 100+开源模型 | 新用户$5-25免费额度 | `https://api.together.xyz/v1` | https://api.together.xyz |
| **Cohere** | Command R, Embed, Rerank | 免费层可用 | `https://api.cohere.ai/v1` | https://dashboard.cohere.com |
| **Cerebras** | Llama 3.3 70B等 | 免费高速推理 | `https://api.cerebras.ai/v1` | https://cloud.cerebras.ai |
| **Fireworks AI** | 100+开源模型 | 新用户免费额度 | `https://api.fireworks.ai/inference/v1` | https://fireworks.ai |
| **HuggingFace** | 数千开源模型 | 免费层（有冷启动） | `https://api-inference.huggingface.co` | https://huggingface.co |
| **Mistral (La Plateforme)** | Mistral Small, Medium | Experiment层免费 | `https://api.mistral.ai/v1` | https://console.mistral.ai |
| **Novita AI** | 多种开源模型 | 每日免费额度 | `https://api.novita.ai/v3` | https://novita.ai |

### 专用能力平台

| 平台 | 能力 | 免费额度 | 说明 |
|------|------|---------|------|
| **Noiz.ai** | TTS/语音克隆/情感控制 | 免费账号可用 | https://developers.noiz.ai |
| **Kimi WebBridge** | 浏览器自动化Agent | Kimi账号可用 | https://www.kimi.com/zh-cn/features/webbridge |

---

## 🧪 连通性测试结果

测试时间：2026-06-07 | 测试环境：智谱战士1号容器

| 平台 | 端点可达 | API响应验证 | 需要Key |
|------|---------|------------|---------|
| DeepSeek | ✅ HTTP 401 | ✅ 返回认证错误（正常） | ✅ |
| 硅基流动 | ✅ HTTP 404 | ✅ 返回token无效（正常） | ✅ |
| Google Gemini | ✅ HTTP 404 | ✅ 端点可达 | ✅ |
| Groq | ✅ HTTP 403 | ✅ 返回Forbidden（正常） | ✅ |
| Kimi/Moonshot | ✅ HTTP 401 | ✅ 返回认证错误（正常） | ✅ |
| Cohere | ✅ HTTP 200 | ✅ 返回no api key（正常） | ✅ |
| Together AI | ✅ HTTP 200 | ✅ 返回Missing API key（正常） | ✅ |
| Fireworks AI | ✅ HTTP 200 | ✅ 返回UNAUTHORIZED（正常） | ✅ |

> 所有端点从容器内均可访问，无网络封锁。

---

## 📝 下一步行动

- [ ] 逐个注册获取 API Key
- [ ] 用统一脚本测试每个 API 的实际推理能力
- [ ] 编写 OpenAI 兼容格式的统一调用封装
- [ ] 建立 token 安全存储和轮换机制
- [ ] 评估 Kimi WebBridge 的浏览器自动化能力
- [ ] 评估 Noiz.ai 的 TTS/语音克隆 API
- [ ] 评估 Agnes AI 的全模态免费 API（文本+图片+视频）

---

## 📌 关键发现

1. **Agnes AI** 最值得关注 — 全球首家全模态（文本+图片+视频）API 无限期免费开放
2. **Google Gemini** 的免费层最慷慨 — 永久免费，1500次/天
3. **Groq** 免费层速度极快 — LPU 推理，30K tokens/min
4. **OpenRouter** 有 28 个永久免费模型 — 可通过 `openrouter/free` 路由自动选择
5. **智谱 GLM-4-Flash** 永久免费 — 128K上下文，30并发
6. **硅基流动** 聚合了 100+ 模型 — 包含 DeepSeek、Qwen、GLM 等免费选项

---

*调研人：智谱战士1号 | 创建时间：2026-06-07*
