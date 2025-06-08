import unittest

from 数据结构与算法小练习.灵茶山艾府基础算法精讲.codes.bin_search import low_bound, Solution

solution = Solution()


class TestDoublePointer(unittest.TestCase):
    def test_successful_pairs(self):
        spells = [[5, 1, 3], [3, 1, 2]]
        potions = [[1, 2, 3, 4, 5], [8, 5, 8]]
        success_lis = [7, 16]
        res_lis = [[4, 0, 3], [2, 0, 2]]
        for spell, potion, success, expected_res in zip(spells, potions, success_lis, res_lis):
            res = solution.successfulPairs(spell, potion, success)
            self.assertEqual(expected_res, res)

    def test_count_fair_pairs(self):
        nums = [[0, 1, 7, 4, 4, 5], [1, 7, 9, 2, 5]]
        lowers = [3, 11]
        uppers = [6, 11]
        res_lis = [6, 1]
        for num, lower, upper, expected_res in zip(nums, lowers, uppers, res_lis):
            res = solution.countFairPairs(num, lower, upper)
            self.assertEqual(expected_res, res)

    def test_max_number_of_alloys(self):
        n = 3
        k = 2
        budget = 15
        composition = [[1, 1, 1], [1, 1, 10]]
        stock = [0, 0, 0]
        cost = [1, 2, 3]
        res = solution.maxNumberOfAlloys(n, k, budget, composition, stock, cost)
        self.assertEqual(2, res)

    def test_find_min(self):
        nums = [3, 1, 3]
        res = solution.findMin(nums)
        self.assertEqual(1, res)
