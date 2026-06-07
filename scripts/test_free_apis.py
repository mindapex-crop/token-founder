#!/usr/bin/env python3
"""
智谱2号战士 - Free AI API Tester
Tests 16+ free AI model API providers and records results.
"""

import requests
import json
import time
import os
import sys
from datetime import datetime, timezone

TEST_PROMPT = "Say hello in one sentence."
TEST_TIMEOUT = 30  # seconds
RESULTS_FILE = "/home/z/my-project/token-founder/test_results.json"

# ============================================================================
# API Key Sources - Check all possible locations
# ============================================================================
def load_keys():
    """Load API keys from environment variables."""
    keys = {}
    mapping = {
        "GOOGLE_GEMINI_API_KEY": ["GOOGLE_API_KEY", "GEMINI_API_KEY", "GOOGLE_GEMINI_API_KEY", "GOOGLE_AI_API_KEY"],
        "GROQ_API_KEY": ["GROQ_API_KEY", "GROQ"],
        "CEREBRAS_API_KEY": ["CEREBRAS_API_KEY", "CEREBRAS"],
        "OPENROUTER_API_KEY": ["OPENROUTER_API_KEY", "OPENROUTER"],
        "DEEPSEEK_API_KEY": ["DEEPSEEK_API_KEY", "DEEPSEEK"],
        "SILICONFLOW_API_KEY": ["SILICONFLOW_API_KEY", "SILICONFLOW_TOKEN", "SILICONFLOW"],
        "MISTRAL_API_KEY": ["MISTRAL_API_KEY", "MISTRAL"],
        "COHERE_API_KEY": ["COHERE_API_KEY", "COHERE", "CO_API_KEY"],
        "XFYUN_API_KEY": ["XFYUN_API_KEY", "XFYUN_APP_ID", "XFYUN"],
        "AGNES_API_KEY": ["AGNES_API_KEY", "AGNES"],
        "NVIDIA_API_KEY": ["NVIDIA_API_KEY", "NVIDIA_NIM_API_KEY", "NIM_API_KEY", "NGC_API_KEY"],
        "SAMBANOVA_API_KEY": ["SAMBANOVA_API_KEY", "SAMBA_API_KEY"],
        "TOGETHER_API_KEY": ["TOGETHER_API_KEY", "TOGETHER_AI_API_KEY"],
        "NOVITA_API_KEY": ["NOVITA_API_KEY", "NOVITA"],
        "ZHIPU_API_KEY": ["ZHIPU_API_KEY", "ZHIPU", "BIGMODEL_API_KEY"],
        "BAICHUAN_API_KEY": ["BAICHUAN_API_KEY", "BAICHUAN"],
        "MINIMAX_API_KEY": ["MINIMAX_API_KEY", "MINIMAX"],
        "DASHSCOPE_API_KEY": ["DASHSCOPE_API_KEY", "DASHSCOPE", "ALIYUN_DASHSCOPE"],
        "MOONSHOT_API_KEY": ["MOONSHOT_API_KEY", "MOONSHOT"],
        "STEPFUN_API_KEY": ["STEPFUN_API_KEY", "STEPFUN"],
        "HUGGINGFACE_API_KEY": ["HF_TOKEN", "HUGGINGFACE_API_KEY", "HF_API_KEY", "HUGGINGFACE_TOKEN"],
        "CLOUDFLARE_API_KEY": ["CLOUDFLARE_API_TOKEN", "CF_API_TOKEN", "CLOUDFLARE_AUTH_TOKEN"],
        "OPENAI_API_KEY": ["OPENAI_API_KEY"],
    }
    for canonical, env_names in mapping.items():
        for env_name in env_names:
            val = os.environ.get(env_name)
            if val:
                keys[canonical] = val
                break
    return keys

API_KEYS = load_keys()

