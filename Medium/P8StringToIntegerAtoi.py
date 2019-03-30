"""
Author    :   eeyu
Date      :   2019/3/29 11:06
File Name :   P8StringToIntegerAtoi.py
Description :   https://leetcode-cn.com/problems/string-to-integer-atoi/
Problem:
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical value is out of the range of representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.

Example 1:
Input: "42"
Output: 42

Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.

Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign. Therefore no valid conversion could be performed.

Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
             Thefore INT_MIN (−2^31) is returned.
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/29     eeyu   Initial creation
    
"""
# coding: utf-8


class P8StringToIntegerAtoi(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        if str is None or len(str) == 0:
            return 0
        else:
            max_value = pow(2, 31) - 1
            min_value = pow(2, 31) * (-1)
            candidate_str = str.strip().split(' ')[0].split('.')[0]
            valid_index = 0

            try:
                while candidate_str.find('-0') == 0:
                    candidate_str = candidate_str.replace('-0', '-')

                if candidate_str.startswith('+') and candidate_str.count('+') == 1 and not candidate_str.startswith('+-'):
                    candidate_str = candidate_str.replace('+', '')

                for i in range(0, len(candidate_str)):
                    if i == 0 and (candidate_str[i] == '-' or self.is_num(candidate_str[i])):
                        valid_index = i
                    elif self.is_num(candidate_str[i]):
                        valid_index = i
                    else:
                        break

                candidate_str = candidate_str[0:valid_index+1]

                candidate_num = int(candidate_str)

                if candidate_num > max_value:
                    return max_value
                if candidate_num < min_value:
                    return min_value

                return candidate_num

            except ValueError:
                return 0
            except OverflowError:
                if candidate_str.find('-') == 0:
                    return min_value
                else:
                    return max_value

    def is_num(self, s):
        num_str_list = [str(x) for x in range(0, 10)]
        if s in num_str_list:
            return True
        else:
            return False

if __name__ == '__main__':
    print(P8StringToIntegerAtoi().myAtoi("42"))
    print(P8StringToIntegerAtoi().myAtoi("   -42"))
    print(P8StringToIntegerAtoi().myAtoi("4193 with words"))
    print(P8StringToIntegerAtoi().myAtoi("words and 987"))
    print(P8StringToIntegerAtoi().myAtoi("-91283472332"))
    print(P8StringToIntegerAtoi().myAtoi("3.1415926"))
    print(P8StringToIntegerAtoi().myAtoi("-001242"))
    print(P8StringToIntegerAtoi().myAtoi("-0012a42"))
    print(P8StringToIntegerAtoi().myAtoi("+1"))
    print(P8StringToIntegerAtoi().myAtoi("+-1"))
    print(P8StringToIntegerAtoi().myAtoi("-+1"))