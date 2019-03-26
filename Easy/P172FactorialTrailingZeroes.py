"""
Author    :   eeyu
Date      :   2019/3/26 11:27
File Name :   P172FactorialTrailingZeroes.py
Description :   https://leetcode-cn.com/problems/factorial-trailing-zeroes
Problem:
Given an integer n, return the number of trailing zeroes in n!.

Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/26     eeyu   Initial creation
    
"""
# coding: utf-8


class P172FactorialTrailingZeroes(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        zero_count = 0
        while n != 0:
            n = n//5
            zero_count += n

        return zero_count

if __name__ == '__main__':
    print(P172FactorialTrailingZeroes().trailingZeroes(15))