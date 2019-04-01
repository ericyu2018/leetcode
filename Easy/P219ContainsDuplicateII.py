"""
Author    :   eeyu
Date      :   2019/4/1 11:39
File Name :   P219ContainsDuplicateII.py
Description :   https://leetcode-cn.com/problems/contains-duplicate-ii/
Problem:
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/1     eeyu   Initial creation
    
"""
# coding: utf-8


class P219ContainsDuplicateII(object):
    def contains_nearby_duplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        if len(nums) == len(set(nums)):
            return False

        item_index_mapping = dict()

        for index in range(0, len(nums)):
            if nums[index] not in item_index_mapping.keys():
                item_index_mapping[nums[index]] = index
            else:
                if abs(index - item_index_mapping[nums[index]]) <= k:
                    return True
                else:
                    item_index_mapping[nums[index]] = index
        return False

if __name__ == '__main__':
    print(P219ContainsDuplicateII().contains_nearby_duplicate([1, 2, 3, 1], 3))
    print(P219ContainsDuplicateII().contains_nearby_duplicate([1,0,1,1], 1))
    print(P219ContainsDuplicateII().contains_nearby_duplicate([1,2,3,1,2,3], 2))