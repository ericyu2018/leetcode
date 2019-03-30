"""
Author    :   eeyu
Date      :   2019/3/20 14:47
File Name :   P155MinStack.py
Description :   https://leetcode-cn.com/problems/min-stack/
Problem:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/20     eeyu   Initial creation
    
"""
# coding: utf-8

class P155MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = list()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x is not None:
            self.min_stack.append(x)
        else:
            raise ValueError('Invalid x to push')

    def pop(self):
        """
        :rtype: None
        """
        if len(self.min_stack) > 0:
            self.min_stack.pop()
        else:
            raise RuntimeError('Stack empty')

    def top(self):
        """
        :rtype: int
        """
        if len(self.min_stack) > 0:
            return self.min_stack[len(self.min_stack) - 1]
        else:
            raise RuntimeError('Stack empty')

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min_stack) > 0:
            return min(self.min_stack)
        else:
            raise RuntimeError('Stack empty')

if __name__ == '__main__':
    min_stack = P155MinStack()
    min_stack.push(0)
    min_stack.push(1)
    min_stack.push(0)
    print(min_stack.getMin())
    min_stack.pop()
    print(min_stack.top())
    print(min_stack.getMin())
