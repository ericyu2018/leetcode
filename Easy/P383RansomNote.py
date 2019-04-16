"""
Author    :   eeyu
Date      :   2019/4/16 10:19
File Name :   P383RansomNote.py
Description : https://leetcode-cn.com/problems/ransom-note/
Problem:
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/16     eeyu   Initial creation
    
"""
# coding: utf-8

class P383RansomNote(object):
    def __init__(self):
        self.ransom_note_mapping = dict()
        self.magazine_mapping = dict()

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if ransomNote is None or magazine is None:
            return False

        if len(ransomNote) > len(magazine):
            return False

        self.fill_dict(ransomNote, self.ransom_note_mapping)
        self.fill_dict(magazine, self.magazine_mapping)

        for item in self.ransom_note_mapping.keys():
            if item not in self.magazine_mapping.keys():
                return False
            elif self.ransom_note_mapping[item] > self.magazine_mapping[item]:
                return False

        return True

    def fill_dict(self, string, mapping):
        for item in string:
            if item not in mapping.keys():
                mapping[item] = string.count(item)

if __name__ == '__main__':
    print(P383RansomNote().canConstruct('abcedfg','aabbcceeddff'))



