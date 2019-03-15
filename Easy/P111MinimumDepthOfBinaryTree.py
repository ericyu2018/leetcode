"""
Author    :   eeyu
Date      :   2019/3/15 9:37
File Name :   P111MinimumDepthOfBinaryTree.py
Description :  https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/
Problem:
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/15     eeyu   Initial creation
    
"""
# coding: utf-8


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class P111MinimumDepthOfBinaryTree(object):
    def min_depth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            if root.left and root.right:
                return 1 + min(self.min_depth(root.left), self.min_depth(root.right))
            elif root.left:
                return 1 + self.min_depth(root.left)
            elif root.right:
                return 1 + self.min_depth(root.right)
            else:
                return 1


if __name__ == '__main__':
    n1 = TreeNode(3)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n4 = None
    n5 = None
    n6 = TreeNode(15)
    n7 = TreeNode(7)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    print(P111MinimumDepthOfBinaryTree().min_depth(n1))