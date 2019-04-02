"""
Author    :   eeyu
Date      :   2019/4/2 9:11
File Name :   P226InvertBinaryTree.py
Description :  https://leetcode-cn.com/problems/invert-binary-tree/
Problem:
Invert a binary tree.

Example:
Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/2     eeyu   Initial creation
    
"""
# coding: utf-8


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class P226InvertBinaryTree(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)

        return root

    def invertTree2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None:
            temp = root.left
            root.left = root.right
            root.right = temp

            self.invertTree2(root.left)
            self.invertTree2(root.right)

        return root

    def traverse_tree(self, root):
        if root is not None:
            self.traverse_tree(root.left)
            print(root.val)
            self.traverse_tree(root.right)

if __name__ == '__main__':
    n1 = TreeNode(4)
    n2 = TreeNode(2)
    n3 = TreeNode(7)
    n4 = TreeNode(1)
    n5 = TreeNode(3)
    n6 = TreeNode(6)
    n7 = TreeNode(9)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    P226InvertBinaryTree().traverse_tree(n1)
    print('*' * 60)
    P226InvertBinaryTree().traverse_tree(P226InvertBinaryTree().invertTree2(n1))
