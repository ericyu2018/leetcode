"""
Author    :   eeyu
Date      :   2019/3/27 13:13
File Name :   P5LongestPalindromicSubstring.py
Description :  https://leetcode-cn.com/problems/longest-palindromic-substring
Problem:
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/27     eeyu   Initial creation
    
"""
# coding: utf-8


class P5LongestPalindromicSubstring(object):
    def longest_palindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) <= 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        else:
            substr_start_index = 0
            substr_end_index = 0
            max_length = 0
            dp_lookup = [[ False for x in range(0, len(s))] for y in range(0, len(s))]

            for i in range(len(s)-1, -1, -1):
                for j in range(i, len(s)):
                    if s[i] == s[j] and (j-i <=2 or dp_lookup[i+1][j-1] is True):
                        dp_lookup[i][j] = True

                        if max_length < j-i+1:
                            max_length = j-i+1
                            substr_start_index = i
                            substr_end_index = j

            if substr_start_index < substr_end_index:
                return s[substr_start_index:substr_end_index+1]
            else:
                return ''

if __name__ == '__main__':
    print(P5LongestPalindromicSubstring().longest_palindrome('babad'))
    print(P5LongestPalindromicSubstring().longest_palindrome('cbbd'))
    print(P5LongestPalindromicSubstring().longest_palindrome('a'))
    print(P5LongestPalindromicSubstring().longest_palindrome('ab'))
    print(P5LongestPalindromicSubstring().longest_palindrome('bb'))
    print(P5LongestPalindromicSubstring().longest_palindrome('abcba'))
    print(P5LongestPalindromicSubstring().longest_palindrome('abcda'))
    print(P5LongestPalindromicSubstring().longest_palindrome('abcd'))