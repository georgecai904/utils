from dotenv import load_dotenv
load_dotenv()  # 确保在创建app之前加载环境变量

from app import create_app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True) 