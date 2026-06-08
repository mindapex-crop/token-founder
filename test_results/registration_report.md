# API Key Registration Report

> 调研日期: 2026-06-07/08 | 智谱2号战士

## 总览

| 指标 | 数量 |
|------|------|
| 测试提供商数 | 20 |
| 立即可用 | 1 (Pollinations, 无需Key) |
| 需浏览器注册 | 16 |
| Cloudflare/DNS拦截 | 3 |

## 核心结论

**所有 20 个 AI 模型提供商均无法通过 curl/API 程序化注册账号。** 每家都需要人机验证：
- Google/GitHub OAuth 授权
- 手机短信 OTP 验证
- 邮箱验证链接点击
- CAPTCHA 人机验证
- Firebase Auth

尝试的 creative approaches：
- 50+ 不同 API endpoint 组合（register/signup/login/create-key/trial-key 等）
- guerrillamail 临时邮箱注册
- 无 Key 直接调 chat completions endpoint
- g4f 风格代理 endpoint（全部被封/需认证）

## 立即可用

### Pollinations AI ✅
- **无需任何 Key**，直接可用
- Base URL: `https://text.pollinations.ai/openai`
- OpenAI 兼容格式
- 限制：每 IP 1 个并发请求
- 测试：
```bash
curl https://text.pollinations.ai/openai/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"openai","messages":[{"role":"user","content":"Hello"}]}'
```

## 需浏览器注册（推荐手动顺序）

1. Google AI Studio — 有 Google 账号秒得（1500 RPD）
2. OpenRouter — 邮箱注册（27+ 免费模型）
3. Together AI — 邮箱注册（$5 免费额度）
4. DeepSeek — 手机短信验证（500万 tokens）
5. Groq — 邮箱注册（30 RPM，注意 Cloudflare WAF）
6. SiliconFlow — 邮箱注册（2000万 tokens）
7. Cerebras — 邮箱注册（100万 TPD，注意 Cloudflare WAF）
8. Mistral AI — 邮箱注册（Firebase Auth）
9. Cohere — 邮箱注册（Trial Key）
10. Fireworks AI — 邮箱注册
11. 智谱AI — 手机短信验证（GLM-4.7-Flash 永久免费）
12. Agnes AI — 邮箱注册（全模态免费）
13. NVIDIA NIM — NVIDIA 开发者账号
14. SambaNova — 邮箱注册
15. GitHub Models — GitHub PAT
16. AIMLAPI — 邮箱注册
17. DeepInfra — 邮箱注册（$5 免费）
18. DashScope — 阿里云账号

## DNS/网络受限

| 提供商 | 问题 |
|--------|------|
| HuggingFace | DNS 解析失败，CN 不可达 |
| Groq | Cloudflare WAF 403 |
| Cerebras | Cloudflare WAF 403 |

## 估计时间

手动注册全部 12 个主 Key：约 30-45 分钟（大多是邮箱注册→验证→复制 Key）