# ============================================================================
# Provider Definitions
# ============================================================================
PROVIDERS = [
    # --- Tier 1: No API key needed ---
    {
        "id": "pollinations_get",
        "name": "Pollinations.ai (GET)",
        "url": "https://text.pollinations.ai/openai",
        "model": "openai",
        "needs_key": False,
        "notes": "Completely free, no key needed. GET or POST to /openai endpoint.",
        "test_fn": "test_pollinations",
    },
    {
        "id": "pollinations_post",
        "name": "Pollinations.ai (POST)",
        "url": "https://text.pollinations.ai/openai",
        "model": "openai-large",
        "needs_key": False,
        "notes": "OpenAI-compatible POST endpoint, no key needed.",
        "test_fn": "test_pollinations_openai",
    },

    # --- Tier 2: Free models on OpenRouter ---
    {
        "id": "openrouter_free",
        "name": "OpenRouter (Free Models)",
        "url": "https://openrouter.ai/api/v1",
        "model": "google/gemma-3-27b-it:free",
        "needs_key": True,
        "key_var": "OPENROUTER_API_KEY",
        "notes": "Has free models, no CC required. Email registration.",
        "test_fn": "test_openai_compatible",
    },

    # --- Tier 3: Free tier / free credits ---
    {
        "id": "google_gemini",
        "name": "Google Gemini",
        "url": "https://generativelanguage.googleapis.com/v1beta/openai/",
        "model": "gemini-2.0-flash",
        "needs_key": True,
        "key_var": "GOOGLE_GEMINI_API_KEY",
        "notes": "AI Studio free tier. Generous free quota.",
        "test_fn": "test_gemini",
    },
    {
        "id": "groq",
        "name": "Groq",
        "url": "https://api.groq.com/openai/v1",
        "model": "llama-3.3-70b-versatile",
        "needs_key": True,
        "key_var": "GROQ_API_KEY",
        "notes": "Ultra-fast inference. Free tier available. Email registration.",
        "test_fn": "test_openai_compatible",
    },
    {
        "id": "cerebras",
        "name": "Cerebras",
        "url": "https://api.cerebras.ai/v1",
        "model": "llama-3.3-70b",
        "needs_key": True,
        "key_var": "CEREBRAS_API_KEY",
        "notes": "Fast wafer-scale inference. Free tier available.",
        "test_fn": "test_openai_compatible",
    },
    {
        "id": "deepseek",
        "name": "DeepSeek",
        "url": "https://api.deepseek.com/v1",
        "model": "deepseek-chat",
        "needs_key": True,
        "key_var": "DEEPSEEK_API_KEY",
        "notes": "Chinese provider. Very cheap. Free quota for new users.",
        "test_fn": "test_openai_compatible",
    },
    {
        "id": "siliconflow",
        "name": "SiliconFlow",
        "url": "https://api.siliconflow.cn/v1",
        "model": "deepseek-ai/DeepSeek-V3",
        "needs_key": True,
        "key_var": "SILICONFLOW_API_KEY",
        "notes": "Chinese provider. Free models available including DeepSeek-V3, Qwen, etc.",
        "test_fn": "test_openai_compatible",
    },
    {
        "id": "mistral",
        "name": "Mistral AI",
        "url": "https://api.mistral.ai/v1",
        "model": "mistral-small-latest",
        "needs_key": True,
        "key_var": "MISTRAL_API_KEY",
        "notes": "European provider. Free tier with rate limits.",
        "test_fn": "test_mistral",
    },
    {
        "id": "cohere",
        "name": "Cohere",
        "url": "https://api.cohere.ai/v1",
        "model": "command-r-plus",
        "needs_key": True,
        "key_var": "COHERE_API_KEY",
        "notes": "Enterprise AI. Free trial key available.",
        "test_fn": "test_cohere",
    },
    {
        "id": "nvidia_nim",
        "name": "NVIDIA NIM",
        "url": "https://integrate.api.nvidia.com/v1",
        "model": "meta/llama-3.3-70b-instruct",
        "needs_key": True,
        "key_var": "NVIDIA_API_KEY",
        "notes": "Free NIM endpoints for developers. NVIDIA developer account needed.",
        "test_fn": "test_openai_compatible",
    },
    {
        "id": "sambanova",
        "name": "SambaNova",
        "url": "https://api.sambanova.ai/v1",
        "model": "Meta-Llama-3.3-70B-Instruct",
        "needs_key": True,
        "key_var": "SAMBANOVA_API_KEY",
        "notes": "Free fast inference. Provides free API keys.",
        "test_fn": "test_openai_compatible",
    },
    {
        "id": "together_ai",
        "name": "Together AI",
        "url": "https://api.together.xyz/v1",
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",
        "needs_key": True,
        "key_var": "TOGETHER_API_KEY",
        "notes": "$5-100 free credits depending on registration type.",
        "test_fn": "test_openai_compatible",
    },
    {
        "id": "huggingface",
        "name": "HuggingFace Inference",
        "url": "https://api-inference.huggingface.co/",
        "model": "meta-llama/Llama-3.3-70B-Instruct",
        "needs_key": True,
        "key_var": "HUGGINGFACE_API_KEY",
        "notes": "Free tier with rate limits. Can also work without key for serverless models.",
        "test_fn": "test_huggingface",
    },
    {
        "id": "agnes_ai",
        "name": "Agnes AI",
        "url": "https://apihub.agnes-ai.com/v1",
        "model": "agnes-2.0-flash",
        "needs_key": True,
        "key_var": "AGNES_API_KEY",
        "notes": "Free multimodal API. Claims free access.",
        "test_fn": "test_openai_compatible",
    },
    {
        "id": "xfyun",
        "name": "讯飞 MaaS (XFYun)",
        "url": "https://maas-api.cn-huabei-1.xf-yun.com/v2",
        "model": "Qwen3.6-35B-A3B",
        "needs_key": True,
        "key_var": "XFYUN_API_KEY",
        "notes": "Chinese provider. Free Qwen3.6 until June 30, 2025. Custom API format.",
        "test_fn": "test_xfyun",
    },
    {
        "id": "cloudflare_workers_ai",
        "name": "Cloudflare Workers AI",
        "url": "https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1",
        "model": "@cf/meta/llama-3.1-8b-instruct",
        "needs_key": True,
        "key_var": "CLOUDFLARE_API_KEY",
        "notes": "Free tier with Workers AI. Needs Cloudflare account ID + API token.",
        "test_fn": "test_cloudflare",
    },

    # --- Tier 4: Extra free endpoints discovered ---
    {
        "id": "duckduckgo_chat",
        "name": "DuckDuckGo AI Chat (Free)",
        "url": "https://duckduckgo.com/duckchat/",
        "model": "gpt-4o-mini",
        "needs_key": False,
        "notes": "Free AI chat via DuckDuckGo. No key needed but requires cookie-based auth.",
        "test_fn": "test_duckduckgo",
    },
    {
        "id": "zhipu_glm_free",
        "name": "智谱 BigModel Free",
        "url": "https://open.bigmodel.cn/api/paas/v4",
        "model": "glm-4-flash",
        "needs_key": True,
        "key_var": "ZHIPU_API_KEY",
        "notes": "Chinese provider. GLM-4-Flash is FREE. Register at open.bigmodel.cn.",
        "test_fn": "test_openai_compatible",
    },
    {
        "id": "baichuan",
        "name": "百川 Baichuan Free",
        "url": "https://api.baichuan-ai.com/v1",
        "model": "Baichuan4",
        "needs_key": True,
        "key_var": "BAICHUAN_API_KEY",
        "notes": "Chinese provider. Free tier available.",
        "test_fn": "test_openai_compatible",
    },
    {
        "id": "minimax",
        "name": "MiniMax Free",
        "url": "https://api.minimax.chat/v1",
        "model": "MiniMax-Text-01",
        "needs_key": True,
        "key_var": "MINIMAX_API_KEY",
        "notes": "Chinese provider. Free models available.",
        "test_fn": "test_openai_compatible",
    },
    {
        "id": "dashscope",
        "name": "阿里 DashScope (Free Qwen)",
        "url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "model": "qwen-turbo",
        "needs_key": True,
        "key_var": "DASHSCOPE_API_KEY",
        "notes": "Alibaba Cloud. Qwen models free tier. 1M free tokens/month.",
        "test_fn": "test_openai_compatible",
    },
    {
        "id": "yi_moonshot",
        "name": "Moonshot / Yi (Free)",
        "url": "https://api.moonshot.cn/v1",
        "model": "moonshot-v1-8k",
        "needs_key": True,
        "key_var": "MOONSHOT_API_KEY",
        "notes": "Chinese provider. Free quota available. Register at platform.moonshot.cn.",
        "test_fn": "test_openai_compatible",
    },
    {
        "id": "stepfun",
        "name": "阶跃星辰 StepFun",
        "url": "https://api.stepfun.com/v1",
        "model": "step-1-8k",
        "needs_key": True,
        "key_var": "STEPFUN_API_KEY",
        "notes": "Chinese provider. Free tier available.",
        "test_fn": "test_openai_compatible",
    },
    {
        "id": "novita",
        "name": "Novita AI (Free Tier)",
        "url": "https://api.novita.ai/v3",
        "model": "meta-llama/Meta-Llama-3.1-8B-Instruct",
        "needs_key": True,
        "key_var": "NOVITA_API_KEY",
        "notes": "$0.5 free credits on signup. Various open models.",
        "test_fn": "test_novita",
    },
]

