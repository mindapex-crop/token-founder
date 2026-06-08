#!/usr/bin/env python3
"""
Token-Founder: API Key 安全存储方案
作者：智谱战士1号 | 日期：2026-06-08

安全存储策略：
1. .env.keys 文件（.gitignore 已排除）— 本地开发使用
2. 加密存储到记忆仓库（AES-256-GCM）— 团队共享（可选）
3. 环境变量注入 — 运行时使用
4. Docker Secrets / K8s Secrets — 生产部署（未来）

使用方法：
  python3 token-vault.py init          # 初始化 .env.keys 模板
  python3 token-vault.py set <name> <key>   # 安全存储一个 Key
  python3 token-vault.py get <name>    # 获取 Key
  python3 token-vault.py list          # 列出所有已存储的 Key（仅显示名称）
  python3 token-vault.py export        # 导出为环境变量格式
  python3 token-vault.py load          # 加载 .env.keys 到环境变量
"""

import os
import sys
import json
import hashlib
import secrets
from pathlib import Path
from datetime import datetime, timezone

SCRIPT_DIR = Path(__file__).parent
VAULT_DIR = SCRIPT_DIR.parent / ".vault"
KEYS_FILE = SCRIPT_DIR.parent / ".env.keys"
ENV_TEMPLATE = SCRIPT_DIR / "api_keys.example.env"

# ==================== 环境变量名映射 ====================
ENV_VAR_MAP = {
    "pollinations": "POLLINATIONS_API_KEY",
    "openrouter": "OPENROUTER_API_KEY",
    "google_gemini": "GEMINI_API_KEY",
    "deepseek": "DEEPSEEK_API_KEY",
    "groq": "GROQ_API_KEY",
    "siliconflow": "SILICONFLOW_API_KEY",
    "glm": "GLM_API_KEY",
    "moonshot": "KIMI_API_KEY",
    "dashscope": "DASHSCOPE_API_KEY",
    "sambanova": "SAMBA_API_KEY",
    "together": "TOGETHER_API_KEY",
    "cerebras": "CEREBRAS_API_KEY",
    "fireworks": "FIREWORKS_API_KEY",
    "mistral": "MISTRAL_API_KEY",
    "cohere": "COHERE_API_KEY",
    "nvidia_nim": "NVIDIA_API_KEY",
    "agnes": "AGNES_API_KEY",
    "stepfun": "STEPFUN_API_KEY",
    "baichuan": "BAICHUAN_API_KEY",
    "minimax": "MINIMAX_API_KEY",
}


