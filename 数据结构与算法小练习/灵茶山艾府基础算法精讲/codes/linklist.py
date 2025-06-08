# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rhead1 = self.reverseList(l1)
        rhead2 = self.reverseList(l2)
        node1 = rhead1
        node2 = rhead2
        mod_ = 0

        pre = None
        while node1 or node2 or mod_:
            num1 = node1.val if node1 else 0
            num2 = node2.val if node2 else 0
            i, j = divmod((num1 + num2 + mod_), 10)
            cur = ListNode(val=j, next=pre)
            mod_ = i
            if node1:
                node1 = node1.next
            if node2:
                node2 = node2.next
            pre = cur

        return pre

    def reverseList(self, head: ListNode):
        pre = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre
