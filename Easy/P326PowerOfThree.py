"""
Author    :   eeyu
Date      :   2019/4/11 11:59
File Name :   P326PowerOfThree.py
Description :   https://leetcode-cn.com/problems/power-of-three/
Problem:
Given an integer, write a function to determine if it is a power of three.

Example 1:
Input: 27
Output: true

Example 2:
Input: 0
Output: false

Example 3:
Input: 9
Output: true

Example 4:
Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/11     eeyu   Initial creation
    
"""
# coding: utf-8


class P326PowerOfThree(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        possible_power_of_three_list = [pow(3, x) for x in range(0, 40)]
        if n in possible_power_of_three_list:
            return True
        else:
            return False

if __name__ == '__main__':
    print(P326PowerOfThree().isPowerOfThree(-1))
    print(P326PowerOfThree().isPowerOfThree(0))
    print(P326PowerOfThree().isPowerOfThree(1))
    print(P326PowerOfThree().isPowerOfThree(2))
    print(P326PowerOfThree().isPowerOfThree(3))
    print(P326PowerOfThree().isPowerOfThree(6))
    print(P326PowerOfThree().isPowerOfThree(9))
    print(P326PowerOfThree().isPowerOfThree(18))
    print(P326PowerOfThree().isPowerOfThree(21))
    print(P326PowerOfThree().isPowerOfThree(27))