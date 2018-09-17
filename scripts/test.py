# -*- coding: utf-8 -*-
# @Create Time : 2018/9/11 22:13
# @Author  : Alex-tan
# @FileName: test.py

OPEN_JOB_FLOW = False

def switch_on_required(func):
    def _check_open(a,b,c):
        global OPEN_JOB_FLOW
        if OPEN_JOB_FLOW:
            ret = func(a,b,c)
            return ret
        else:
            print('switch is off!!please open first')
            return False
    return _check_open


class ExecuteByStep(object):
    def __init__(self,info):
        self.index = 0
        self.next_step = self.index + 1
        self.execute_next = False
        self.todolist = info

    def execute(self):
        if self.index == len(self.todolist):
            print('finish!!!!!!!!!!!')
        else:
            print('now I am doing the step:',self.todolist[self.index])
            self.index = self.next_step
            self.next_step += 1
            self.execute()




def chengfa(x,y):
    return x*y

@switch_on_required
def calculator(x,y,suanfa):
    return suanfa(x,y)

if __name__ == '__main__':
    # OPEN_JOB_FLOW = True
    a = calculator(2,2,chengfa)
    print(a)
    # todolist = [['buy', 1], ['cut', 3], ['cook', 5], ['eat', 2], ['wash', 9], ['play', 7], ['sleep', 3]]
    # todoobj = ExecuteByStep(todolist)
    # todoobj.execute()