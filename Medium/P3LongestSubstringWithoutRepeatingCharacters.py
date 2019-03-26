"""
Author    :   eeyu
Date      :   2019/3/26 12:37
File Name :   P3LongestSubstringWithoutRepeatingCharacters.py
Description :  https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
Problem:
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/26     eeyu   Initial creation
    
"""
# coding: utf-8

class P3LongestSubstringWithoutRepeatingCharacters(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: in
        """

        substr_start_index = 0
        max_length = 0
        used_char_map = dict()

        for index, char in enumerate(s):
            if char in used_char_map.keys() and substr_start_index <= used_char_map[char]:
                substr_start_index = used_char_map[char] + 1
            else:
                max_length = max(max_length, index - substr_start_index + 1)
            used_char_map[char] = index

        return max_length

if __name__ == '__main__':
    print(P3LongestSubstringWithoutRepeatingCharacters().lengthOfLongestSubstring('abcabcdbb'))
    print(P3LongestSubstringWithoutRepeatingCharacters().lengthOfLongestSubstring('bbbbb'))
    print(P3LongestSubstringWithoutRepeatingCharacters().lengthOfLongestSubstring('pwwkew'))
