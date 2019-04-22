"""
Author    :   eeyu
Date      :   2019/4/22 10:12
File Name :   P414ThirdMaximumNumber.py
Description :   https://leetcode-cn.com/problems/third-maximum-number/
Problem:
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/22     eeyu   Initial creation
    
"""
# coding: utf-8


class P414ThirdMaximumNumber(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums_set = set(nums)
        first = second = third = min(nums_set)
        for item in nums_set:
            if item > first:
                third = second
                second = first
                first = item
            elif second < item < first:
                third = second
                second = item
            elif third < item < second:
                third = item

        if second == third:
            return first

        return third

if __name__ == '__main__':
    print(P414ThirdMaximumNumber().thirdMax([3, 2, 1]))
    print(P414ThirdMaximumNumber().thirdMax([1, 2]))
    print(P414ThirdMaximumNumber().thirdMax([2, 2, 3, 1]))



