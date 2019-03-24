"""
Author    :   eeyu
Date      :   2019/3/12 11:23
File Name :   P101SymmetricTree.py
Description :   https://leetcode-cn.com/problems/symmetric-tree/
Problem:
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/12     eeyu   Initial creation
    
"""
# coding: utf-8


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class P101SymmetricTree(object):
    def is_symmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #return self.is_symmetric_help(root, root)
        return self.is_symmetric_help2(root, root)

    def is_symmetric_help(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        elif t1 is None or t2 is None:
            return False
        elif t1.val == t2.val:
            return self.is_symmetric_help(t1.left, t2.right) and self.is_symmetric_help(t1.right, t2.left)
        else:
            return False

    def is_symmetric_help2(self, t1, t2):
        queue = list()
        queue.append(t1)
        queue.append(t2)

        while len(queue) != 0:
            t1 = queue.pop(0)
            t2 = queue.pop(0)

            if t1 is None and t2 is None:
                continue
            elif t1 is None or t2 is None:
                return False
            elif t1.val != t2.val:
                return False
            else:
                queue.append(t1.left)
                queue.append(t2.right)
                queue.append(t1.right)
                queue.append(t2.left)

        return True

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n4 = TreeNode(3)
    n5 = TreeNode(4)
    n6 = TreeNode(4)
    n7 = TreeNode(3)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7

    print(P101SymmetricTree().is_symmetric(n1))


