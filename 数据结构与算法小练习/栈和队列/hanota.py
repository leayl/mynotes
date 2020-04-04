"""
汉诺塔问题
"""
from 数据结构与算法小练习.栈和队列.stack_bin2dec import Stack


def hanota(n, x, y, z):
    """
    实现汉诺塔,实现将x上的n个盘子依靠y移动到z上，
    每次移动一个盘子，最终z上盘子顺序同x最初一样
          |             |            |
         _|_            |            |
        __|__           |            |
       ___|___          |            |
      ____|____         |            |
          x             y            z

    :param n:汉诺塔层数
    :return: 打印移动顺序
    """
    if n == 1:
        print(f"{x}-->{z}")
    else:
        hanota(n - 1, x, z, y)
        print(f"{x}-->{z}")
        hanota(n - 1, y, x, z)


if __name__ == '__main__':
    hanota(3, "x", "y", "z")
