"""
Author    :   eeyu
Date      :   2019/2/27 13:42
File Name :   P35SearchInsertPosition.py
Description :   https://leetcode-cn.com/problems/search-insert-position/
Problem:
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 4:
Input: [1,3,5,6], 0
Output: 0
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/2/27     eeyu   Initial creation
    
"""
# coding: utf-8


class SearchInsertPosition(object):
    @staticmethod
    def search_insert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = high = 0
        nums.sort()

        if nums[0] > target:
            return 0

        if nums[len(nums) - 1] < target:
            return len(nums)

        for index in range(0, len(nums)):
            if nums[index] == target:
                return index

            elif nums[index] < target:
                low = index
            else:
                high = index

        return min(low, high) + 1


if __name__ == "__main__":
    print(SearchInsertPosition.search_insert([1, 3, 5, 6], 5))
    print(SearchInsertPosition.search_insert([1, 3, 5, 6], 2))
    print(SearchInsertPosition.search_insert([1, 3, 5, 6], 7))
    print(SearchInsertPosition.search_insert([1, 3, 5, 6], 0))
