#!/bin/bash
# Buffett Wisdom - 查询脚本

SKILL_DIR="$(dirname "$0")/.."
DATA_DIR="$SKILL_DIR/data"

query_year() {
    local year=$1
    local file="$DATA_DIR/letters/${year}.md"
    if [ -f "$file" ]; then
        cat "$file"
    else
        echo "未找到 ${year} 年的数据"
    fi
}

query_holdings() {
    local year=$1
    local quarter=$2
    local file="$DATA_DIR/holdings/${year}-q${quarter}.json"
    if [ -f "$file" ]; then
        cat "$file"
    else
        echo "未找到 ${year}Q${quarter} 的持仓数据"
    fi
}

case "$1" in
    letter)
        query_year "$2"
        ;;
    holdings)
        query_holdings "$2" "$3"
        ;;
    *)
        echo "用法: $0 {letter <年份> | holdings <年份> <季度>}"
        ;;
esac