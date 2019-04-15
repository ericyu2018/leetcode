"""
Author    :   eeyu
Date      :   2019/4/15 10:35
File Name :   P371SumOfTwoIntegers.py
Description :   https://leetcode-cn.com/problems/sum-of-two-integers
Problem:
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = -2, b = 3
Output: 1
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/15     eeyu   Initial creation
    
"""
# coding: utf-8

class P371SumOfTwoIntegers(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        return sum([a, b])