"""
统一免费 AI 模型调用脚本
支持 OpenAI 兼容格式的所有平台
作者：智谱战士1号 | 日期：2026-06-07
"""

import os
import json
import time
from openai import OpenAI

# ==================== 平台配置 ====================
# 使用前请设置对应的环境变量，或直接替换下面的 key

PROVIDERS = {
    # 国内平台
    "deepseek": {
        "base_url": "https://api.deepseek.com/v1",
        "model": "deepseek-chat",
        "env_key": "DEEPSEEK_API_KEY",
        "desc": "DeepSeek V3 - 新用户送500万Token",
    },
    "siliconflow": {
        "base_url": "https://api.siliconflow.cn/v1",
        "model": "deepseek-ai/DeepSeek-V3",
        "env_key": "SILICONFLOW_API_KEY",
        "desc": "硅基流动 - 聚合100+模型，新人免费",
    },
    "glm": {
        "base_url": "https://open.bigmodel.cn/api/paas/v4",
        "model": "glm-4-flash",
        "env_key": "GLM_API_KEY",
        "desc": "智谱GLM-4-Flash - 永久免费",
    },
    "kimi": {
        "base_url": "https://api.moonshot.cn/v1",
        "model": "moonshot-v1-8k",
        "env_key": "KIMI_API_KEY",
        "desc": "Kimi/Moonshot - 新用户送15元",
    },
    "dashscope": {
        "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "model": "qwen-plus",
        "env_key": "DASHSCOPE_API_KEY",
        "desc": "阿里百炼通义千问 - 每月100万Token免费",
    },
    "agnes": {
        "base_url": "https://apihub.agnes-ai.com/v1",
        "model": "agnes-2.0-flash",
        "env_key": "AGNES_API_KEY",
        "desc": "Agnes AI - 全模态无限期免费",
    },
    # 海外平台
    "gemini": {
        "base_url": "https://generativelanguage.googleapis.com/v1beta/openai",
        "model": "gemini-1.5-flash",
        "env_key": "GEMINI_API_KEY",
        "desc": "Google Gemini - 永久免费1500次/天",
    },
    "groq": {
        "base_url": "https://api.groq.com/openai/v1",
        "model": "llama-4-scout-17b-16e-instruct",
        "env_key": "GROQ_API_KEY",
        "desc": "Groq - LPU极速推理，免费层",
    },
    "openrouter": {
        "base_url": "https://openrouter.ai/api/v1",
        "model": "openrouter/free",
        "env_key": "OPENROUTER_API_KEY",
        "desc": "OpenRouter - 28个永久免费模型",
    },
    "together": {
        "base_url": "https://api.together.xyz/v1",
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        "env_key": "TOGETHER_API_KEY",
        "desc": "Together AI - 新用户$5-25免费",
    },
    "cerebras": {
        "base_url": "https://api.cerebras.ai/v1",
        "model": "llama-3.3-70b",
        "env_key": "CEREBRAS_API_KEY",
        "desc": "Cerebras - 极速推理免费层",
    },
    "fireworks": {
        "base_url": "https://api.fireworks.ai/inference/v1",
        "model": "accounts/fireworks/models/llama-v3p1-70b-instruct",
        "env_key": "FIREWORKS_API_KEY",
        "desc": "Fireworks AI - 新用户免费额度",
    },
    "mistral": {
        "base_url": "https://api.mistral.ai/v1",
        "model": "mistral-small-latest",
        "env_key": "MISTRAL_API_KEY",
        "desc": "Mistral - Experiment层免费",
    },
    "cohere": {
        "base_url": "https://api.cohere.ai/v1",
        "model": "command-r",
        "env_key": "COHERE_API_KEY",
        "desc": "Cohere - 免费层可用",
    },
}


def call_llm(provider: str, prompt: str, system: str = None, max_retries: int = 2) -> str:
    """
    统一调用免费 LLM API
    
    Args:
        provider: 平台名称（见 PROVIDERS 字典的 key）
        prompt: 用户输入
        system: 系统提示词（可选）
        max_retries: 最大重试次数
    
    Returns:
        模型回复内容
    
    Raises:
        ValueError: 平台不存在
        KeyError: API Key 未设置
        Exception: API 调用失败
    """
    if provider not in PROVIDERS:
        raise ValueError(f"未知平台: {provider}，可用: {list(PROVIDERS.keys())}")
    
    config = PROVIDERS[provider]
    api_key = os.environ.get(config["env_key"])
    
    if not api_key:
        raise KeyError(
            f"请设置环境变量 {config['env_key']} "
            f"({config['desc']})"
        )
    
    client = OpenAI(
        api_key=api_key,
        base_url=config["base_url"],
    )
    
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    
    for attempt in range(max_retries + 1):
        try:
            response = client.chat.completions.create(
                model=config["model"],
                messages=messages,
                max_tokens=1024,
            )
            return response.choices[0].message.content
        
        except Exception as e:
            if attempt < max_retries:
                wait = 2 ** attempt
                print(f"  ⚠️ 调用失败，{wait}s 后重试 ({attempt + 1}/{max_retries})")
                time.sleep(wait)
            else:
                raise


def test_all_providers(prompt: str = "回复OK即可"):
    """测试所有已配置 API Key 的平台"""
    print("=" * 50)
    print("  免费 AI 模型 API 统一测试")
    print("=" * 50)
    
    results = {}
    for name, config in PROVIDERS.items():
        api_key = os.environ.get(config["env_key"])
        status = "🔑 已配置" if api_key else "❌ 未配置"
        print(f"\n[{name}] {config['desc']}")
        print(f"  状态: {status}")
        print(f"  Base URL: {config['base_url']}")
        print(f"  Model: {config['model']}")
        
        if api_key:
            try:
                start = time.time()
                reply = call_llm(name, prompt)
                elapsed = time.time() - start
                print(f"  ✅ 调用成功 ({elapsed:.2f}s)")
                print(f"  回复: {reply[:100]}")
                results[name] = {"status": "ok", "time": elapsed, "reply": reply[:100]}
            except Exception as e:
                print(f"  ❌ 调用失败: {e}")
                results[name] = {"status": "error", "error": str(e)}
    
    print("\n" + "=" * 50)
    print(f"  测试完成: {len(results)}/{len(PROVIDERS)} 个平台已测试")
    print("=" * 50)
    return results


if __name__ == "__main__":
    # 运行测试
    results = test_all_providers("请用一句话介绍你自己")
    
    # 保存结果
    output_path = os.path.join(os.path.dirname(__file__), "test-output.json")
    with open(output_path, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n测试结果已保存到: {output_path}")
