"""
Author    :   eeyu
Date      :   2019/3/22 14:27
File Name :   P168ExcelSheetColumnTitle.py
Description :  https://leetcode-cn.com/problems/excel-sheet-column-title/
Problem:
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:
Input: 1
Output: "A"

Example 2:
Input: 28
Output: "AB"

Example 3:
Input: 701
Output: "ZY"
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/22     eeyu   Initial creation
    
"""
# coding: utf-8

class P168ExcelSheetColumnTitle(object):
    def convert_to_title(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n < 1:
            raise ValueError('Invalid value for n')

        else:
            res = ''
            while n != 0:
                q, r = divmod(n - 1, 26)
                res = chr(r + 65) + res
                n = q

            return res


if __name__ == '__main__':
    print(P168ExcelSheetColumnTitle().convert_to_title(1))
    print(P168ExcelSheetColumnTitle().convert_to_title(26))
    print(P168ExcelSheetColumnTitle().convert_to_title(28))
    print(P168ExcelSheetColumnTitle().convert_to_title(52))
    print(P168ExcelSheetColumnTitle().convert_to_title(701))
    print(P168ExcelSheetColumnTitle().convert_to_title(998701))
