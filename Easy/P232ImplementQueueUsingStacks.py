"""
Author    :   eeyu
Date      :   2019/4/2 9:45
File Name :   P232ImplementQueueUsingStacks.py
Description : https://leetcode-cn.com/problems/implement-queue-using-stacks/
Problem:
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/2     eeyu   Initial creation
    
"""
# coding: utf-8


class P232ImplementQueueUsingStacks(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__queue = list()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.__queue.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.__queue) != 0:
            return self.__queue.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.__queue) != 0:
            return self.__queue[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.__queue) == 0

if __name__ == '__main__':
    my_queue = P232ImplementQueueUsingStacks()
    my_queue.push(1)
    my_queue.push(2)
    print(my_queue.peek())
    print(my_queue.pop())
    print(my_queue.peek())
    print(my_queue.empty())
