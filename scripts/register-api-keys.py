#!/usr/bin/env python3
"""
免费 API Key 注册指引与状态追踪
作者：智谱战士1号 | 日期：2026-06-08

使用方法：
1. 查看注册指引：python3 register-api-keys.py --guide
2. 查看当前状态：python3 register-api-keys.py --status
3. 标记已注册：python3 register-api-keys.py --mark <provider> <api_key>
4. 测试已注册Key：python3 register-api-keys.py --test
5. 生成注册链接列表：python3 register-api-keys.py --links

注册状态保存在 registration_status.json
"""

import os
import sys
import json
import time
import requests
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
STATUS_FILE = SCRIPT_DIR / "registration_status.json"

# ==================== 注册指引 ====================
REGISTRATION_GUIDE = {
    # ---- 即时可用（无需注册）----
    "pollinations": {
        "name": "Pollinations.ai",
        "priority": "P0 - 即时可用",
        "register_url": "https://pollinations.ai",
        "key_url": "无需 API Key",
        "free_quota": "完全免费，无限调用（有IP限速）",
        "models": ["openai (GPT-4o-mini等效)", "openai-large", "mistral", "llama", "deepseek"],
        "setup": "直接调用，无需任何注册",
        "code": 'requests.post("https://text.pollinations.ai/openai/chat/completions", json={"model":"openai","messages":[...]})',
        "note": "从当前IP测试受到速率限制（429），建议配合认证使用或从其他IP调用",
    },
    "openrouter_free": {
        "name": "OpenRouter (免费模型)",
        "priority": "P1 - 邮箱注册",
        "register_url": "https://openrouter.ai/keys",
        "key_url": "https://openrouter.ai/settings/keys",
        "free_quota": "27+ 个永久免费模型，无需信用卡",
        "models": ["google/gemma-3-27b-it:free", "meta-llama/llama-4-scout-17b-16e-instruct:free",
                   "deepseek/deepseek-r1-0528:free", "qwen/qwen3-235b-a22b:free",
                   "microsoft/phi-4-reasoning:free", "nvidia/llama-3.1-nemotron-70b-instruct:free"],
        "setup": "1. 用邮箱注册 OpenRouter 账户\n2. 进入 Settings → API Keys → Create Key\n3. 复制 Key 设置环境变量 OPENROUTER_API_KEY",
        "code": "OPENROUTER_API_KEY=sk-or-xxx python3 unified-call.py",
        "note": "强烈推荐！免费模型最多，质量好，OpenAI兼容格式，每日限额宽裕",
    },

    # ---- 邮箱注册（免费额度）----
    "google_gemini": {
        "name": "Google Gemini (AI Studio)",
        "priority": "P1 - 邮箱注册",
        "register_url": "https://aistudio.google.com/apikey",
        "key_url": "https://aistudio.google.com/apikey",
        "free_quota": "Gemini 2.5 Flash: 1500次/天; Gemini 2.0 Flash: 无限制",
        "models": ["gemini-2.5-flash-preview-05-20", "gemini-2.0-flash", "gemini-1.5-pro", "gemini-1.5-flash"],
        "setup": "1. Google 账号登录 aistudio.google.com\n2. 点击 'Get API Key' → 'Create API Key'\n3. 复制 Key 设置环境变量 GEMINI_API_KEY",
        "code": "GEMINI_API_KEY=AIzaSyxxx python3 unified-call.py",
        "note": "Google出品，免费额度极其慷慨，支持超长上下文(1M tokens)",
    },
    "deepseek": {
        "name": "DeepSeek",
        "priority": "P1 - 手机注册",
        "register_url": "https://platform.deepseek.com/register",
        "key_url": "https://platform.deepseek.com/api_keys",
        "free_quota": "新用户注册赠送 500万 Tokens（DeepSeek-V3）",
        "models": ["deepseek-chat (V3)", "deepseek-reasoner (R1)"],
        "setup": "1. 手机号注册 DeepSeek 平台\n2. 进入 API Keys 页面创建 Key\n3. 复制 Key 设置环境变量 DEEPSEEK_API_KEY",
        "code": "DEEPSEEK_API_KEY=sk-xxx python3 unified-call.py",
        "note": "国产最强推理模型 R1 免费额度，V3 性价比极高",
    },
    "groq": {
        "name": "Groq",
        "priority": "P1 - 邮箱注册",
        "register_url": "https://console.groq.com/keys",
        "key_url": "https://console.groq.com/keys",
        "free_quota": "免费层：每分钟30请求，每日14400请求，限制速率",
        "models": ["llama-3.3-70b-versatile", "llama-4-scout-17b-16e-instruct",
                   "gemma2-9b-it", "mixtral-8x7b-32768"],
        "setup": "1. 邮箱/GitHub 注册 Groq Console\n2. 进入 API Keys → Create Key\n3. 复制 Key 设置环境变量 GROQ_API_KEY",
        "code": "GROQ_API_KEY=gsk_xxx python3 unified-call.py",
        "note": "LPU芯片极速推理（<1s响应），注意：从当前环境IP被Cloudflare WAF拦截，需代理",
    },
    "siliconflow": {
        "name": "硅基流动 SiliconFlow",
        "priority": "P1 - 手机注册",
        "register_url": "https://cloud.siliconflow.cn",
        "key_url": "https://cloud.siliconflow.cn/account/ak",
        "free_quota": "新人注册送 14元额度，DeepSeek-V3/Qwen免费",
        "models": ["deepseek-ai/DeepSeek-V3", "Qwen/Qwen2.5-72B-Instruct",
                   "THUDM/glm-4-9b-chat", "meta-llama/Meta-Llama-3.1-8B-Instruct"],
        "setup": "1. 手机号注册 SiliconFlow\n2. 进入 账户管理 → API密钥\n3. 复制 Key 设置环境变量 SILICONFLOW_API_KEY",
        "code": "SILICONFLOW_API_KEY=sk-xxx python3 unified-call.py",
        "note": "国内平台速度快，聚合100+模型，DeepSeek-V3 免费调用",
    },
    "glm": {
        "name": "智谱 BigModel (GLM-4-Flash)",
        "priority": "P1 - 手机注册",
        "register_url": "https://open.bigmodel.cn",
        "key_url": "https://open.bigmodel.cn/usercenter/apikeys",
        "free_quota": "GLM-4-Flash 永久免费，无Token限制",
        "models": ["glm-4-flash (免费)", "glm-4-plus", "glm-4-long", "glm-4v-flash"],
        "setup": "1. 手机号注册智谱开放平台\n2. 进入 控制台 → API Keys\n3. 复制 Key 设置环境变量 GLM_API_KEY",
        "code": "GLM_API_KEY=xxx.xxx python3 unified-call.py",
        "note": "GLM-4-Flash 永久免费！适合日常大量调用",
    },
    "moonshot": {
        "name": "Moonshot / Kimi",
        "priority": "P2 - 邮箱注册",
        "register_url": "https://platform.moonshot.cn",
        "key_url": "https://platform.moonshot.cn/api-keys",
        "free_quota": "新用户赠送 15元额度",
        "models": ["moonshot-v1-8k", "moonshot-v1-32k", "moonshot-v1-128k"],
        "setup": "1. 邮箱/手机注册 Moonshot 平台\n2. API Keys → 创建 Key\n3. 复制 Key 设置环境变量 KIMI_API_KEY",
        "code": "KIMI_API_KEY=sk-xxx python3 unified-call.py",
        "note": "128K超长上下文，适合文档处理",
    },
    "dashscope": {
        "name": "阿里 DashScope (通义千问)",
        "priority": "P1 - 阿里账号",
        "register_url": "https://dashscope.console.aliyun.com",
        "key_url": "https://dashscope.console.aliyun.com/apiKey",
        "free_quota": "Qwen-Turbo: 每月100万Token免费; Qwen-Plus: 每月100万Token免费",
        "models": ["qwen-turbo", "qwen-plus", "qwen-max", "qwen-long"],
        "setup": "1. 阿里云账号登录 DashScope 控制台\n2. API-KEY 管理 → 创建\n3. 复制 Key 设置环境变量 DASHSCOPE_API_KEY",
        "code": "DASHSCOPE_API_KEY=sk-xxx python3 unified-call.py",
        "note": "阿里云出品，Qwen系列模型质量优秀，国内访问快",
    },

    # ---- 需要更多步骤 ----
    "sambanova": {
        "name": "SambaNova",
        "priority": "P2 - 邮箱注册",
        "register_url": "https://cloud.sambanova.ai",
        "key_url": "https://cloud.sambanova.ai/api-keys",
        "free_quota": "免费 API 访问 Llama/Mistral 模型",
        "models": ["Meta-Llama-3.3-70B-Instruct", "Meta-Llama-3.1-405B-Instruct",
                   "mistral-7b", "qwen2.5-72b"],
        "setup": "1. 邮箱注册 SambaNova Cloud\n2. API Keys → Create API Key\n3. 复制 Key",
        "code": "SAMBA_API_KEY=xxx python3 unified-call.py",
        "note": "免费端点可列出8个模型，推理速度快",
    },
    "together": {
        "name": "Together AI",
        "priority": "P2 - 邮箱注册",
        "register_url": "https://api.together.xyz",
        "key_url": "https://api.together.xyz/settings/api-keys",
        "free_quota": "新用户赠送 $5 额度",
        "models": ["meta-llama/Llama-3.3-70B-Instruct-Turbo", "mistralai/Mixtral-8x7B-Instruct-v0.1"],
        "setup": "1. 邮箱/GitHub 注册 Together AI\n2. Settings → API Keys → New Key\n3. 复制 Key",
        "code": "TOGETHER_API_KEY=xxx python3 unified-call.py",
        "note": "开源模型聚合平台，$5免费额度可调用大量模型",
    },
    "cerebras": {
        "name": "Cerebras",
        "priority": "P2 - 邮箱注册",
        "register_url": "https://cloud.cerebras.ai",
        "key_url": "https://cloud.cerebras.ai/",
        "free_quota": "免费极速推理层",
        "models": ["llama-3.3-70b", "llama-3.1-8b"],
        "setup": "1. 邮箱注册 Cerebras Cloud\n2. 获取 API Key\n3. 注意：当前环境IP被Cloudflare拦截",
        "code": "CEREBRAS_API_KEY=xxx python3 unified-call.py",
        "note": "晶圆级推理芯片，速度极快。但从当前IP被Cloudflare WAF拦截",
    },
    "fireworks": {
        "name": "Fireworks AI",
        "priority": "P2 - 邮箱注册",
        "register_url": "https://fireworks.ai",
        "key_url": "https://fireworks.ai/account/api-keys",
        "free_quota": "新用户赠送免费额度",
        "models": ["llama-v3p1-70b-instruct", "llama-v3.1-8b-instruct", "mixtral-8x7b-instruct"],
        "setup": "1. 邮箱/GitHub 注册\n2. Account → API Keys\n3. 复制 Key",
        "code": "FIREWORKS_API_KEY=xxx python3 unified-call.py",
        "note": "专注开源模型推理加速",
    },
    "mistral": {
        "name": "Mistral AI",
        "priority": "P2 - 邮箱注册",
        "register_url": "https://console.mistral.ai",
        "key_url": "https://console.mistral.ai/api-keys",
        "free_quota": "La Plateforme: 免费层可调用 small 模型",
        "models": ["mistral-small-latest", "mistral-tiny", "open-mistral-7b", "open-mixtral-8x7b"],
        "setup": "1. 邮箱注册 Mistral La Plateforme\n2. API Keys → Create Key\n3. 复制 Key",
        "code": "MISTRAL_API_KEY=xxx python3 unified-call.py",
        "note": "欧洲AI公司，免费层可用mistral-small",
    },
    "cohere": {
        "name": "Cohere",
        "priority": "P3 - 邮箱注册",
        "register_url": "https://dashboard.cohere.com",
        "key_url": "https://dashboard.cohere.com/api-keys",
        "free_quota": "Trial Key: 有限免费额度，支持Command R+",
        "models": ["command-r", "command-r-plus", "command-light"],
        "setup": "1. 邮箱注册 Cohere Dashboard\n2. API Keys → Create Trial Key\n3. 复制 Key",
        "code": "COHERE_API_KEY=xxx python3 unified-call.py",
        "note": "Command R+ 是强大的RAG专用模型，免费层有限制",
    },
    "agnes": {
        "name": "Agnes AI",
        "priority": "P3 - 邮箱注册",
        "register_url": "https://apihub.agnes-ai.com",
        "key_url": "https://apihub.agnes-ai.com",
        "free_quota": "宣称全模态无限期免费",
        "models": ["agnes-2.0-flash"],
        "setup": "1. 访问 Agnes AI 平台注册\n2. 获取 API Key\n3. 端点已验证在线",
        "code": "AGNES_API_KEY=xxx python3 unified-call.py",
        "note": "国产平台，宣称免费但具体额度需注册后确认",
    },
    "nvidia_nim": {
        "name": "NVIDIA NIM",
        "priority": "P2 - NVIDIA账号",
        "register_url": "https://build.nvidia.com",
        "key_url": "https://build.nvidia.com/",
        "free_quota": "免费NIM端点，120个模型可列表",
        "models": ["meta/llama-3.3-70b-instruct", "mistralai/mixtral-8x22b-instruct-v0.1", "google/gemma-2-27b-it"],
        "setup": "1. NVIDIA 开发者账号\n2. build.nvidia.com 获取 API Key\n3. 复制 Key",
        "code": "NVIDIA_API_KEY=nvapi-xxx python3 unified-call.py",
        "note": "120个模型可列表，NVIDIA官方免费推理",
    },
    "stepfun": {
        "name": "阶跃星辰 StepFun",
        "priority": "P3 - 手机注册",
        "register_url": "https://platform.stepfun.com",
        "key_url": "https://platform.stepfun.com/api-keys",
        "free_quota": "免费层可用",
        "models": ["step-1-8k", "step-1-32k", "step-2-16k"],
        "setup": "1. 注册阶跃星辰开放平台\n2. 创建 API Key\n3. 复制 Key",
        "code": "STEPFUN_API_KEY=xxx python3 unified-call.py",
        "note": "国产新锐AI公司",
    },
    "baichuan": {
        "name": "百川 Baichuan",
        "priority": "P3 - 手机注册",
        "register_url": "https://platform.baichuan-ai.com",
        "key_url": "https://platform.baichuan-ai.com/account/api-key",
        "free_quota": "免费层可用",
        "models": ["Baichuan4"],
        "setup": "1. 注册百川开放平台\n2. 创建 API Key\n3. 复制 Key",
        "code": "BAICHUAN_API_KEY=xxx python3 unified-call.py",
        "note": "国产大模型平台",
    },
    "minimax": {
        "name": "MiniMax",
        "priority": "P3 - 邮箱注册",
        "register_url": "https://platform.minimaxi.com",
        "key_url": "https://platform.minimaxi.com/api-key",
        "free_quota": "免费层可用",
        "models": ["MiniMax-Text-01"],
        "setup": "1. 注册 MiniMax 平台\n2. 创建 API Key\n3. 复制 Key",
        "code": "MINIMAX_API_KEY=xxx python3 unified-call.py",
        "note": "国产大模型，MiniMax-Text-01是开放权重模型",
    },
}


