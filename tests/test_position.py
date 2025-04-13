# tests/test_position.py
import pytest
from src.position import calculate_position_value, calculate_delta

@pytest.mark.parametrize("shares,price,expected", [
    (100, 50, 5000),      # 正常場景
    (0, 50, 0),           # 邊界：零持倉
    (100, 0, 0),          # 邊界：零價格
])
def test_calculate_position_value(shares, price, expected):
    """測試持倉價值計算"""
    assert calculate_position_value(shares, price) == expected

def test_position_value_negative_shares():
    """測試異常：負持倉"""
    with pytest.raises(ValueError):
        calculate_position_value(-100, 50)

def test_position_value_negative_price():
    """測試異常：負價格"""
    with pytest.raises(ValueError):
        calculate_position_value(100, -50)

def test_calculate_delta_above_strike():
    """測試Delta：價格高於行權價"""
    assert calculate_delta(110, 100) == 0.5

def test_calculate_delta_below_strike():
    """測試Delta：價格低於行權價"""
    assert calculate_delta(90, 100) == 0.4