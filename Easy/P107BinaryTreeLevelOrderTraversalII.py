"""
Author    :   eeyu
Date      :   2019/3/13 11:36
File Name :   P107BinaryTreeLevelOrderTraversalII.py
Description :  https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/13     eeyu   Initial creation
    
"""
# coding: utf-8
import queue
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class P107BinaryTreeLevelOrderTraversalII(object):
    def level_order_bottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        tree_depth = 0
        my_queue = queue.Queue()
        my_list = list()
        result_dict = dict()

        my_queue.put((tree_depth, root))
        while my_queue.qsize() != 0:
            tree_depth, node = my_queue.get()

            if node is not None:
                my_list.append((tree_depth, node.val))
                my_queue.put((tree_depth + 1, node.left))
                my_queue.put((tree_depth + 1, node.right))
            else:
                my_list.append((tree_depth, 'null'))

        for tuple_item in my_list:
            level_number = tuple_item[0]
            if level_number in result_dict.keys():
                result_dict[level_number].append(tuple_item[1])
            else:
                temp = list()
                temp.append(tuple_item[1])
                result_dict[level_number] = temp

        my_list.clear()
        for i in range(len(result_dict)-2, -1, -1):
            while 'null' in result_dict[i]:
                result_dict[i].remove('null')
            my_list.append(result_dict[i])
        return my_list

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        stack = [root]
        ans = []

        while stack:
            tmp_stack = []
            tmp_ans = []
            for i in stack:
                tmp_ans.append(i.val)
                if i.left:
                    tmp_stack.append(i.left)
                if i.right:
                    tmp_stack.append(i.right)
            stack = tmp_stack
            ans.append(tmp_ans)

        return ans[::-1]

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    print(P107BinaryTreeLevelOrderTraversalII().level_order_bottom(n1))
    print(P107BinaryTreeLevelOrderTraversalII().level_order_bottom(None))

    print(P107BinaryTreeLevelOrderTraversalII().levelOrderBottom(n1))
    print(P107BinaryTreeLevelOrderTraversalII().levelOrderBottom(None))