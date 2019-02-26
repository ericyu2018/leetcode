"""
Author    :   eeyu
Date      :   2019/2/25 21:14
File Name :   P1TwoSum.py
Description :   https://leetcode-cn.com/problems/two-sum/solution/
Problem：
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/2/25     eeyu   Initial creation
    
"""
# coding: utf-8


class P1TwoSum(object):
    @staticmethod
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = 0
        while i < len(nums):
            while j < len(nums):
                if i != j and nums[i] + nums[j] == target:
                    return i, j
                else:
                    j = j + 1
            i = i + 1

        raise Exception('no solution')

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(list(P1TwoSum.two_sum(nums, target)))

