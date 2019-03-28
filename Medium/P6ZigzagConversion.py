"""
Author    :   eeyu
Date      :   2019/3/28 11:48
File Name :   P6ZigzagConversion.py
Description :   https://leetcode-cn.com/problems/zigzag-conversion
Problem:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/28     eeyu   Initial creation
    
"""
# coding: utf-8


class P6ZigzagConversion(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type num_rows: int
        :rtype: str
        """

        str_length = len(s)
        node_length = 2 * numRows - 2  # index diff between two columns
        result = ""

        if str_length == 0 or numRows == 0 or numRows == 1:
            return s

        for i in range(numRows):
            for j in range(i, str_length, node_length):
                result += s[j]

                if i != 0 and i != numRows - 1 and j - 2 * i + node_length < str_length:
                    result += s[j - 2 * i + node_length]
        return result


if __name__ == '__main__':
   # print(P6ZigzagConversion().convert('PAYPALISHIRING',3))
    print(P6ZigzagConversion().convert('PAYPALISHIRING', 4))