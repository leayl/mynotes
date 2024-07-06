# 1.输入一个整数，代表树干的高度
# 打印一颗‘圣诞树’
# 如：
# 输入２：
# 打印　
#     ＊
# 　　＊＊＊
#     ＊
#     ＊
# 输入３：
# 打印　
#     ＊
# 　　＊＊＊
# ＊＊＊＊＊
#     ＊
#     ＊
#     ＊
n = int(input('请输入树干高度：'))
w = 2 * n - 1
for i in range(1,n + 1):
    s = "*" * (2 * i - 1)
    s1 = s.center(w)
    print(s1)
for i in range(1,n + 1):
    s2 = "*" 
    s3 = s2.center(w)
    print(s3)
print('-'*15)
# ２．用循环语句生成如下字符串(用ord与chr函数结合循环语句实现)
# 　　　　'ABC...XYZ'
i1 = ord('A')
for i3 in range(i1,i1 + 26):
    s1 = chr(i3)
    print(s1,end = ' ')
print()
# 　　　　'AaBbCc...XxYyZz'
print('-'*15)
i1 = ord('A')
i2 = ord('a')
j = i2 - i1
for i3 in range(i1,i1 + 26):
    s1 = chr(i3)
    s2 = chr(i3 + j)
    print(s1,s2,sep='',end = ' ')
print()
print('-'*15)
# ３．算出１００－９９９以内的水仙花数
# （百位的３次方加上十位的三次方加上个位的三次方等于原数字）
# 如：１５３等于1**3 + 5**3 + 3**3
# 参考答案：１５３，３７０．．．．
for i in range(100,1000):
    a = i // 100
    b = (i % 100) // 10
    c = i % 10
    if i == a ** 3 + b ** 3 + c ** 3:
        print(i)