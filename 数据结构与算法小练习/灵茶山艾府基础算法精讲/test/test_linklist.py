import unittest
from typing import List

from 数据结构与算法小练习.灵茶山艾府基础算法精讲.codes.linklist import Solution, ListNode

solution = Solution()

class LinkedList:
    def __init__(self, ls:List):
        dummy = ListNode()
        pre = dummy
        for val in ls:
            pre.next = ListNode(val)
            pre = pre.next
        self.head = dummy.next

class TestLinklist(unittest.TestCase):
    def test_reverse_list(self):
        nums = [LinkedList([1, 2, 3, 4, 5]).head, LinkedList([3, 2, 6, 3, 1, 9, 8]).head]
        res_lis = [5, 8]
        for head, expected_res in zip(nums, res_lis):
            res = solution.reverseList(head=head)
            self.assertEqual(expected_res, res.val)

    def test_addTwoNumbers(self):
        nums1 = [
            LinkedList([7,2,4,3]).head,
            LinkedList([2,4,3]).head,
            LinkedList([0]).head,
        ]
        nums2 = [
            LinkedList([5,6,4]).head,
            LinkedList([5,6,4]).head,
            LinkedList([0]).head,
        ]
        res_lis = [
            LinkedList([7,8,0,7]).head,
            LinkedList([8,0,7]).head,
            LinkedList([0]).head,
        ]
        for head1, head2, expected_res in zip(nums1, nums2, res_lis):
            res = solution.addTwoNumbers(head1, head2)
            self.assertEqual(expected_res.val, res.val)