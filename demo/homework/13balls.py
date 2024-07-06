# # 1.一个球从100米高空落下，每次落下后反弹高度是原高度的一半
# #     1)算出皮球在第10次落下后反弹的高度是多少
# #     2)打印出球共经历了多少米的路程
# # 递归
# def ball(x):
#     if x == 1:
#         return 50
#     return ball(x - 1) / 2

# def path(x):
#     if x == 1:
#         return 1.5*100
#     return path(x - 1) + ball(x - 1)*1.5
# # # 循环
# # def ball(height,times):
# #     for _ in range(times):
# #         height = height / 2
# #     return height

# # def path(height,times):
# #     s = 0
# #     for _ in range(times):
# #         s += height
# #         height /= 2
# #         s += height
# #     return s

# times = int(input('请输入弹跳次数：'))
# h = ball(times)
# print('第%d次落地后弹起高度为%f米'%(times, h))
# h = path(times)
# print('第%d次落地后共经历了%f米'%(times, h))


# 2.分解质因数，输入一个正整数，分解质因数：
#     如：
#         输入：90
#         打印：90=2*3*3*5
def isprime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0 :
            return False
    else:
        return True

def factor(x):
    if isprime(x):
        fact.append(x)
        return
    for i in range(2,x):
        if x % i == 0:
            return (factor(i),factor(x//i))

def myprint(l):
    s = []
    for i in l:
        s.append(str(i))
    return '*'.join(s)

fact = []
try:
    n = int(input('请输入要求质因数的正整数：'))
    factor(n)
    print('%d='%n,myprint(fact),sep = '')
except ValueError:
    print('您的输入不正确，请查证后重试')



