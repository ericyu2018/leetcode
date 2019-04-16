"""
Author    :   eeyu
Date      :   2019/4/16 9:38
File Name :   P374GuessNumberHigherOrLower.py
Description :  https://leetcode-cn.com/problems/guess-number-higher-or-lower/
Problem:
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!

Example :
Input: n = 10, pick = 6
Output: 6
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/16     eeyu   Initial creation
    
"""
# coding: utf-8
# The guess API is already defined for you.
#@param num, your guess
#@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
def guess(num):
    expected_num = 6
    if num > expected_num:
        return 1
    elif num < expected_num:
        return -1
    else:
        return 0

class P374GuessNumberHigherOrLower(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n

        while low < high:
            mid_value = (low + high) // 2
            guess_result = guess(mid_value)
            if guess_result == 1:
                high = mid_value - 1
            elif guess_result == -1:
                low = mid_value + 1
            else:
                return mid_value

        return low
if __name__ == '__main__':
    print(P374GuessNumberHigherOrLower().guessNumber(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))
