"""
Author    :   eeyu
Date      :   2019/4/12 10:48
File Name :   P349IntersectionOfTwoArrays.py
Description :  https://leetcode-cn.com/problems/intersection-of-two-arrays/
Problem:
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/12     eeyu   Initial creation
    
"""
# coding: utf-8

class P349IntersectionOfTwoArrays(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        return list(set(nums1) & set(nums2))

if __name__ == '__main__':
    print(P349IntersectionOfTwoArrays().intersection([1, 2, 2, 1], [2, 2]))
    print(P349IntersectionOfTwoArrays().intersection([4,9,5], [9,4,9,8,4]))