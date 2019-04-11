"""
Author    :   eeyu
Date      :   2019/4/11 14:34
File Name :   P344ReverseString.py
Description :  https://leetcode-cn.com/problems/reverse-string/
Problem:
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/11     eeyu   Initial creation
    
"""
# coding: utf-8


class P344ReverseString(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        if len(s) <= 1:
            pass
        else:
            for index in range(0, int(len(s)/2)):
                temp = s[index]
                s[index] = s[len(s) - 1 - index]
                s[len(s) - 1 - index] =temp

        print(s)

if __name__ == '__main__':
    P344ReverseString().reverseString(["h","e","l","l","o"])