# ============================================================================
# Test Functions
# ============================================================================

def test_pollinations(provider):
    """Pollinations.ai - completely free, no key needed. GET request."""
    url = "https://text.pollinations.ai/openai"
    params = {
        "model": "openai",
    }
    payload = {
        "model": "openai",
        "messages": [{"role": "user", "content": TEST_PROMPT}],
    }
    headers = {"User-Agent": "Mozilla/5.0 (compatible; API-Tester/1.0)"}
    
    start = time.time()
    try:
        resp = requests.get(url, params=params, json=payload, headers=headers, timeout=TEST_TIMEOUT)
        elapsed = time.time() - start
        if resp.status_code == 200:
            try:
                data = resp.json()
                text = ""
                if "choices" in data and len(data["choices"]) > 0:
                    text = data["choices"][0].get("message", {}).get("content", "")
                return {
                    "status_code": 200,
                    "response_time": round(elapsed, 3),
                    "success": True,
                    "response_text": text[:500],
                    "model": data.get("model", "openai"),
                    "error": None,
                }
            except json.JSONDecodeError:
                # Maybe it returned plain text
                return {
                    "status_code": 200,
                    "response_time": round(elapsed, 3),
                    "success": True,
                    "response_text": resp.text[:500],
                    "error": None,
                }
        return {
            "status_code": resp.status_code,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": resp.text[:500],
            "error": f"HTTP {resp.status_code}: {resp.text[:200]}",
        }
    except Exception as e:
        elapsed = time.time() - start
        return {
            "status_code": 0,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": None,
            "error": str(e)[:300],
        }


