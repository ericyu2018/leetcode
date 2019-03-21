"""
Author    :   eeyu
Date      :   2019/3/21 16:37
File Name :   P167TwoSumIIInputArrayIsSorted.py
Description :  https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/
Problem:
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/21     eeyu   Initial creation
    
"""
# coding: utf-8

class P167TwoSumIIInputArrayIsSorted(object):
    def two_Sum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(0, len(numbers)):
            complement = target - numbers[index]
            complement_index = self.find_complement_index(numbers, complement, index+1)

            if complement_index != -1:
                    return list((index + 1, complement_index + 1))

    def find_complement_index(self, nums, complement, start_index):
        low = start_index
        high = len(nums)-1
        while low <= high:
            mid = low + int((high - low)/2)
            if nums[mid] < complement:
                low = mid + 1
            elif nums[mid] > complement:
                high = mid - 1
            else:
                return mid

        return -1

if __name__ == '__main__':
    print(P167TwoSumIIInputArrayIsSorted().find_complement_index([1,2,3,4,4,9,56,90],8, 0))
    print(P167TwoSumIIInputArrayIsSorted().two_Sum([1,2,3,4,4,9,56,90],8))