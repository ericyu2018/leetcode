"""
Author    :   eeyu
Date      :   2019/4/17 10:15
File Name :   P24SwapNodesInPairs.py
Description :   https://leetcode-cn.com/problems/swap-nodes-in-pairs/
Problem:
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/17     eeyu   Initial creation
    
"""
# coding: utf-8

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class P24SwapNodesInPairs(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        current = head
        new_head = None
        new_current = None
        stack = list()
        while current is not None and current.next is not None:
            while len(stack) != 2 and current is not None:
                stack.append(current)
                current = current.next

            while len(stack) != 0:
                if new_head is None:
                    new_head = stack.pop()
                    new_current = new_head
                else:
                    new_current.next = stack.pop()
                    new_current = new_current.next

        if current is not None:
            new_current.next = current
            new_current.next.next = None
        else:
            new_current.next = None

        return new_head

    def traverse_linked_list(self, head):
        while head is not None:
            print(head.val, end='->')
            head = head.next

        print('\n')

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    P24SwapNodesInPairs().traverse_linked_list(n1)
    new_list = P24SwapNodesInPairs().swapPairs(n1)
    P24SwapNodesInPairs().traverse_linked_list(new_list)