def test_pollinations_openai(provider):
    """Pollinations.ai OpenAI-compatible POST endpoint."""
    url = "https://text.pollinations.ai/openai/chat/completions"
    payload = {
        "model": "openai-large",
        "messages": [{"role": "user", "content": TEST_PROMPT}],
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (compatible; API-Tester/1.0)",
    }
    
    start = time.time()
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=TEST_TIMEOUT)
        elapsed = time.time() - start
        if resp.status_code == 200:
            data = resp.json()
            text = ""
            if "choices" in data and len(data["choices"]) > 0:
                text = data["choices"][0].get("message", {}).get("content", "")
            return {
                "status_code": 200,
                "response_time": round(elapsed, 3),
                "success": True,
                "response_text": text[:500],
                "model": data.get("model", "unknown"),
                "error": None,
            }
        return {
            "status_code": resp.status_code,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": resp.text[:500],
            "error": f"HTTP {resp.status_code}: {resp.text[:200]}",
        }
    except Exception as e:
        elapsed = time.time() - start
        return {
            "status_code": 0,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": None,
            "error": str(e)[:300],
        }


def test_openai_compatible(provider):
    """Test any OpenAI-compatible /v1/chat/completions endpoint."""
    base_url = provider["url"].rstrip("/")
    model = provider["model"]
    key_var = provider.get("key_var")
    key = API_KEYS.get(key_var, "")
    
    url = f"{base_url}/chat/completions"
    headers = {
        "Content-Type": "application/json",
    }
    if key:
        headers["Authorization"] = f"Bearer {key}"
    
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": TEST_PROMPT}],
        "max_tokens": 100,
    }
    
    start = time.time()
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=TEST_TIMEOUT)
        elapsed = time.time() - start
        
        if resp.status_code == 200:
            data = resp.json()
            text = ""
            if "choices" in data and len(data["choices"]) > 0:
                text = data["choices"][0].get("message", {}).get("content", "")
            return {
                "status_code": 200,
                "response_time": round(elapsed, 3),
                "success": True,
                "response_text": text[:500],
                "model_used": data.get("model", model),
                "usage": data.get("usage", {}),
                "error": None,
                "had_key": bool(key),
            }
        else:
            return {
                "status_code": resp.status_code,
                "response_time": round(elapsed, 3),
                "success": False,
                "response_text": resp.text[:500],
                "error": f"HTTP {resp.status_code}: {resp.text[:300]}",
                "had_key": bool(key),
            }
    except Exception as e:
        elapsed = time.time() - start
        return {
            "status_code": 0,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": None,
            "error": str(e)[:300],
            "had_key": bool(key),
        }


