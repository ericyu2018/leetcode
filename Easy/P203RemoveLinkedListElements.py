"""
Author    :   eeyu
Date      :   2019/3/27 10:15
File Name :   P203RemoveLinkedListElements.py
Description :  https://leetcode-cn.com/problems/remove-linked-list-elements/
Problem:
Remove all elements from a linked list of integers that have value val.

Example:
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/27     eeyu   Initial creation
    
"""
# coding: utf-8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class P203RemoveLinkedListElements(object):
    def remove_elements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        if head is None:
            return None
        else:
            current = head

            while current is not None and current.val == val:
                if current.next is not None:
                    current = current.next
                else:
                    current = None
                head = current

            while current is not None and current.next is not None:
                if current.next.val != val:
                    current = current.next
                else:
                    if current.next.next is not None:
                        current.next = current.next.next
                    else:
                        current.next = None

        return head

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(6)
    n4 = ListNode(3)
    n5 = ListNode(4)
    n6 = ListNode(5)
    n7 = ListNode(6)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    n6.next = n7

    n1 = P203RemoveLinkedListElements().remove_elements(n1, 6)

    while n1 is not None:
        print(n1.val, end=' ')
        n1 = n1.next

