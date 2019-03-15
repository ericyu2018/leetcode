"""
Author    :   eeyu
Date      :   2019/3/15 11:02
File Name :   P112PathSum.py
Description :   https://leetcode-cn.com/problems/path-sum/
Problem:
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along
the path equals the given sum.

Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
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


class P112PathSum(object):
    def has_path_sum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        elif root.left is None and root.right is None:
            return root.val == sum
        else:
            return self.has_path_sum(root.left, sum - root.val) or self.has_path_sum(root.right, sum - root.val)

if __name__ == '__main__':
    n1 = TreeNode(5)
    n2 = TreeNode(4)
    n3 = TreeNode(8)
    n4 = TreeNode(11)
    n5 = None
    n6 = TreeNode(13)
    n7 = TreeNode(4)
    n8 = TreeNode(7)
    n9 = TreeNode(2)
    n10 = None
    n11 = TreeNode(1)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n4.right = n9
    n7.left = n10
    n7.right = n11

    print(P112PathSum().has_path_sum(n1, 22))