"""
Author    :   eeyu
Date      :   2019/3/21 16:02
File Name :   P160IntersectionOfTwoLinkedLists.py
Description :   https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/21     eeyu   Initial creation
    
"""
# coding: utf-8

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class P160IntersectionOfTwoLinkedLists(object):
    def get_intersection_node(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None

        self.print_list(headA)
        print()
        self.print_list(headB)
        print()

        node_set = set()

        while headA is not None:
            if headA not in node_set:
                node_set.add(headA)
                headA = headA.next

        while headB is not None:
            if headB not in node_set:
                node_set.add(headB)
                headB = headB.next
            else:
                return headB

        return None

    def print_list(self, head):
        while head is not None:
            print(head.val, end=' ')
            head = head.next

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        b = headB
        while a != b:
            if a is not None:
                a = a.next
            else:
                a = headB

            if b is not None:
                b = b.next
            else:
                b = headA
        print(b.val)
        print(a.val)
        return a

if __name__ == '__main__':
    a1 = ListNode(4)
    a2 = ListNode(1)
    c1 = ListNode(8)
    c2 = ListNode(4)
    c3 = ListNode(5)
    b1 = ListNode(5)
    b2 = ListNode(0)
    b3 = ListNode(1)

    a1.next = a2
    a2.next = c1
    c1.next = c2
    c2.next = c3

    b1.next = b2
    b2.next = b3
    b3.next = c1



    print(P160IntersectionOfTwoLinkedLists().get_intersection_node(a1, b1).val)
    print(P160IntersectionOfTwoLinkedLists().getIntersectionNode(a1, b1).val)
