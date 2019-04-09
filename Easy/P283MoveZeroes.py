"""
Author    :   eeyu
Date      :   2019/4/9 11:32
File Name :   P283MoveZeroes.py
Description :  https://leetcode-cn.com/problems/move-zeroes/
Problem:
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/9     eeyu   Initial creation
    
"""
# coding: utf-8


class P283MoveZeroes(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return

        temp_nums = list()

        zero_count = nums.count(0)

        while zero_count != 0:
            temp_nums.append(0)
            zero_count -= 1

        j = 0
        for index in range(0, len(nums)):
            if nums[index] != 0:
                temp_nums.insert(j, nums[index])
                j += 1

        for index in range(0, len(nums)):
            nums[index] = temp_nums[index]

        print(nums)

if __name__ == '__main__':
    P283MoveZeroes().moveZeroes([0,1,0,3,12])