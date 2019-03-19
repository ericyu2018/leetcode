"""
Author    :   eeyu
Date      :   2019/3/19 10:48
File Name :   P136SingleNumber.py
Description :   https://leetcode-cn.com/problems/single-number/
Problem:
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/19     eeyu   Initial creation
    
"""
# coding: utf-8


class P136SingleNumber(object):
    def single_number(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        for index in range(0, len(nums)):
            if index - 1 < 0:
                if nums[index] != nums[index + 1]:
                    return nums[index]

            if index + 1 < len(nums):
                if nums[index - 1] != nums[index] and nums[index] != nums[index + 1]:
                    return nums[index]
            else:
                return nums[index]



if __name__ == '__main__':
    print(P136SingleNumber().single_number([2, 2, 1]))
    print(P136SingleNumber().single_number([4, 1, 2, 1, 2]))
