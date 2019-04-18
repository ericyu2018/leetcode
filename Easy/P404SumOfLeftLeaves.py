"""
Author    :   eeyu
Date      :   2019/4/18 10:58
File Name :   P404SumOfLeftLeaves.py
Description :   https://leetcode-cn.com/problems/sum-of-left-leaves/
Find the sum of all left leaves in a given binary tree.
Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/18     eeyu   Initial creation
    
"""
# coding: utf-8


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class P404SumOfLeftLeaves(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            if root.left is not None:
                if root.left.left is None and root.left.right is None:
                    return root.left.val + self.sumOfLeftLeaves(root.right)
                else:
                    return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
            else:
                return self.sumOfLeftLeaves(root.right)

if __name__ == '__main__':
    n1 = TreeNode(3)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n4 = TreeNode(15)
    n5 = TreeNode(7)

    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5

    print(P404SumOfLeftLeaves().sumOfLeftLeaves(n1))
