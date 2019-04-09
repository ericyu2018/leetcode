"""
Author    :   eeyu
Date      :   2019/4/9 11:48
File Name :   P290WordPattern.py
Description :  https://leetcode-cn.com/problems/word-pattern/
Problem:
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/9     eeyu   Initial creation
    
"""
# coding: utf-8


class P290WordPattern(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        pattern_len = len(pattern)
        str_list = str.split(" ")
        str_list_len = len(str_list)

        if not pattern_len == str_list_len:
            return False
        else:
            mapping = dict()

            for index in range(0, pattern_len):
                if pattern[index] in mapping.keys():
                    if mapping[pattern[index]] != str_list[index]:
                        return False
                else:
                    if str_list[index] not in mapping.values():
                        mapping[pattern[index]] = str_list[index]
                    else:
                        return False

        return True


if __name__ == '__main__':
    print(P290WordPattern().wordPattern("abba", "dog cat cat dog"))
    print(P290WordPattern().wordPattern("abba", "dog cat cat fish"))
    print(P290WordPattern().wordPattern("aaaa", "dog cat cat dog"))
    print(P290WordPattern().wordPattern("abba", "dog dog dog dog"))
