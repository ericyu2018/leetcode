"""
Author    :   eeyu
Date      :   2019/4/20 10:35
File Name :   P31NextPermutation.py
Description :   https://leetcode-cn.com/problems/next-permutation/
Problem:
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/20     eeyu   Initial creation
    
"""
# coding: utf-8

class P31NextPermutation(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        '''
        从数组末尾往头部遍历，对第i个元素，如果他小于第i+1个元素，则从第i+1个元素往数组末尾遍历， 
        找到 j 使得 j=n-1或者nums[j+1]<num[i], 交换 i, j的值， 然后翻转 num[i+1:]，即可。 
        如果找不到，即数组为递减数组，直接翻转
        '''
        sign = True
        for i in range(2, len(nums)+1):
            if nums[-i] < nums[-i+1]:
                sign = False
                j = -i+1
                while j < 0:
                    if nums[j] <= nums[-i]:
                        break
                    j += 1
                break
        if sign:
            nums.reverse()
        else:
            nums[-i], nums[j-1] = nums[j-1], nums[-i]
            nums[-i+1:] = nums[-i+1:][::-1]

if __name__ == '__main__':
    nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]  # [1, 5, 8, 5, 1, 3, 4, 6, 7]
    P31NextPermutation().nextPermutation(nums)
    print(nums)
