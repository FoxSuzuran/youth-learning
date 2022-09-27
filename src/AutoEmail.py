import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_sender = os.environ.get("mail_sender")  # 用户名
mail_pass = os.environ.get("mail_pass")  # 口令

receivers = [os.environ.get("mail_receiver")]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText("青年大学习自动学习出现问题", "plain", "utf-8")

message["From"] = Header("铃兰", "utf-8")

subject = "GitHub青年大学习"
message["Subject"] = Header(subject, "utf-8")


def EmailSend():
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 465为QQ SMTP端口号
        smtpObj.login(mail_sender, mail_pass)
        smtpObj.sendmail(mail_sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
    finally:
        smtpObj.quit()

