"""
Author    :   eeyu
Date      :   2019/3/31 21:42
File Name :   CH1Basic.py
Description :   
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/31     eeyu   Initial creation
    
"""
# coding: utf-8

class CH1Basic(object):
    def get_segment(self, current_index, get_size):
        '''
        :param current_index: current page index
        :param get_size: count of letters to show
        :return: (letters of specified page index, total page count)
        '''
        letter_list = [chr(x) for x in range(65,91)]
        start_get = (current_index - 1) * get_size
        get_data = letter_list[start_get: current_index * get_size]
        total_index_touple = divmod(len(letter_list), get_size)
        total_index = total_index_touple[0] + total_index_touple[1]
        return (get_data, total_index)


if __name__ == '__main__':
    result = CH1Basic().get_segment(2, 5)
    print(result[0])
    print(result[1])