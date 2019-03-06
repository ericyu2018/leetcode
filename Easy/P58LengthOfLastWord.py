"""
Author    :   eeyu
Date      :   2019/3/6 9:48
File Name :   P58LengthOfLastWord.py
Description :   https://leetcode-cn.com/problems/length-of-last-word/
Problem:
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Input: "Hello World"
Output: 5
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/6     eeyu   Initial creation
    
"""
# coding: utf-8

class P58LengthOfLastWord(object):

    @staticmethod
    def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        elif s.count(' ') == len(s):
            return 0
        else:
            s_list = s.split(' ')
            space_count = s_list.count('')

            for i in range(0, space_count):
                s_list.remove('')

            return len(s_list[len(s_list)-1])

            # better solution
            # return len(s.strip(' ').split(' ')[-1])

if __name__ == '__main__':
    print(P58LengthOfLastWord.lengthOfLastWord("Hello World"))
    print(P58LengthOfLastWord.lengthOfLastWord(""))
    print(P58LengthOfLastWord.lengthOfLastWord(None))
    print(P58LengthOfLastWord.lengthOfLastWord(" "))