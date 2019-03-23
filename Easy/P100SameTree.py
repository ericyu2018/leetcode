"""
Author    :   eeyu
Date      :   2019/3/12 9:48
File Name :   P100SameTree.py
Description :   https://leetcode-cn.com/problems/same-tree/
Problem:
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
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


class P100SameTree(object):
    def is_same_tree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            return self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right) and p.val == q.val

    def is_same_tree2(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            p_stack = list()
            q_stack = list()

            # push root node of both tree to stacks
            p_stack.append(p)
            q_stack.append(q)

            # when both stacks are not empty
            while len(p_stack) != 0 and len(q_stack) !=0:
                p = p_stack.pop()
                q = q_stack.pop()

                if p.val != q.val:
                    return False

                # check right child
                if p.right is not None:
                    if q.right is not None:
                        p_stack.append(p.right)
                        q_stack.append(q.right)
                    else:
                        return False
                else:
                    if q.right is not None:
                        return False

                # check left child
                if p.left is not None:
                    if q.left is not None:
                        p_stack.append(p.left)
                        q_stack.append(q.left)
                    else:
                        return False
                else:
                    if q.left is not None:
                        return False

            return True

if __name__ == '__main__':
    t1_node1 = TreeNode(1)
    t1_node2 = TreeNode(2)
    t1_node3 = TreeNode(3)
    t1_node4 = TreeNode(4)
    t1_node5 = TreeNode(5)
    t1_node6 = TreeNode(6)
    t1_node7 = TreeNode(7)

    t1_node1.left = t1_node2
    t1_node1.right = t1_node3

    t1_node2.left = t1_node4
    t1_node2.right = t1_node5

    t1_node3.left = t1_node6
    t1_node3.right = t1_node7

    # T2
    t2_node1 = TreeNode(1)
    t2_node2 = TreeNode(2)
    t2_node3 = TreeNode(3)
    t2_node4 = TreeNode(4)
    t2_node5 = TreeNode(5)
    t2_node6 = TreeNode(6)
    t2_node7 = TreeNode(7)

    t2_node1.left = t2_node2
    t2_node1.right = t2_node3

    t2_node2.left = t2_node4
    t2_node2.right = t2_node5

    t2_node3.left = t2_node6
    t2_node3.right = t2_node7

    print(P100SameTree().is_same_tree(t1_node1, t2_node1))
    print(P100SameTree().is_same_tree2(t1_node1, t2_node1))
