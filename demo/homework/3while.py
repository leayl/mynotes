# 1.任意输入一些整数，每次输入一个，
# 当输入负数时结束输入，然后打印输入的数的和
sum1 = 0
while True:
    n = int(input('请输入整数：'))
    if n < 0:
        break
    sum1 = sum1 + n
print(sum1)
 # 2.写程序用while实现打印三角形，
 # 要求输入一个整数表示三角形的宽度和高度，
 # 打印输出如下三种直角三角形：
 #        *     ***     ***
 #       **      **     **
 #      ***       *     *
a = int(input('请输入三角边长：'))  
i = 1
while i <= a:
    print(' '*(a-i),'*'*i)
    i += 1

b = int(input('请输入三角边长：'))  
j = 0
while j < b:
    print(' '*j,'*'*(b-j))
    j += 1

c = int(input('请输入三角边长：'))  
k = 0
while k < c:
    print('*'*(c-k))
    k += 1
 # 3.写程序求多项式的和：
 #    1/1 -1/3+1/5-1/7...+1/(2*n-1)的和
 #    n最大取1000000
 #    打印这个和以及和乘以4的值
n = int(input('请输多项式个数：'))
sum2 = 0
i2 = 1
while i2 <= n:
    d = ((-1)**(i2-1)*1)/(2*i2-1)
    sum2 = sum2 + d
    i2 = i2 + 1
print(sum2)
print(sum2*4)
