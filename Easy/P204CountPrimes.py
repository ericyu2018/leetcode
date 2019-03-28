"""
Author    :   eeyu
Date      :   2019/3/28 10:17
File Name :   P204CountPrimes.py
Description :   https://leetcode-cn.com/problems/count-primes/
Problem:
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/28     eeyu   Initial creation
    
"""
# coding: utf-8
import math

class P204CountPrimes(object):
    def count_primes(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0

        for i in range(0, n):
            if self.is_prime(i):
                count += 1

        return count

    def is_prime(self, n):
        if n <= 1:
            return False

        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False

        return True


    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 3:
            return 0
        else:
            output = [1 for x in range(0, n)]
            output[0] = 0
            output[1] = 0

            for i in range(2, int(math.sqrt(n)) + 1):
                if output[i] == 1:
                    self.filter_multiple(n, output, i)

        return sum(output)


    def filter_multiple(self,n,nums,base):
        i = 2
        while base * i < n:
            nums[base*i] = 0
            i += 1

if __name__ == '__main__':
    print(P204CountPrimes().countPrimes(10))