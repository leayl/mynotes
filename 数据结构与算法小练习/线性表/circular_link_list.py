"""
使用python实现链表，使用快慢指针的原理找到链表的中间位置的值
"""
import random


class Node:
    def __init__(self, data):
        self.data = data
        self._next = None

    def __repr__(self):
        return str(self.data)


class CircularLinkList:
    def __init__(self, ):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        if self.is_empty():
            return 0
        count = 1
        cur = self.head
        while cur._next != self.head:
            count += 1
            cur = cur._next
        return count

    def add(self, data):
        node = Node(data)
        if self.is_empty():
            self.head._next = node
            node._next = self.head
        else:
            cur = self.head
            while cur._next != self.head:
                cur = cur._next
            node._next = cur._next
            cur._next = node
            self.head = node

    def append(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            node._next = self.head
        else:
            temp = self.head
            while temp._next != self.head:
                temp = temp._next
            temp._next = node
            node._next = self.head

    def insert(self, index, data):
        print(self.length())
        if index < 1 or index > self.length() + 1:
            print('不在范围内!')
        else:
            if index == 1:
                self.add(data)
            else:
                item = Node(data)
                cur = self.head
                i = 1
                while i < index - 1:
                    cur = cur._next
                    i += 1
                item._next = cur._next
                cur._next = item

    def remove(self, data):
        if self.is_empty():
            return

        cur = self.head
        prev = None
        if cur.data == data:  # 第一个节点就是目标节点
            if cur._next != self.head:  # 不止一个节点
                while cur._next != self.head:
                    cur = cur._next
                cur._next = self.head._next
            else:  # 只有一个节点
                self.head = None
        else:  # 第一个节点不是目标节点
            prev = self.head
            cur = cur._next
            while cur._next != self.head:
                if cur.data == data:
                    prev._next = cur._next
                    return
                else:
                    prev = cur
                    cur = cur._next
            if cur.data == data:
                prev._next = cur._next

    def __repr__(self):
        node = self.head
        ret = ""
        while node._next != self.head:
            ret += str(node.data) + ", "
            node = node._next
        ret += str(node.data)
        return ret


if __name__ == '__main__':
    circular_link_list = CircularLinkList()
    # 随机生成链表
    for i in range(1, 42):
        circular_link_list.append(i)
    print(circular_link_list)
    # circular_link_list.append(4)
    # circular_link_list.add(455)
    # circular_link_list.insert(4, 555)
    # circular_link_list.remove(555)
