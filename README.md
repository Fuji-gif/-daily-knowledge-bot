# -daily-knowledge-bot
每日知识推送机器人
# 1. 创建隐藏的.github/workflows目录（注意-p后面有空格）
mkdir -p .github/workflows

# 2. 创建主程序文件（一次touch多个文件，不用重复写touch）
touch knowledge_bot.py requirements.txt README.md

# 3. 创建工作流文件（注意是点github，不是下划线）
touch .github/workflows/daily-bot.yml
