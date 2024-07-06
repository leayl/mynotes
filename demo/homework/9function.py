# 1.写一个mysum函数，要求给出一个数n，求
#     1+2+...+n的和
def mysum(n):
    s = 0
    for i in range(n+1):
            s += i
    return s

print(mysum(10))
#　2.写一个函数myfac来计算n!
#     n! = 1*2*....*n
def myfac(n):
    s = 1
    for i in range(1,n+1):
            s *= i
    return s

print(myfac(4))
# 3.写一个函数，求
#         1+2**2+3**3+n**n的和
def mysum3(n):
    s = 0
    for i in range(1,n+1):
            s += i**i
    return s

print(mysum3(10))
#　4.修改学生管理系统，实现添加菜单和选择菜单操作功能：
# 菜单：
#     +------------------------+
#     |  1） 添加学生信息    　　  |
#     |  2） 查看所有学生信息 　　　 |
#     |  3） 修改学生成绩     　　 |
#     |  4） 删除学生信息     　　 |
#     |  q） 退出              　|
#     +------------------------+
# 请选择：1
#     请输入姓名：....
# 请选择：3
#     请输入修改学生的姓名：...
# (要求每个功能对应一个函数)
def open():
    print('+'+'-'*23+'+')
    print('|'+'1) 添加学生信息'+' '*8+'|')
    print('|'+'2) 查看所有学生信息'+' '*4+'|')
    print('|'+'3) 修改学生成绩'+' '*8+'|')
    print('|'+'4) 删除学生信息'+' '*8+'|')
    print('|'+'q) 退出'+' '*16+'|')
    print('+'+'-'*23+'+')

def modify_info(L):
    while True:
        name = input('请输入修改学生的姓名：')
        if not name:
            break
        score = int(input('请输入修改的成绩：'))
        for i in L:
            if i['name'] == name:
                i['score'] = score
            else:
                print('未找到相关学生信息')
    return L

def remov(L):
    while True:
        name = input('请输入要删除信息的学生姓名：')
        if not name:
            break
        for i in range(len(L)):
            if L[i]['name'] == name:
                del L[i]
                print('删除成功')
                return L
        else:
                print('未找到相关学生')
    

def input_student():
    L = []
    while True:
        name = input('姓名：')
        if name == '':
            break
        age = int(input('年龄：'))
        score = int(input('成绩：'))
        D = {'name':name,'age':age,'score':score}
        L.append(D)
    return L

def output_student(L):
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

def output_turn(L):
    choise = input('请选择排序方式：1)按成绩 2)按年龄')
    if choise == '1':
        L2 = sorted(L, key=lambda l: l['score'], reverse=True)
        output_student(L2)
    elif choise == '2':
        L3 = sorted(L, key=lambda l: l['age'], reverse=True)
        output_student(L3)
def main():
    L = []
    while True:
        open()
        choise = input('请选择：')
        if choise == '1':
            L += input_student()
        elif choise == '2':
            output_turn(L)
        elif choise == '3':
            L = modify_info(L)
        elif choise == '4':
            L = remov(L)
        elif choise == 'q':
            return

main()




# #     验证测试：
# L = input_student()
# output_student(L)
# print('再添加几个学生信息')
# L += input_student()
# print('添加后的学生信息如下')
# output_student(L)