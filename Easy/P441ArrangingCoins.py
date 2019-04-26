"""
Author    :   eeyu
Date      :   2019/4/26 9:31
File Name :   P441ArrangingCoins.py
Description :   https://leetcode-cn.com/problems/arranging-coins/
Problem:
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:
n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

Example 2:
n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/26     eeyu   Initial creation
    
"""
# coding: utf-8
import math

class P441ArrangingCoins(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """

        # n = k * (k+1) /2  => 2n = k** 2 + k  => 2n == k ** 2 => k = sqrt(2n)

        k = int(math.sqrt(2 * n))

        if n < 2 or self.sum_of_coins(k) <= n:
            return k
        else:
            return k -1

    def sum_of_coins(self, k):
        return int((k * (k + 1)) / 2)


if __name__ == '__main__':
    print(P441ArrangingCoins().sum_of_coins(4))
    print(P441ArrangingCoins().sum_of_coins(100))
    print(P441ArrangingCoins().arrangeCoins(1))
    print(P441ArrangingCoins().arrangeCoins(2))
    print(P441ArrangingCoins().arrangeCoins(3))
    print(P441ArrangingCoins().arrangeCoins(5))
    print(P441ArrangingCoins().arrangeCoins(8))
    print(P441ArrangingCoins().arrangeCoins(10))
    print(P441ArrangingCoins().arrangeCoins(500))
    print(P441ArrangingCoins().arrangeCoins(500000000))
    print(P441ArrangingCoins().arrangeCoins(1804289383))
    print(P441ArrangingCoins().arrangeCoins(1129566413))



