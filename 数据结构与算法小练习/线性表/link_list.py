"""
使用python实现链表，使用快慢指针的原理找到链表的中间位置的值
"""
import random


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self._next = next

    def __repr__(self):
        return str(self.data)


class LinkList:
    def __init__(self, head=Node(None), length=0):
        self.head = head
        self.length = length

    def is_empty(self):
        return self.length == 0

    def append(self, data_or_node):
        if isinstance(data_or_node, Node):
            item = data_or_node
        else:
            item = Node(data_or_node)
        if not self.head:
            self.head = item
        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
        self.length += 1

    def delete(self, index):
        if index < 0 or index >= self.length:
            print("下标超出范围！")
            return
        if self.is_empty():
            print("空链表！")
            return
        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return
        i = 0
        prev = self.head
        node = self.head
        while i < index and node._next:
            prev = node
            node = node._next
            i += 1
        if i == index:
            prev._next = node._next
            self.length -= 1

    def __repr__(self):
        node = self.head
        ret = ""
        while node._next:
            ret += str(node.data) + ", "
            node = node._next
        return ret


def find_mid_link_list(L: LinkList):
    # 使用快慢指针原理查找链表中间位置的值
    mid = search = L.head
    while search._next:
        if search._next._next:
            # search是mid移动速度的两倍，当search移动到末尾(即search._next为空)时，mid到达链表中间位置
            mid = mid._next
            search = search._next._next
        else:
            search = search._next
    return mid.data


if __name__ == '__main__':
    link_list = LinkList()
    # 随机生成链表
    for i in range(19):
        node = Node(random.randint(1, 50))
        link_list.append(node)
    mid = find_mid_link_list(link_list)  # 获取中间位置的值
    print(mid)
