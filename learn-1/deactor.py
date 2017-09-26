#!/usr/bin/python
# -*- coding:utf-8 -*-
#===============================================================
#       AUTHOR: YangYang yangyang@suishouji.com
#       CREATER: 2017-09-26 18:48:22
#       FILENAME: deactor.py
#       DESCRIPTION:
#===============================================================
###
##装饰器是一个函数（或者一个可调用对象）。它接受一个类作为参数，返回一个类作为返回值
##
def deactor(config):
    print(config)
    def hello(func):
        """
        方法函数装饰器
        :param func:
        :return:
        """
        print("go to hello")
        def wrapper(self):
            result = func(self)
            return result
        print("out to hello")

        return wrapper
    return hello

def classDeactor(cls):
    """
    类装饰器 用于给类动态添加方法
    :param cls:
    :return:
    """
    def say(self):
        print("hello")
    cls.say = say
    return cls



@classDeactor
class Hello(object):


    def __init__(self):
        pass

    @deactor("config")
    def get(self):
        print("get")





