# 1.写程序，让用户输入一系列整数，当输入小于零的数时，结束输入
#     1.将输入的数字存于列表中
#     2.将列表中的数字写入到文件numbers.txt中
#     需要将整数转为字节串或字符串
def get_numbers():
    l = []
    while True:
        n = int(input('请输入整数：'))
        if n < 0:
            break
        l.append(n)
    return l

def numbers_write(l):
    try:
        f = open('numbers.txt','w')
        for i in l:
            f.write(str(i))
            f.write('\n')
        f.close()
    except OSError:
        print('文件打开失败')

l = get_numbers()
numbers_write(l)

# 2.写程序，将文件中的整数读入到内存中，
# 重新形成数字组成的列表，计算这些数的max，min，sum
def numbers_read(filename):
    l = []
    try:
        f = open('numbers.txt')
        try:
            for line in f:
                n = int(line.rstrip())
                l.append(n)
        except ValueError:
            print('读取文件出错，数据可能不完整')
        finally:
            f.close()
    except OSError:
        print('文件打开失败')
    return l

L = numbers_read('numbers.txt')
print('最大值为：',max(L))
print('最小值为：',min(L))
print('和为：',sum(L))
