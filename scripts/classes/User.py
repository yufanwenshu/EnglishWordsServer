#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   User.py
@Time    :   2023/03/31 16:49:34
@Author  :   YuFanWenShu 
@Contact :   1365240381@qq.com

'''

# here put the import lib

class User:
    def __init__(self,username="", password="", uid="", name="", nickname="", sex="", 
    telephone="", email="", registerDate="", birthday="", isSuper=""):
        self.id = str(uid) # 用户id
        self.username = str(username) # 用户名
        self.password = str(password) # 密码
        self.name = str(name) # 真实姓名
        self.nickname = str(nickname) # 昵称
        self.sex = str(sex) # 性别
        self.telephone = str(telephone) # 电话号码
        self.email = str(email) # 电子邮箱
        self.registerDate = str(registerDate) # 注册日期
        self.birthday = str(birthday) # 生日
        self.isSuper = str(isSuper) # 是否为管理员

    def convert(self):
        res = dict()
        res['id'] = self.id 
        res['username'] = self.username
        res['password'] = self.password
        res['name'] = self.name
        res['nickname'] = self.nickname
        res['sex'] = self.sex
        res['telephone'] = self.telephone
        res['email'] = self.email
        res['registerDate'] = self.registerDate
        res['birthday'] = self.birthday
        res['isSuper'] = self.isSuper
        return res

    def __repr__(self):
        data = self.convert()
        return "".join([f"{k}: {v}\n" for k,v in data.items()])

if __name__ == "__main__":
    user = User("yufanwenshu", "cwj010728", "1", "赵梵宇", "宇梵文书", "男", "15225931333",
    "20301030034@fudan.edu.cn", "2023/3/31", "2001/4/20", "true")
    print(user)