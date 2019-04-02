"""
Author    :   eeyu
Date      :   2019/4/2 10:25
File Name :   P234PalindromeLinkedList.py
Description :   https://leetcode-cn.com/problems/palindrome-linked-list/
Problem:
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/2     eeyu   Initial creation
    
"""
# coding: utf-8


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class P234PalindromeLinkedList(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        items_list = list()
        while head is not None:
            items_list.append(head.val)
            head = head.next

        for index in range(0, int(len(items_list)/2)):
            if items_list[index] != items_list[len(items_list) - index -1]:
                return False

        return True

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(2)
    n4 = ListNode(1)

    n1.next = n2
    n2.next = n3
    n3.next = n4

    print(P234PalindromeLinkedList().isPalindrome(n1))


