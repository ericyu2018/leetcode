"""
Author    :   eeyu
Date      :   2019/3/5 9:44
File Name :   P28ImplementStrstr.py
Description :  https://leetcode-cn.com/problems/implement-strstr/
Problem:
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/5     eeyu   Initial creation
    
"""
# coding: utf-8


class P28ImplementStrstr(object):

    @staticmethod
    def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(haystack) == 0 and len(needle) == 0:
            return 0

        if len(haystack) == 0 and len(needle) != 0:
            return -1

        if needle not in haystack:
            return -1
        else:
            #return haystack.find(needle)
            return haystack.index(needle)

    def str_str_bruce(self, haystack, needle):
        if len(haystack) == 0 and len(needle) == 0:
            return 0

        if len(haystack) == 0 and len(needle) != 0:
            return -1

        if needle not in haystack:
            return -1
        else:
            start_position = 0
            pattern_position = 0

            while start_position < len(haystack) and pattern_position < len(needle):
                if haystack[start_position] == needle[pattern_position]:
                    start_position += 1
                    pattern_position += 1
                else:
                    start_position = start_position - pattern_position + 1
                    pattern_position = 0

            if pattern_position >= len(needle):
                return start_position - pattern_position
            else:
                return -1

if __name__ == '__main__':
    print(P28ImplementStrstr.strStr('', ''))
    print(P28ImplementStrstr.strStr('', 'aaa'))
    print(P28ImplementStrstr.strStr('hello', 'll'))
    print(P28ImplementStrstr.strStr('aaaaa', 'bba'))

    print(P28ImplementStrstr().str_str_bruce('', ''))
    print(P28ImplementStrstr().str_str_bruce('', 'aaa'))
    print(P28ImplementStrstr().str_str_bruce('hello', 'll'))
    print(P28ImplementStrstr().str_str_bruce('aaaaa', 'bba'))
