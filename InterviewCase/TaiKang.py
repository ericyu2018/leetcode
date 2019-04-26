"""
Author    :   eeyu
Date      :   2019/4/26 13:18
File Name :   TaiKang.py
Description :   Interview problem coming from Tai Kang from Qin
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/26     eeyu   Initial creation
    
"""
# coding: utf-8

class TaiKang(object):
    def filter_three_digits(self, nums):
        '''
        Filter num of three digits from given nums list. No duplicated number should be returned
        :param nums:
        :return:
        '''
        nums_set = set(nums)
        result_list = list()
        for num in nums_set:
            if 100 <= num <= 999 or -999 <= num <= -100:
                result_list.append(num)

        return result_list

    def print_diamond(self, n):
        """
        print diamond of * by given n count. Ex: n = 7 means 7 * 7 diamond
        https://blog.csdn.net/chenlinan_2017/article/details/81434967
        :param n:
        :return:
        """
        for i in range(-n+1, n):
            if i < 0:
                j = -i
            else:
                j = i
            print(' ' * j + '*' * (2*n -1 - 2 * j))


    def compute_twenty_four(self, nums):
        """
        Given 4 numbers and check if you can get result of 24 by using them for +, -, * and / operation
        :param nums:
        :return:
        """
        pass


if __name__ == '__main__':
    taikang_interview = TaiKang()
    print(taikang_interview.filter_three_digits([1, -9, 128, -987, 0]))
    taikang_interview.print_diamond(7)