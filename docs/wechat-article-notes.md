# 微信文章笔记：白嫖Qwen3.6无限Token

**来源**: [免费白嫖 Qwen3.6，Token 无限量](https://mp.weixin.qq.com/s/PlxEXAhaJFtqe4t9WSH40A)
**公众号**: 逛逛GitHub

## 核心信息

讯飞MaaS平台提供**无限量Token**免费使用Qwen3.6和Qwen3.5模型。

## 关键信息

| 项目 | 详情 |
|------|------|
| 免费模型 | Qwen3.6-35B-A3B、Qwen3.5-35B-A3B |
| 免费额度 | Token **无限量** |
| 截止日期 | **2026年6月30日** |
| 注册地址 | https://maas.xfyun.cn/modelSquare?ch=maas-cg-kol-102 |

## 注册与配置步骤

1. 打开上面的链接
2. 找到 Qwen 3.6 模型
3. 点击右上角「API 调用」
4. 输入名称，创建应用
5. 复制以下信息：
   - `modelId`
   - HTTP协议的 `APIKey`
   - API地址：https://maas.xfyun.cn/modelService

## 配置到 Claude Code

推荐使用 **CC Switch** 工具配置：
1. 下载地址: https://ccswitch.io/zh/
2. 安装后选择 Claude Code
3. 点击「创建」→ 选中「自定义配置」
4. 输入 API Key 和请求地址：
   - **Claude Code**: `https://maas-api.cn-huabei-1.xf-yun.com/anthropic`
   - **Codex/其他**: `https://maas-api.cn-huabei-1.xf-yun.com/v2`
5. 输入 modelId
6. 保存启用

## 注意事项

- **限时活动**：6月底截止，需尽快注册
- 无限Token但可能有速率限制
- 建议尽早注册占位
