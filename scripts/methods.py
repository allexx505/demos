# -*- coding: utf-8 -*-
__author__ = 'tanzicong'

import time

"""
各种通用的方法
"""

def save_to_file(file_name, contents):
    """
    save str to file
    path: E:\script\log
    :param file_name: name
    :param contents: str
    :return:
    """
    file_name = 'E:/script/log/'+file_name
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()

def change_str_to_timeStamp(str, format):
    '''
    根据格式将字符串的时间转换成时间戳并返回
    :param str: 字符串时间
    :param format: 格式
    :return:
    '''
    timeArray = time.strptime(str, format)
    timeStamp = int(time.mktime(timeArray))
    return timeStamp