def load_status():
    """Load registration status from JSON file."""
    if STATUS_FILE.exists():
        with open(STATUS_FILE, 'r') as f:
            return json.load(f)
    return {"registered": {}, "last_updated": None, "notes": []}


def save_status(status):
    """Save registration status to JSON file."""
    status["last_updated"] = datetime.now(timezone.utc).isoformat()
    with open(STATUS_FILE, 'w') as f:
        json.dump(status, f, indent=2, ensure_ascii=False)


def cmd_guide():
    """Print full registration guide."""
    print("=" * 70)
    print("  Token-Founder: 免费 API Key 注册指引")
    print(f"  更新时间: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 70)

    # Group by priority
    groups = {}
    for pid, info in REGISTRATION_GUIDE.items():
        p = info["priority"]
        if p not in groups:
            groups[p] = []
        groups[p].append((pid, info))

    for priority in sorted(groups.keys()):
        print(f"\n{'='*70}")
        print(f"  {priority}")
        print(f"{'='*70}")
        for pid, info in groups[priority]:
            print(f"\n📋 {info['name']} ({pid})")
            print(f"   注册地址: {info['register_url']}")
            print(f"   Key管理:  {info['key_url']}")
            print(f"   免费额度: {info['free_quota']}")
            print(f"   可用模型: {', '.join(info['models'][:3])}")
            if len(info['models']) > 3:
                print(f"             +{len(info['models'])-3} more")
            print(f"   注册步骤: {info['setup'].split(chr(10))[0]}")
            print(f"   备注:     {info['note']}")

    status = load_status()
    registered = list(status.get("registered", {}).keys())
    if registered:
        print(f"\n{'='*70}")
        print(f"  已注册 ({len(registered)}/{len(REGISTRATION_GUIDE)})")
        print(f"{'='*70}")
        for pid in registered:
            key = status["registered"][pid].get("key", "")
            key_display = key[:6] + "..." + key[-4:] if len(key) > 10 else "***"
            print(f"  ✅ {REGISTRATION_GUIDE.get(pid, {}).get('name', pid)}: {key_display}")

    print(f"\n未注册: {len(REGISTRATION_GUIDE) - len(registered)}/{len(REGISTRATION_GUIDE)}")


def cmd_status():
    """Print current registration status."""
    status = load_status()
    registered = status.get("registered", {})

    print("=" * 70)
    print("  Token-Founder: 注册状态")
    print(f"  最后更新: {status.get('last_updated', 'N/A')}")
    print("=" * 70)

    for pid, info in REGISTRATION_GUIDE.items():
        if pid in registered:
            reg = registered[pid]
            key = reg.get("key", "")
            key_display = key[:6] + "..." + key[-4:] if len(key) > 10 else "***"
            tested = reg.get("tested", False)
            test_result = reg.get("test_result", "")
            print(f"  ✅ {info['name']:<25} Key: {key_display}  Test: {'✅' if tested else '⏳'} {test_result}")
        else:
            print(f"  ❌ {info['name']:<25} 未注册")

    print(f"\n总计: {len(registered)}/{len(REGISTRATION_GUIDE)} 已注册")


def cmd_mark(provider, api_key):
    """Mark a provider as registered with an API key."""
    if provider not in REGISTRATION_GUIDE:
        print(f"❌ 未知提供商: {provider}")
        print(f"   可用: {', '.join(REGISTRATION_GUIDE.keys())}")
        return

    status = load_status()
    if "registered" not in status:
        status["registered"] = {}

    status["registered"][provider] = {
        "key": api_key,
        "registered_at": datetime.now(timezone.utc).isoformat(),
        "tested": False,
    }
    save_status(status)

    name = REGISTRATION_GUIDE[provider]["name"]
    print(f"✅ {name} 注册成功！")
    print(f"   Key: {api_key[:6]}...{api_key[-4:]}")
    print(f"   运行 --test 来验证此 Key")


def cmd_test():
    """Test all registered API keys."""
    status = load_status()
    registered = status.get("registered", {})

    if not registered:
        print("❌ 尚未注册任何 API Key")
        print("   使用 --mark <provider> <api_key> 添加")
        return

    print("=" * 70)
    print("  Token-Founder: API Key 测试")
    print("=" * 70)

    test_prompt = "回复OK即可"

    for pid, reg in registered.items():
        key = reg.get("key", "")
        info = REGISTRATION_GUIDE.get(pid)
        if not info:
            continue

        name = info["name"]
        print(f"\n🔧 测试 {name}...")

        # Map provider to test config
        test_configs = {
            "google_gemini": {
                "url": "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
                "model": "gemini-2.0-flash",
                "auth_type": "query_param",
            },
            "deepseek": {
                "url": "https://api.deepseek.com/v1/chat/completions",
                "model": "deepseek-chat",
            },
            "groq": {
                "url": "https://api.groq.com/openai/v1/chat/completions",
                "model": "llama-3.3-70b-versatile",
            },
            "openrouter_free": {
                "url": "https://openrouter.ai/api/v1/chat/completions",
                "model": "google/gemma-3-27b-it:free",
            },
            "siliconflow": {
                "url": "https://api.siliconflow.cn/v1/chat/completions",
                "model": "deepseek-ai/DeepSeek-V3",
            },
            "glm": {
                "url": "https://open.bigmodel.cn/api/paas/v4/chat/completions",
                "model": "glm-4-flash",
            },
            "moonshot": {
                "url": "https://api.moonshot.cn/v1/chat/completions",
                "model": "moonshot-v1-8k",
            },
            "dashscope": {
                "url": "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions",
                "model": "qwen-turbo",
            },
            "mistral": {
                "url": "https://api.mistral.ai/v1/chat/completions",
                "model": "mistral-small-latest",
            },
            "together": {
                "url": "https://api.together.xyz/v1/chat/completions",
                "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
            },
            "cerebras": {
                "url": "https://api.cerebras.ai/v1/chat/completions",
                "model": "llama-3.3-70b",
            },
            "fireworks": {
                "url": "https://api.fireworks.ai/inference/v1/chat/completions",
                "model": "accounts/fireworks/models/llama-v3p1-70b-instruct",
            },
            "cohere": {
                "url": "https://api.cohere.ai/v1/chat",
                "model": "command-r",
                "payload_override": {"message": test_prompt},
            },
            "sambanova": {
                "url": "https://api.sambanova.ai/v1/chat/completions",
                "model": "Meta-Llama-3.3-70B-Instruct",
            },
            "nvidia_nim": {
                "url": "https://integrate.api.nvidia.com/v1/chat/completions",
                "model": "meta/llama-3.3-70b-instruct",
            },
            "agnes": {
                "url": "https://apihub.agnes-ai.com/v1/chat/completions",
                "model": "agnes-2.0-flash",
            },
            "stepfun": {
                "url": "https://api.stepfun.com/v1/chat/completions",
                "model": "step-1-8k",
            },
            "baichuan": {
                "url": "https://api.baichuan-ai.com/v1/chat/completions",
                "model": "Baichuan4",
            },
            "minimax": {
                "url": "https://api.minimax.chat/v1/chat/completions",
                "model": "MiniMax-Text-01",
            },
        }

        config = test_configs.get(pid)
        if not config:
            print(f"  ⏳ 跳过（无测试配置）")
            continue

        url = config["url"]
        model = config["model"]
        headers = {"Content-Type": "application/json"}

        if config.get("auth_type") == "query_param":
            url = f"{url}?key={key}"
        else:
            headers["Authorization"] = f"Bearer {key}"

        if pid == "cohere" and "payload_override" in config:
            payload = config["payload_override"]
            payload["model"] = model
            payload["max_tokens"] = 100
        else:
            payload = {
                "model": model,
                "messages": [{"role": "user", "content": test_prompt}],
                "max_tokens": 100,
            }

        try:
            start = time.time()
            resp = requests.post(url, json=payload, headers=headers, timeout=30)
            elapsed = time.time() - start

            if resp.status_code == 200:
                try:
                    data = resp.json()
                    if pid == "cohere":
                        text = data.get("text", "")
                    elif "choices" in data:
                        text = data["choices"][0].get("message", {}).get("content", "")
                    else:
                        text = str(data)[:100]
                    print(f"  ✅ 成功 ({elapsed:.2f}s) — 回复: {text[:80]}")
                    status["registered"][pid]["tested"] = True
                    status["registered"][pid]["test_result"] = f"OK {elapsed:.2f}s"
                except:
                    print(f"  ⚠️ 200 但解析失败: {resp.text[:100]}")
                    status["registered"][pid]["test_result"] = f"Parse error"
            else:
                error_text = resp.text[:200]
                print(f"  ❌ HTTP {resp.status_code}: {error_text[:100]}")
                status["registered"][pid]["test_result"] = f"HTTP {resp.status_code}"
        except Exception as e:
            print(f"  ❌ 错误: {str(e)[:100]}")
            status["registered"][pid]["test_result"] = f"Error: {str(e)[:80]}"

    save_status(status)


def cmd_links():
    """Output quick registration links."""
    print("=" * 70)
    print("  Token-Founder: 快速注册链接")
    print("=" * 70)

    # Priority order: P0 first, then P1, P2, P3
    priority_order = {"P0 - 即时可用": 0, "P1 - 邮箱注册": 1, "P2 - 邮箱注册": 2, "P3 - 邮箱注册": 3}

    sorted_providers = sorted(
        REGISTRATION_GUIDE.items(),
        key=lambda x: priority_order.get(x[1]["priority"], 99)
    )

    for pid, info in sorted_providers:
        status = load_status()
        registered = pid in status.get("registered", {})
        icon = "✅" if registered else "❌"
        print(f"  {icon} {info['name']:<30} → {info['register_url']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法:")
        print("  python3 register-api-keys.py --guide    # 查看完整注册指引")
        print("  python3 register-api-keys.py --status   # 查看注册状态")
        print("  python3 register-api-keys.py --mark <provider> <api_key>  # 标记已注册")
        print("  python3 register-api-keys.py --test     # 测试所有已注册Key")
        print("  python3 register-api-keys.py --links    # 快速注册链接")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "--guide":
        cmd_guide()
    elif cmd == "--status":
        cmd_status()
    elif cmd == "--mark":
        if len(sys.argv) < 4:
            print("❌ 用法: --mark <provider> <api_key>")
            sys.exit(1)
        cmd_mark(sys.argv[2], sys.argv[3])
    elif cmd == "--test":
        cmd_test()
    elif cmd == "--links":
        cmd_links()
    else:
        print(f"❌ 未知命令: {cmd}")
        sys.exit(1)
