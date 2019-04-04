"""
Author    :   eeyu
Date      :   2019/4/4 10:51
File Name :   P258AddDigits.py
Description :   https://leetcode-cn.com/problems/add-digits
Problem:
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/4     eeyu   Initial creation
    
"""
# coding: utf-8

class P258AddDigits(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num > 0:
            return 1 + (num -1)% 9
        else:
            return 0

    def addDigits2(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num > 9:
            num = num % 9
            if num == 0:
                return 9

        return num


if __name__ == '__main__':
    print(P258AddDigits().addDigits(899897))
    print(P258AddDigits().addDigits2(899897))