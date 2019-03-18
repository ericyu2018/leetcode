"""
Author    :   eeyu
Date      :   2019/3/18 10:05
File Name :   P121BestTimeToBuyAndSellStock.py
Description :  https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
Problem:
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/18     eeyu   Initial creation
    
"""
# coding: utf-8
import sys

class P121BestTimeToBuyAndSellStock(object):
    def max_profit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if prices is None or len(prices) <= 1:
            return 0

        min_price = sys.maxsize
        max_profit = 0

        for i in range(0, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]

            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit


if __name__ == '__main__':
    print(P121BestTimeToBuyAndSellStock().max_profit([7, 1, 5, 3, 6, 4]))
    print(P121BestTimeToBuyAndSellStock().max_profit([7, 6, 4, 3, 1]))
    print(P121BestTimeToBuyAndSellStock().max_profit([2, 4, 1]))
