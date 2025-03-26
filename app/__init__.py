import os
from flask import Flask
from config import Config
from flask_cors import CORS

def create_app():

    app = Flask(__name__, static_url_path='/static', static_folder='static')
    CORS(app, resources={
        r"/*": {
            "origins": "*",
            "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"],
            "expose_headers": ["Content-Type", "Authorization"],
            "supports_credentials": True
        }
    })
    
    app.config.from_object(Config)
    
     # 确保上传目录存在
    os.makedirs(os.path.join(app.static_folder, 'uploads', 'html'), exist_ok=True)
    
    from app.routes import bp
    app.register_blueprint(bp)
    
    return app