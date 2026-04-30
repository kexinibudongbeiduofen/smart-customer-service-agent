from agents.classifier import ClassifierAgent
from agents.retriever import RetrieverAgent
from agents.generator import GeneratorAgent
from external_api import get_order_status

class CustomerServiceOrchestrator:
    """主控器：协调多 Agent，实现长链推理"""
    
    def __init__(self):
        self.classifier = ClassifierAgent()
        self.retriever = RetrieverAgent()
        self.generator = GeneratorAgent()
        self.confidence_threshold = 0.4   # 低于此阈值触发二次确认
    
    def extract_order_id(self, message: str) -> str or None:
        """简单提取消息中的订单号（格式 ORD+数字）"""
        import re
        match = re.search(r'ORD\d+', message)
        return match.group(0) if match else None
    
    def process_message(self, user_message: str) -> str:
        # Step 1: 分类
        intent, confidence = self.classifier.classify(user_message)
        print(f"[分类Agent] 意图={intent}, 置信度={confidence:.2f}")
        
        extra_info = None
        
        # 长链推理：置信度低于阈值，触发二次确认（调用外部 API）
        if confidence < self.confidence_threshold:
            print("[长链推理] 置信度过低，尝试获取订单信息...")
            order_id = self.extract_order_id(user_message)
            if order_id:
                order_status = get_order_status(order_id)
                if order_status and order_status.get("status") != "未知订单":
                    extra_info = {"order_status": {**order_status, "order_id": order_id}}
                    # 重新分类：如果订单状态包含“退款”，则修正为退款问题
                    if "退款" in order_status.get("status", ""):
                        intent = "退款问题"
                        confidence = 0.8
                        print(f"[推理修正] 根据订单状态，将意图改为 '{intent}'")
            else:
                print("[长链推理] 未找到订单号，保持原意图")
        
        # Step 2: 检索
        answer, ret_conf = self.retriever.retrieve(intent)
        print(f"[检索Agent] 检索到答案 (置信度={ret_conf:.2f})")
        
        # Step 3: 生成
        final_response = self.generator.generate(intent, answer, extra_info)
        print(f"[生成Agent] 最终回复: {final_response[:50]}...")
        
        return final_response

# 命令行交互示例
if __name__ == "__main__":
    bot = CustomerServiceOrchestrator()
    print("智能客服 Agent 已启动（输入 'exit' 退出）")
    while True:
        msg = input("\n用户: ")
        if msg.lower() == 'exit':
            break
        response = bot.process_message(msg)
        print(f"客服: {response}")
