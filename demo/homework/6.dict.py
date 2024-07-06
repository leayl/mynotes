# 1.输入单词和解释，将单词作为键，解释作为值，保存在字典中，
# 然后输入查询的单词，显示解释
#录入单词
L = {}
while True:
    word = input('请输入单词：')
    if word == '':   #if not word:
        break
    translation = input('请输入解释：')
    L[word] = translation
print(L)
#查询单词
while True:
  s = input('请输入需查询的单词：')
  if not s:
    break
  a = L.get(s,'没有相关单词信息！')
  print(a)
# 2.学生管理项目准备工作：
#     任意输入n个学生的信息，形成字典后存于列表中：
#         学生信息包括：
#             姓名（字符串）
#             年龄（整数）
#             成绩（整数）
#         1.循环输入学生信息，直到姓名为空时结束，最后形成字典列表如下：
#             L = [
#                 {'name':'xiaozhang,'age':20,'score':100},
#                 {'name':'xiaozhang,'age':20,'score':100},
#                 {'name':'xiaozhang,'age':20,'score':100},
#                 ......
#                 ]
#         2.将以下上列表显示为如下表格：
#         +----------+-------+-------+
#         |   name   |   age | score |
#         +----------+-------+-------+
#         | xiaozhang|   20  |  100  |
#         | xiaozhang|   20  |  100  |
#         | xiaozhang|   20  |  100  |
#         +----------+-------+-------+

L = []
while True:
    name = input('姓名：')
    if name == '':
        break
    age = int(input('年龄：'))
    score = int(input('成绩：'))
    D = {'name':name,'age':age,'score':score}
    # D = {}
    # D[name] = name...
    L.append(D)
print(L)

print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
print('|'+'name'.center(20)
       +'|'+'age'.center(10)
       +'|'+'score'.center(10)+'|')
print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
for x in L:
    print('|',x['name'].center(20),
          '|',str(x['age']).center(10),
          '|',str(x['score']).center(10),'|',sep = '')
print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
