"""
Author    :   eeyu
Date      :   2019/4/18 9:55
File Name :   P400NthDigit.py
Description :   https://leetcode-cn.com/problems/nth-digit/
Problem:
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:
Input:
3

Output:
3

Example 2:
Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/18     eeyu   Initial creation
    
"""
# coding: utf-8

class P400NthDigit(object):
    def findNthDigit2(self, n):
        """
        :type n: int
        :rtype: int
        """

        candidate_list = [str(i) for i in range(1, n+1)]

        count = 0
        for item in candidate_list:
            for index in range(0, len(item)):
                count += 1
                if count == n:
                    return int(item[index])

    #根据数学规律，前9个数有1个字符，后90个数有2个字符，后900个数有3个字符。。。
    def findNthDigit1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n

        i = 1
        while n > 9 * 10 ** (i - 1) * i:
            n -= 9 * 10 ** (i - 1) * i
            i += 1

        if n % i == 0:
            return int(str(10 ** (i - 1) + n // i - 1)[-1])
        else:
            return int(str(10 ** (i - 1) + n // i)[n % i - 1])

    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        w = 1
        k = 9
        while n > k * w:
            n -= k * w
            k *= 10
            w += 1
        tmp = 10 ** (w - 1) + (n - 1) / w
        return int(str(tmp)[(n - 1) % w])

if __name__ == '__main__':
    print(P400NthDigit().findNthDigit(5))
    print(P400NthDigit().findNthDigit(11))
    print(P400NthDigit().findNthDigit(10000000))
