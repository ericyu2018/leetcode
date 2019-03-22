"""
Author    :   eeyu
Date      :   2019/3/7 11:06
File Name :   P67AddBinary.py
Description :  https://leetcode-cn.com/problems/add-binary/
Problem:
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/7     eeyu   Initial creation
    
"""
# coding: utf-8

class P67AddBinary(object):

    @staticmethod
    def add_binary(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        try:
            a_int = int(a)
            b_int = int(b)
        except ValueError:
            return ''

        sum_int = a_int + b_int

        sum_str_list = list(str(sum_int))

        while '2' in sum_str_list:
            for index in range(0, len(sum_str_list)):
                if sum_str_list[index] == '2':
                    if index == 0:
                        sum_str_list[index] = '0'
                        sum_str_list.insert(index, '1')
                    else:
                        sum_str_list[index] = '0'
                        sum_str_list[index - 1] = str(int(sum_str_list[index - 1]) + 1)

        result = ''
        for index in range(0, len(sum_str_list)):
            result = result + sum_str_list[index]

        return result


    @staticmethod
    def add_binary2(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]
if __name__ == '__main__':
    print(P67AddBinary.add_binary("1010", "1011"))
    print(P67AddBinary.add_binary2("1010", "1011"))
