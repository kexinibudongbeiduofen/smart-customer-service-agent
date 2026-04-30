class GeneratorAgent:
    """生成 Agent：根据检索结果和额外信息生成最终回复"""
    
    def generate(self, intent: str, retrieved_answer: str, extra_info: dict = None) -> str:
        if extra_info and "order_status" in extra_info:
            # 如果有订单信息，添加到回复中
            order = extra_info["order_status"]
            return (f"我查询到您的订单 {order.get('order_id', '')} 当前状态为：{order.get('status', '未知')}，"
                    f"金额：{order.get('amount', 0)} 元。\n{retrieved_answer}")
        else:
            return retrieved_answer
