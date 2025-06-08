def low_bound(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def low_bound2(nums, start_idx, target):
    left = start_idx + 1
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if mid < target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def get_max_cnt(budget, composition, stock, cost):
    left = 0
    right = min(stock) + budget
    while left < right:
        mid = (left + right) // 2
        total_cost = 0
        for com, s, c in zip(composition, stock, cost):
            if mid * com > s:
                total_cost += (mid * com - s) * c

        if total_cost >= budget:
            right = mid - 1
        else:
            left = mid + 1
    return left



class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        n = len(potions)
        res = []
        for spell in spells:
            if spell == 0:
                res.append(0)
                continue
            pair_start = low_bound(potions, success / spell)
            res.append(n - pair_start)
        return

    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        res = 0
        for idx, x in enumerate(nums):
            start = low_bound2(nums, idx, lower - x)
            end = low_bound2(nums, idx, upper - x + 1)
            res += end - start
        return res

    def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
        """
        :type n: int
        :type k: int
        :type budget: int
        :type composition: List[List[int]]
        :type stock: List[int]
        :type cost: List[int]
        :rtype: int
        """
        res = 0
        for i in range(k):
            res = max(get_max_cnt(budget, composition[i], stock, cost), res)
        return res

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == nums[right]:
                right -= 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left +1]
