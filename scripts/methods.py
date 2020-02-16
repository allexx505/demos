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

'''
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''
def change_str_to_timeStamp(str, format):
    '''
    根据格式将字符串的时间转换成时间戳并返回
    :param str: 字符串时间
    :param format: 格式
    :return:
    '''
    timeArray = time.strptime(str, format)
    print(timeArray)
    timeStamp = int(time.mktime(timeArray))
    print(timeStamp)
    return timeStamp

def test_in_func():
    print(abcd)

if __name__ == '__main__':
    # a = change_str_to_timeStamp('2019-12-12', '%Y-%m-%d')
    # b = change_str_to_timeStamp('2019-10-12', '%Y-%m-%d')
    # print(b-a)
    # import request
    # a = {'cn':{1:2,3:4,5:6},'oversea':{1:2,3:4,5:6}}
    # del a['cn'][1]
    # print(a)
    abcd = '11111'
    test_in_func()

