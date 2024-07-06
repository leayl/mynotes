# # 1.编写函数求阶乘myfac(x)
# def myfac(x):
#     if x == 1:
#         return x
#     return x * myfac(x - 1)
# print(myfac(5))

# # 2.写程序算出1--20的阶乘的和
# print(sum(map(myfac, range(1, 21))))
# def myfacsum(x):
#     if x == 1:
#         return x
#     return myfac(x) + myfacsum(x - 1)
# print(myfacsum(20))

# # 3.学生管理系统添加如下功能：
# #     1.按成绩从高到低打印学生信息
# #     2.按成绩从低到高打印学生信息
# #     3.按年龄从大到小打印学生信息
# #     4.按年龄从小到大打印学生信息
# #     (要求原来输入的列表顺序不变)
# def open():
#     print('+'+'-'*23+'+')
#     print('|'+'1) 添加学生信息'+' '*8+'|')
#     print('|'+'2) 查看所有学生信息'+' '*4+'|')
#     print('|'+'3) 修改学生成绩'+' '*8+'|')
#     print('|'+'4) 删除学生信息'+' '*8+'|')
#     print('|'+'q) 退出'+' '*16+'|')
#     print('+'+'-'*23+'+')

# def modify_info(L):
#     while True:
#         name = input('请输入修改学生的姓名：')
#         if not name:
#             break
#         score = int(input('请输入修改的成绩：'))
#         for i in L:
#             if i['name'] == name:
#                 i['score'] = score
#             else:
#                 print('未找到相关学生信息')
#     return L

# def remov(L):
#     while True:
#         name = input('请输入要删除信息的学生姓名：')
#         if not name:
#             break
#         for i in range(len(L)):
#             if L[i]['name'] == name:
#                 del L[i]
#                 print('删除成功')
#                 return L
#         else:
#                 print('未找到相关学生')
    

# def input_student():
#     L = []
#     while True:
#         name = input('姓名：')
#         if name == '':
#             break
#         age = int(input('年龄：'))
#         score = int(input('成绩：'))
#         D = {'name':name,'age':age,'score':score}
#         L.append(D)
#     return L

# def output_student(L):
#     print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
#     print('|'+'name'.center(20)
#            +'|'+'age'.center(10)
#            +'|'+'score'.center(10)+'|')
#     print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')
#     for x in L:
#         print('|',x['name'].center(20),
#               '|',str(x['age']).center(10),
#               '|',str(x['score']).center(10),'|',sep = '')
#     print('+'+'-'*20+'+'+'-'*10+'+'+'-'*10+'+')

# def output_turn(L):
#     choise = input('''请选择排序方式：
#     1)成绩升序 
#     2)成绩降序
#     3)年龄升序
#     4)年龄降序''')
#     if choise == '1':
#         L1 = sorted(L, key=lambda l: l['score'])
#         output_student(L1)
#     elif choise == '2':
#         L2 = sorted(L, key=lambda l: l['score'], reverse=True)
#         output_student(L2)
#     elif choise == '3':
#         L3 = sorted(L, key=lambda l: l['age'])
#         output_student(L3)
#     elif choise == '4':
#         L４ = sorted(L, key=lambda l: l['age'], reverse=True)
#         output_student(L４)
# def main():
#     L = []
#     while True:
#         open()
#         choise = input('请选择：')
#         if choise == '1':
#             L += input_student()
#         elif choise == '2':
#             output_turn(L)
#         elif choise == '3':
#             L = modify_info(L)
#         elif choise == '4':
#             L = remov(L)
#         elif choise == 'q':
#             return

# main()

# 4.已知有列表：
#      L =  [[3,5,6], 10, [[13, 14], 15, 18], 20]
#      1)写一个函数print_list(lst)打印出所有元素
#         print_list(L)
L = [[3,5,6], 10 , [[13, 14], 15, 18], 20]
def print_list(L):
    for i in L:
        if type(i) is list:
            print_list(i)
        else:
            print(i)

print_list(L)
print('-'*20)
#      2)写一个函数sum_list(lst)
#         返回这个列表中所有元素的和
def sum_list(L):
    s = 0
    for i in L:
        if type(i) is list:
            s += sum_list(i)
        else:
            s += i
    return s
         
print(sum_list(L))
#      注：type(x)可以返回一个变量的类型
