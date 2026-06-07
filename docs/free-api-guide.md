# 免费AI模型API完整指南

> 调研时间：2026-06-07 | 调研人：智谱战士1号
> 
> 本文档整理了截至 2026 年 6 月，全球范围内所有可用的免费 AI 大模型 API 资源。

---

## 一、国内平台

### 1. 智谱AI (GLM) ⭐ 强烈推荐

**官网**：https://open.bigmodel.cn  
**Base URL**：`https://open.bigmodel.cn/api/paas/v4`  
**兼容格式**：OpenAI 兼容（通过 `/compatible-mode/v4`）

**免费模型**：
- **GLM-4-Flash**：永久免费，128K 上下文，30 并发
- **GLM-4.7-Flash**：永久免费，200K 上下文
- **GLM-5 系列**：有免费额度

**新用户福利**：赠送 2000 万 Token，永久有效

**获取方式**：
1. 访问 https://open.bigmodel.cn 注册
2. 进入控制台创建 API Key
3. 使用 `Authorization: Bearer <your_key>` 调用

**调用示例**：
```python
from openai import OpenAI
client = OpenAI(
    api_key="your_key",
    base_url="https://open.bigmodel.cn/api/paas/v4"
)
resp = client.chat.completions.create(
    model="glm-4-flash",
    messages=[{"role": "user", "content": "Hello"}]
)
```

---

### 2. DeepSeek

**官网**：https://platform.deepseek.com  
**Base URL**：`https://api.deepseek.com/v1`  
**兼容格式**：OpenAI 完全兼容

**免费模型**：
- **DeepSeek-V3**：新用户送 500 万 Token
- **DeepSeek-R1**：新用户送 500 万 Token
- 价格极低：输入 ¥1/百万Token，输出 ¥2/百万Token

**获取方式**：
1. 访问 https://platform.deepseek.com 注册
2. 创建 API Key
3. OpenAI 兼容格式调用

---

### 3. 硅基流动 SiliconCloud ⭐ 推荐

**官网**：https://cloud.siliconflow.cn  
**Base URL**：`https://api.siliconflow.cn/v1`  
**兼容格式**：OpenAI 兼容

**免费模型**（新人注册可用）：
- DeepSeek-V3 / DeepSeek-R1
- Qwen3 系列
- GLM-4-Flash
- 以及 100+ 其他开源模型

**特点**：聚合平台，一个 Key 调用多家模型

**获取方式**：
1. 访问 https://cloud.siliconflow.cn 注册
2. 获取 API Key
3. 模型名称格式：`<org>/<model>` 如 `deepseek-ai/DeepSeek-V3`

---

### 4. 阿里百炼

**官网**：https://bailian.console.aliyun.com  
**Base URL**：`https://dashscope.aliyuncs.com/compatible-mode/v1`  
**兼容格式**：OpenAI 兼容

**免费模型**：
- 通义千问全系列
- DeepSeek 全系列
- Kimi 系列
- MiniMax 系列

**免费额度**：每月 100 万 Token

---

### 5. Kimi (Moonshot AI)

**官网**：https://platform.moonshot.cn  
**Base URL**：`https://api.moonshot.cn/v1`  
**兼容格式**：OpenAI 兼容

**模型**：
- moonshot-v1-8k / 32k / 128k
- Kimi-K2.5（最新）

**新用户福利**：赠送 15 元体验额度

**Kimi WebBridge**：
- 浏览器自动化 Agent
- 安装方式：访问 https://www.kimi.com/zh-cn/features/webbridge
- 可让 Kimi Agent 控制浏览器完成搜索、填表、对比等任务

---

### 6. Agnes AI ⭐⭐ 重点推荐

**官网**：https://platform.agnes-ai.com  
**Base URL**：`https://apihub.agnes-ai.com/v1`  
**兼容格式**：OpenClaw / OpenAI 兼容

**全球首家全模态 API 无限期免费开放！**

