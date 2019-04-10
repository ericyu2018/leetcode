"""
Author    :   eeyu
Date      :   2019/4/10 10:16
File Name :   P292NimGame.py
Description : https://leetcode-cn.com/problems/nim-game/
Problem:
You are playing the following Nim Game with your friend: There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones. The one who removes the last stone will be the winner. You will take the first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write a function to determine whether you can win the game given the number of stones in the heap.

Example:
Input: 4
Output: false
Explanation: If there are 4 stones in the heap, then you will never win the game;
             No matter 1, 2, or 3 stones you remove, the last stone will always be
             removed by your friend.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/10     eeyu   Initial creation
    
"""
# coding: utf-8


class P292NimGame(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 3:
            return True
        else:
            if n % 4 == 0:
                return False
            else:
                return True

if __name__ == '__main__':
    print(P292NimGame().canWinNim(3))
    print(P292NimGame().canWinNim(4))
    print(P292NimGame().canWinNim(5))
    print(P292NimGame().canWinNim(6))
