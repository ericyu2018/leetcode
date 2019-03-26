"""
Author    :   eeyu
Date      :   2019/3/26 11:39
File Name :   P171ExcelSheetColumnNumber.py
Description :   https://leetcode-cn.com/problems/excel-sheet-column-number/
Problem:
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 701
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/26     eeyu   Initial creation
    
"""
# coding: utf-8

class P171ExcelSheetColumnNumber(object):
    def title_to_number(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_list = [chr(x) for x in range(65, 91)]
        number_list = list(range(1, 27))
        letter_number_mapping = dict(zip(letter_list, number_list))

        s_len = len(s)
        number_value = 0
        if s_len == 0:
            raise ValueError('Invalid input')
        else:
            for index in range(0, s_len):
                number_value = number_value + letter_number_mapping[s[index]] * pow(26, s_len - index -1)

        return number_value

if __name__ == '__main__':
    print(P171ExcelSheetColumnNumber().title_to_number('AB'))