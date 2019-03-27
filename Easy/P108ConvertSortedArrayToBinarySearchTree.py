"""
Author    :   eeyu
Date      :   2019/3/14 12:40
File Name :   P108ConvertSortedArrayToBinarySearchTree.py
Description :   https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
Problem:
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of
every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
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

class P108ConvertSortedArrayToBinarySearchTree(object):
    def sorted_array_to_BST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None or len(nums) == 0:
            return None

        nums.sort()

        mid = int(len(nums)/2)

        root = TreeNode(nums[mid])
        root.left = self.sorted_array_to_BST(nums[0:mid])
        root.right = self.sorted_array_to_BST(nums[mid+1:])

        return root

    def traverse_tree(self, root):
        if root is not None:
            self.traverse_tree(root.left)
            print(root.val)
            self.traverse_tree(root.right)

if __name__ == '__main__':
    nums = [-100, -88, -50, -10, -3, 0, 5, 9, 70]
    root = P108ConvertSortedArrayToBinarySearchTree().sorted_array_to_BST(nums)
    P108ConvertSortedArrayToBinarySearchTree().traverse_tree(root)



