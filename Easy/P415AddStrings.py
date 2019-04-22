"""
Author    :   eeyu
Date      :   2019/4/22 13:08
File Name :   P415AddStrings.py
Description :   https://leetcode-cn.com/problems/add-strings/
Problem:
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:
The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/22     eeyu   Initial creation
    
"""
# coding: utf-8

class P415AddStrings(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        num_value = [ x for x in range(0,10) ]
        num_str_list = [ str(x) for x in range(0,10)]
        num_str_value_mapping = dict(zip(num_str_list, num_value))
        num1_sum, num2_sum = 0, 0

        for index in range(0, len(num1)):
            num1_sum = num1_sum + num_str_value_mapping[num1[index]] * pow(10, len(num1) - 1 - index)

        for index in range(0, len(num2)):
            num2_sum = num2_sum + num_str_value_mapping[num2[index]] * pow(10, len(num2) - 1 - index)

        return str(num1_sum + num2_sum)

if __name__ == '__main__':
    print(P415AddStrings().addStrings('123','456'))
    print(P415AddStrings().addStrings('401716832807512840963', '167141802233061013023557397451289113296441069'))
