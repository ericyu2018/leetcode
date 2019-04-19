"""
Author    :   eeyu
Date      :   2019/4/19 9:48
File Name :   P409LongestPalindrome.py
Description :  https://leetcode-cn.com/problems/longest-palindrome/
Problem:
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/19     eeyu   Initial creation
    
"""
# coding: utf-8


class P409LongestPalindrome(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        letter_count_list = list()
        result_list = list()
        single_letter = 0

        for item in set(list(s)):
            letter_count_list.append(s.count(item))

        for letter_count in letter_count_list:
            if letter_count % 2 == 0:
                result_list.append(letter_count)
            else:
                result_list.append(letter_count -1)
                single_letter = 1

        return sum(result_list, single_letter)

if __name__ == '__main__':
    print(P409LongestPalindrome().longestPalindrome('abccccdd'))
    print(P409LongestPalindrome().longestPalindrome('ccc'))
    print(P409LongestPalindrome().longestPalindrome('ababababa'))