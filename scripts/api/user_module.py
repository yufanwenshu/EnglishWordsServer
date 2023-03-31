#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   userModule.py
@Time    :   2023/03/31 16:32:14
@Author  :   YuFanWenShu 
@Contact :   1365240381@qq.com

'''

# here put the import lib
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.extend([current_dir, current_dir+"\\..\\database"])

import json
from flask import Blueprint, request #url_for,render_template,session,redirect, jsonify
import db_login

userModule = Blueprint('user',__name__)

@userModule.route('/login', methods=["POST", "GET"])
def api_login():
    if request.method == "GET":
        username = request.args.get("username", "")
        password = request.args.get("password", "")
    elif request.method == "POST":
        data = request.get_data()
        data = json.loads(data)
        username = data.get("username")
        password = data.get("password")
    return json.dumps(db_login.login(username, password))