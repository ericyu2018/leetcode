"""
Author    :   eeyu
Date      :   2019/2/28 11:12
File Name :   P14LongestCommonPrefix.py
Description : https://leetcode-cn.com/problems/longest-common-prefix/
Problem :
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.

===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/2/28     eeyu   Initial creation
    
"""
# coding: utf-8


class P14LongestCommonPrefix(object):

    @staticmethod
    def longest_common_prefix(strs):

        strs.sort()

        if len(strs) == 0:
            print('Explanation: There is no common prefix among the input strings.')
            return ""

        if len(strs) == 1:
            return strs[0]

        if len(strs[0]) == 0 or len(strs[len(strs)-1]) == 0 or strs[0][0] != strs[len(strs)-1][0]:
            print('Explanation: There is no common prefix among the input strings.')
            return ""

        else:
            shortest_string_index = 0
            shortest_string_length = len(strs[0])
            for index in range(1, len(strs)):
                if len(strs[index]) < shortest_string_length:
                    shortest_string_index = index
                    shortest_string_length = len(strs[index])

            shortest_string_value = strs[shortest_string_index]

            for i in range(0, len(strs) + 1):
                longest_common_prefix_candidate = shortest_string_value[0:len(shortest_string_value)-i].lower()
                find_count = 0
                for item in strs:
                    if item.lower().startswith(longest_common_prefix_candidate):
                        find_count = find_count + 1

                    if find_count == len(strs):
                        return longest_common_prefix_candidate


if __name__ == '__main__':
    print(P14LongestCommonPrefix.longest_common_prefix(["flower", "flow", "flight"]))
    print(P14LongestCommonPrefix.longest_common_prefix(["dog", "racecar", "car"]))
    print(P14LongestCommonPrefix.longest_common_prefix(["some", "flow", "same", "for"]))
    print(P14LongestCommonPrefix.longest_common_prefix([]))
    print(P14LongestCommonPrefix.longest_common_prefix([""]))
    print(P14LongestCommonPrefix.longest_common_prefix(["", ""]))
    print(P14LongestCommonPrefix.longest_common_prefix(["a"]))
    print(P14LongestCommonPrefix.longest_common_prefix(["abca", "aba", "aaab"]))
