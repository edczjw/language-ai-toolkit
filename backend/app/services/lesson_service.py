from typing import Dict, Any
from .ai_service import AIService

class LessonService:
    def __init__(self):
        self.ai_service = AIService()
    
    def create_lesson(self, topic: str, level: str) -> Dict[str, Any]:
        """创建课程内容"""
        return self.ai_service.generate_teaching_material(topic, level)
    
    def generate_exercise(self, params: Dict[str, str]) -> Dict[str, Any]:
        """生成练习题"""
        topic = params.get('topic', '')
        level = params.get('level', 'intermediate')
        
        # 使用 AI 服务生成练习题
        return self.ai_service.generate_teaching_material(
            topic=topic,
            level=level
        )
    
    def get_lesson(self, lesson_id: str) -> Dict[str, Any]:
        """获取特定课程内容"""
        # TODO: 实现从数据库获取课程的逻辑
        return {
            "id": lesson_id,
            "content": "示例课程内容",
            "level": "intermediate",
            "status": "success"
        } 