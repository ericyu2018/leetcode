"""
Author    :   eeyu
Date      :   2019/4/16 12:42
File Name :   P22GenerateParentheses.py
Description :  https://leetcode-cn.com/problems/generate-parentheses/
Problem:
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/16     eeyu   Initial creation
    
"""
# coding: utf-8


class P22GenerateParentheses(object):
    def __init__(self):
        self.backtrack_accessed = 0

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        solution_list = list()
        self.backtrack('', solution_list, n, n)
        return solution_list

    def backtrack(self, current_solution_string, solution_list, left_parenthese_count, right_parenthese_count):
        self.backtrack_accessed += 1
        print('{0}:{1}:{2}:{3}:{4}'.format(self.backtrack_accessed, current_solution_string, left_parenthese_count, right_parenthese_count, solution_list))
        if left_parenthese_count == 0 and right_parenthese_count == 0:
            solution_list.append(current_solution_string)
            return

        if left_parenthese_count > right_parenthese_count:
            return

        if left_parenthese_count > 0:
            self.backtrack(current_solution_string + '(', solution_list, left_parenthese_count - 1, right_parenthese_count)

        if right_parenthese_count > 0:
            self.backtrack(current_solution_string + ')', solution_list, left_parenthese_count, right_parenthese_count - 1)

if __name__ == '__main__':
    print(P22GenerateParentheses().generateParenthesis(3))