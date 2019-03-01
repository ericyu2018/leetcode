"""
Author    :   eeyu
Date      :   2019/3/1 14:08
File Name :   P21MergeTwoSortedLists.py
Description :   https://leetcode-cn.com/problems/merge-two-sorted-lists/
Problem:
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/1     eeyu   Initial creation
    
"""
# coding: utf-8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class P21MergeTwoSortedLists(object):

    @staticmethod
    def merge_two_lists(l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None and l2 is None:
            return None

        if l1 is None and l2 is not None:
            return l2

        if l1 is not None and l2 is None:
            return l1

        if l1.val > l2.val:
            l2.next = P21MergeTwoSortedLists.merge_two_lists(l1, l2.next)
            return l2
        else:
            l1.next = P21MergeTwoSortedLists.merge_two_lists(l1.next, l2)
            return l1



if __name__ == '__main__':
    L11 = ListNode(1)
    L12 = ListNode(2)
    L13 = ListNode(4)
    L11.next = L12
    L12.next = L13

    L21 = ListNode(1)
    L22 = ListNode(3)
    L23 = ListNode(4)
    L21.next = L22
    L22.next = L23

    result = P21MergeTwoSortedLists.merge_two_lists(L11, L21)
    next = result.next
    while next is not None:
        print(next.val)
        next = next.next
