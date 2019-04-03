"""
Author    :   eeyu
Date      :   2019/4/3 10:20
File Name :   P237DeleteNodeInALinkedList.py
Description :   https://leetcode-cn.com/problems/delete-node-in-a-linked-list/
Problem:
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

Note:
The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/3     eeyu   Initial creation
    
"""
# coding: utf-8

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class P237DeleteNodeInALinkedList(object):
    def delete_node(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        if node is None or node.next is None:
            return
        else:
            node.val = node.next.val
            node.next = node.next.next

    def traverse_list(self, head):
        while head is not None:
            print(head.val, end=" ")
            head = head.next

if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6

    P237DeleteNodeInALinkedList().traverse_list(n1)
    print()
    P237DeleteNodeInALinkedList().delete_node(n3)
    P237DeleteNodeInALinkedList().traverse_list(n1)




