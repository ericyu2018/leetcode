"""
Author    :   eeyu
Date      :   2019/4/22 13:37
File Name :   P34FindFirstAndLastPositionOfElementInSortedArray.py
Description :   https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Problem:
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/22     eeyu   Initial creation
    
"""
# coding: utf-8


class P34FindFirstAndLastPositionOfElementInSortedArray(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if target not in nums:
            return [-1, -1]
        else:
            possible_index = self.binary_search(nums, target)
            result_list = list()
            low_index, high_index = -1, -1
            for i in range(1, int(len(nums)/2) + 1):
                if nums[possible_index] == nums[possible_index-i]:
                    low_index = possible_index-i

                if possible_index + i < len(nums) and nums[possible_index] == nums[possible_index + i]:
                    high_index = possible_index + i

            if low_index != -1:
                result_list.append(low_index)
            if high_index != -1:
                result_list.append(high_index)
            result_list.append(possible_index)
            result_list.sort()

            return [result_list[0], result_list[-1]]

    def binary_search(self, nums, target):
        low = 0
        high = len(nums)
        while low <= high:
            mid = low + int((high - low)/2)
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid -1
            else:
                return mid

        return -1


if __name__ == '__main__':
    print(P34FindFirstAndLastPositionOfElementInSortedArray().searchRange([5, 7, 7, 8, 8, 10], 8))
    print(P34FindFirstAndLastPositionOfElementInSortedArray().searchRange([5, 7, 7, 8, 8, 10], 6))
    print(P34FindFirstAndLastPositionOfElementInSortedArray().searchRange([5, 7, 7, 8, 8, 10], 10))
    print(P34FindFirstAndLastPositionOfElementInSortedArray().searchRange([2, 2], 2))
