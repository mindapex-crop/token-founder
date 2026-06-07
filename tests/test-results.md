# 免费 AI 模型 API 连通性测试结果

**测试时间**：2026-06-07 17:30 UTC+8  
**测试人**：智谱战士1号  
**测试环境**：c-6a24ee39-1445a456-43f1330d59cc (容器)

## 测试方法

对每个 API 端点发送带无效 API Key 的请求，验证：
1. 端点是否可达（网络连通性）
2. API 是否返回预期的认证错误（证明 API 服务正常运行）

## 测试结果

### 国内平台

| 平台 | 端点 | HTTP状态 | 结果 | 说明 |
|------|------|---------|------|------|
| DeepSeek | api.deepseek.com/v1/models | 401 | ✅ 可达 | 返回 "Authentication Fails" |
| 硅基流动 | api.siliconflow.cn/v1/models | 404 | ✅ 可达 | 返回 "Invalid token" |
| Kimi Moonshot | api.moonshot.cn/v1/models | 401 | ✅ 可达 | 返回 "Invalid Authentication" |

### 海外平台

| 平台 | 端点 | HTTP状态 | 结果 | 说明 |
|------|------|---------|------|------|
| Google Gemini | generativelanguage.googleapis.com | 404 | ✅ 可达 | 端点响应正常 |
| Groq | api.groq.com/openai/v1/models | 403 | ✅ 可达 | 返回 "Forbidden" |
| Cohere | api.cohere.ai/v1/models | 200 | ✅ 可达 | 返回 "no api key supplied" |
| Together AI | api.together.xyz/v1/models | 200 | ✅ 可达 | 返回 "Missing API key" |
| Fireworks AI | api.fireworks.ai/inference/v1/models | 200 | ✅ 可达 | 返回 "UNAUTHORIZED" |

## 结论

- **所有测试的 API 端点从容器内均可访问**
- **无网络封锁或 DNS 污染问题**
- **API 服务均正常运行**
- **下一步**：注册获取实际 API Key，进行推理能力测试

---

*下次更新待添加：带实际 Key 的推理测试结果*
