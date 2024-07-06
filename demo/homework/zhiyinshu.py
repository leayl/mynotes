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

if __name__=='__main__':
    fact = []
    try:
        n = int(input('请输入要求质因数的正整数：'))
        factor(n)
        print('%d='%n,myprint(fact),sep = '')
    except ValueError:
        print('您的输入不正确，请查证后重试')

