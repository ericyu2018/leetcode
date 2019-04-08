"""
Author    :   eeyu
Date      :   2019/4/8 10:49
File Name :   P278FirstBadVersion.py
Description : https://leetcode-cn.com/problems/first-bad-version/
Problem:
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/8     eeyu   Initial creation
    
"""
# coding: utf-8
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version >= 60:
        return True
    else:
        return False

class P278FirstBadVersion(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low_version = 1
        high_version = n
        first_bad_version_candidate = -1
        while low_version <= high_version:
            mid_version = low_version + int((high_version - low_version) / 2)
            if isBadVersion(mid_version):
                first_bad_version_candidate = mid_version
                high_version = mid_version - 1
            else:
                low_version = mid_version + 1

        return first_bad_version_candidate

if __name__ == '__main__':
    print(P278FirstBadVersion().firstBadVersion(200))
    print(P278FirstBadVersion().firstBadVersion(7))
    print(P278FirstBadVersion().firstBadVersion(1))