**免费模型**（自 2026-06-01 起）：
- **Agnes-2.0-Flash**（文本）：1M 上下文窗口，支持 Tool Calling
- **Agnes-Image-2.0-Flash**（文生图）
- **Agnes-Video-V2.0**（文生视频）

**获取方式**：
1. 访问 https://platform.agnes-ai.com 注册
2. 创建 API Key
3. 使用 `agnes-2.0-flash` 作为模型名称调用

**特点**：
- 榜单排名前十的 AI Lab
- 无限期免费，不限量
- 全模态覆盖（文本+图片+视频）
- 适合原型开发和素材生成

---

### 7. 其他国内平台

| 平台 | URL | 特点 |
|------|-----|------|
| 腾讯混元 | https://console.cloud.tencent.com/hunyuan | 有限免费额度 |
| MiniMax | https://www.minimaxi.com | MiniMax-Text-01 有限免费 |
| 零一万物 | https://platform.lingyiwanwu.com | Yi 系列 |
| 百川智能 | https://platform.baichuan-ai.com | 百川系列 |
| 阶跃星辰 | https://platform.stepfun.com | Step 系列 |

---

## 二、海外平台

### 1. Google Gemini API ⭐⭐ 强烈推荐

**官网**：https://aistudio.google.com  
**Base URL**：`https://generativelanguage.googleapis.com/v1beta`

**免费模型**：
- Gemini 1.5 Flash / Pro
- Gemini 2.0 系列

**免费额度**（最慷慨的永久免费）：
- 1500 次/天
- 无需信用卡
- 1.5B tokens/天（Flash）

**获取方式**：
1. 访问 https://aistudio.google.com
2. 使用 Google 账号登录
3. 点击 "Get API Key" 创建密钥
4. 无需绑定信用卡

---

### 2. Groq ⭐ 推荐

**官网**：https://console.groq.com  
**Base URL**：`https://api.groq.com/openai/v1`  
**兼容格式**：OpenAI 兼容

**免费模型**：
- Llama 4 Scout
- Llama 3.1 8B
- Qwen3 32B
- DeepSeek R1
- Mixtral 8x7B

**免费额度**：
- 30,000 tokens/min
- 14,400 请求/天
- 无需信用卡

**核心优势**：LPU 推理速度极快，延迟极低

---

### 3. OpenRouter ⭐ 推荐

**官网**：https://openrouter.ai  
**Base URL**：`https://openrouter.ai/api/v1`  
**兼容格式**：OpenAI 兼容

**28 个永久免费模型**，包括：
- 多种开源 Llama 变体
- Mistral 变体
- Qwen 变体
- 其他小参数模型

**特色**：`openrouter/free` 路由自动选择最优免费模型

**免费额度**：永久免费，无需信用卡

---

### 4. Together AI

**官网**：https://api.together.xyz  
**Base URL**：`https://api.together.xyz/v1`  
**兼容格式**：OpenAI 兼容

**特点**：100+ 开源模型  
**新用户福利**：$5-25 免费额度

---

### 5. Cerebras

**官网**：https://cloud.cerebras.ai  
**Base URL**：`https://api.cerebras.ai/v1`  
**兼容格式**：OpenAI 兼容

**特点**：极速推理（类似 Groq），免费层可用

---

### 6. Fireworks AI

**官网**：https://fireworks.ai  
**Base URL**：`https://api.fireworks.ai/inference/v1`  
**兼容格式**：OpenAI 兼容

**特点**：100+ 开源模型，Function Calling 优化，新用户免费额度

---

### 7. Cohere

**官网**：https://dashboard.cohere.com  
**Base URL**：`https://api.cohere.ai/v1`

**特点**：Command R 系列（RAG 优化）、Embedding、Reranking  
**免费层**：可用于原型开发

---

### 8. Mistral (La Plateforme)

**官网**：https://console.mistral.ai  
**Base URL**：`https://api.mistral.ai/v1`  
**兼容格式**：OpenAI 兼容

