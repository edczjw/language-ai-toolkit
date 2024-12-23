from flask import Flask, send_from_directory
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='')
    
    # 允许所有域名访问
    CORS(app, resources={
        r"/*": {
            "origins": "*",
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })
    
    # 配置应用
    app.config.from_object('config.Config')
    
    # 导入并注册蓝图
    from .routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # 添加根路由来提供静态文件
    @app.route('/')
    def serve_index():
        return app.send_static_file('index.html')
    
    return app