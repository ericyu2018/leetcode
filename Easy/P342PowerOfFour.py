"""
Author    :   eeyu
Date      :   2019/4/11 13:01
File Name :   P342PowerOfFour.py
Description :  https://leetcode-cn.com/problems/power-of-four/
Problem:
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:
Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/11     eeyu   Initial creation
    
"""
# coding: utf-8


class P342PowerOfFour(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        possible_power_of_four_list = [pow(4, x) for x in range(0, 32)]
        if num in possible_power_of_four_list:
            return True
        else:
            return False

if __name__ == '__main__':
    print(P342PowerOfFour().isPowerOfFour(-1))
    print(P342PowerOfFour().isPowerOfFour(0))
    print(P342PowerOfFour().isPowerOfFour(1))
    print(P342PowerOfFour().isPowerOfFour(2))
    print(P342PowerOfFour().isPowerOfFour(3))
    print(P342PowerOfFour().isPowerOfFour(4))
    print(P342PowerOfFour().isPowerOfFour(8))
    print(P342PowerOfFour().isPowerOfFour(16))
    print(P342PowerOfFour().isPowerOfFour(32))
    print(P342PowerOfFour().isPowerOfFour(64))