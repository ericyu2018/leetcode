"""
Author    :   eeyu
Date      :   2019/4/3 11:08
File Name :   P242ValidAnagram.py
Description :  https://leetcode-cn.com/problems/valid-anagram/
Problem:
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/3     eeyu   Initial creation
    
"""
# coding: utf-8


class P242ValidAnagram(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if s is None or t is None or len(s) != len(t):
            return False

        s_sum = 0
        t_sum = 0

        s_set = set()
        t_set = set()

        for index in range(0, len(s)):
            s_sum += ord(s[index])
            s_set.add(s[index])

            t_sum += ord(t[index])
            t_set.add(t[index])

        return s_sum == t_sum and len(s_set - t_set) == 0

if __name__ == '__main__':
    print(P242ValidAnagram().isAnagram("anagram", "nagaram"))
    print(P242ValidAnagram().isAnagram("rat", "car"))
    print(P242ValidAnagram().isAnagram("ac", "bb"))
