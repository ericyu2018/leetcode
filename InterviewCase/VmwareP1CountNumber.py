"""
Author    :   eeyu
Date      :   2019/3/14 16:29
File Name :   VmwareP1CountNumber.py
Description :   Count the number of specified number in a integer list
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/14     eeyu   Initial creation
    
"""
# coding: utf-8


class VmwareP1CountNumber(object):
    def count_number(self, nums, key):
        count = 0
        temp_list_contains_key = list()

        for i in nums:
            if str(key) in str(i):
                temp_list_contains_key.append(i)

        print(temp_list_contains_key)
        for j in temp_list_contains_key:
            count = count + self.count_helper(j, key)

        return count

    def count_helper(self, num, key):
        num_string = str(num)
        count = 0

        key_length = len(str(key))
        if key_length == 1:
            for i in num_string:
                if i == str(key):
                    count += 1
        else:
            start_index = 0
            end_index = key_length
            while end_index <= len(num_string):
                if num_string[start_index: end_index] == str(key):
                    count += 1
                start_index += 1
                end_index += 1

        return count


if __name__ == '__main__':
    print(VmwareP1CountNumber().count_number([i for i in range(1, 51)], 5))
    print(VmwareP1CountNumber().count_number([i for i in range(1, 556)], 55))