def test_gemini(provider):
    """Test Google Gemini API with OpenAI-compatible endpoint."""
    key = API_KEYS.get("GOOGLE_GEMINI_API_KEY", "")
    model = provider["model"]
    
    url = f"https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
    headers = {
        "Content-Type": "application/json",
    }
    if key:
        url = f"{url}?key={key}"
    
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": TEST_PROMPT}],
    }
    
    start = time.time()
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=TEST_TIMEOUT)
        elapsed = time.time() - start
        
        if resp.status_code == 200:
            data = resp.json()
            text = ""
            if "choices" in data and len(data["choices"]) > 0:
                text = data["choices"][0].get("message", {}).get("content", "")
            return {
                "status_code": 200,
                "response_time": round(elapsed, 3),
                "success": True,
                "response_text": text[:500],
                "model_used": data.get("model", model),
                "error": None,
                "had_key": bool(key),
            }
        else:
            return {
                "status_code": resp.status_code,
                "response_time": round(elapsed, 3),
                "success": False,
                "response_text": resp.text[:500],
                "error": f"HTTP {resp.status_code}: {resp.text[:300]}",
                "had_key": bool(key),
            }
    except Exception as e:
        elapsed = time.time() - start
        return {
            "status_code": 0,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": None,
            "error": str(e)[:300],
            "had_key": bool(key),
        }


def test_mistral(provider):
    """Test Mistral API - uses 'messages' directly, not OpenAI format."""
    key = API_KEYS.get("MISTRAL_API_KEY", "")
    model = provider["model"]
    
    url = f"https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
    }
    if key:
        headers["Authorization"] = f"Bearer {key}"
    
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": TEST_PROMPT}],
        "max_tokens": 100,
    }
    
    start = time.time()
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=TEST_TIMEOUT)
        elapsed = time.time() - start
        
        if resp.status_code == 200:
            data = resp.json()
            text = ""
            if "choices" in data and len(data["choices"]) > 0:
                text = data["choices"][0].get("message", {}).get("content", "")
            return {
                "status_code": 200,
                "response_time": round(elapsed, 3),
                "success": True,
                "response_text": text[:500],
                "model_used": data.get("model", model),
                "error": None,
                "had_key": bool(key),
            }
        return {
            "status_code": resp.status_code,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": resp.text[:500],
            "error": f"HTTP {resp.status_code}: {resp.text[:300]}",
            "had_key": bool(key),
        }
    except Exception as e:
        elapsed = time.time() - start
        return {
            "status_code": 0,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": None,
            "error": str(e)[:300],
            "had_key": bool(key),
        }


