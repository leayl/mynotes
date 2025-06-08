import unittest

from 数据结构与算法小练习.灵茶山艾府基础算法精讲.codes.double_pointer import find_max_capacity, find_exist_capacity


class TestDoublePointer(unittest.TestCase):
    def test_find_max_capacity(self):
        nums = [[1, 2, 3, 4, 5], [3, 2, 6, 3, 1, 9, 8]]
        res_lis = [6, 24]
        for num_lis, max_capacity in zip(nums, res_lis):
            res = find_max_capacity(num_lis)
            self.assertEqual(max_capacity, res)

    def test_find_exist_capacity(self):
        nums = [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]]
        res_lis = [6]
        for num_lis, capacity in zip(nums, res_lis):
            res = find_exist_capacity(num_lis)
            self.assertEqual(capacity, res)