# 每日知识推送机器人

基于GitHub Actions的自动化知识推送系统，每天定时发送多种知识内容到邮箱。

## 功能特点
- 📰 新闻摘要
- 🗣️ 英语学习
- 🔧 编程技巧
- 📚 书籍推荐
- 💫 励志名言

## 使用方法
1. 配置Secrets（邮箱信息）
2. 系统会自动每天上午9点运行
3. 在邮箱查收知识摘要

## 配置说明
需要在GitHub Secrets中设置以下环境变量：
- EMAIL_SENDER：发送邮箱
- EMAIL_PASSWORD：邮箱SMTP授权码  
- EMAIL_RECEIVER：接收邮箱
