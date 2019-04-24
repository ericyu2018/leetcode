"""
Author    :   eeyu
Date      :   2019/4/24 9:48
File Name :   P434NumberOfSegmentsInAString.py
Description :   https://leetcode-cn.com/problems/number-of-segments-in-a-string/
Problem:
Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:
Input: "Hello, my name is John"
Output: 5
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/24     eeyu   Initial creation
    
"""
# coding: utf-8


class P434NumberOfSegmentsInAString(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s.strip()) == 0:
            return 0
        else:
            return len(s.strip().split())

if __name__ == '__main__':
    print(P434NumberOfSegmentsInAString().countSegments('Hello, my name is John'))
    print(P434NumberOfSegmentsInAString().countSegments(''))
    print(P434NumberOfSegmentsInAString().countSegments('   '))
    print(P434NumberOfSegmentsInAString().countSegments('\t'))
    print(P434NumberOfSegmentsInAString().countSegments(", , , ,        a, eaefa"))