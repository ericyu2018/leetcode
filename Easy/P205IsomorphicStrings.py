"""
Author    :   eeyu
Date      :   2019/3/28 11:19
File Name :   P205IsomorphicStrings.py
Description :   https://leetcode-cn.com/problems/isomorphic-strings
Problem:
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/28     eeyu   Initial creation
    
"""
# coding: utf-8


class P205IsomorphicStrings(object):
    def is_isomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        if len(s) == 0:
            return True

        mapping = dict()

        for i in range(0, len(s)):
            if s[i] not in mapping.keys():
                if t[i] not in mapping.values():
                    mapping[s[i]] = t[i]
                else:
                    return False
            else:
                if mapping[s[i]] != t[i]:
                    return False

        return True

if __name__ == '__main__':
    print(P205IsomorphicStrings().is_isomorphic('egg', 'add'))
    print(P205IsomorphicStrings().is_isomorphic('foo', 'bar'))
    print(P205IsomorphicStrings().is_isomorphic('paper', 'title'))
    print(P205IsomorphicStrings().is_isomorphic('paper', 'titles'))
    print(P205IsomorphicStrings().is_isomorphic('', ''))
    print(P205IsomorphicStrings().is_isomorphic('ab', 'aa'))
