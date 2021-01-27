"""
实现BF算法和KMP算法
BF算法：
    在目标串target_str中匹配模式串source_str的字符，并输出目标串中匹配成功的字符的起始下标，未匹配上则返回-1
KMP算法：
    在BF算法的前提上进行优化，目标串索引不回溯，利用模式串自身的前缀和后缀相同的个数
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


def get_kmp_next_lis(sour_str):
    """
    获取模式串中每个位置匹配失败后应该去匹配目标串当前位置的模式串位置
    :param sour_str: 模式串
    """
    print(sour_str)
    ret_lis = [-1] * len(sour_str)
    ret_lis[1] = 0
    pre_index = 0  # 前缀位置
    suf_index = 1  # 后缀位置
    # 由于配对成功后索引是先增加1再记录next的，这里在索引为：字符长度-1（最后一个位置）时，已经记录了最后一个的值
    while suf_index < len(sour_str) - 1:
        if pre_index == -1 or sour_str[suf_index] == sour_str[pre_index]:
            pre_index += 1
            suf_index += 1
            ret_lis[suf_index] = pre_index
        else:
            # 匹配失败后，前缀的起始匹配位置往前走，注意了，脑子里的图形中，下面的是前缀，所以移动的是前缀啊！！！
            pre_index = ret_lis[pre_index]
    return ret_lis


def kmp(tar_str, sour_str):
    next_lis = get_kmp_next_lis(sour_str)
    print(next_lis)
    tar_index = sour_index = 0
    while tar_index < len(tar_str) and sour_index < len(sour_str):
        if tar_str[tar_index] == sour_str[sour_index]:
            tar_index += 1
            sour_index += 1
        elif sour_index != 0:
            sour_index = next_lis[sour_index]
        else:
            tar_index += 1

    if sour_index == len(sour_str):
        return tar_index - len(sour_str)
    return -1


if __name__ == '__main__':
    # str1 = "hi I Love You"
    # str2 = "ov"
    # ret = bf(str1, str2, 0)
    # print(ret)
    t = 'abaacabacaca'
    s = 'acaca'
    print(kmp(t, s))

