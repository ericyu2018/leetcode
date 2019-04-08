"""
Author    :   eeyu
Date      :   2019/4/8 11:13
File Name :   P17LetterCombinationsOfAPhoneNumber.py
Description :  https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
Problem:
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order, your answer could be in any order you want.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/8     eeyu   Initial creation
    
"""
# coding: utf-8


class P17LetterCombinationsOfAPhoneNumber(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if len(digits) == 0:
            return list()

        num_letters_mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                               '9': 'wxyz'}

        result_list = [letter for letter in num_letters_mapping[digits[0]]]
        print(result_list)
        left_digits = digits[1:]
        print(left_digits)

        for num_item in left_digits:
            num_item_mapped_letters = num_letters_mapping[num_item]
            num_item_mapped_letters_length = len(num_item_mapped_letters)
            current_result_list_length = len(result_list)
            result_list = result_list * num_item_mapped_letters_length
            num_item_mapped_letters = [letter * current_result_list_length for letter in num_item_mapped_letters]
            num_item_mapped_letters = "".join(num_item_mapped_letters)
            for index in range(len(num_item_mapped_letters)):
                result_list[index] = result_list[index] + num_item_mapped_letters[index]

        return result_list

if __name__ == '__main__':
    print(P17LetterCombinationsOfAPhoneNumber().letterCombinations('23'))