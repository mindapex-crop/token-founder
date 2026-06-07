# 知乎文章笔记：Agnes AI 全模态免费API

**来源**: [今天起，无限期免费！全球首个全模态API开放](https://zhuanlan.zhihu.com/p/2044805921726100061)
**发布**: 量子位 | QbitAI

## 核心信息

Agnes AI（全球Top 10 AI Lab）从即日起**无限期免费**开放旗下核心模型API。

## 免费模型

| 模型 | 类型 | 说明 |
|------|------|------|
| Agnes-2.0-Flash | 文本 | 代码生成、复杂结构化任务 |
| Agnes-Image-2.0-Flash | 图像 | 电商主图、信息图、赛博朋克风 |
| Agnes-Video-2.0 | 视频 | 含音频，电影级质量 |

## 关键亮点

- **全模态免费**：文本+图片+视频三类API全部免费
- **Agent友好**：免费API让Agent多轮规划不再算成本
- **榜单成绩**：Claw-Eval、Artificial Analysis榜单均有名次

## 使用方式

1. **官方API平台**: https://platform.agnes-ai.com/
2. **API地址**: https://apihub.agnes-ai.com/v1
3. **模型名**: agnes-2.0-flash

### Claude Code / Hermes 配置

```
API Key: [从平台获取]
接口地址: https://apihub.agnes-ai.com/v1
模型名称: agnes-2.0-flash
```

### OpenAI SDK 示例

```python
from openai import OpenAI
client = OpenAI(
    api_key="YOUR_AGNES_KEY",
    base_url="https://apihub.agnes-ai.com/v1"
)
response = client.chat.completions.create(
    model="agnes-2.0-flash",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

## 注册步骤

1. 打开 https://platform.agnes-ai.com/
2. 注册账号
3. 创建 API Key
4. 按文档调用对应模型
