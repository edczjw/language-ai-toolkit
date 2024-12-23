import requests
from typing import Dict, Any
from ...config import Config

class AIService:
    def __init__(self):
        self.api_key = Config.KIMI_API_KEY
        self.api_url = "https://api.moonshot.cn/v1/chat/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
    def analyze_text(self, text: str) -> Dict[str, Any]:
        """分析学生文本并提供反馈"""
        payload = {
            "model": "moonshot-v1-8k",  # Kimi的模型名称
            "messages": [
                {"role": "system", "content": "你是一位专业的语言教师助手。请用中文回复。"},
                {"role": "user", "content": f"请分析以下文本的语法错误和提供改进建议：\n{text}"}
            ],
            "temperature": 0.7
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            result = response.json()
            
            return {
                "corrections": result["choices"][0]["message"]["content"],
                "difficulty_level": self._assess_difficulty(text),
                "suggestions": self._generate_suggestions(text)
            }
            
        except requests.exceptions.RequestException as e:
            return {
                "error": f"API请求失败: {str(e)}",
                "corrections": None,
                "difficulty_level": None,
                "suggestions": None
            }
    
    def generate_teaching_material(self, topic: str, level: str) -> Dict[str, Any]:
        """生成教学材料"""
        payload = {
            "model": "moonshot-v1-8k",
            "messages": [
                {"role": "system", "content": "你是一位专业的语言教材编写专家。请用中文回复。"},
                {"role": "user", "content": f"请为{level}级别的学生生成关于'{topic}'的教学材料，包含课文和练习题。"}
            ],
            "temperature": 0.8
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            result = response.json()
            
            return {
                "content": result["choices"][0]["message"]["content"],
                "status": "success"
            }
            
        except requests.exceptions.RequestException as e:
            return {
                "error": f"生成教学材料失败: {str(e)}",
                "status": "error"
            }
    
    def _assess_difficulty(self, text: str) -> int:
        """评估文本难度等级"""
        # 使用Kimi API评估文本难度
        payload = {
            "model": "moonshot-v1-8k",
            "messages": [
                {"role": "system", "content": "你是一位语言难度评估专家。请用1-5的数字表示文本难度。"},
                {"role": "user", "content": f"请评估以下文本的难度等级(1最简单，5最难)：\n{text}"}
            ],
            "temperature": 0.3
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            result = response.json()
            difficulty_text = result["choices"][0]["message"]["content"]
            # 提取数字
            return int(difficulty_text[0]) if difficulty_text[0].isdigit() else 3
            
        except:
            return 3  # 默认中等难度
    
    def _generate_suggestions(self, text: str) -> list:
        """生成改进建议"""
        payload = {
            "model": "moonshot-v1-8k",
            "messages": [
                {"role": "system", "content": "你是一位语言教学专家。请提供具体的改进建议，用列表形式返回。"},
                {"role": "user", "content": f"请为以下文本提供3-5条改进建议：\n{text}"}
            ],
            "temperature": 0.7
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            result = response.json()
            suggestions = result["choices"][0]["message"]["content"].split("\n")
            return [s.strip("- ") for s in suggestions if s.strip()]
            
        except:
            return ["无法生成建议"]
    
    def generate_teaching_plan(self, subject: str, level: str, duration: str) -> Dict[str, Any]:
        """生成教学计划"""
        payload = {
            "model": "moonshot-v1-8k",
            "messages": [
                {"role": "system", "content": "你是一位专业的教育课程规划专家。请用中文回复。"},
                {"role": "user", "content": f"请为{level}级别的学生制定一个{duration}的{subject}教学计划，包含学习目标、教学重点、课程安排和考核方式。"}
            ],
            "temperature": 0.7
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            result = response.json()
            
            return {
                "content": result["choices"][0]["message"]["content"],
                "status": "success"
            }
        except requests.exceptions.RequestException as e:
            return {
                "error": f"生成教学计划失败: {str(e)}",
                "status": "error"
            }
    
    def translate_text(self, text: str, target_lang: str) -> Dict[str, Any]:
        """文本翻译"""
        payload = {
            "model": "moonshot-v1-8k",
            "messages": [
                {"role": "system", "content": "你是一位专业的翻译专家。请准确翻译以下内容，保持原文风格和语气。"},
                {"role": "user", "content": f"请将以下文本翻译成{target_lang}：\n{text}"}
            ],
            "temperature": 0.3
        }
        
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json=payload
            )
            response.raise_for_status()
            result = response.json()
            
            return {
                "translation": result["choices"][0]["message"]["content"],
                "source_text": text,
                "target_language": target_lang,
                "status": "success"
            }
        except requests.exceptions.RequestException as e:
            return {
                "error": f"翻译失败: {str(e)}",
                "status": "error"
            }