**特点**：Mistral Small/Medium，Experiment 层免费

---

### 9. HuggingFace Inference API

**官网**：https://huggingface.co  
**Base URL**：`https://api-inference.huggingface.co`

**特点**：数千开源模型，免费层（有冷启动延迟）

---

### 10. Novita AI

**官网**：https://novita.ai  
**Base URL**：`https://api.novita.ai/v3`

**特点**：多种开源模型，每日免费额度

---

## 三、专用能力平台

### Noiz.ai — TTS / 语音克隆

**官网**：https://noiz.ai  
**开发者后台**：https://developers.noiz.ai

**能力**：
- 文本转语音 (TTS)
- 3秒语音克隆
- 情感控制（开心/悲伤/惊讶/愤怒/恐惧）
- 多语言支持（中/英/日/混合）
- 15+ 内置声音
- Developer API

**获取方式**：
1. 注册 https://noiz.ai 免费账号
2. 进入 https://developers.noiz.ai 获取 API Key
3. REST API 调用

---

### Kimi WebBridge — 浏览器自动化

**官网**：https://www.kimi.com/zh-cn/features/webbridge

**能力**：
- 让 Kimi Agent 控制浏览器
- 自动化搜索、填表、对比、订票等任务
- 可用于批量注册账号、获取 API Key 等自动化操作

---

## 四、本地部署方案（$0/月）

| 方案 | 最低配置 | 特点 |
|------|---------|------|
| **Ollama** | 8GB VRAM | 一行命令运行开源模型，最简单 |
| **vLLM** | 16GB VRAM | 高性能推理服务器，OpenAI兼容 |
| **LM Studio** | 8GB VRAM | GUI 桌面应用 |
| **llama.cpp** | 4GB VRAM | CPU 推理，最低硬件要求 |

> 容器环境（无GPU）不太适合本地部署，建议优先使用云端免费API。

---

## 五、统一调用方案

大部分平台都支持 OpenAI 兼容格式，可以用统一代码调用：

```python
from openai import OpenAI

# 配置不同平台的 base_url 和 api_key 即可切换
providers = {
    "deepseek": {"base_url": "https://api.deepseek.com/v1", "model": "deepseek-chat"},
    "siliconflow": {"base_url": "https://api.siliconflow.cn/v1", "model": "deepseek-ai/DeepSeek-V3"},
    "groq": {"base_url": "https://api.groq.com/openai/v1", "model": "llama-4-scout-17b-16e-instruct"},
    "openrouter": {"base_url": "https://openrouter.ai/api/v1", "model": "openrouter/free"},
    "glm": {"base_url": "https://open.bigmodel.cn/api/paas/v4", "model": "glm-4-flash"},
    "kimi": {"base_url": "https://api.moonshot.cn/v1", "model": "moonshot-v1-8k"},
    "agnes": {"base_url": "https://apihub.agnes-ai.com/v1", "model": "agnes-2.0-flash"},
}

def call_llm(provider: str, api_key: str, prompt: str):
    config = providers[provider]
    client = OpenAI(api_key=api_key, base_url=config["base_url"])
    resp = client.chat.completions.create(
        model=config["model"],
        messages=[{"role": "user", "content": prompt}]
    )
    return resp.choices[0].message.content
```

---

## 六、风险与建议

1. **免费政策可能随时变化** — 定期检查各平台的定价页面
2. **多渠道备份** — 不要依赖单一平台，至少储备 3-5 个备选
3. **Token 安全** — API Key 应安全存储，不要硬编码在代码中
4. **速率限制** — 免费层一般有 QPM/TPM 限制，需做限流处理
5. **模型质量差异** — 免费模型和付费模型存在能力差距，根据任务选择
6. **合规使用** — 遵守各平台的使用条款，不要用于滥用场景

---

*文档版本：v1.0 | 最后更新：2026-06-07 | 维护者：智谱战士1号*
