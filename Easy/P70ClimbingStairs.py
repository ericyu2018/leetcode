"""
Author    :   eeyu
Date      :   2019/3/8 10:27
File Name :   P70ClimbingStairs.py
Description :   https://leetcode-cn.com/problems/climbing-stairs/
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/8     eeyu   Initial creation
    
"""
# coding: utf-8
from functools import lru_cache

class P70ClimbingStairs(object):

    @staticmethod
    @lru_cache(10)
    def climb_stairs(n):
        """
        :type n: int
        :rtype: int
        """
        assert n > 0, 'stair number should be positive'

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return P70ClimbingStairs.climb_stairs(n-1) + P70ClimbingStairs.climb_stairs(n-2)

    @staticmethod
    def climb_stairs2(n):
        """
        :type n: int
        :rtype: int
        """
        step_list = list()
        step_list.append(1)
        step_list.append(1)

        for index in range(2, n+1):
            step_list.append(step_list[index - 1] + step_list[index - 2])

        return step_list[n]


if __name__ == '__main__':
    print(P70ClimbingStairs.climb_stairs(1))
    print(P70ClimbingStairs.climb_stairs(2))
    print(P70ClimbingStairs.climb_stairs(3))
    print(P70ClimbingStairs.climb_stairs(4))
    print(P70ClimbingStairs.climb_stairs(5))
    print(P70ClimbingStairs.climb_stairs(6))
    print(P70ClimbingStairs.climb_stairs(38))
    print(P70ClimbingStairs.climb_stairs(44))
    print(P70ClimbingStairs.climb_stairs2(44))



