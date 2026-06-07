# Verified Providers - 已验证端点

> 以下端点通过实际 HTTP 请求验证，确认为在线且可访问。

## 已验证端点（2026-06-07）

### 端点在线（无需Key可列出模型）

| 提供商 | 端点 | /models 状态 | 免费模型数 |
|--------|------|-------------|-----------|
| OpenRouter | `openrouter.ai/api/v1` | ✅ 200 | 27 |
| NVIDIA NIM | `integrate.api.nvidia.com/v1` | ✅ 200 | 120 |
| SambaNova | `api.sambanova.ai/v1` | ✅ 200 | 8 |
| GitHub Models | `models.inference.ai.azure.com` | ✅ 200 | 8 |
| AIMLAPI | `api.aimlapi.com/v1` | ✅ 200 | 617 |

### 认证端点确认在线（需API Key）

以下端点返回正确的认证错误(401/403)，证明API在线但需要Key：

| 提供商 | 端点 | HTTP状态 | 错误信息 |
|--------|------|---------|---------|
| Google Gemini | `generativelanguage.googleapis.com/v1beta/openai/` | 400 | Missing Authorization |
| DeepSeek | `api.deepseek.com/v1` | 401 | Authentication Fails |
| SiliconFlow | `api.siliconflow.cn/v1` | 401 | Invalid token |
| Mistral | `api.mistral.ai/v1` | 401 | Unauthorized |
| Cohere | `api.cohere.ai/v1` | 401 | No API key supplied |
| 智谱AI | `open.bigmodel.cn/api/paas/v4` | 401 | 未收到Authorization |
| DashScope | `dashscope.aliyuncs.com/compatible-mode/v1` | 401 | No API key |
| Agnes AI | `apihub.agnes-ai.com/v1` | 401 | 未提供令牌 |
| Together AI | `api.together.xyz/v1` | 401 | Missing API key |
| Fireworks AI | `api.fireworks.ai/inference/v1` | 401 | Missing API key |

### DNS/网络受限

| 提供商 | 端点 | 状态 | 备注 |
|--------|------|------|------|
| HuggingFace | `api-inference.huggingface.co` | DNS失败 | 需代理 |
| Groq | `api.groq.com` | 403 Cloudflare | IP被Cloudflare WAF拦截 |
| Cerebras | `api.cerebras.ai` | 403 Cloudflare | IP被Cloudflare WAF拦截 |

## 验证方法

使用 `scripts/test_free_apis.py` 脚本运行完整测试：
```bash
cp scripts/api_keys.example.env .env.keys
# 填入API Keys
python3 scripts/test_free_apis.py
```

## 下一步

- [ ] 注册 OpenRouter 获取 Key
- [ ] 注册 Google AI Studio 获取 Key
- [ ] 注册 DeepSeek 获取 Key
- [ ] 注册 Groq 获取 Key
- [ ] 配置 .env.keys 并重新测试
- [ ] 添加更多提供商
