"""
Author    :   eeyu
Date      :   2019/4/17 10:05
File Name :   P389FindTheDifference.py
Description :   https://leetcode-cn.com/problems/find-the-difference/
Problem:
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:
Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/17     eeyu   Initial creation
    
"""
# coding: utf-8

class P389FindTheDifference(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(self.sum_of_string(t) - self.sum_of_string(s))

    def sum_of_string(self, s):
        sum = 0
        for item in s:
            sum += ord(item)

        return sum

if __name__ == '__main__':
    print(P389FindTheDifference().findTheDifference('abcd','abcde'))
    print(P389FindTheDifference().findTheDifference('abcd', 'abcdd'))