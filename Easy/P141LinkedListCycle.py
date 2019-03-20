"""
Author    :   eeyu
Date      :   2019/3/20 21:26
File Name :   P141LinkedListCycle.py
Description :  https://leetcode-cn.com/problems/linked-list-cycle
Problem:
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the
 linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.


Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Follow up:
Can you solve it using O(1) (i.e. constant) memory?
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/20     eeyu   Initial creation
    
"""
# coding: utf-8


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class P141LinkedListCycle(object):
    def has_cycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node_collection = set()

        if head is None:
            return False

        node = head
        while node is not None:
            if node in node_collection:
                return True
            else:
                node_collection.add(node)
                node = node.next

        return False

if __name__ == '__main__':
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(4)

    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n1

    print(P141LinkedListCycle().has_cycle(n1))

