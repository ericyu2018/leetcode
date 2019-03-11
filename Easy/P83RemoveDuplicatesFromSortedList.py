"""
Author    :   eeyu
Date      :   2019/3/11 12:35
File Name :   P83RemoveDuplicatesFromSortedList.py
Description :   https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
Problem:
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/11     eeyu   Initial creation
    
"""
# coding: utf-8


class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class P83RemoveDuplicatesFromSortedList(object):
    def delete_duplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        current_node = head

        while current_node is not None and current_node.next is not None:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next

        return head

if __name__ == '__main__':

    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(2)

    n1.next = n2
    n2.next = n3
    n3.next = None

    t1 = P83RemoveDuplicatesFromSortedList().delete_duplicates(n1)

    print(t1.val)
    while t1.next is not None:
        print(t1.next.val)
        t1 = t1.next

    print('*' * 50)

    n4 = ListNode(1)
    n5 = ListNode(1)
    n6 = ListNode(2)
    n7 = ListNode(3)
    n8 = ListNode(3)

    n4.next = n5
    n5.next = n6
    n6.next = n7
    n7.next = n8
    n8.next = None

    t2 = P83RemoveDuplicatesFromSortedList().delete_duplicates(n4)

    print(t2.val)
    while t2.next is not None:
        print(t2.next.val)
        t2 = t2.next
