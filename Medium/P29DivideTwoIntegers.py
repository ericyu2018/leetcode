"""
Author    :   eeyu
Date      :   2019/4/18 12:53
File Name :   P29DivideTwoIntegers.py
Description :  https://leetcode-cn.com/problems/divide-two-integers
Problem:

===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/18     eeyu   Initial creation
    
"""
# coding: utf-8

class P29DivideTwoIntegers(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        if divisor == 0:
            raise ValueError('Invalid divisor. It should not be 0')

        result = 0
        flag = (divisor > 0) == (dividend > 0)
        dividend, divisor = abs(dividend), abs(divisor)

        while True:
            if dividend < divisor:
                break
            for i in range(31, -1, -1):
                if (divisor << i) <= dividend:
                    result += pow(2, i)
                    dividend = dividend - (divisor << i)
                    break

        result = result if flag else -result
        if result < -pow(2, 31):
            return -pow(2, 31)
        elif result > pow(2, 31) -1:
            return pow(2, 31) -1
        else:
            return result

if __name__ == '__main__':
    print(P29DivideTwoIntegers().divide(10, 3))
    print(P29DivideTwoIntegers().divide(10, 5))
    print(P29DivideTwoIntegers().divide(3, 10))
    print(P29DivideTwoIntegers().divide(-10, 3))
    print(P29DivideTwoIntegers().divide(-10, -3))
    print(P29DivideTwoIntegers().divide(10, 0))