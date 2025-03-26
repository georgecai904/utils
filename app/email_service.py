import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import current_app

def send_email(to, subject, body):
    """
    使用SMTP发送邮件的函数
    
    参数:
        to (str): 收件人邮箱
        subject (str): 邮件主题
        body (str): 邮件内容
    """
    # 创建邮件对象
    msg = MIMEMultipart()
    msg['From'] = current_app.config['SMTP_USERNAME']
    msg['To'] = to
    msg['Subject'] = subject
    
    # 添加邮件正文
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
    try:
        # 连接SMTP服务器
        server = smtplib.SMTP_SSL(current_app.config['SMTP_SERVER'], 
                                current_app.config['SMTP_PORT'])  # 使用SMTP_SSL
        
        # 登录
        server.login(current_app.config['SMTP_USERNAME'],
                    current_app.config['SMTP_PASSWORD'])
        
        # 发送邮件
        server.send_message(msg)
        
        # 关闭连接
        server.quit()
        
    except Exception as e:
        print(f"发送邮件时出错: {str(e)}")  # 添加错误打印
        raise Exception(f"发送邮件失败: {str(e)}") 