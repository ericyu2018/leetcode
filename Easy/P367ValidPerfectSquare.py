"""
Author    :   eeyu
Date      :   2019/4/15 10:17
File Name :   P367ValidPerfectSquare.py
Description :  https://leetcode-cn.com/problems/valid-perfect-square/
Problem:
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true

Example 2:
Input: 14
Output: false
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/15     eeyu   Initial creation
    
"""
# coding: utf-8


class P367ValidPerfectSquare(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        i = 1

        while i * i <= num:
            if i * i == num:
                return True
            else:
                i += 1

        return False

if __name__ == '__main__':
    print(P367ValidPerfectSquare().isPerfectSquare(16))
    print(P367ValidPerfectSquare().isPerfectSquare(14))
