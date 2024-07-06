# # 1.编写一个程序，以电子时钟格式打印时间：
# #     时钟格式为：
# #         HH:MM:SS
# #     时钟每隔一秒刷新一次
# import time
# while True:
#     t = time.localtime()
#     time.sleep(1)
#     print('%02d:%02d:%02d' % t[3:6],end='\r')

# # 2.编写一个闹钟程序，启动时设置定时间，到时候打印出一句话，程序退出
# def clock():
#     import time
#     h = int(input('请输入定时小时：'))
#     m = int(input('请输入定时分钟：'))
#     while True:
#         s = time.localtime()
#         print('%02d:%02d:%02d' % s[3:6],end='\r')
#         if s[3:5] == (h,m):
#             print('该去上课了')
#             return
# clock()

# 3.编写函数fun，其功能是计算多项式的和
#     sn = 1/1! +2/2! + ...3/3!
#     计算n=100时的值 

def fun(x):
    import math
    s = sum(map(lambda n: n/math.factorial(n), range(1, x+1)))
    return s

print(fun(100))

