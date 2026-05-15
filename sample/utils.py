"""
工具模块 —— 被测试程序
包含：计算器、字符串校验、简单数据结构
"""


class Calculator:
    """基础计算器，支持四则运算"""

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b

    @staticmethod
    def power(base, exp):
        if exp < 0:
            raise ValueError("暂不支持负指数")
        return base ** exp


class StringValidator:
    """字符串校验工具"""

    @staticmethod
    def is_valid_email(email):
        if not email or "@" not in email:
            return False
        local, domain = email.rsplit("@", 1)
        if not local or not domain:
            return False
        if "." not in domain:
            return False
        return True

    @staticmethod
    def is_valid_phone(phone):
        if not phone:
            return False
        # 中国大陆手机号：1开头，11位数字
        return len(phone) == 11 and phone.startswith("1") and phone.isdigit()

    @staticmethod
    def password_strength(pwd):
        """返回密码强度: 0=弱, 1=中, 2=强"""
        if not pwd or len(pwd) < 6:
            return 0
        has_digit = any(c.isdigit() for c in pwd)
        has_alpha = any(c.isalpha() for c in pwd)
        has_special = any(not c.isalnum() for c in pwd)
        if len(pwd) >= 8 and has_digit and has_alpha and has_special:
            return 2
        if has_digit and has_alpha:
            return 1
        return 0

    @staticmethod
    def truncate(text, max_len):
        if not text:
            return ""
        if max_len <= 0:
            raise ValueError("max_len 必须大于0")
        if len(text) <= max_len:
            return text
        return text[:max_len] + "..."


class Stack:
    """简单栈实现"""

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("栈为空，无法弹出")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("栈为空，无法查看")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)
