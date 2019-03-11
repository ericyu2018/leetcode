"""
Author    :   eeyu
Date      :   2019/3/11 15:16
File Name :   P88MergeSortedArray.py
Description :   https://leetcode-cn.com/problems/merge-sorted-array/
Problem:
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/11     eeyu   Initial creation
    
"""
# coding: utf-8


class P88MergeSortedArray(object):

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        if len(nums1) - m < n:
            raise Exception('Not enough space in nums1')

        for item in nums2:
            nums1[m] = item
            m = m + 1

        nums1.sort()

if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]

    P88MergeSortedArray().merge(nums1, 3, nums2, 3)
    print(nums1)