def test_cohere(provider):
    """Test Cohere API - uses custom format with 'message' endpoint."""
    key = API_KEYS.get("COHERE_API_KEY", "")
    model = provider["model"]
    
    url = "https://api.cohere.ai/v1/chat"
    headers = {
        "Content-Type": "application/json",
    }
    if key:
        headers["Authorization"] = f"Bearer {key}"
    
    payload = {
        "model": model,
        "message": TEST_PROMPT,
        "max_tokens": 100,
    }
    
    start = time.time()
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=TEST_TIMEOUT)
        elapsed = time.time() - start
        
        if resp.status_code == 200:
            data = resp.json()
            text = data.get("text", data.get("chat", {}).get("response", ""))
            return {
                "status_code": 200,
                "response_time": round(elapsed, 3),
                "success": True,
                "response_text": text[:500],
                "model_used": model,
                "error": None,
                "had_key": bool(key),
            }
        return {
            "status_code": resp.status_code,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": resp.text[:500],
            "error": f"HTTP {resp.status_code}: {resp.text[:300]}",
            "had_key": bool(key),
        }
    except Exception as e:
        elapsed = time.time() - start
        return {
            "status_code": 0,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": None,
            "error": str(e)[:300],
            "had_key": bool(key),
        }


def test_huggingface(provider):
    """Test HuggingFace Inference API - both with and without key."""
    key = API_KEYS.get("HUGGINGFACE_API_KEY", "")
    model = provider["model"]
    
    # Try with the model endpoint first
    url = f"https://api-inference.huggingface.co/models/{model}"
    headers = {
        "Content-Type": "application/json",
    }
    if key:
        headers["Authorization"] = f"Bearer {key}"
    
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": TEST_PROMPT}],
        "max_tokens": 100,
    }
    
    start = time.time()
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=TEST_TIMEOUT)
        elapsed = time.time() - start
        
        if resp.status_code == 200:
            data = resp.json()
            text = ""
            if isinstance(data, list):
                text = data[0].get("generated_text", "") if data else ""
            elif isinstance(data, dict):
                if "choices" in data:
                    text = data["choices"][0].get("message", {}).get("content", "")
                elif "generated_text" in data:
                    text = data["generated_text"]
            return {
                "status_code": 200,
                "response_time": round(elapsed, 3),
                "success": True,
                "response_text": str(text)[:500],
                "model_used": model,
                "error": None,
                "had_key": bool(key),
            }
        return {
            "status_code": resp.status_code,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": resp.text[:500],
            "error": f"HTTP {resp.status_code}: {resp.text[:300]}",
            "had_key": bool(key),
        }
    except Exception as e:
        elapsed = time.time() - start
        return {
            "status_code": 0,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": None,
            "error": str(e)[:300],
            "had_key": bool(key),
        }


def test_xfyun(provider):
    """Test 讯飞 MaaS API - custom format with HMAC auth."""
    key = API_KEYS.get("XFYUN_API_KEY", "")
    
    if not key:
        return {
            "status_code": 0,
            "response_time": 0,
            "success": False,
            "response_text": None,
            "error": "No XFYUN API key available. Need app_id + api_key + api_secret.",
            "had_key": False,
        }
    
    # XFYun requires HMAC authentication - complex setup
    return {
        "status_code": 0,
        "response_time": 0,
        "success": False,
        "response_text": None,
        "error": "XFYun requires app_id + api_key + api_secret with HMAC auth. Cannot test without credentials.",
        "had_key": True,
    }


def test_cloudflare(provider):
    """Test Cloudflare Workers AI."""
    key = API_KEYS.get("CLOUDFLARE_API_KEY", "")
    account_id = os.environ.get("CLOUDFLARE_ACCOUNT_ID", "")
    
    if not key or not account_id:
        return {
            "status_code": 0,
            "response_time": 0,
            "success": False,
            "response_text": None,
            "error": "Need both CLOUDFLARE_API_TOKEN and CLOUDFLARE_ACCOUNT_ID.",
            "had_key": bool(key),
            "had_account_id": bool(account_id),
        }
    
    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}",
    }
    payload = {
        "model": provider["model"],
        "messages": [{"role": "user", "content": TEST_PROMPT}],
    }
    
    start = time.time()
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=TEST_TIMEOUT)
        elapsed = time.time() - start
        if resp.status_code == 200:
            data = resp.json()
            text = ""
            if "result" in data:
                text = data["result"]
            elif "choices" in data:
                text = data["choices"][0].get("message", {}).get("content", "")
            return {
                "status_code": 200,
                "response_time": round(elapsed, 3),
                "success": True,
                "response_text": str(text)[:500],
                "error": None,
                "had_key": True,
            }
        return {
            "status_code": resp.status_code,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": resp.text[:500],
            "error": f"HTTP {resp.status_code}: {resp.text[:300]}",
            "had_key": True,
        }
    except Exception as e:
        elapsed = time.time() - start
        return {
            "status_code": 0,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": None,
            "error": str(e)[:300],
            "had_key": True,
        }


