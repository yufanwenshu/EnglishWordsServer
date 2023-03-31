#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   app.py
@Time    :   2023/03/29 00:50:08
@Author  :   YuFanWenShu 
@Contact :   1365240381@qq.com

'''

# here put the import lib
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.extend([current_dir, current_dir+'/database', current_dir+'/api'])

from flask import Flask, request
import json
import database.db_login
from flask_cors import CORS
from user_module import userModule

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}}) # 设置允许跨域请求
app.register_blueprint(userModule, url_prefix='/api/user')

@app.route('/api')
def hello_world():
    return 'Server is running!!!'

if __name__ == '__main__':
    app.run(port=8080)