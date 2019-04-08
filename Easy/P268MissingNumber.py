"""
Author    :   eeyu
Date      :   2019/4/8 10:06
File Name :   P268MissingNumber.py
Description :  https://leetcode-cn.com/problems/missing-number/
Problem:
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/8     eeyu   Initial creation
    
"""
# coding: utf-8


class P268MissingNumber(object):
    def missing_number(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = max(nums)
        nums_length = len(nums)

        full_sum = 0
        i = 0
        while i <= max_value:
            full_sum += i
            i += 1

        if max_value >= nums_length:
            return full_sum - sum(nums)
        else:
            return nums_length

if __name__ == '__main__':
    print(P268MissingNumber().missing_number([3, 0, 1]))
    print(P268MissingNumber().missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(P268MissingNumber().missing_number([0]))
        