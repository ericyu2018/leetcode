"""
Author    :   eeyu
Date      :   2019/3/28 11:48
File Name :   P6ZigzagConversion.py
Description :   https://leetcode-cn.com/problems/zigzag-conversion
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