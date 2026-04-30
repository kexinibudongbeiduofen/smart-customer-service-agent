import re

class ClassifierAgent:
    """意图分类 Agent，返回意图和置信度"""
    
    def __init__(self):
        self.intent_keywords = {
            "密码重置": ["密码", "忘记密码", "重置密码", "登录不了"],
            "账单查询": ["账单", "消费", "扣费", "花了多少钱", "费用"],
            "功能使用指引": ["怎么用", "功能", "操作", "使用教程", "帮助"],
            "退款问题": ["退款", "退货", "钱退回来", "申请退款"]
        }
    
    def classify(self, user_message: str):
        """返回 (intent, confidence)"""
        user_lower = user_message.lower()
        best_intent = "未知"
        best_score = 0.0
        
        for intent, keywords in self.intent_keywords.items():
            score = sum(1 for kw in keywords if kw in user_lower) / len(keywords)
            # 简单加权：如果直接完全匹配关键词，提高分数
            if any(kw in user_lower for kw in keywords):
                score = min(score + 0.3, 1.0)
            if score > best_score:
                best_score = score
                best_intent = intent
        
        # 如果没有匹配到任何关键词，置信度很低
        if best_score == 0:
            best_intent = "未知"
            best_score = 0.1
        
        return best_intent, best_score
