# 模拟外部订单查询 API
def get_order_status(order_id: str) -> dict:
    # 模拟数据
    mock_orders = {
        "ORD123": {"status": "已发货", "amount": 299.0},
        "ORD456": {"status": "退款中", "amount": 89.9},
    }
    return mock_orders.get(order_id, {"status": "未知订单", "amount": 0})
