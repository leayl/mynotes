"""
实现BF算法
在目标串target_str中匹配模式串source_str的字符，并输出目标串中匹配成功的字符的起始下标，未匹配上则返回-1
"""


def bf(target_str: str, source_str: str, pos: int):
    """
    实现BF算法，在target_str中匹配source_str
    :param target_str: 目标字符串，被匹配
    :param source_str: 要在target_str中匹配的字符串
    :param pos: 目标字符串中开始匹配的下标
    :return:target_str中source_str的起始位置下标
    """
    i = pos
    j = 0
    # 从两个字符串的0号字符开始匹配
    while i < len(target_str) and j < len(source_str):
        if target_str[i] == source_str[j]:
            # 如果匹配成功则匹配两者的下一个字符
            i += 1
            j += 1
        else:
            # 如果某个字符未匹配上，则目标串的索引回溯到此次匹配的开头的下一个字符，模式串回溯为0
            i = i - j + 1
            j = 0
    # 如果模式串索引等于其长度，表示完全匹配上了，返回此时目标串的索引-模式串的长度，为此次匹配成功的开始下标
    if j == len(source_str):
        return i - j
    return -1


if __name__ == '__main__':
    str1 = "hi I Love You"
    str2 = "ov"
    ret = bf(str1, str2, 0)
    print(ret)
