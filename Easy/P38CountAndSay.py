"""
Author    :   eeyu
Date      :   2019/3/5 11:51
File Name :   P38CountAndSay.py
Description : https://leetcode-cn.com/problems/count-and-say/
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/5     eeyu   Initial creation
    
"""
# coding: utf-8

class P38CountAndSay(object):

    @staticmethod
    def countAndSay(n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return str(1)
        else:
            return P38CountAndSay.read_string(P38CountAndSay.countAndSay(n-1))

    @staticmethod
    def read_string(string):
        result_len = len(string)
        read_result = ''

        count = 1
        for i in range(0, result_len):
            if i+1 < result_len and string[i] == string[i+1]:
                count = count + 1
            else:
                read_result = read_result + str(count) + string[i]
                count = 1

        return read_result


if __name__ == '__main__':
    print(P38CountAndSay.countAndSay(1))
    print(P38CountAndSay.countAndSay(2))
    print(P38CountAndSay.countAndSay(3))
    print(P38CountAndSay.countAndSay(4))
    print(P38CountAndSay.countAndSay(5))
    print(P38CountAndSay.countAndSay(6))
    print(P38CountAndSay.countAndSay(7))
    print(P38CountAndSay.countAndSay(8))
    print(P38CountAndSay.countAndSay(9))
    print(P38CountAndSay.countAndSay(10))
    #print(P38CountAndSay.read_string('111221'))
