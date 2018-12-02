# -*- coding: utf-8 -*-
# @Create Time : 2018/11/4 17:04
# @Author  : Alex-tan
# @FileName: test_for_pystand.py

'''python 标准库尝试'''
import unittest  #python用例测试库

def order_dict():
    '''
    有顺序的字典格式
    :return:
    '''
    from collections import OrderedDict

    order_dict = OrderedDict()

    order_dict['first'] = 'car'
    order_dict['second'] = 'house'
    order_dict['third'] = 'money'

    for sequence,details in order_dict.items():
        print('The ', sequence, 'is', details)

def get_formatted_name(first, last, middle = ''):
    '''
    格式化名字并拼接的方法
    :param first:
    :param last:
    :return:
    '''
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()

class AnonymousSurvey():
    '''收集匿名调查问卷的答案--测试使用unittest模块对该类进行测试'''

    def __init__(self, question):
        '''存储一个问题，并为存储答案作准备'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''显示调查问卷'''
        print(self.question)

    def store_response(self,new_response):
        '''存储答案'''
        self.responses.append(new_response)

    def show_results(self):
        '''显示所有答案'''
        print('Survey answers:')
        for response in self.responses:
            print('-' + response)


class NamesTestCase(unittest.TestCase):
    '''测试get_formatted_name的方法'''

    def test_first_last_name(self):
        '''测试不包含中间名的情况'''
        rst = get_formatted_name('alex', 'tan')
        self.assertEqual(rst, 'Alex Tan')

    def test_middle_name(self):
        '''测试包含中间名的情况'''
        rst = get_formatted_name('alex', 'tan', 'mm')
        self.assertEqual(rst, 'Alex Mm Tan')


if __name__ == '__main__':
    question = 'What lanuage did you first learn to speak?'
    my_survey = AnonymousSurvey(question)
    my_survey.show_question()
    unittest.main()