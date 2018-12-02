# -*- coding: utf-8 -*-
# @Create Time : 2018/11/4 17:16
# @Author  : Alex-tan
# @FileName: test_for_file_handle.py

'''文件以及异常处理的练习代码'''


def read_file():
    '''
    写文件操作
    :return:
    '''
    file_name = 'pi_digits.txt'
    with open(file_name) as file_object:
        # contents = file_object.read()
        # print(contents.rstrip())
        for line in file_object:
            print(line.rstrip())

def wirte_file():
    '''
    写文件操作
    :return:
    '''
    file_name = 'write_log.txt'
    with open(file_name,'w') as file_object:
        file_object.write('just for a test, do not feel fear!!!')

def handle_error(up, down):
    '''
    处理异常
    :return:
    '''
    try:
        answer = up/ down
    except Exception as e:
        print('ERROR:',e)
    else:
        print(answer)

def save_data():
    '''
    存储数据
    :return:
    '''
    import json
    numbers = [1, 2, 3, 4, 5]
    file_name = 'save_data.json'
    with open(file_name, 'w') as file_object:
        json.dump(numbers,file_object)

def read_data():
    '''
    读取数据
    :return:
    '''
    import json
    file_name = 'save_data.json'
    with open(file_name, 'r') as file_object:
        data = json.load(file_object)
    print(data)


if __name__ == '__main__':
    # read_file()
    # wirte_file()
    # handle_error(5, 0)
    # handle_error(5, 1)
    save_data()
    read_data()