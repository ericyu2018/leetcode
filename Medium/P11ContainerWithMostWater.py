"""
Author    :   eeyu
Date      :   2019/4/1 14:40
File Name :   P11ContainerWithMostWater.py
Description :  https://leetcode-cn.com/problems/container-with-most-water/
Problem:
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/1     eeyu   Initial creation
    
"""
# coding: utf-8

class P11ContainerWithMostWater(object):
    def maxArea2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        height_count = len(height)

        for i in range(0, height_count):
            for j in range(i+1, height_count):
                max_area = max(min(height[i], height[j]) * (j - i), max_area)

        return max_area

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


if __name__ == '__main__':
    print(P11ContainerWithMostWater().maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(P11ContainerWithMostWater().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


