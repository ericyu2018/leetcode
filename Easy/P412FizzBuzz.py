"""
Author    :   eeyu
Date      :   2019/4/19 13:18
File Name :   P412FizzBuzz.py
Description :  https://leetcode-cn.com/problems/fizz-buzz/
Problem:
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/19     eeyu   Initial creation
    
"""
# coding: utf-8

class P412FizzBuzz(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result_list = list()
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                result_list.append('FizzBuzz')
            elif i % 3 == 0:
                result_list.append('Fizz')
            elif i % 5 == 0:
                result_list.append('Buzz')
            else:
                result_list.append(str(i))

        return result_list

if __name__ == '__main__':
    print(P412FizzBuzz().fizzBuzz(100))