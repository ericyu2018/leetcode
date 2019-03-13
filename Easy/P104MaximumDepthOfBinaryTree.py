"""
Author    :   eeyu
Date      :   2019/3/13 9:46
File Name :   P104MaximumDepthOfBinaryTree.py
Description :  https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
Problem:
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.
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

class P104MaximumDepthOfBinaryTree(object):
    def max_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        tree_depth = 0
        my_queue = queue.Queue()

        my_queue.put((tree_depth, root))
        while my_queue.qsize() != 0:
            tree_depth, node = my_queue.get()

            if node is not None:
                print(node.val)
                my_queue.put((tree_depth + 1, node.left))
                my_queue.put((tree_depth + 1, node.right))

        return tree_depth

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

    print(P104MaximumDepthOfBinaryTree().max_depth(n1))
