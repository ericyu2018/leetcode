"""
Author    :   eeyu
Date      :   2019/4/8 10:06
File Name :   P268MissingNumber.py
Description :  https://leetcode-cn.com/problems/missing-number/
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/8     eeyu   Initial creation
    
"""
# coding: utf-8


class P268MissingNumber(object):
    def missing_number(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = max(nums)
        nums_length = len(nums)

        full_sum = 0
        i = 0
        while i <= max_value:
            full_sum += i
            i += 1

        if max_value >= nums_length:
            return full_sum - sum(nums)
        else:
            return nums_length

if __name__ == '__main__':
    print(P268MissingNumber().missing_number([3, 0, 1]))
    print(P268MissingNumber().missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
    print(P268MissingNumber().missing_number([0]))
        