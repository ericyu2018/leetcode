"""
Author    :   eeyu
Date      :   2019/3/15 11:35
File Name :   P118PascalsTriangle.py
Description :   https://leetcode-cn.com/problems/pascals-triangle/
Problem:
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/15     eeyu   Initial creation
    
"""
# coding: utf-8


class P118PascalsTriangle(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows < 1:
            return list()
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            known_result = [[1], [1, 1]]
            while numRows - 2 > 0:
                known_result.append(self.generate_next_line(known_result[-1]))
                numRows -= 1
            print(known_result)
            return known_result

    def generate_next_line(self, current_line):
        next_line = list()
        current_line_length = len(current_line)
        start_index = 0

        while start_index < current_line_length - 1:
            next_line.append(current_line[start_index] + current_line[start_index + 1])
            start_index += 1

        next_line.insert(0, 1)
        next_line.append(1)

        return next_line


if __name__ == '__main__':
    P118PascalsTriangle().generate(5)

