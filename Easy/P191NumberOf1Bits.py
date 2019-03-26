"""
Author    :   eeyu
Date      :   2019/3/26 9:45
File Name :   P191NumberOf1Bits.py
Description :   https://leetcode-cn.com/problems/number-of-1-bits/
Problem:
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

Example 1:
Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/26     eeyu   Initial creation
    
"""
# coding: utf-8


class P191NumberOf1Bits(object):
    def hamming_weight(self, n):
        """
        :type n: int
        :rtype: int
        """

        bin_string = bin(n)[2:]
        count = 0
        for index in range(0, len(bin_string)):
            if bin_string[index] == '1':
                count += 1

        return count


if __name__ == '__main__':
    print(P191NumberOf1Bits().hamming_weight(11))