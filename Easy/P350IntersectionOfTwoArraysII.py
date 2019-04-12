"""
Author    :   eeyu
Date      :   2019/4/12 11:19
File Name :   P350IntersectionOfTwoArraysII.py
Description :  https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
Problem:
Given two arrays, write a function to compute their intersection.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/12     eeyu   Initial creation
    
"""
# coding: utf-8

class P350IntersectionOfTwoArraysII(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        result_list = list()
        pure_intersect_list = list(set(nums1) & set(nums2))

        for item in pure_intersect_list:
            count = min(nums1.count(item), nums2.count(item))
            while count != 0:
                result_list.append(item)
                count -= 1

        return result_list

if __name__ == '__main__':
    print(P350IntersectionOfTwoArraysII().intersect([1, 2, 2, 1], [2, 2]))
    print(P350IntersectionOfTwoArraysII().intersect([4, 9, 5], [9, 4, 9, 8, 4]))
    print(P350IntersectionOfTwoArraysII().intersect([3, 1, 2], [1, 1]))
