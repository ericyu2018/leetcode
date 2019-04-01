"""
Author    :   eeyu
Date      :   2019/4/1 11:56
File Name :   P225ImplementStackUsingQueues.py
Description :  https://leetcode-cn.com/problems/implement-stack-using-queues/
Problem:
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/1     eeyu   Initial creation
    
"""
# coding: utf-8

class P225ImplementStackUsingQueues(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__stack = list()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """

        self.__stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.__stack.pop()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """

        return self.__stack[len(self.__stack)-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.__stack) == 0


if __name__ == '__main__':
    stack = P225ImplementStackUsingQueues()
    stack.push(1)
    stack.push(2)
    print(stack.top())
    print(stack.pop())
    print(stack.empty())
