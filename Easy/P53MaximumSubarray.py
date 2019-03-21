"""
Author    :   eeyu
Date      :   2019/3/6 10:41
File Name :   P53MaximumSubarray.py
Description : https://leetcode-cn.com/problems/maximum-subarray/
Problem:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/6     eeyu   Initial creation
    
"""
# coding: utf-8

class P53MaximumSubarray(object):

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        return self.max_sub_array(nums, 0, len(nums) - 1)

    def max_sub_array(self, nums, left, right):
        if left == right:
            sum_value = nums[left]
        else:
            mid = int((left + right)/2)
            left_sum = self.max_sub_array(nums, left, mid)
            right_sum = self.max_sub_array(nums, mid + 1, right)

            left_sum_max = nums[mid]
            left_temp = 0

            i = mid
            while i >= left:
                left_temp = left_temp + nums[i]
                if left_temp > left_sum_max:
                    left_sum_max = left_temp
                i = i - 1

            right_sum_max = nums[mid+1]
            right_temp = 0

            j = mid + 1
            while j <= right:
                right_temp = right_temp + nums[j]
                if right_temp > right_sum_max:
                    right_sum_max = right_temp
                j = j + 1

            sum_value = left_sum_max + right_sum_max

            if sum_value < left_sum:
                sum_value = left_sum

            if sum_value < right_sum:
                sum_value = right_sum

        return sum_value

    def maxSubArray2(self, nums):
        result = nums[0]
        sum = 0

        for num in nums:
            if sum > 0:
                sum = sum + num
            else:
                sum = num
            result = max(result, sum)

        return result

if __name__ == '__main__':
   print(P53MaximumSubarray().maxSubArray(None))
   print(P53MaximumSubarray().maxSubArray([]))
   print(P53MaximumSubarray().maxSubArray([7]))
   print(P53MaximumSubarray().maxSubArray([1, -1, 1]))
   print(P53MaximumSubarray().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
   print(P53MaximumSubarray().maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
