import random
import sys
import time
from typing import List, Set


def fun(*, a=1, b=1, c=1):
    return a + b + c


def fun2(*args, **kwargs):
    pass


def f1(a, b, *args, c, **kwargs):
    # 参数传递
    print(a, b, c)
    print(args)
    print(kwargs)


def f2(n: int):
    """递归实现阶乘"""
    if n == 1:
        return 1
    return n * f2(n - 1)


def f_map(func: callable, *args):
    return map(func, *args)


def f_filter(l):
    return filter(lambda val: val > 2, l)


class MyClass:
    instance_counter = 0

    def base(self):
        print("father class base")


class MyChildClass(MyClass):
    def base(self):
        print("child class base")
        # super(__class__, self).base()  # 访问父类的方法


class A:
    def test(self):
        print("A")


class B(A):
    def test(self):
        print("B")


class C(A):
    def test(self):
        print("C")


class D(B, C):
    def test(self):
        print("D")


class MyInt:
    def __init__(self, n: int):
        self.data = n

    def __repr__(self):
        return f"my int {self.data}"

    def __int__(self):
        return int(self.data)


# 展开嵌套列表
def expand_list(l: list, out_l=None):
    if out_l is None:
        out_l = []
    for i in l:
        if isinstance(i, list):
            expand_list(i, out_l)
        else:
            out_l.append(i)
    return out_l


# 一个球从100米高空落下，每次落下后反弹高度是原高度的一半
# #     1)算出皮球在第10次落下后反弹的高度是多少
# #     2)打印出球共经历了多少米的路程
def ball_height(times: int):
    if times == 1:
        return 100 * 0.5
    return ball_height(times - 1) * 0.5


def ball_path(times: int):
    if times == 1:
        return 100 * 1.5
    return ball_path(times - 1) + ball_height(times - 1) * 1.5


# 分解质因数
# 判断是否质数
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# 分解质因数
def prime_factors(n: int, l: List[int]):
    if is_prime(n):
        l.append(n)
        return
    for i in range(2, n):
        if n % i == 0:
            # 这里使用return是因为避免重复查找，如6=2*3,i = 2找到后会递归查找n // i(即3)，return后不会再继续循环到i=3，避免重复
            return prime_factors(i, l), prime_factors(n // i, l),


if __name__ == '__main__':
    n = 100
    l = []
    prime_factors(n, l)
    print(l)

    # ball_times = 2
    # print(ball_height(ball_times))
    # print(ball_path(ball_times))
    # l = [[1, 2, 3], 4, [5, 6, [7, 8, [9]]]]
    # print(expand_list(l))
    # a = MyInt(10)
    # b = int(a)
    # print(type(a))
    # print(str(a))
    # print(b)
    # print(type(b))
    # # 查看MRO
    # print(D.mro())
    # # d = D()
    # D().test()
    # print(D.__mro__)  # D B C A objict
    # d.m()
    # print(issubclass(C, B))
    # print(issubclass(C, A))
    # c_class = MyChildClass()
    # c_class.base()
    # super(MyChildClass, c_class).base()
    # MyClass.base(c_class)

    # data = fun(a=1, b=2, c=3)
    # print(data)
    # f1(*(1,2,3,4),**{'k1':1,'k2':2,'c':'c3'})
    # print(f2(5))
    # for i in f_map(abs, (1,2,-5)):
    #     print(i, end='\r')
    #     time.sleep(1)
    # print([k for k in f_filter(range(6))])
    # l1 = [1, 34, 5, 63, 4]
    # l2 = sorted(l1, key=lambda x: x % 5)
    # print(l1)
    # print(l2)
    # print(sys.argv)
    ls = [1, 7, 4, 5, 3, 3]
    # random.seed() #如果给了参数，则每次运行本程序时，得到的随机结果一致，便于调试和重复性实验
    # print(random.random())
    # print(random.randint(1,7))
    # print(random.getrandbits(2))
    # print(random.randrange(1,7))
    # print(random.choices(ls,weights=[0.5,0.1,0.1,0.1,0.1,0.1],k=3))
    # print(random.sample(ls,k=3))
    # random.shuffle(ls)
    # print(ls)
    # i= random.randint(1,3)
    # print(i)
    # assert i == 3, '错了'
