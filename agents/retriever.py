import json

class RetrieverAgent:
    """检索 Agent：从知识库中查找最相关的答案"""
    
    def __init__(self, kb_path="knowledge_base.json"):
        with open(kb_path, 'r', encoding='utf-8') as f:
            self.kb = json.load(f)
    
    def retrieve(self, intent: str) -> tuple:
        """返回 (答案文本, 置信度)"""
        if intent in self.kb:
            return self.kb[intent], 0.9
        else:
            return "抱歉，我暂时无法回答这个问题，将为您转接人工客服。", 0.3
