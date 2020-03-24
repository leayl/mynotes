import math
import string


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def bin2dec():
    """
    使用栈实现二进制转十进制
    :return:
    """
    stack = Stack()
    strs = input("请输入二进制数：")
    for str_bin in strs:
        stack.push(int(str_bin))
    i = 0
    dec_num = 0
    while not stack.is_empty():
        bin_num = stack.pop()
        dec_num += bin_num * pow(2, i)
        i += 1
    print("转换为10进制为：", dec_num)


def cal(expr):
    """
    逆波兰表达式
    :return:
    """
    stack = Stack()
    expr_list = expr.split()
    for expression in expr_list:
        if expression.isdigit():
            stack.push(expression)
        else:
            num1 = float(stack.pop())
            num2 = float(stack.pop())
            if expression == "+":
                stack.push(num1 + num2)
            elif expression == "-":
                stack.push(num2 - num1)
            elif expression == "*":
                stack.push(num1 * num2)
            elif expression == "/":
                if num1 == 0:
                    print("除数为0！")
                    return
                stack.push(num2 / num1)
    result = stack.pop()
    print("结果为：", result)


def calculate():
    """
    中缀表达式计算器
    :return:
    """
    stack = Stack()
    in_expr = input("请输入计算表达式（按下Enter键提交）：")
    poland_expr = ''
    expr_list = in_expr.split()
    for expr in expr_list:
        if expr.isdigit():
            poland_expr += expr + " "
        elif expr == ")":
            top = stack.pop()
            while top != "(":
                poland_expr += top + " "
                top = stack.pop()
        elif expr == "+" or expr == "-":
            if stack.is_empty():
                stack.push(expr)
            else:
                while not stack.is_empty():
                    top = stack.pop()
                    if top == "(":
                        stack.push("(")
                        break
                    else:
                        poland_expr += top + " "
                stack.push(expr)
        elif expr == "*" or expr == "/" or expr == "(":
            stack.push(expr)
    while not stack.is_empty():
        poland_expr += stack.pop() + " "
    cal(poland_expr)


if __name__ == '__main__':
    # bin2dec()
    # cal()
    calculate()
