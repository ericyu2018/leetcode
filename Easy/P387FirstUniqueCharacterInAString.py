"""
Author    :   eeyu
Date      :   2019/4/17 9:41
File Name :   P387FirstUniqueCharacterInAString.py
Description : https://leetcode-cn.com/problems/first-unique-character-in-a-string/
Problem:
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/17     eeyu   Initial creation
    
"""
# coding: utf-8

class P387FirstUniqueCharacterInAString(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return -1

        if len(s) == 1:
            return 0

        candidate_list_key = list()
        mapping = dict()
        for index in range(0, len(s)):
            if s[index] not in mapping.keys():
                mapping[s[index]] = s.count(s[index])
                candidate_list_key.append(s[index])

        if len(candidate_list_key) != 0:
            for item in candidate_list_key:
                if mapping[item] == 1:
                    candidate_value = item
                    return s.find(candidate_value)
                else:
                    continue
            return -1
        else:
            return -1

if __name__ == '__main__':
    print(P387FirstUniqueCharacterInAString().firstUniqChar('leetcode'))
    print(P387FirstUniqueCharacterInAString().firstUniqChar('loveleetcode'))
    print(P387FirstUniqueCharacterInAString().firstUniqChar('l'))
    print(P387FirstUniqueCharacterInAString().firstUniqChar(''))
    print(P387FirstUniqueCharacterInAString().firstUniqChar('cc'))



