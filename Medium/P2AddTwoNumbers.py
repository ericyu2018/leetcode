"""
Author    :   eeyu
Date      :   2019/3/25 16:32
File Name :   P2AddTwoNumbers.py
Description :  https://leetcode-cn.com/problems/add-two-numbers/
Problem:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/25     eeyu   Initial creation
    
"""
# coding: utf-8
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class P2AddTwoNumbers(object):
    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy_node = ListNode(0)
        p = l1
        q = l2
        current_node = dummy_node
        carry = 0

        while p is not None or q is not None:
            if p is None:
                x = 0
            else:
                x = p.val

            if q is None:
                y = 0
            else:
                y = q.val

            sum = x + y + carry

            s, r = divmod(sum, 10)
            carry = int(s)
            current_node.next = ListNode(r)
            current_node = current_node.next

            if p is not None:
                p = p.next

            if q is not None:
                q = q.next

        if carry > 0:
            current_node.next = ListNode(1)

        return dummy_node.next

if __name__ == '__main__':
    l1_n1 = ListNode(2)
    l1_n2 = ListNode(4)
    l1_n3 = ListNode(3)
    l1_n1.next = l1_n2
    l1_n2.next = l1_n3

    l2_n1 = ListNode(5)
    l2_n2 = ListNode(6)
    l2_n3 = ListNode(4)
    l2_n1.next = l2_n2
    l2_n2.next = l2_n3

    result_list_node = P2AddTwoNumbers().add_two_numbers(l1_n1, l2_n1)


    while result_list_node is not None:
        print(result_list_node.val, end=' ')
        result_list_node = result_list_node.next
