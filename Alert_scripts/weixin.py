#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Date        : 2015-08-31
Author      : 紫川秀
Email       : yumaojun03@gmail.com
Version     : 0.1
Description : 用于zabbix接入微信公众平台
"""

from __future__ import unicode_literals

from wechat_sdk import WechatExt
from sys import argv, exit
from wechat_sdk.exceptions import NeedLoginError
import json
import os.path

class MyWechat(object):
    """
    my wechat platform
    """
    
    def __init__(self, username, password, cookiePath='/tmp/cook_wexin.zoo'):
        """
        init wechat object
        """
        self.__user = username
        self.__pass = password
        self.__token = ''
        self.__cookies = ''
        self.__cookiePath = cookiePath
    
    def __password_login(self):
        """
        login 后生成缓存文件, 以用户和密码的形式登陆
        """
        self.__wechat = WechatExt(username=self.__user, 
                                  password=self.__pass,
                                  login=False)
        try:
            self.__wechat.login()
        except NeedLoginError:
            print "your need to retry login."

        with open(self.__cookiePath, 'w') as f:
            json.dump(self.__wechat.get_token_cookies(), f)

    def __token_login(self):
        """
        载入缓存 cookie 和 token的文件， 以token的形式登陆
        """
        with open(self.__cookiePath, 'r') as f:
            cookie = json.load(f)
            self.__cookies = cookie['cookies']
            self.__token = cookie['token']
        self.__wechat = WechatExt(username=self.__user, 
                                  password=self.__pass,
                                  token=self.__token,
                                  cookies=self.__cookies,
                                  login=False)
            
            
    def login(self):
        """
        执行login() 可以有效应对可能出现的验证码问题。
        """
        if not os.path.exists(self.__cookiePath):
            self.__password_login()
        else:
            self.__token_login()
        try:
            self.__wechat.get_group_list()
        except NeedLoginError, e:
            self.__password_login()

    def list_group(self):
        """
        列出所有用户组的信息
        """
        groups_json = self.__wechat.get_group_list()
        groups = json.loads(groups_json) 
        return groups['groups']

    def list_group_user(self, groupid): 
        """
        根据用户组ID 列出用于组下面的成员信息
        """
        users_json = self.__wechat.get_user_list(groupid=groupid)
        users = json.loads(users_json)
        return users['contacts']

    def list_all_user(self):
        """
        列出所有的用户
        """
        users = []
        groups_id = [group['id'] for group in self.list_group()]
        for id in groups_id:
            users_list = self.list_group_user(groupid=id)
            if users_list:
                users.extend(users_list)
        return users
    
    def get_user_id(self, nick_name):
        """
        根据nick_name 查询用于的user_id
        """
        user_all = self.list_all_user()
        nick_name = unicode(nick_name.decode('utf-8'))
        
        for user in user_all:
            if user['nick_name'] == nick_name:
                user_id = user['id']
        return user_id

    def send_msg(self, user_id, msg=None):
        """
        向用户发送文本信息
        """
        try:
            self.__wechat.send_message(user_id, content=msg)
        except Exception, e:
            print "Failed, reason: %s" % e
            exit(5)
        print "OK, send msg successful"
        
        
def Main():
    """
    用于执行的主函数
    """
    msg_send_to = argv[1]
    msg_theme = argv[2]
    msg_body = argv[3]

    
    w = MyWechat(username='719118794@qq.com', password='yusky0902') 
    w.login()
    w.send_msg(msg_send_to, msg_body)

if __name__ == "__main__":
    Main()

