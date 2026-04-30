# 智能客服工单自动处理系统

基于多 Agent 协作 + 长链推理的客服自动化示例。

## 特性
- 分类 Agent：意图识别 + 置信度打分
- 检索 Agent：从知识库召回答案
- 生成 Agent：个性化回复
- 长链推理：置信度低于阈值时调用外部订单 API 重新决策

## 运行
```bash
pip install -r requirements.txt
python main.py
