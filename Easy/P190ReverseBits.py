"""
Author    :   eeyu
Date      :   2019/3/25 14:34
File Name :   P190ReverseBits.py
Description :   https://leetcode-cn.com/problems/reverse-bits/
Problem:
Reverse bits of a given 32 bits unsigned integer.

Example 1:
Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Example 2:
Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10101111110010110010011101101001.


Note:
Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.

Follow up:

If this function is called many times, how would you optimize it?
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/25     eeyu   Initial creation
    
"""
# coding: utf-8


class P190ReverseBits(object):
    # @param n, an integer
    # @return an integer
    def reverse_bits(self, n):
        result_string = ''
        while n > 0:
            q, r = divmod(n, 10)
            n = q
            result_string += str(r)

        try:
            result = int(result_string)
        except OverflowError:
            result = 0

        return result


    def reverse_bits2(self, n):
        n_bin_string = bin(n)[2:]
        n_bin_reversed_string = n_bin_string[::-1]

        while len(n_bin_reversed_string) < 32:
            n_bin_reversed_string += '0'

        return int(n_bin_reversed_string, 2)


if __name__ == '__main__':
    print(P190ReverseBits().reverse_bits(10100101000001111010011100))
    print(P190ReverseBits().reverse_bits(11111111111111111111111111111101))
    print('*' * 60)
    print(P190ReverseBits().reverse_bits2(10100101000001111010011100))
    print(P190ReverseBits().reverse_bits2(11111111111111111111111111111101))