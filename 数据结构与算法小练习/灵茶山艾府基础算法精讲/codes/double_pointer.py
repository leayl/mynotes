"""
双指针相关

"""
from typing import List
import unittest


def find_two_sum(nums: List, target: int):
    """
    从一个排好序的数组中找出相加等于给定值的两个数并返回这两个数所构成的数组
    如：
        输入数组为[1,2,3,4,5]，给定值为6
        输出[[1,5], [2,4]]
    测试用例:
        nums = [[1, 2, 3, 4, 5], [2, 3, 4, 5], [4, 5, 8, 9, 10, 13, 15, 18, 48]]
        for num in nums:
            print(num)
            print(find_two_sum(num, 22))
    输出：
        [1, 2, 3, 4, 5]
        []
        [2, 3, 4, 5]
        []
        [4, 5, 8, 9, 10, 13, 15, 18, 48]
        [[4, 18], [9, 13]]
    拓展：
        给定的数组为未排序的，并且 要求给出的时对应值的下标，可以使用字典处理
        题目地址：https://leetcode.cn/problems/two-sum
        解法：
        idx = {}
        for i, x in enumerate(nums):
            if target - x in idx:
                return [idx[target - x], i]
            idx[x] = i
    """
    i = 0
    j = len(nums) - 1
    res = []
    while i < j:
        s = nums[i] + nums[j]
        if s == target:
            res.append([nums[i], nums[j]])
            i += 1
            j -= 1
            continue
        elif s > target:
            j -= 1
        elif s < target:
            i += 1
    return res


def find_3_sum(nums: List[int]) -> List[List[int]]:
    """
    从给定数组中找到和为0的3个数组成的数组，顺序无所谓，不得有相同值组成的数组
    如：
        输入数组为[-1,0,5,3,-2,0,-1,1]
        输出:[[-1,0,1],[-1, -2, 3]
    用例：
        nums = [[-1,0,5,3,-2,0,-1,1], [2, -3, -4, 5, 7], [4, 5, -8, 9, 10, -13, 15, 18, 48]]
        for num in nums:
            print(num)
            print(find_3_sum(num))
    输出：
        [-1, 0, 5, 3, -2, 0, -1, 1]
        [[-2, -1, 3], [-1, 0, 1]]
        [2, -3, -4, 5, 7]
        [[-4, -3, 7]]
        [4, 5, -8, 9, 10, -13, 15, 18, 48]
        [[-13, 4, 9]]
        [-1, 2, 5, 3]
        []
    """
    res = []
    nums.sort()
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        if nums[i] + nums[i + 1] + nums[i + 2] > 0:
            break  # 最小的三个数和都 > 0，说明不存在这样的三个数，直接结束循环
        if nums[i] + nums[-1] + nums[-2] < 0:
            continue  # 由于已经排序, nums[i]还可能增大，可以继续下一轮循环

        j = i + 1
        k = n - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s == 0:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
                continue
            elif s < 0:
                j += 1
            elif s > 0:
                k -= 1

    return res


def find_max_capacity(nums: List[int]) -> int:
    """
    给定的数组代表每木板的长度，计算出其中两根木板构成的容器的最大容积
    容积长度：两根木板的距离；容积高度：最短木板的长度
    """
    i = 0
    j = len(nums) - 1
    res = 0
    while i < j:
        capacity = ((j - i) * min(nums[i], nums[j]))
        res = max(res, capacity)
        if nums[i] < nums[j]:
            i += 1
        else:
            j -= 1
    return res


def find_exist_capacity(nums: List[int]) -> int:
    """接雨水问题"""
    n = len(nums)
    left = 0
    right = n - 1
    res = 0
    pre_max = 0
    suf_max = 0
    while left < right:
        pre_max = max(pre_max, nums[left])
        suf_max = max(suf_max, nums[right])
        if pre_max < suf_max:
            res += pre_max - nums[left]
            left += 1
        else:
            res += suf_max - nums[right]
            right -= 1
    return res



