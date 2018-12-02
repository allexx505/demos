# coding:utf-8
# 导入库文件
import sys
sys.path.append('./lib')
from flask import Flask,render_template,request
from server_const import server_host,server_port
app = Flask(__name__)
app.debug = True


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = server_host,port = server_port)