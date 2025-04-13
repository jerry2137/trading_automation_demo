# src/position.py
def calculate_position_value(shares, price):
    """計算持倉價值"""
    if shares < 0 or price < 0:
        raise ValueError("Shares and price must be non-negative")
    return shares * price

def calculate_delta(price, strike):
    """模擬Greeks：簡單Delta計算"""
    # 假設固定Delta（實際會用Black-Scholes模型）
    return 0.5 if price >= strike else 0.4