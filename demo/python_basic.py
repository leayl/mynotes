# 装饰器

from time import sleep
import functools


def dec_temp(sleep_time):
    def decorate(fun):
        @functools.wraps(fun) # 保证被装饰的函数的文档字符串
        def wrapp(*args, **kwargs):
            print('装饰开始')
            ret = fun(*args, **kwargs)
            sleep(sleep_time)
            print('装饰结束')
            return ret
        return wrapp
    return decorate


@dec_temp(1)
def decorated(name, age):
    """
    adfdfdf
    :param name:
    :param age:
    :return:
    """
    print(name, age)
    return name, age


class Fibs:
    num =4
    count = 5
    def __init__(self, num):
        self.a = 0
        self.b = 1
        self.num = num
        self.count = 1
    def __next__(self):
        if self.count > self.num:
            # 还原起点，否则只能迭代一次
            self.a = 0
            self.b = 1
            self.count = 1
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return self.a
    def __iter__(self):
        return self


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            _instance = super().__new__(cls, *args, **kwargs)
            cls._instance = _instance
        return cls._instance

class MyClass(Singleton):
    pass

c1 = MyClass()
c2 = MyClass()
print(c1 is c2) # True

if __name__ == '__main__':

    class mynumber:
        def __init__(self, v):
            self._data = v

        def __repr__(self):
            return 'mynumber(%d)' % self._data
        @property
        def data(self):
            return self._data

        @data.setter
        def data(self, val):
            self._data=val



    n1 = mynumber(100)
    print(n1.data)
    n1.data = 500
    print(n1.data)
    # print(decorated.__doc__)
    # print(__name__)
    # s = decorated('lea', '26')
    # print(s)
    fib = Fibs(10)
    print(fib.__class__.__base__)
    for j in range(3):
        for i in fib:
            print(i, end=' ')
        print()
