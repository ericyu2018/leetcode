"""
Author    :   eeyu
Date      :   2019/2/28 10:09
File Name :   P9PalindromeNumber.py
Description :   https://leetcode-cn.com/problems/palindrome-number/
Problem:
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Could you solve it without converting the integer to a string?
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/2/28     eeyu   Initial creation
    
"""
# coding: utf-8

class P9PalindromeNumber(object):

    @staticmethod
    def is_palindrome(x):
        """
        Check if integer number x is palindrom
        :param x: integer number
        :return: True if integer number x is palindrom, else returns False
        """
        if not isinstance(x, int):
            return False

        if abs(x) != x:
            return False

        x_copy = x
        remainder_list = list()
        while x != 0:
            quotient, remainder = divmod(x, 10)
            remainder_list.append(remainder)
            x = quotient

        remainder_list_length = len(remainder_list)
        result = 0
        while remainder_list_length > 0:
            result = remainder_list.pop(0) * pow(10, remainder_list_length - 1) + result
            remainder_list_length = remainder_list_length - 1

        return x_copy == result


if __name__ == '__main__':
    print(P9PalindromeNumber.is_palindrome(123))
    print(P9PalindromeNumber.is_palindrome(121))
    print(P9PalindromeNumber.is_palindrome(-121))
    print(P9PalindromeNumber.is_palindrome(0))
