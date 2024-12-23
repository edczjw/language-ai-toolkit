from flask import Flask, Blueprint, request, jsonify
from flask_cors import CORS
import requests
from typing import Dict, Any

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# 配置
class Config:
    KIMI_API_KEY = "sk-PB5AvB1Ndd2E0thBvwtqnPPYPoRtO3h7By4Ph36JOpe9JfcX"
    DEBUG = True

app.config.from_object(Config)

# AI服务
class AIService:
    # ... (之前的 AIService 代码)
    pass

# 路由
@app.route('/test', methods=['GET'])
def test():
    return jsonify({
        "status": "success",
        "message": "API服务正常运行"
    })

@app.route('/api/analyze-text', methods=['POST'])
def analyze_text():
    text = request.json.get('text')
    ai_service = AIService()
    analysis = ai_service.analyze_text(text)
    return jsonify(analysis)

if __name__ == '__main__':
    app.run(debug=True, port=8000) 