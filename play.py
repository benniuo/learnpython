#!/usr/bin/env python
# -*- coding: utf-8 -*-


def benchmark(func):
    """
    装饰器打印一个函数的执行时间
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print func.__name__, time.clock()-t
        return res
    return wrapper

def logging(func):
    """
    装饰器记录函数日志
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print res
        print func.__name__, args, kwargs
        return res
    return wrapper

def counter(func):
    """
    记录并打印一个函数的执行次数
    """
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print "{0} has been used: {1}x".format(func.__name__, wrapper.count)
        return res
    wrapper.count = 0
    return wrapper

@counter
@benchmark
@logging
def reverse_string(string):
    return string

print reverse_string("Able was I ere I saw Elba")
print reverse_string("A man, a plan, a canoe, pasta, heros, rajahs")
print reverse_string("Able was I ere I saw Elba")