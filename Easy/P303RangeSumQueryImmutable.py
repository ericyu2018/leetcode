"""
Author    :   eeyu
Date      :   2019/4/10 11:04
File Name :   P303RangeSumQueryImmutable.py
Description :   https://leetcode-cn.com/problems/range-sum-query-immutable/
Problem:
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:
You may assume that the array does not change.
There are many calls to sumRange function.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/10     eeyu   Initial creation
    
"""
# coding: utf-8

class P303RangeSumQueryImmutable(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """

        return sum(self.nums[i:j+1])

if __name__ == '__main__':
    obj = P303RangeSumQueryImmutable([-2, 0, 3, -5, 2, -1])
    print(obj.sumRange(0, 2))
    print(obj.sumRange(2, 5))
    print(obj.sumRange(0, 5))