"""
Author    :   eeyu
Date      :   2019/4/12 14:34
File Name :   P345ReverseVowelsOfAString.py
Description :  https://leetcode-cn.com/problems/reverse-vowels-of-a-string/
Problem:
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/12     eeyu   Initial creation
    
"""
# coding: utf-8

class P345ReverseVowelsOfAString(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = ['a','e','i','o','u','A','E','I','O','U']

        if len(s) <= 1:
            return s
        else:
            s_list = list(s)
            left = 0
            right = len(s) -1
            while left < right:
                if s_list[left] in vowels and s_list[right] in vowels:
                    s_list[left], s_list[right] = s_list[right], s_list[left]
                    left += 1
                    right -=1
                elif s_list[left] in vowels and s_list[right] not in vowels:
                    right -= 1
                elif s_list[left] not in vowels and s_list[right] in vowels:
                    left += 1
                else:
                    left += 1
                    right -= 1

            return ''.join(s_list)

if __name__ == '__main__':
    print(P345ReverseVowelsOfAString().reverseVowels('hello'))
    print(P345ReverseVowelsOfAString().reverseVowels('leetcode'))
