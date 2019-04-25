"""
Author    :   eeyu
Date      :   2019/3/29 9:36
File Name :   P206ReverseLinkedList.py
Description : https://leetcode-cn.com/problems/reverse-linked-list/
Problem:
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/29     eeyu   Initial creation
    
"""
# coding: utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class P206ReverseLinkedList(object):

    def reverse_list2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head
        else:
            node_stack = list()
            current_node = head
            result_node = None
            return_node = None

            while current_node is not None:
                node_stack.append(current_node)
                current_node = current_node.next

            while len(node_stack) > 0:
                current_node = node_stack.pop()
                print(current_node.val)

                if result_node is None:
                    result_node = current_node
                    assert result_node.next is None, 'Last node next is not None'
                    return_node = result_node
                else:
                    result_node.next = current_node
                    result_node = result_node.next
            result_node.next = None
            return return_node

    def traverse_linked_list(self, head):
        node = head
        while node is not None:
            print(node.val, end='->')
            node = node.next
        print('NULL')

    def reverse_list(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        previous = None
        current = head

        while current is not None:
            next_temp = current.next
            current.next = previous
            previous = current
            current = next_temp

        return previous

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

    r = P206ReverseLinkedList()
    r.traverse_linked_list(n1)
    result = r.reverse_list(n1)
    r.traverse_linked_list(result)


