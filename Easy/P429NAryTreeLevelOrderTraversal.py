"""
Author    :   eeyu
Date      :   2019/4/23 13:22
File Name :   P429NAryTreeLevelOrderTraversal.py
Description :   
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/23     eeyu   Initial creation
    
"""
# coding: utf-8

from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class P429NAryTreeLevelOrderTraversal(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        else:
            return self.level_order_traverse_tree(root)

    def level_order_traverse_tree(self, root):
        q = deque()
        q.append(root)
        result_list = []

        while len(q) != 0:
            res = []
            size = len(q)
            for i in range(size):
                item = q.popleft()
                res.append(item.val)
                for child in item.children:
                    q.append(child)
            result_list.append(res)
        return result_list

if __name__ == '__main__':
    n2 = Node(2, [])
    n4 = Node(4, [])
    n5 = Node(5, [])
    n6 = Node(6, [])
    n3 = Node(3, [n5, n6])
    n1 = Node(1, [n3, n2, n4])

    print(P429NAryTreeLevelOrderTraversal().levelOrder(n1))