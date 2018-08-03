# coding:utf-8
# 导入库文件
import sys
sys.path.append('./lib')
from flask import Flask
app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()