def test_duckduckgo(provider):
    """Test DuckDuckGo AI Chat - needs initial cookie fetch first."""
    start = time.time()
    try:
        # First get a vqd token
        session = requests.Session()
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
        }
        
        # Get the initial page to get cookies
        resp = session.get("https://duckduckgo.com/duckchat/", headers=headers, timeout=TEST_TIMEOUT)
        
        # Try to get vqd token
        status_url = "https://duckduckgo.com/duckchat/vqd-status"
        resp2 = session.post(status_url, headers=headers, timeout=TEST_TIMEOUT)
        
        vqd = None
        try:
            data = resp2.json()
            vqd = data.get("vqd")
        except:
            pass
        
        if not vqd:
            # Alternative: extract from script tags
            import re
            match = re.search(r'vqd=([\'"])([^\'"]+)\1', resp.text)
            if match:
                vqd = match.group(2)
        
        if not vqd:
            elapsed = time.time() - start
            return {
                "status_code": resp.status_code,
                "response_time": round(elapsed, 3),
                "success": False,
                "response_text": None,
                "error": f"Could not get vqd token. Status: {resp.status_code}",
                "had_key": False,
            }
        
        elapsed = time.time() - start
        return {
            "status_code": resp.status_code,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": None,
            "error": f"Got vqd token ({vqd[:10]}...), but full chat requires WebSocket. Marking as partial success.",
            "had_key": False,
            "partial": True,
            "vqd_obtained": True,
        }
    except Exception as e:
        elapsed = time.time() - start
        return {
            "status_code": 0,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": None,
            "error": str(e)[:300],
            "had_key": False,
        }


def test_novita(provider):
    """Test Novita AI API - uses v3 endpoint."""
    key = API_KEYS.get("NOVITA_API_KEY", "")
    model = provider["model"]
    
    url = "https://api.novita.ai/v3/openai/chat/completions"
    headers = {
        "Content-Type": "application/json",
    }
    if key:
        headers["Authorization"] = f"Bearer {key}"
    
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": TEST_PROMPT}],
        "max_tokens": 100,
    }
    
    start = time.time()
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=TEST_TIMEOUT)
        elapsed = time.time() - start
        if resp.status_code == 200:
            data = resp.json()
            text = ""
            if "choices" in data and len(data["choices"]) > 0:
                text = data["choices"][0].get("message", {}).get("content", "")
            return {
                "status_code": 200,
                "response_time": round(elapsed, 3),
                "success": True,
                "response_text": text[:500],
                "model_used": data.get("model", model),
                "error": None,
                "had_key": bool(key),
            }
        return {
            "status_code": resp.status_code,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": resp.text[:500],
            "error": f"HTTP {resp.status_code}: {resp.text[:300]}",
            "had_key": bool(key),
        }
    except Exception as e:
        elapsed = time.time() - start
        return {
            "status_code": 0,
            "response_time": round(elapsed, 3),
            "success": False,
            "response_text": None,
            "error": str(e)[:300],
            "had_key": bool(key),
        }


# ============================================================================
# Additional: Test providers that might work without any key
# ============================================================================

def test_free_tier_check(provider):
    """Check if provider's base URL is reachable even without key."""
    url = provider["url"]
    try:
        start = time.time()
        resp = requests.get(url, timeout=10)
        elapsed = time.time() - start
        return {
            "reachable": True,
            "status_code": resp.status_code,
            "response_time": round(elapsed, 3),
        }
    except Exception as e:
        return {
            "reachable": False,
            "error": str(e)[:200],
        }


# ============================================================================
# Main Test Runner
# ============================================================================

