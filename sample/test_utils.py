"""
测试文件 —— utils.py 的单元测试
覆盖: Calculator, StringValidator, Stack 类的所有方法
设计方法: 等价类划分 + 边界值分析 + 分支覆盖 + 异常测试
"""
import pytest
import sys
import os

# 将被测模块所在目录加入路径
sys.path.insert(0, os.path.dirname(__file__))
from utils import Calculator, StringValidator, Stack


# ==================== Calculator 测试 ====================

class TestCalculatorAdd:
    """add(a, b) 测试"""

    def test_add_positive(self):
        assert Calculator.add(2, 3) == 5

    def test_add_negative(self):
        assert Calculator.add(-2, -3) == -5

    def test_add_zero(self):
        assert Calculator.add(5, 0) == 5
        assert Calculator.add(0, 0) == 0

    def test_add_large_numbers(self):
        assert Calculator.add(999999, 1) == 1000000


class TestCalculatorSubtract:
    """subtract(a, b) 测试"""

    def test_subtract_positive_result(self):
        assert Calculator.subtract(5, 2) == 3

    def test_subtract_negative_result(self):
        assert Calculator.subtract(2, 5) == -3

    def test_subtract_zero(self):
        assert Calculator.subtract(5, 5) == 0


class TestCalculatorMultiply:
    """multiply(a, b) 测试"""

    def test_multiply_positive(self):
        assert Calculator.multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert Calculator.multiply(100, 0) == 0

    def test_multiply_negative(self):
        assert Calculator.multiply(-3, 4) == -12


class TestCalculatorDivide:
    """divide(a, b) 测试"""

    def test_divide_normal(self):
        assert Calculator.divide(10, 2) == 5.0

    def test_divide_result_float(self):
        assert Calculator.divide(10, 3) == pytest.approx(3.333, 0.001)

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="除数不能为零"):
            Calculator.divide(10, 0)

    def test_divide_zero_by_number(self):
        assert Calculator.divide(0, 5) == 0.0

    def test_divide_negative(self):
        assert Calculator.divide(-10, 2) == -5.0


class TestCalculatorPower:
    """power(base, exp) 测试"""

    def test_power_normal(self):
        assert Calculator.power(2, 3) == 8

    def test_power_zero_exp(self):
        assert Calculator.power(5, 0) == 1

    def test_power_one_exp(self):
        assert Calculator.power(7, 1) == 7

    def test_power_negative_exp_raises(self):
        with pytest.raises(ValueError, match="暂不支持负指数"):
            Calculator.power(2, -1)

    def test_power_zero_base(self):
        assert Calculator.power(0, 5) == 0


# ==================== StringValidator 测试 ====================

class TestStringValidatorEmail:
    """is_valid_email(email) 测试"""

    @pytest.mark.parametrize("email,expected", [
        ("test@example.com", True),           # 正常
        ("user.name@domain.co", True),        # 含点号
        ("a@b.cn", True),                     # 短域名
        ("", False),                          # 空字符串
        ("notanemail", False),                # 无@
        ("@nodomain.com", False),             # 无本地部分
        ("nolocal@nodot", False),             # 域名无点
        ("@.", False),                        # 仅特殊字符
    ])
    def test_is_valid_email(self, email, expected):
        assert StringValidator.is_valid_email(email) == expected


class TestStringValidatorPhone:
    """is_valid_phone(phone) 测试"""

    @pytest.mark.parametrize("phone,expected", [
        ("13800138000", True),                # 正常手机号
        ("19912345678", True),                # 新号段
        ("12345678901", True),                # 不同前缀
        ("", False),                          # 空字符串
        ("12345", False),                     # 长度不足
        ("123456789012", False),              # 长度超出
        ("23800138000", False),               # 非1开头
        ("1380013800a", False),               # 含字母
    ])
    def test_is_valid_phone(self, phone, expected):
        assert StringValidator.is_valid_phone(phone) == expected


class TestStringValidatorPassword:
    """password_strength(pwd) 测试"""

    @pytest.mark.parametrize("pwd,expected_level", [
        ("abc123!@", 2),                      # 强: >=8 + 数字 + 字母 + 特殊
        ("Pass123!", 2),                      # 强
        ("abc12345", 1),                      # 中: >=6 + 数字 + 字母
        ("abcdefg", 0),                       # 弱: 仅字母
        ("123456", 0),                        # 弱: 仅数字 (长度=6)
        ("ab12", 0),                          # 弱: 太短 (<6)
        ("", 0),                              # 弱: 空
    ])
    def test_password_strength(self, pwd, expected_level):
        assert StringValidator.password_strength(pwd) == expected_level

    def test_password_strength_edge_six_chars_alpha_digit(self):
        """边界: 刚好6位, 数字+字母 → 中"""
        assert StringValidator.password_strength("abc123") == 1


class TestStringValidatorTruncate:
    """truncate(text, max_len) 测试"""

    def test_truncate_shorter_than_max(self):
        assert StringValidator.truncate("hello", 10) == "hello"

    def test_truncate_exactly_max(self):
        assert StringValidator.truncate("hello", 5) == "hello"

    def test_truncate_longer_than_max(self):
        assert StringValidator.truncate("hello world", 5) == "hello..."

    def test_truncate_empty(self):
        assert StringValidator.truncate("", 5) == ""

    def test_truncate_max_len_zero_raises(self):
        with pytest.raises(ValueError, match="max_len 必须大于0"):
            StringValidator.truncate("hello", 0)

    def test_truncate_max_len_negative_raises(self):
        with pytest.raises(ValueError, match="max_len 必须大于0"):
            StringValidator.truncate("hello", -1)


# ==================== Stack 测试 ====================

class TestStack:
    """Stack 完整测试"""

    def test_push_and_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        assert s.pop() == 2
        assert s.pop() == 1

    def test_push_and_peek(self):
        s = Stack()
        s.push("item")
        assert s.peek() == "item"
        assert s.size() == 1       # peek 不移除

    def test_is_empty_initial(self):
        assert Stack().is_empty() is True

    def test_is_empty_after_push(self):
        s = Stack()
        s.push(1)
        assert s.is_empty() is False

    def test_size_empty(self):
        assert Stack().size() == 0

    def test_size_after_operations(self):
        s = Stack()
        s.push("a")
        s.push("b")
        s.push("c")
        assert s.size() == 3
        s.pop()
        assert s.size() == 2

    def test_pop_empty_raises(self):
        with pytest.raises(IndexError, match="栈为空，无法弹出"):
            Stack().pop()

    def test_peek_empty_raises(self):
        with pytest.raises(IndexError, match="栈为空，无法查看"):
            Stack().peek()

    def test_multiple_types(self):
        """栈应支持任意类型"""
        s = Stack()
        s.push(42)
        s.push("str")
        s.push(None)
        assert s.pop() is None
        assert s.pop() == "str"
        assert s.pop() == 42

    def test_large_volume(self):
        """压力测试: 1000 次 push/pop"""
        s = Stack()
        for i in range(1000):
            s.push(i)
        assert s.size() == 1000
        for i in range(999, -1, -1):
            assert s.pop() == i
        assert s.is_empty()
