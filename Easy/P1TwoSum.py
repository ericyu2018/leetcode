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

        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

        raise Exception('no solution')

if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    print(list(P1TwoSum.two_sum(nums, target)))

