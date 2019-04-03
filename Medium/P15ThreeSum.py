"""
Author    :   eeyu
Date      :   2019/2/25 21:37
File Name :   P15ThreeSum.py
Description :   https://leetcode-cn.com/problems/3sum/
Problem:
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/2/25     eeyu   Initial creation
    
"""
# coding: utf-8


class P15ThreeSum(object):

    def three_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        count_dict = dict()  # 给每个数字计数 O(n)
        for n in nums:
            if count_dict.get(n, 0) > 0:
                count_dict[n] += 1
            else:
                count_dict[n] = 1
        print(count_dict)

        # a,b,c 中有两个相等情形 O(n)
        for n in count_dict.keys():
            if count_dict[n] > 1:
                if count_dict.get(-2 * n, 0) > 0 and n != 0:
                    res.append([n, n, -2 * n])
                    print('2', [n, n, -2 * n])

        # a,b,c 中有三个相等情形，即全为0 O(1)
        if count_dict.get(0, 0) > 2:
            res.append([0, 0, 0])

        # a,b,c 各不相等情形 O(n^2/2)
        diff_nums = list(set(nums))
        if len(diff_nums) > 2:
            for i in range(len(diff_nums) - 2):
                diff_nums_value_index_mapping = dict()
                for k in range(i + 1, len(diff_nums)):
                    complement = -(diff_nums[i] + diff_nums[k])
                    if complement not in diff_nums_value_index_mapping.keys():
                        diff_nums_value_index_mapping[diff_nums[k]] = k
                    else:
                        res.append([diff_nums[i], diff_nums[k], complement])
                        print('3', [diff_nums[i], diff_nums[k], complement])
        return res

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_value_count_mapping = dict()
        result = list()

        for num in nums:
            nums_value_count_mapping[num] = nums_value_count_mapping.get(num, 0) + 1

        if 0 in nums_value_count_mapping.keys() and nums_value_count_mapping[0] >= 3:
            result.append([0, 0, 0])

        uniq_nums = sorted(list(nums_value_count_mapping.keys()))

        for i, num1 in enumerate(uniq_nums):
            for num2 in uniq_nums[i + 1:]:
                if num1 * 2 + num2 == 0 and nums_value_count_mapping[num1] >= 2:
                    result.append([num1, num1, num2])
                if num2 * 2 + num1 == 0 and nums_value_count_mapping[num2] >= 2:
                    result.append([num2, num2, num1])

                num3 = 0 - num1 - num2
                if num3 > num2 and num3 in nums_value_count_mapping.keys():
                    result.append([num1, num2, num3])

        return result




if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4, 0, 0, 2]
    #nums = [-1, 0, 1, -1, 1, 0]
    print(P15ThreeSum().three_sum(nums))
    print(P15ThreeSum().threeSum(nums))