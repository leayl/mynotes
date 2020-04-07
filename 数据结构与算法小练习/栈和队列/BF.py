"""
实现BF算法
"""


def bf(target_str: str, source_str: str):
    """
    实现BF算法，在target_str中匹配source_str
    :param target_str: 目标字符串，被匹配
    :param source_str: 要在target_str中匹配的字符串
    :return:target_str中source_str的起始位置列表
    """
    if source_str == '':
        return []
    ret = []
    i = 0
    while i <= (len(target_str) - len(source_str)):
        if target_str[i] == source_str[0]:
            end = i
            j = 1
            while j < len(source_str):
                if target_str[i + j] == source_str[j]:
                    j += 1
                    end += 1
                else:
                    break
            if end - i + 1 == len(source_str):
                ret.append(i + 1)  # 从1开始计数
                i += j
            else:
                i += j
        else:
            i += 1
    return ret


if __name__ == '__main__':
    str1 = "hi I Love Yov"
    str2 = "ov"
    ret = bf(str1, str2)
    print(ret)
