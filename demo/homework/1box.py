str1 = input('请输入第一串字符：')
str2 = input('请输入第二串字符：')
str3 = input('请输入第三串字符：')
w = int(input('方框宽度：'))
l1 = len(str1)
l2 = len(str2)
l3 = len(str3)
a1 = (w - 2 - l1) // 2
a2 = (w - 2 - l2) // 2
a3 = (w - 2 - l3) // 2
print('+' + '-' * (w - 2) + '+')
print('|' + ' ' * a1 + str1 + ' ' * (w - 2 - l1 - a1) + '|')
print('|' + ' ' * a2 + str2 + ' ' * (w - 2 - l2 - a2) + '|')
print('|' + ' ' * a3 + str3 + ' ' * (w - 2 - l3 - a3) + '|')
print('+' + '-' * (w - 2) + '+')
