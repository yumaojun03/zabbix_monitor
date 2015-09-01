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
from weixin import MyWechat
import argparse

class WechatCLI(object):
    """
    微信公众平台命令行工具
    """
    def __init__(self):
        """
        pass
        """
        pass

    def __get_args(self):
        """
        获取命令行参数
        """
        parser = argparse.ArgumentParser(
            description='Arguments for get weixin platform status')
        
        parser.add_argument("-u","--username", 
                            required=True,
                            action="store",
                            help="weixin login username")

        parser.add_argument("-p","--password", 
                            required=True,
                            action="store",
                            help="weixin login password")

        parser.add_argument("-a", "--arguments", 
                            choices=["list_user"],
                            required=True,
                            action="store",
                            help="which information your want to get")

        args = parser.parse_args()
        return args

    def run(self):
        """
        fly...
        """
        args = self.__get_args()
        w = MyWechat(username=args.username, password=args.password) 
        w.login()
        if args.arguments == "list_user":
            users = w.list_all_user()
            for user in users:
                print "%-20s ==>  %-20s" % (user['nick_name'], user['id'])

        
        
if __name__ == "__main__":
    w = WechatCLI()
    w.run()
    

