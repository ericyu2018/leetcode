"""
Author    :   eeyu
Date      :   2019/3/8 10:15
File Name :   P69Sqrtx.py
Description :   https://leetcode-cn.com/problems/sqrtx/
Problem:
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/8     eeyu   Initial creation
    
"""
# coding: utf-8
import math

class P69Sqrtx(object):

    @staticmethod
    def my_Sqrt(x):
        """
        :type x: int
        :rtype: int
        """
        if not isinstance(x, int):
            raise TypeError('x should be integer')

        if x < 0:
            raise ValueError('x should be positive value')

        return int(math.sqrt(x))

    @staticmethod
    def my_Sqrt2(x):
        return int(pow(x, 1/2))


if __name__ == '__main__':
    try:
       # print(P69Sqrtx.my_Sqrt(3.14))
       # print(P69Sqrtx.my_Sqrt(-7))
        print(P69Sqrtx.my_Sqrt(8))
        print(P69Sqrtx.my_Sqrt2(8))
    except Exception as e:
        print(e)
