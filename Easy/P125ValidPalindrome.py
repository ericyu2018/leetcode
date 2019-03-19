"""
Author    :   eeyu
Date      :   2019/3/19 9:56
File Name :   P125ValidPalindrome.py
Description :   https://leetcode-cn.com/problems/valid-palindrome/
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/19     eeyu   Initial creation
    
"""
# coding: utf-8


class P125ValidPalindrome(object):
    def is_palindrome_python27(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_string = filter(str.isalnum, str(s.lower()))
        clean_string_length = len(clean_string)

        if clean_string_length == 0:
            return True

        for i in range(0, int(clean_string_length/2)):
            if clean_string[i] != clean_string[clean_string_length -1 -i]:
                return False

        return True

    def is_palindrome_python37(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_string = list(filter(str.isalnum, s.lower()))
        dir(clean_string)

        clean_string_length = len(clean_string)

        if clean_string_length == 0:
            return True

        for i in range(0, int(clean_string_length / 2)):
            if clean_string[i] != clean_string[clean_string_length - 1 - i]:
                return False

        return True


if __name__ == '__main__':
    print(P125ValidPalindrome().is_palindrome_python37("A man, a plan, a canal: Panama"))
    print(P125ValidPalindrome().is_palindrome_python37("race a car"))