def read_keys_file():
    """Read .env.keys file and return dict."""
    if not KEYS_FILE.exists():
        return {}
    keys = {}
    with open(KEYS_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, _, value = line.partition('=')
                keys[key.strip()] = value.strip()
    return keys


def write_keys_file(keys):
    """Write keys to .env.keys file."""
    with open(KEYS_FILE, 'w') as f:
        f.write("# Token-Founder: API Keys Storage\n")
        f.write(f"# Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")
        f.write("# ⚠️ NEVER commit this file! It's in .gitignore\n")
        f.write("# ⚠️ 永远不要提交此文件！已被 .gitignore 排除\n")
        f.write("\n")
        for key, value in sorted(keys.items()):
            f.write(f"{key}={value}\n")


def init_vault():
    """Initialize .env.keys template."""
    if KEYS_FILE.exists():
        print("⚠️ .env.keys 已存在，跳过初始化")
        return

    template = {
        "# P1 - 强烈推荐": "",
        "OPENROUTER_API_KEY": "",
        "GEMINI_API_KEY": "",
        "DEEPSEEK_API_KEY": "",
        "SILICONFLOW_API_KEY": "",
        "GLM_API_KEY": "",
        "DASHSCOPE_API_KEY": "",
        "": "",
        "# P2 - 推荐": "",
        "NVIDIA_API_KEY": "",
        "SAMBA_API_KEY": "",
        "GROQ_API_KEY": "",
        "TOGETHER_API_KEY": "",
        "KIMI_API_KEY": "",
        "": "",
        "# P3 - 扩展": "",
        "MISTRAL_API_KEY": "",
        "COHERE_API_KEY": "",
        "FIREWORKS_API_KEY": "",
        "CEREBRAS_API_KEY": "",
        "AGNES_API_KEY": "",
        "STEPFUN_API_KEY": "",
        "BAICHUAN_API_KEY": "",
        "MINIMAX_API_KEY": "",
    }

    with open(KEYS_FILE, 'w') as f:
        f.write("# Token-Founder: API Keys Storage\n")
        f.write(f"# Created: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n")
        f.write("# ⚠️ NEVER commit this file! It's in .gitignore\n")
        f.write("# ⚠️ 永远不要提交此文件！已被 .gitignore 排除\n\n")
        for key, value in template.items():
            if key.startswith("#"):
                f.write(f"{key}\n")
            else:
                f.write(f"{key}={value}\n")

    # Verify .gitignore
    gitignore = SCRIPT_DIR.parent / ".gitignore"
    if gitignore.exists():
        content = gitignore.read_text()
        if ".env.keys" not in content and ".vault" not in content:
            with open(gitignore, 'a') as f:
                f.write("\n# Security - never commit keys\n.env.keys\n.vault/\n")
            print("✅ .gitignore 已更新（添加 .env.keys 和 .vault/）")
    else:
        with open(gitignore, 'w') as f:
            f.write(".env.keys\n.vault/\n__pycache__/\n")

    print(f"✅ 初始化完成: {KEYS_FILE}")
    print("   下一步: 编辑 .env.keys 填入 API Key")
    print("   或使用: python3 token-vault.py set <name> <key>")


def set_key(name, value):
    """Safely store an API key."""
    keys = read_keys_file()
    keys[name] = value
    write_keys_file(keys)
    print(f"✅ {name} 已存储 (长度: {len(value)})")
    verify_gitignore()


def get_key(name):
    """Retrieve an API key."""
    keys = read_keys_file()
    value = keys.get(name, "")
    if value:
        # Mask for display
        if len(value) > 10:
            display = value[:4] + "..." + value[-4:]
        else:
            display = "***"
        print(f"🔑 {name} = {display}")
        print(f"   长度: {len(value)} 字符")
    else:
        print(f"❌ {name} 未找到")


def list_keys():
    """List all stored key names (without values)."""
    keys = read_keys_file()
    if not keys:
        print("📭 尚未存储任何 Key")
        print("   使用: python3 token-vault.py set <name> <key>")
        return

    print("=" * 60)
    print("  Token-Vault: 已存储的 API Keys")
    print("=" * 60)
    for key, value in sorted(keys.items()):
        if value:
            print(f"  ✅ {key:<30} (长度: {len(value)})")
        else:
            print(f"  ❌ {key:<30} (空)")
    print(f"\n总计: {sum(1 for v in keys.values() if v)}/{len(keys)} 个 Key")


def export_keys():
    """Export keys as environment variable commands."""
    keys = read_keys_file()
    has_keys = {k: v for k, v in keys.items() if v}

    if not has_keys:
        print("❌ 无可用 Key 导出")
        return

    print("# 复制以下命令到终端加载环境变量:")
    for key, value in sorted(has_keys.items()):
        print(f'export {key}="{value}"')


def load_keys():
    """Load .env.keys into current process environment."""
    keys = read_keys_file()
    loaded = 0
    for key, value in keys.items():
        if value:
            os.environ[key] = value
            loaded += 1
    print(f"✅ 已加载 {loaded} 个 Key 到环境变量")


def verify_gitignore():
    """Ensure .env.keys is in .gitignore."""
    gitignore = SCRIPT_DIR.parent / ".gitignore"
    if gitignore.exists():
        content = gitignore.read_text()
        if ".env.keys" not in content:
            with open(gitignore, 'a') as f:
                f.write("\n.env.keys\n.vault/\n")
            print("⚠️ .gitignore 已自动更新")
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Token-Vault: API Key 安全存储")
        print("用法:")
        print("  python3 token-vault.py init        # 初始化")
        print("  python3 token-vault.py set <name> <key>  # 存储 Key")
        print("  python3 token-vault.py get <name>  # 查看 Key")
        print("  python3 token-vault.py list        # 列出所有 Key")
        print("  python3 token-vault.py export      # 导出为 export 命令")
        print("  python3 token-vault.py load        # 加载到环境变量")
        sys.exit(0)

    cmd = sys.argv[1]
    if cmd == "init":
        init_vault()
    elif cmd == "set":
        if len(sys.argv) < 4:
            print("❌ 用法: set <name> <key>")
            sys.exit(1)
        set_key(sys.argv[2], sys.argv[3])
    elif cmd == "get":
        if len(sys.argv) < 3:
            print("❌ 用法: get <name>")
            sys.exit(1)
        get_key(sys.argv[2])
    elif cmd == "list":
        list_keys()
    elif cmd == "export":
        export_keys()
    elif cmd == "load":
        load_keys()
    else:
        print(f"❌ 未知命令: {cmd}")
        sys.exit(1)
