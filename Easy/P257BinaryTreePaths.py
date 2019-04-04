"""
Author    :   eeyu
Date      :   2019/4/4 13:13
File Name :   P257BinaryTreePaths.py
Description :   https://leetcode-cn.com/problems/binary-tree-paths/
Problem:
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/4     eeyu   Initial creation
    
"""
# coding: utf-8


# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class P257BinaryTreePaths(object):
    def __init__(self):
        self.__result_list = list()
        self.__first_node = None

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.__first_node = root
        self.get_child(self.__first_node, '')
        return self.__result_list

    def get_child(self, root, path):
        if root is None:
            return
        if root == self.__first_node:
            path = str(root.val)
        else:
            path = '{0}->{1}'.format(path, str(root.val))

        if root.left is None and root.right is None:
            self.__result_list.append(path)

        self.get_child(root.left, path)
        self.get_child(root.right, path)


    def traverse(self, root):
        if root is not None:
            self.traverse(root.left)
            print(root.val, end='->')
            self.traverse(root.right)


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(5)

    n1.left = n2
    n1.right = n3
    n2.right = n4

    btp =  P257BinaryTreePaths()
    btp.traverse(n1)
    print()
    print(btp.binaryTreePaths(n1))

