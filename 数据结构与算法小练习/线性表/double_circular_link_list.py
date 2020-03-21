"""
双向循环链表
"""
import string


class Node:
    def __init__(self, data, prior=None, next=None):
        self.data = data
        self.prior = prior
        self.next = next

    def __repr__(self):
        return self.data


class DoubleCirclarLinkList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def length(self):
        if self.is_empty():
            return 0
        i = 1
        temp = self.head
        while temp.next != self.head:
            i += 1
            temp = temp.next
        return i

    def append(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
            self.head.next = self.head
            self.head.prior = self.head
        else:
            node.prior = self.head.prior
            self.head.prior.next = node
            self.head.prior = node
            node.next = self.head

    def insert(self, index, data):
        if index > self.length() or index < 1:
            print('不在范围内')
            return
        temp = self.head
        node = Node(data)
        i = 1
        while i < index:
            temp = temp.next
            i += 1
        node.prior = temp.prior
        temp.prior.next = node
        temp.prior = node
        node.next = temp

    def remove(self, data):
        if self.is_empty():
            print('空表')
            return
        temp = self.head
        if temp.data == data:  # 第一个节点是目标节点
            if temp.next != self.head:  # 表中不止一个节点
                temp.next.prior = temp.prior
                temp.prior.next = temp.next
                return
            else:  # 只有一个节点
                self.head = None
        else:
            temp = temp.next
            while temp != self.head:
                if temp.data == data:
                    temp.next.prior = temp.prior
                    temp.prior.next = temp.next
                    return
                else:
                    temp = temp.next

    def __repr__(self):
        if self.is_empty():
            return ''
        temp = self.head
        ret = ''
        while temp.next != self.head:
            ret += str(temp.data) + " "
            temp = temp.next
        ret += str(temp.data)
        return ret


def caesar(l, num):
    """
    输入循环链表和数字，输出改变链表中的排序结果
    :param l:
    :param num:要移动的步数，为正向左移动，反之向右
    :return:
    """
    temp = l.head
    if not isinstance(num, int):
        print('请输入整数')
        return
    step = abs(num)
    temp = l.head

    def print_l(head):
        head = head
        temp = head
        while temp.next != head:
            print(temp.data, end=' ')
            temp = temp.next
            # temp += 1
        print(temp.data, end=' ')
        print()

    if num > 0:
        for i in range(step):
            temp = temp.next
        print_l(temp)


    elif num < 0:
        for i in range(step):
            temp = temp.prior
        print_l(temp)
    else:
        print_l(l.head)


if __name__ == '__main__':
    l = DoubleCirclarLinkList()
    for i in string.ascii_uppercase:
        l.append(i)
    caesar(l, 3)
