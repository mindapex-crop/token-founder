# Verified Providers - 已验证端点

> 以下端点通过实际 HTTP 请求验证，确认为在线且可访问。

## 已验证端点（2026-06-08 刷新）

### 端点在线（无需Key可列出模型）

| 提供商 | 端点 | /models 状态 | 可列出模型数 | 响应时间 |
|--------|------|-------------|-------------|---------|
| OpenRouter | `openrouter.ai/api/v1` | ✅ 200 | 341 | 0.13s |
| NVIDIA NIM | `integrate.api.nvidia.com/v1` | ✅ 200 | 120 | 0.18s |
| SambaNova | `api.sambanova.ai/v1` | ✅ 200 | 8 | 0.24s |
| GitHub Models | `models.inference.ai.azure.com` | ✅ 200 | N/A | 0.90s |
| AIMLAPI | `api.aimlapi.com/v1` | ✅ 200 | 617 | 0.93s |

### 认证端点确认在线（需API Key）

以下端点返回正确的认证错误(401/403)，证明API在线但需要Key：

| 提供商 | 端点 | HTTP状态 | 响应时间 | 备注 |
|--------|------|---------|---------|------|
| DeepSeek | `api.deepseek.com/v1` | 401 | 0.17s | 手机注册，送500万Token |
| SiliconFlow | `api.siliconflow.cn/v1` | 401 | 0.05s | 国内平台，新人送14元 |
| 智谱AI | `open.bigmodel.cn/api/paas/v4` | 401 | 0.09s | GLM-4-Flash永久免费 |
| DashScope | `dashscope.aliyuncs.com/compatible-mode/v1` | 401 | 0.20s | 阿里百炼，月100万Token免费 |
| Agnes AI | `apihub.agnes-ai.com/v1` | 401 | 0.07s | 宣称全模态无限期免费 |
| Mistral | `api.mistral.ai/v1` | 401 | 0.27s | 欧洲AI，免费层可用 |
| Cohere | `api.cohere.ai/v1` | 401 | 0.23s | Command R+ RAG专用 |
| Together AI | `api.together.xyz/v1` | 401 | 0.19s | 新用户送$5 |
| Fireworks AI | `api.fireworks.ai/inference/v1` | 401 | 0.22s | 开源模型推理加速 |
| Groq | `api.groq.com/openai/v1` | 403 | 0.04s | LPU极速推理，IP需代理 |
| Cerebras | `api.cerebras.ai/v1` | 403 | 0.08s | 晶圆级推理，IP需代理 |
| Moonshot | `api.moonshot.cn/v1` | 401 | 0.34s | 128K超长上下文 |
| StepFun | `api.stepfun.com/v1` | 401 | 0.18s | 阶跃星辰 |
| 百川 | `api.baichuan-ai.com/v1` | 401 | 0.30s | Baichuan4 |
| MiniMax | `api.minimax.chat/v1` | 401 | 0.40s | MiniMax-Text-01 |

### 即时可用（无需注册）

| 提供商 | 端点 | 状态 | 备注 |
|--------|------|------|------|
| Pollinations.ai | `text.pollinations.ai/openai` | ⚠️ 429 | 完全免费但当前IP限速 |

### DNS/网络受限

| 提供商 | 端点 | 状态 | 备注 |
|--------|------|------|------|
| HuggingFace | `api-inference.huggingface.co` | DNS失败 | 需代理 |
| Google Gemini /models | `generativelanguage.googleapis.com` | 404 | /models路径不适用Gemini，API本身在线 |

## 推荐注册优先级

**P0 - 即时可用**: Pollinations.ai（但IP限速）
**P1 - 强烈推荐**（免费额度大、模型强）:
- OpenRouter — 341个模型，27个永久免费
- Google Gemini — 无限免费调用
- DeepSeek — 500万Token，R1免费
- 硅基流动 — DeepSeek-V3免费
- 智谱GLM — Flash永久免费
- 阿里DashScope — 月100万Token免费

**P2 - 推荐**（值得注册）:
- NVIDIA NIM, SambaNova, Groq, Together AI, Moonshot

**P3 - 扩展**:
- Mistral, Cohere, Fireworks, Cerebras, StepFun, 百川, MiniMax, Agnes AI

## 工具使用

### 注册指引
```bash
python3 scripts/register-api-keys.py --guide   # 完整注册指引
python3 scripts/register-api-keys.py --links   # 快速注册链接
```

### 注册后测试
```bash
python3 scripts/register-api-keys.py --mark deepseek sk-your-key   # 标记已注册
python3 scripts/register-api-keys.py --test                       # 测试所有Key
python3 scripts/register-api-keys.py --status                    # 查看状态
```

### 端点连通性测试
```bash
python3 scripts/test_free_apis.py   # 完整连通性测试
```

### 统一调用封装
```bash
DEEPSEEK_API_KEY=sk-xxx python3 scripts/unified-call.py   # 调用DeepSeek
OPENROUTER_API_KEY=sk-xxx python3 scripts/unified-call.py # 调用OpenRouter
```
