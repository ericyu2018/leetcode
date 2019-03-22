"""
Author    :   eeyu
Date      :   2019/3/22 16:29
File Name :   P169MajorityElement.py
Description :   https://leetcode-cn.com/problems/majority-element/
Problem:
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/22     eeyu   Initial creation
    
"""
# coding: utf-8

import math

class P169MajorityElement(object):
    def majority_element(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_length = len(nums)

        if nums_length == 1:
            return nums[0]

        expected_length = math.floor(nums_length/2)

        number_count_mapping = dict()

        for num in nums:
            if num not in number_count_mapping.keys():
                number_count_mapping[num] = nums.count(num)
            else:
                if number_count_mapping.get(num) > expected_length:
                    return num

if __name__ == '__main__':
    print(P169MajorityElement().majority_element([3, 2, 3]))
    print(P169MajorityElement().majority_element([2, 2, 1, 1, 1, 2, 2]))
    print(P169MajorityElement().majority_element([1]))
    print(P169MajorityElement().majority_element([1, 2]))