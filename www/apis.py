#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'LanceCopper'

'''
JSON API definition.
'''

import json, logging, inspect, functools

#简单的几个api错误异常类，用于跑出异常
class APIError(Exception):
    '''
    the base APIError which contains error(required), data(optional) and message(optional).
    '''
    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message

class APIValueError(APIError):
    '''
    Indicate the input value has error or invalid. The data specifies the error field of input form.
    '''
    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)

class APIResourceNotFoundError(APIError):
    '''
    Indicate the resource was not found. The data specifies the resource name.
    '''
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)

class APIPermissionError(APIError):
    '''
    Indicate the api has no permission.
    '''
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)


#页面属性,做出分页效果
class Page(object):
    """docstring for Page"""
    #参数说明：
    #item_count：要显示的条目数量
    #page_index：要显示的是第几页
    #page_size：每页的条目数量
    def __init__(self, item_count, page_index = 1, page_size = 2):
        '''
        Init Pagination by item_count, page_index and page_size.

        >>> p1 = Page(100, 1)
        >>> p1.page_count
        10
        >>> p1.offset
        0
        >>> p1.limit
        10
        >>> p2 = Page(90, 9, 10)
        >>> p2.page_count
        9
        >>> p2.offset
        80
        >>> p2.limit
        10
        >>> p3 = Page(91, 10, 10)
        >>> p3.page_count
        10
        >>> p3.offset
        90
        >>> p3.limit
        10
        '''
        self.item_count = item_count
        self.page_size = page_size
        #计算出应该有多少页才能显示全部的条目
        self.page_count = item_count // page_size + (1 if item_count % page_size > 0 else 0)
        #如果没有条目或者要显示的页超出了能显示的页的范围
        if (item_count == 0) or (page_index > self.page_count):
            #则不显示
            self.offset = 0
            self.limit = 0
            self.page_index = 1
        else:
            #否则说明要显示
            #设置显示页就是传入的要求显示的页
            self.page_index = page_index
            #这页的初始条目的offset
            self.offset = self.page_size * (page_index - 1)
            #这页能显示的数量
            self.limit = self.page_size
        #这页后面是否还有下一页
        self.has_next = self.page_index < self.page_count
        #这页之前是否还有上一页
        self.has_previous = self.page_index > 1

if __name__=='__main__':
    import doctest
    doctest.testmod()
