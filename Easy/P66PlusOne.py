"""
Author    :   eeyu
Date      :   2019/3/7 10:28
File Name :   P66PlusOne.py
Description :  https://leetcode-cn.com/problems/plus-one/
Problem:
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/7     eeyu   Initial creation
    
"""
# coding: utf-8


class P66PlusOne(object):

    @staticmethod
    def plus_one(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if digits is None or len(digits) == 0:
            return list()
        else:
            digits_str = ''
            for index in range(0, len(digits)):
                digits_str = digits_str + str(digits[index])

            try:
                digits_int = int(digits_str)
            except ValueError:
                return list()

            digits_int = digits_int + 1
            return [int(x) for x in list(str(digits_int))]

if __name__ == '__main__':
    print(P66PlusOne.plus_one([1,2,3]))
    print(P66PlusOne.plus_one([4,3,2,1]))
    print(P66PlusOne.plus_one([9]))
    print(P66PlusOne.plus_one([9,9,9]))
    print(P66PlusOne.plus_one(None))
    print(P66PlusOne.plus_one(list()))
    print(P66PlusOne.plus_one([9, 'B', 9]))

