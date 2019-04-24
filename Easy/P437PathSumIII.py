"""
Author    :   eeyu
Date      :   2019/4/24 15:06
File Name :   P437PathSumIII.py
Description :  https://leetcode-cn.com/problems/path-sum-iii/
Problem:
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/24     eeyu   Initial creation
    
"""
# coding: utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class P437PathSumIII(object):
    def __init__(self):
        self. result = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        if root is None:
            return 0
        else:
            self.mypathsum(root, sum)
            self.pathSum(root.left, sum)
            self.pathSum(root.right, sum)
            return self.result

    def mypathsum(self, root, sum):
        if root is None:
            return
        else:
            sum -= root.val

        if sum == 0:
            self.result += 1

        self.mypathsum(root.left, sum)
        self.mypathsum(root.right, sum)

if __name__ == '__main__':
    n1 = TreeNode(10)
    n2 = TreeNode(5)
    n3 = TreeNode(-3)
    n4 = TreeNode(3)
    n5 = TreeNode(2)
    n6 = TreeNode(11)
    n7 = TreeNode(3)
    n8 = TreeNode(-2)
    n9 = TreeNode(1)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.right = n6
    n4.left = n7
    n4.right = n8
    n5.right = n9

    print(P437PathSumIII().pathSum(n1, 8))
