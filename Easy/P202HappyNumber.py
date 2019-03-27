"""
Author    :   eeyu
Date      :   2019/3/27 9:40
File Name :   P202HappyNumber.py
Description :  https://leetcode-cn.com/problems/happy-number/
Problem:
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:
Input: 19
Output: true

Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/27     eeyu   Initial creation
    
"""
# coding: utf-8


class P202HappyNumber(object):
    def is_happy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False
        else:
            known_sum_set = set()
            while True:
                next_value = self.__get_next(n)

                if next_value not in known_sum_set:
                    known_sum_set.add(next_value)
                else:
                    return False

                if next_value == 1:
                    return True
                else:
                    n = next_value


    def __get_next(self, n):
        return sum([int(i) ** 2 for i in str(n)])

if __name__ == '__main__':
    print(P202HappyNumber().is_happy(19))
    print(P202HappyNumber().is_happy(20))
    print(P202HappyNumber().is_happy(2))