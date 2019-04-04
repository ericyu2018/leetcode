"""
Author    :   eeyu
Date      :   2019/4/4 15:19
File Name :   P16ThreeSumClosest.py
Description :   https://leetcode-cn.com/problems/3sum-closest
Problem:
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to
target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/4     eeyu   Initial creation
    
"""
# coding: utf-8


class P16ThreeSumClosest(object):
    def three_sum_closest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if len(nums) <= 2:
            return 0

        nums.sort()
        current_closest_sum = nums[0] + nums[1] + nums[len(nums) - 1]
        for i in range(0, len(nums)-2):
            head = i + 1
            tail = len(nums)-1

            while head < tail:
                temp_sum = nums[i] + nums[head] + nums[tail]
                if abs(temp_sum - target) < abs(current_closest_sum - target):
                    current_closest_sum = temp_sum

                if target <= temp_sum:
                    tail -= 1
                else:
                    head += 1

        return current_closest_sum

if __name__ == '__main__':
    print(P16ThreeSumClosest().three_sum_closest([-1, 2, 1, -4], 1))

