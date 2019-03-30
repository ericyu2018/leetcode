"""
Author    :   eeyu
Date      :   2019/3/14 9:55
File Name :   P110BalancedBinaryTree.py
Description : https://leetcode-cn.com/problems/balanced-binary-tree/
Problem:
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/14     eeyu   Initial creation
    
"""
# coding: utf-8


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class P110BalancedBinaryTree(object):
    def is_balanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            left_tree_depth = self.tree_depth(root.left, 1)
            right_tree_depth = self.tree_depth(root.right, 1)

            delta = abs(left_tree_depth - right_tree_depth)

            if delta > 1:
                return False
            else:
                return self.is_balanced(root.left) and self.is_balanced(root.right)

    def tree_depth(self, node, depth):
        if node is None:
            return depth
        else:
            return max(self.tree_depth(node.left, depth + 1), self.tree_depth(node.right, depth + 1))



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

    print(P110BalancedBinaryTree().tree_depth(n1, 0))
    print(P110BalancedBinaryTree().is_balanced(n1))
