# 1.用字符串 s = 'ABC'　和 s2 = '123'生成如下列表：
# ['A1','A2','A3','B1','B2','B3','C1','C2','C3',]
s = 'ABC'
s2 = '123'
L = [x + y for x in s for y in s2]
print(L)
print('-'*40)
# 2.有一些数存在于列表L中，如：
# L = [1,3,2,1,6,3,...,3,3](自己定义)
# 将列表L中的数存入于另一个列表L2中（要求重复出现的数字只在L2列表中保留一份）
L = []
while True: 
    n = int(input('请输入数据（00结束）：'))
    if n == 00:
        break
    L.append(n)
print(L)
#############################################
# 一．顺序不变
L2 = []
for i in L:
    if i not in L2:
        L2.append(i)
print(L2)
L2.sort()     #验证两种方法是否相同
print(L2)
#############################################
# 二．排序后去重
L.sort()
l = len(L)
L2 = [L[0]]
for i in range(1,l):
    if L[i] == L[i - 1]:
        continue
    L2.append(L[i])
print(L2)
print('-'*40)

# 3.生成前40个斐波那契数，要求这些数保存在列表中，打印出此列表
# 1 1 2 3 5 8 13 21 34 55 89
i = 1
j = 1
L = []
k = 0  # k = len(L)
n = int(input('请输入打印数量：'))
while k < n:
    L.append(i)
    i,j = j,i+j
    k += 1
print(L)
############################
L = [1,1]
while len(L)<40:
        L.append(L[-1]+L[-2])
print(L)