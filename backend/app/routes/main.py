from flask import Blueprint, request, jsonify
from ..services.ai_service import AIService
from ..services.lesson_service import LessonService

main = Blueprint('main', __name__)

@main.route('/api/analyze-text', methods=['POST'])
def analyze_text():
    """分析学生提交的文本，返回语法纠正和建议"""
    text = request.json.get('text')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    ai_service = AIService()
    analysis = ai_service.analyze_text(text)
    return jsonify(analysis)

@main.route('/api/generate-exercise', methods=['POST'])
def generate_exercise():
    """根据教学目标生成练习题"""
    params = request.json
    if not params or 'topic' not in params:
        return jsonify({"error": "No topic provided"}), 400
    
    lesson_service = LessonService()
    exercise = lesson_service.generate_exercise(params)
    return jsonify(exercise)

@main.route('/test', methods=['GET'])
def test():
    """测试路由"""
    return jsonify({
        "status": "success",
        "message": "API服务正常运行"
    })

@main.route('/api/generate-teaching-plan', methods=['POST'])
def generate_teaching_plan():
    """生成教学计划"""
    params = request.json
    if not params or 'subject' not in params:
        return jsonify({"error": "No subject provided"}), 400
    
    ai_service = AIService()
    plan = ai_service.generate_teaching_plan(
        subject=params.get('subject'),
        level=params.get('level', 'intermediate'),
        duration=params.get('duration', '一学期')
    )
    return jsonify(plan)

@main.route('/api/translate', methods=['POST'])
def translate():
    """文本翻译"""
    params = request.json
    if not params or 'text' not in params:
        return jsonify({"error": "No text provided"}), 400
    
    ai_service = AIService()
    translation = ai_service.translate_text(
        text=params.get('text'),
        target_lang=params.get('target_lang', '中文')
    )
    return jsonify(translation) 