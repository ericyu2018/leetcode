"""
Author    :   eeyu
Date      :   2019/3/1 9:58
File Name :   P20ValidParentheses.py
Description :  https://leetcode-cn.com/problems/valid-parentheses/
Problem:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/1     eeyu   Initial creation
    
"""


# coding: utf-8


class P20ValidParentheses(object):

    @staticmethod
    def is_valid(s):
        """
        :type s: str
        :rtype: bool
        """

        rule_map = {'[': ']', '{': '}', '(': ')'}

        if len(s) == 0:
            return True

        if len(s) % 2 != 0:
            return False

        str_list = list(s)

        for i in range(0, len(str_list)):
                if str_list[i] in rule_map.keys() and i+1 < len(str_list) and str_list[i+1] == rule_map[str_list[i]]:
                    str_list.pop(i)
                    str_list.pop(i)

                    temp = ""
                    for j in range(0, len(str_list)):
                        temp = temp + str_list[j]
                    return P20ValidParentheses.is_valid(temp)
                else:
                    continue

        return False


    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping.keys():
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = '#'

                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

if __name__ == '__main__':
    print(P20ValidParentheses.is_valid('()'))
    print(P20ValidParentheses.is_valid('(('))
    print(P20ValidParentheses.is_valid('()[]{}'))
    print(P20ValidParentheses.is_valid('(]'))
    print(P20ValidParentheses.is_valid('([)]'))
    print(P20ValidParentheses.is_valid('{[]}'))
    print(P20ValidParentheses.is_valid(''))
    print(P20ValidParentheses.is_valid('()['))

    print(P20ValidParentheses().isValid(''))
    print(P20ValidParentheses().isValid('()['))
