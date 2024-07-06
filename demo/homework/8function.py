 # 1.素数prime函数练习
 #     1.写一个函数isprime（x），判断x是否为素数，如果是返回True，否则返回False
def isprime(x):
    if x < 2:           
        return False
    for i in range(2,x):
        if x % i == 0:   
            return False                     
    return True      
#print(isprime(99))
 #     2.写一个函数prime_m2n(m,n),返回m到n之间的素数列表，不包含 n
def prime_m2n(m,n):
    if m > n:
        m,n=n,m
    # return [x for x in range(m, n) if isprime(x)]
    l = []
    for x in range(m,n):
        if isprime(x):
            l.append(x)
    return(l)
#print(prime_m2n(1,100))
 #     3.写一个函数primes(n)，返回指定范围内的素数列表，不包含n，并打印这些素数
def primes(n):
    return prime_m2n(0,n)
primes(100)

 #        1.打印100以内的素数
a = primes(100)
for i in a:
  print(i)
 #        2.打印100以内的所有素数的和
print('100以内的素数的和是：',sum(a))
 # 2.修改学生信息管理程序，编写两个函数用于封装录入信息和打印信息的功能
 #     1.input_student()
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
    print(L)
    return L
 #     2.output_student(L)
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

　　　　　
#     验证测试：
L = input_student()
output_student(L)
print('再添加几个学生信息')
L += input_student()
print('添加后的学生信息如下')
output_student(L)
