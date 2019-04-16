"""
Author    :   eeyu
Date      :   2019/4/9 16:22
File Name :   ChinaTelecomCloud.py
Description :   Test developer job in eCloud team, Cloud team of ChinaTelecom
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/4/9     eeyu   Initial creation
    
"""
# coding: utf-8
import json
import functools
import time
from datetime import datetime


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        date_str = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        print("[{0}] Start to call function {1}".format(date_str, func.__name__))
        r = func(*args, **kwargs)
        date_str = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
        print("[{0}] Completed to call function {1}".format(date_str, func.__name__))
        return r
    return wrapper


def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            date_str = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
            print("[{0}] {1}".format(date_str, text))
            return func(*args, **kwargs)
        return wrapper
    return decorator


def metric(func):
    def wrapper(*args, **kwargs):
        start_time = int(time.time())
        r = func(*args, **kwargs)
        complete_time = int(time.time())
        print('Completed function call in {0} seconds'.format(complete_time - start_time))
        return r
    return wrapper


class ChinaTelecomCloud(object):
    def format_content_coming_from_file(self, text_file):
        '''
        Read text from text_file and format the output to csv and output based on salary value in desc order
        :param text_file:
        :return:
        '''
        person_mapping = dict()
        with open(text_file, 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()
                if line == '':
                    break
                else:
                    person_raw = line.split(' ')
                    person_id = person_raw[0]
                    person_age = person_raw[-4]
                    person_city = person_raw[-3]
                    person_job = person_raw[-2]
                    person_salary = person_raw[-1]
                    person_name = "".join(person_raw[1:-4])
                    output = '{0},{1},{2},{3},{4},{5}'.format(person_id, person_name, person_age, person_city,
                                                              person_job, person_salary)
                    person_mapping[output] = int(output.split(',')[-1])

        with open('output.txt', 'w+', encoding='utf-8') as wf:
            salary_list = list(person_mapping.values())
            salary_list.sort(reverse=True)
            for salary in salary_list:
                for item in person_mapping.keys():
                    if person_mapping[item] == salary:
                        wf.writelines('{0}\n'.format(item))
                        print(item)

    def filter_key_information_from_log_file_and_output_result_to_json(self, log_file, app_name):
        '''
        Get application name, deployment status and deployment argument from log file and dump these information to json file
        :param log_file:
        :param app_name:
        :return:
        '''
        log_list = list()
        with open(log_file, 'r', encoding='utf-8') as file:
            while True:
                line = file.readline()
                if line == '':
                    break
                else:
                    if line.find(app_name) != -1:
                        log_list.append(line)
                    else:
                        continue

        if log_list[0].find('json args:') != -1:
            log_list[0] = log_list[0].split('json args:')[1].strip()

        if log_list[1].find('Success') != -1:
            result = 'Success'
        else:
            result = 'Fail'

        json_dict = dict()
        json_dict[result] = {app_name: log_list[0]}
        with open('output.json', 'w+') as dump_f:
            json.dump(json_dict, dump_f)


    def use_of_stack(self):
        pass

    @log
    def use_of_decorator(self):
        print('This is a common function which will decorated by a decorator with default log message')
        time.sleep(3)

    @log2('I am user defined message')
    def use_of_decorator2(self):
        print('This is a common function which will decorated by a decorator with user defined log message')
        time.sleep(3)

    @metric
    def use_of_decorator3(self):
        print('This method will sleep 5 seconds')
        time.sleep(5)

if __name__ == '__main__':
    ctyun_test = ChinaTelecomCloud()
    ctyun_test.format_content_coming_from_file('ChinaTelecomCloud.txt')
    ctyun_test.filter_key_information_from_log_file_and_output_result_to_json('ChinaTelecomCloud.log', 'App1')
    ctyun_test.use_of_decorator()

    # function is also an object and can be assigned to a parameter. Don't use parenthesis when assign func to parameter
    f = ctyun_test.use_of_decorator2
    f()
    print(f.__name__)

    ctyun_test.use_of_decorator3()