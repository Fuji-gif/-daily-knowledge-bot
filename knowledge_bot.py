import os
import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import random

class KnowledgeBot:
    def __init__(self):
        # 从环境变量获取配置（GitHub Secrets）
        self.email_sender = os.getenv('EMAIL_SENDER')
        self.email_password = os.getenv('EMAIL_PASSWORD')
        self.email_receiver = os.getenv('EMAIL_RECEIVER')
        self.news_api_key = os.getenv('NEWS_API_KEY', '')
        
    def get_daily_news(self):
        """获取每日新闻摘要"""
        try:
            return self.get_simple_news()
        except Exception as e:
            return f"📰 新闻获取失败：{str(e)}"
    
    def get_simple_news(self):
        """简单新闻内容（避免API依赖）"""
        news_list = [
            "科技行业持续关注AI发展新趋势",
            "全球气候变化议题引发广泛讨论", 
            "数字化转型推动各行业创新变革",
            "教育科技为学习方式带来新可能",
            "远程办公模式逐渐成为新常态"
        ]
        selected = random.sample(news_list, 3)
        return "📰 今日热点：\n" + "\n".join([f"• {item}" for item in selected])
    
    def get_english_lesson(self):
        """获取每日英语学习内容"""
        try:
            # 从免费API获取英语名言
            response = requests.get('https://api.quotable.io/random', timeout=10)
            quote_data = response.json()
            english_quote = f"\"{quote_data['content']}\" - {quote_data['author']}"
            
            tips = [
                "💡 学习建议：尝试用这个句子造一个新的英文句子",
                "💡 记忆技巧：把这个句子读三遍，然后尝试背诵",
                "💡 扩展学习：查找这句话中不熟悉的单词"
            ]
            tip = random.choice(tips)
            
            return f"🗣️ 每日英语：\n{english_quote}\n\n{tip}"
        except Exception:
            # 备用英语内容
            quotes = [
                "The only way to do great work is to love what you do. - Steve Jobs",
                "It does not matter how slowly you go as long as you do not stop. - Confucius",
                "Life is what happens to you while you're busy making other plans. - John Lennon"
            ]
            return f"🗣️ 每日英语：\n{random.choice(quotes)}"
    
    def get_tech_tips(self):
        """获取编程技巧"""
        tech_tips = [
            "💻 Python技巧：使用 f-string 格式化字符串，更简洁高效",
            "💻 Git技巧：使用 `git commit --amend` 修改最近一次提交",
            "💻 调试技巧：使用 print 调试时，添加有意义的标识符",
            "💻 代码优化：尽量避免深层嵌套，使用早返回(early return)",
            "💻 学习资源：多阅读优秀开源项目的代码",
            "💻 工具推荐：使用 VS Code 的代码片段功能提高编码效率"
        ]
        return f"🔧 编程技巧：\n{random.choice(tech_tips)}"
    
    def get_book_recommendation(self):
        """获取书籍推荐"""
        books = [
            "📚 《深入理解计算机系统》- 计算机科学经典",
            "📚 《代码大全》- 软件构建的实用指南", 
            "📚 《设计模式》- 可复用面向对象软件的基础",
            "📚 《算法导论》- 算法学习的权威教材",
            "📚 《重构》- 改善既有代码的设计"
        ]
        return f"📖 今日书籍推荐：\n{random.choice(books)}"
    
    def get_motivational_quote(self):
        """获取励志名言"""
        quotes = [
            "🌟 成功的秘诀在于对目标的执着追求",
            "🌟 今天是你余生中最年轻的一天，好好利用",
            "🌟 学习不是填充水桶，而是点燃火焰",
            "🌟 代码写出来是给人看的，只是顺带让机器执行",
            "🌟 最好的时机是十年前，其次是现在"
        ]
        return f"💫 励志名言：\n{random.choice(quotes)}"
    
    def compile_daily_digest(self):
        """编译每日知识摘要"""
        current_date = datetime.now().strftime('%Y年%m月%d日')
        
        digest = f"""🌅 每日知识摘要 - {current_date}

{self.get_daily_news()}

{self.get_english_lesson()}

{self.get_tech_tips()}

{self.get_book_recommendation()}

{self.get_motivational_quote()}

---
📊 知识就是力量，每天进步一点点！
此邮件由GitHub Actions自动生成
"""
        return digest
    
    def send_email(self, subject, content):
        """发送邮件"""
        try:
            # 配置邮件
            msg = MIMEMultipart()
            msg['From'] = self.email_sender
            msg['To'] = self.email_receiver
            msg['Subject'] = subject
            
            # 添加邮件内容
            msg.attach(MIMEText(content, 'plain', 'utf-8'))
            
            # 发送邮件（QQ邮箱SMTP）
            server = smtplib.SMTP_SSL('smtp.qq.com', 465)
            server.login(self.email_sender, self.email_password)
            server.send_message(msg)
            server.quit()
            
            print("邮件发送成功！")
            return True
        except Exception as e:
            print(f"邮件发送失败：{e}")
            return False
    
    def run(self):
        """主运行函数"""
        print("开始生成每日知识摘要...")
        
        # 检查环境变量
        if not all([self.email_sender, self.email_password, self.email_receiver]):
            print("❌ 环境变量未设置完整")
            return
        
        # 生成摘要内容
        digest_content = self.compile_daily_digest()
        subject = f"🌅 每日知识摘要 - {datetime.now().strftime('%Y-%m-%d')}"
        
        # 发送邮件
        if self.send_email(subject, digest_content):
            print("每日知识推送完成！")
        else:
            print("推送失败，请检查配置")

if __name__ == "__main__":
    bot = KnowledgeBot()
    bot.run()
