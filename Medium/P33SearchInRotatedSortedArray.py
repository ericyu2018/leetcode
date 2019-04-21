"""
Author    :   eeyu
Date      :   2019/4/21 10:28
File Name :   P33SearchInRotatedSortedArray.py
Description :  https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
Problem:
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/21     eeyu   Initial creation
    
"""
# coding: utf-8

class P33SearchInRotatedSortedArray(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if target not in nums:
            return -1
        else:
            rotate_index = 0
            for index in range(0, len(nums)):
                if index + 1 < len(nums) and nums[index] > nums[index + 1]:
                    rotate_index = index + 1
                    break

            list_with_large_values = nums[0:rotate_index]
            list_with_small_values = nums[rotate_index:]
            if len(list_with_large_values) > 0 and target >= list_with_large_values[0]:
                return self.binary_search(list_with_large_values, target)
            else:
                return len(list_with_large_values) + self.binary_search(list_with_small_values, target)

    def binary_search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + int((high - low) / 2)
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid -1
            else:
                return mid

        return -1


if __name__ == '__main__':
    print(P33SearchInRotatedSortedArray().search([4, 5, 6, 7, 0, 1, 2], 0))
    print(P33SearchInRotatedSortedArray().search([4, 5, 6, 7, 0, 1, 2], 3))
    print(P33SearchInRotatedSortedArray().search([4, 5, 6, 7, 0, 1, 2], 4))
    print(P33SearchInRotatedSortedArray().search([4, 5, 6, 7, 0, 1, 2], 2))
    print(P33SearchInRotatedSortedArray().search([4, 5], 4))
    print(P33SearchInRotatedSortedArray().search([4, 5], 5))
    print(P33SearchInRotatedSortedArray().search([1], 1))
