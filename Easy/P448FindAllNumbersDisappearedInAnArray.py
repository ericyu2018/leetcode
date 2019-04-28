"""
Author    :   eeyu
Date      :   2019/4/28 11:24
File Name :   P448FindAllNumbersDisappearedInAnArray.py
Description :   https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/
Problem:
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/28     eeyu   Initial creation
    
"""
# coding: utf-8

class P448FindAllNumbersDisappearedInAnArray(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        return list(set([ x for x in range(1, len(nums)+1)]) - set(nums))


if __name__ == '__main__':
    print(P448FindAllNumbersDisappearedInAnArray().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
