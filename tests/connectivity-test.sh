#!/bin/bash
# 免费 AI 模型 API 连通性测试脚本
# 用法：bash connectivity-test.sh
# 作者：智谱战士1号 | 日期：2026-06-07

echo "=========================================="
echo "  免费 AI 模型 API 连通性测试"
echo "  测试时间：$(date '+%Y-%m-%d %H:%M:%S')"
echo "  测试环境：$(hostname)"
echo "=========================================="
echo ""

# 颜色定义
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

test_endpoint() {
    local name="$1"
    local url="$2"
    local header="$3"
    
    echo -n "测试 $name ... "
    
    if [ -n "$header" ]; then
        response=$(curl -s --max-time 10 -w "\n%{http_code}" "$url" -H "$header" 2>/dev/null)
    else
        response=$(curl -s --max-time 10 -w "\n%{http_code}" "$url" 2>/dev/null)
    fi
    
    http_code=$(echo "$response" | tail -1)
    body=$(echo "$response" | sed '$d')
    
    if [ "$http_code" = "000" ]; then
        echo -e "${RED}❌ 不可达 (timeout)${NC}"
    elif [ "$http_code" = "401" ] || [ "$http_code" = "403" ]; then
        echo -e "${GREEN}✅ 端点可达 (HTTP $http_code - 需要API Key)${NC}"
    elif [ "$http_code" = "200" ] || [ "$http_code" = "404" ]; then
        echo -e "${GREEN}✅ 端点可达 (HTTP $http_code)${NC}"
    else
        echo -e "${YELLOW}⚠️  HTTP $http_code${NC}"
    fi
}

echo "=== 国内平台 ==="
test_endpoint "智谱AI (GLM)" "https://open.bigmodel.cn/api/paas/v4/models" "Authorization: Bearer test"
test_endpoint "DeepSeek" "https://api.deepseek.com/v1/models" "Authorization: Bearer test"
test_endpoint "硅基流动 SiliconCloud" "https://api.siliconflow.cn/v1/models" "Authorization: Bearer test"
test_endpoint "阿里百炼 DashScope" "https://dashscope.aliyuncs.com/compatible-mode/v1/models" "Authorization: Bearer test"
test_endpoint "Kimi Moonshot" "https://api.moonshot.cn/v1/models" "Authorization: Bearer test"
test_endpoint "腾讯混元" "https://api.hunyuan.cloud.tencent.com/v1/models" "Authorization: Bearer test"
test_endpoint "Agnes AI" "https://apihub.agnes-ai.com/v1/models" "Authorization: Bearer test"
test_endpoint "MiniMax" "https://api.minimax.chat/v1/models" "Authorization: Bearer test"

echo ""
echo "=== 海外平台 ==="
test_endpoint "Google Gemini" "https://generativelanguage.googleapis.com/v1beta/models" ""
test_endpoint "Groq" "https://api.groq.com/openai/v1/models" "Authorization: Bearer test"
test_endpoint "OpenRouter" "https://openrouter.ai/api/v1/models" "Authorization: Bearer test"
test_endpoint "Together AI" "https://api.together.xyz/v1/models" ""
test_endpoint "Cohere" "https://api.cohere.ai/v1/models" ""
test_endpoint "Cerebras" "https://api.cerebras.ai/v1/models" "Authorization: Bearer test"
test_endpoint "Fireworks AI" "https://api.fireworks.ai/inference/v1/models" "Authorization: Bearer test"
test_endpoint "Mistral" "https://api.mistral.ai/v1/models" "Authorization: Bearer test"
test_endpoint "HuggingFace" "https://api-inference.huggingface.co/models" "Authorization: Bearer test"

echo ""
echo "=== 专用能力 ==="
test_endpoint "Noiz.ai" "https://api.noiz.ai/v1" "Authorization: Bearer test"

echo ""
echo "=========================================="
echo "  测试完成"
echo "=========================================="
