# 1.用生成器函数primes(begin,end)生成素数，
# 给出起始值begin和终止值end，
# 生成此范围内的全部素数，不包含end
def isprime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0 :
            return False
    else:
        return True

def primes(begin, end):
    for i in range(begin, end):
        if isprime(i):
            yield i

l = [x for x in primes(1,10)]
print(l)

# 2.仿制range函数的功能，写一个生成器函数myrange，
# 要求功能与range功能相近，能实现1,2,3个参数传参，生成正向的整数
def myrange(start,end=None,step=1):
    if end is None:
        start,end = 0,start
    i = start
    while i < end:
        yield i
        i += step

l = [x for x in myrange(10)]
print(l)