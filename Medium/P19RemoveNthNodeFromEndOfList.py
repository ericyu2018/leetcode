"""
Author    :   eeyu
Date      :   2019/4/15 10:41
File Name :   P19RemoveNthNodeFromEndOfList.py
Description : https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
Problem:
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/15     eeyu   Initial creation
    
"""
# coding: utf-8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class P19RemoveNthNodeFromEndOfList(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        stack = list()
        current = head
        original_count = n

        while current is not None:
            stack.append(current)
            current = current.next

        while n > 0:
            stack.pop()
            n -= 1

        if len(stack) != 0:
            node = stack.pop()
            node.next = node.next.next
        else:
            if original_count == 1:
                return None
            else:
                head = head.next

        return head

    def traverse_linked_list(self, head):
        while head is not None:
            print(head.val, end="->")
            head = head.next

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

    test = P19RemoveNthNodeFromEndOfList()
    test.traverse_linked_list(test.removeNthFromEnd(n1,2))