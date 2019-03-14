"""
Author    :   eeyu
Date      :   2019/2/26 10:55
File Name :   P7ReverseInteger.py
Description :  https://leetcode-cn.com/problems/reverse-integer/
Problem:
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−2^31,  2^31 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/2/26     eeyu   Initial creation
    
"""
# coding: utf-8


class P7ReverseInteger(object):
    @staticmethod
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0

        x_str = str(x)
        if x_str.endswith('0'):
            return P7ReverseInteger.reverse(int(x/10))

        if x_str.startswith('-'):
            return -1 * P7ReverseInteger.reverse(x * (-1))

        x_list = list(x_str)
        x_list.reverse()

        x_reversed_str = ''
        for item in x_list:
            x_reversed_str = x_reversed_str + item

        try:
            result = int(x_reversed_str)
        except OverflowError:
            result = 0

        if result > pow(2, 31) - 1 or result < - pow(2, 31):
            return 0
        else:
            return result

    @staticmethod
    def reverse2(x):
        rev_value = 0

        if x == 0:
            return 0

        if abs(x) != x:
            return -1 * P7ReverseInteger.reverse2(abs(x))

        while x != 0:
            q, r = divmod(x, 10)
            x = q

            try:
                rev_value = rev_value * 10 + r
            except OverflowError:
                rev_value = 0

        if rev_value > pow(2, 31) - 1 or rev_value < - pow(2, 31):
            return 0
        else:
            return rev_value

if __name__ == '__main__':
    print(P7ReverseInteger.reverse(123))
    print(P7ReverseInteger.reverse(321))
    print(P7ReverseInteger.reverse(0))
    print(P7ReverseInteger.reverse(120))
    print(P7ReverseInteger.reverse(-321))
    print(P7ReverseInteger.reverse(123))
    print(P7ReverseInteger.reverse(1534236469))
    print(P7ReverseInteger.reverse(1563847412))

    print(P7ReverseInteger.reverse2(123))
    print(P7ReverseInteger.reverse2(-321))
    print(P7ReverseInteger.reverse2(0))
    print(P7ReverseInteger.reverse2(1534236469))
    print(P7ReverseInteger.reverse2(1563847412))
