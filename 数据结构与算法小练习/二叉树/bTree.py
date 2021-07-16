"""
二叉树相关demo
# todo 只有个大概，没弄完，递归生成树时如何退出还不清楚
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


class BTree:
    def __init__(self):
        self.root = None

    @classmethod
    def create_tree(self, ):
        """
        生成二叉树
        :param s: 按照二叉树前序遍历的顺序输入的字符串
        """
        s = input('input:')
        if s == '#':
            return -1
        if s == ' ':
            node = None
        else:
            node = Node(s)
            lchild = self.create_tree()
            rchild = self.create_tree()
            node.lchild = lchild
            node.rchild = rchild
        if not self.root:
            self.root = node
        return node

if __name__ == '__main__':
    tree = BTree()
    tree.create_tree()

