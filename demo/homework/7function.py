#1.写一个函数myfun，此函数用于显示两个参数的相关信息的函数：
# def myfun(a, b):
#     此处自己实现
# 此函数给定两个参数，打印关于两个参数的信息：
#     1.打印两个参数的最大值
#     2.打印两个参数的和
#     3.打印两个参数的积
#     4.打印从a到b的所有偶数
# 如：myfun(3, 10)
# 打印如下：
#     最大值是：10
#     和是：13
#     积是：30
#     3到10的偶数是：4 6 8


def myfun(a, b):
    print('%d和%d的最大值是：%d' % (a, b, max(a, b)))
    print('%d和%d的和是：%d' % (a, b, a + b))
    print('%d和%d积是：%d' % (a, b, a * b))
    l = []
    for i in range(a, b):
        if i % 2 == 0:
            l.append(i)
    print('%d到%d的偶数有：' % (a, b), l)
myfun(5, 20)

# 2.猴子吃桃
#     有一只小猴子，摘了很多桃
#         第一天吃了一半 + 1
#         第二天吃了一半 + 1
#         到第十天还剩一个
#         问总共有多少个

#方法一
def peaches(a):
    x = 1
    for i in range(a):
        x = (x + 1) * 2
        print(x)
    print('一共有%d个桃子'% x)
  
peaches(9)
#方法2：
# def last_peachs(x):
#     y = (x + 1) * 2
#     return y

# p = 1
# day = 10
# while day > 1:
#     day -= 1
#     p = last_peachs(p)
#     print('第',day,'天的桃子数是：',p)
    
# 3.完全数：
#     1 + 2 + 3 = 6
#     1 2 3都是6的因数
#     1 * 6 = 6
#     2 * 3 = 6
#     完全数是指除了自身以外所有的的因数的和等与自身。求4 - 5个完全数并打印
#     答案：6  28  496 ...

def factor(a):  #求数字除本身外的所有的因数
    l = []
    for i in range(1, a):
        if a % i == 0:
            l.append(i)
    return l
l = []
a = 0
for i in range(1, 10000):
    if sum(factor(i)) == i:
        l.append(i)
        a += 1
print(l)
