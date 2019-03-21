"""
Author    :   eeyu
Date      :   2019/3/21 20:06
File Name :   Singleton.py
Description :   https://www.cnblogs.com/benric/p/5069347.html and https://www.cnblogs.com/huchong/p/8244279.html
===============================================================================
                                     Change log
===============================================================================

    Date         GUID        Comment
----------------------------------------------------------------
    2019/3/21     eeyu   Initial creation
    
"""
# coding: utf-8

class Singleton(object):
    __singleton_object = None

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    @staticmethod
    def get_singleton_object(name, gender):
        if Singleton.__singleton_object is None:
            Singleton.__singleton_object = Singleton(name, gender)

        return Singleton.__singleton_object


if __name__ == '__main__':
    obj1 = Singleton.get_singleton_object('Eric','male')
    obj2 = Singleton.get_singleton_object('Tom', 'male')
    obj3 = Singleton.get_singleton_object('Eric', 'female')
    print(obj1)
    print(obj2)
    print(obj3)
    print(id(obj1))
    print(id(obj2))
    print(id(obj3))
    print(obj1.gender)
    print(obj1.name)
    # property assigned to obj2 and obj3 will not be effective because of singleton instance
    print(obj2.gender)
    print(obj2.name)

    # they are different object because they are not created using static method of the singleton class
    obj4 = Singleton('Eric','male')
    obj5 = Singleton('Tom', 'male')
    obj6 = Singleton('Eric', 'female')
    print(obj4)
    print(obj5)
    print(obj6)
    print(id(obj4))
    print(id(obj5))
    print(id(obj6))
    print(obj4.name)
    print(obj5.name)
    print(obj6.gender)