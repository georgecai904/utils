import os
from dotenv import load_dotenv
import pathlib

# 获取当前文件的目录
BASE_DIR = pathlib.Path(__file__).parent

# 加载.env文件，指定具体路径
load_dotenv(BASE_DIR / '.env')

class Config:
    # Flask配置
    SECRET_KEY = os.getenv('SECRET_KEY')
    
    # 邮件服务器配置
    SMTP_SERVER = os.getenv('SMTP_SERVER')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 465))  # QQ邮箱使用465端口
    SMTP_USERNAME = os.getenv('SMTP_USERNAME')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
    MAIL_DEVELOPER = os.getenv('MAIL_DEVELOPER')
    
    BASE_URL = os.getenv('BASE_URL')  # 根据实际部署环境修改
    STATIC_URL_PATH = '/static'  # 静态文件URL路径
    STATIC_FOLDER = 'static'     # 静态文件夹路径
    
    # print("当前配置：", {
    #     "SMTP_SERVER": SMTP_SERVER,
    #     "SMTP_PORT": SMTP_PORT,
    #     "SMTP_USERNAME": SMTP_USERNAME,
    #     "SMTP_PASSWORD": SMTP_PASSWORD,
    #     "MAIL_DEVELOPER": MAIL_DEVELOPER
    # })
