"""
使用python实现链表，使用快慢指针的原理找到链表的中间位置的值
"""
import random

from 数据结构与算法小练习.线性表.link_list import LinkList


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


def create_link_list_with_circle(L):
    length_l = L.length
    circle_node_num = random.randint(1, length_l)
    print('设定环节点：', circle_node_num)
    circle_node = L.head
    i = 1
    while i < circle_node_num:
        circle_node = circle_node._next
        i += 1
    circle_node = circle_node._next
    temp = L.head
    while temp._next:
        temp = temp._next
    temp._next = circle_node
    return L


def if_link_with_circle(L):
    """
    :desc:判断链表是否带有环
    :param L:
    :return:
    """
    # 方法一：q一直往前走，p每次从头开始走，计算每次p走到q同等位置时，步数是否相同，一直相同则无环，反之则有
    # q = L.head
    # i = 0
    # while q._next:
    #     p = L.head
    #     j = 0
    #     while p._next:
    #         if p == q:
    #             if i == j:
    #                 break
    #             else:
    #                 return j
    #         else:
    #             p = p._next
    #             j += 1
    #     q = q._next
    #     i += 1
    # return False
    # 方法二：q,p 以不同速度向前，如果一直不碰到则无环，反之则有
    q = L.head
    p = L.head
    i = 0
    while p and q:
        p = p._next
        i += 1
        if q._next:
            q = q._next._next
        else:
            return False
        if q == p:
            return i
    return False


def magician_card():
    """
    魔术师发牌问题
    第一个为1
    每发一次牌，放到桌子上
    发第n张牌，从手里从1开始数，每数一张忘手中下面放，直到数到n，发出手中的牌
    发到桌子上的牌要从1开始连续
    :return:
    """
    l = CircularLinkList()

    for i in range(1, 14):
        l.append(0)

    temp = l.head
    temp.data = 1
    card_num = 2
    while True:
        j = 0
        while j < card_num:
            temp = temp._next
            j += 1
            if temp.data != 0:
                j -= 1

        if temp.data == 0:
            temp.data = card_num
            card_num += 1
        if card_num == 14:
            break
    return l


def latin_square(n):
    """
    拉丁方阵:
    如下为3x3方阵
    1 2 3
    2 3 1
    3 2 1
    """
    # 生成长度为n的循环链表
    l = CircularLinkList()
    for i in range(1, n + 1):
        l.append(i)
    # 新行的头一个元素
    temp1 = l.head
    for j in range(1, n + 1):
        # 新行开始元素为temp1
        temp2 = temp1
        for k in range(n):
            print(temp2.data, end=' ')
            temp2 = temp2._next
        print()
        temp1 = temp1._next


if __name__ == '__main__':
    # circular_link_list = CircularLinkList()
    # # 随机生成链表
    # for i in range(1, 42):
    #     circular_link_list.append(i)
    # print(circular_link_list)
    # circular_link_list.append(4)
    # circular_link_list.add(455)
    # circular_link_list.insert(4, 555)
    # circular_link_list.remove(555)

    # link_list = LinkList()
    # # 随机生成链表
    # for i in range(19):
    #     node = Node(random.randint(1, 50))
    #     link_list.append(node)
    # print(link_list)
    # print(if_link_with_circle(link_list))
    # link_list = create_link_list_with_circle(link_list)
    # print(if_link_with_circle(link_list))

    # l = magician_card()
    # print(l)
    latin_square(9)