def run_all_tests():
    """Run tests for all providers and collect results."""
    results = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "test_prompt": TEST_PROMPT,
        "timeout_seconds": TEST_TIMEOUT,
        "available_keys": {k: "***" + v[-4:] if v else "NOT_SET" for k, v in API_KEYS.items()},
        "providers": [],
    }
    
    print("=" * 80)
    print("智谱2号战士 - Free AI API Tester")
    print(f"Time: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"Test Prompt: \"{TEST_PROMPT}\"")
    print(f"Available API keys: {sum(1 for v in API_KEYS.values() if v)}/{len(API_KEYS)}")
    print("=" * 80)
    
    test_fns = {
        "test_pollinations": test_pollinations,
        "test_pollinations_openai": test_pollinations_openai,
        "test_openai_compatible": test_openai_compatible,
        "test_gemini": test_gemini,
        "test_mistral": test_mistral,
        "test_cohere": test_cohere,
        "test_huggingface": test_huggingface,
        "test_xfyun": test_xfyun,
        "test_cloudflare": test_cloudflare,
        "test_duckduckgo": test_duckduckgo,
        "test_novita": test_novita,
    }
    
    for i, provider in enumerate(PROVIDERS):
        pid = provider["id"]
        name = provider["name"]
        needs_key = provider["needs_key"]
        key_var = provider.get("key_var", "")
        has_key = bool(API_KEYS.get(key_var))
        
        status_icon = "🔑" if has_key else "❌" if needs_key else "🔓"
        print(f"\n[{i+1}/{len(PROVIDERS)}] {status_icon} {name}")
        print(f"    URL: {provider['url']}")
        print(f"    Model: {provider['model']}")
        print(f"    Needs key: {needs_key}, Has key: {has_key}")
        
        test_fn_name = provider.get("test_fn", "test_openai_compatible")
        test_fn = test_fns.get(test_fn_name)
        
        if not test_fn:
            result = {
                "error": f"Unknown test function: {test_fn_name}",
                "success": False,
            }
        else:
            try:
                result = test_fn(provider)
            except Exception as e:
                result = {
                    "error": str(e)[:500],
                    "success": False,
                    "status_code": 0,
                    "response_time": 0,
                }
        
        # Merge provider info with result
        entry = {
            "id": pid,
            "name": name,
            "url": provider["url"],
            "model": provider["model"],
            "needs_key": needs_key,
            "has_key": has_key,
            "notes": provider.get("notes", ""),
            **result,
        }
        
        results["providers"].append(entry)
        
        # Print result
        if result.get("success"):
            print(f"    ✅ SUCCESS in {result.get('response_time', '?')}s")
            text = result.get("response_text", "")
            if text:
                print(f"    Response: {text[:100]}...")
        elif result.get("partial"):
            print(f"    ⚠️ PARTIAL: {result.get('error', '')[:100]}")
        else:
            print(f"    ❌ FAILED: {result.get('error', 'Unknown error')[:100]}")
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    total = len(results["providers"])
    succeeded = sum(1 for p in results["providers"] if p.get("success"))
    failed_no_key = sum(1 for p in results["providers"] if not p.get("success") and p.get("needs_key") and not p.get("has_key"))
    failed_with_key = sum(1 for p in results["providers"] if not p.get("success") and p.get("needs_key") and p.get("has_key"))
    failed_no_key_needed = sum(1 for p in results["providers"] if not p.get("success") and not p.get("needs_key"))
    
    print(f"Total providers tested: {total}")
    print(f"Succeeded: {succeeded}")
    print(f"Failed (no key): {failed_no_key}")
    print(f"Failed (with key): {failed_with_key}")
    print(f"Failed (no key needed): {failed_no_key_needed}")
    
    # Success table
    print(f"\n{'Provider':<35} {'Status':<10} {'Time':<8} {'Response'}")
    print("-" * 80)
    for p in results["providers"]:
        status = "✅ OK" if p.get("success") else "❌ FAIL"
        rt = f"{p.get('response_time', 0):.2f}s" if p.get('response_time') else "-"
        resp = (p.get("response_text") or "")[:50]
        if p.get("success"):
            resp = f'"{resp}"'
        else:
            resp = p.get("error", "")[:50]
        print(f"{p['name']:<35} {status:<10} {rt:<8} {resp}")
    
    # Save results
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False, default=str)
    
    print(f"\nResults saved to: {RESULTS_FILE}")
    
    return results


if __name__ == "__main__":
    results = run_all_tests()
