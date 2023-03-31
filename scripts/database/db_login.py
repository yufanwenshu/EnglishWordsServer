#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   login.py
@Time    :   2023/03/29 00:57:10
@Author  :   YuFanWenShu 
@Contact :   1365240381@qq.com

'''

# here put the import lib
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.extend([current_dir, current_dir+"\\..\\classes"])

from sqlalchemy import create_engine, text
from sqlalchemy.pool import QueuePool

from db_config import *
from User import User
engine = create_engine(DB_URL, poolclass=QueuePool, pool_size=10, pool_timeout=30)

def login(username, password):
    with engine.connect() as conn:
        cursor = conn.execute(text(LOGIN_SQL_PASSWORD.format(username, password)))
        user_data = cursor.fetchone()
        result = dict()
        if user_data:
            user = User(*user_data)
            result['status'] = 'ok'
            result['data'] = user.convert()
            return result
        else: 
            result['status'] = 'no'
            result['data'] = None
            return result
        
if __name__ == "__main__":
    a = login("yufanwenshu", "cwj010728")
    # b = login("yufanwenshu", "Cwj010728")
    # c = login("cwj", "Cwj010728")
    # print(a)
    # print(b)
    # print(c)
    import json
    print(json.dumps(None))
