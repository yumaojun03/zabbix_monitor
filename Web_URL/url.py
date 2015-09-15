#!/usr/bin/env python
# coding: utf-8

from __future__ import  unicode_literals

"""
Date        : 2015-09-14
Author      : 紫川秀
Email       : yumaojun03@gmail.com
Version     : 0.1
Description :
              用于 zabbix 监控 website
"""


import re
import pycurl
import argparse
from urllib import urlencode
try:
    from cStringIO import StringIO
except ImportErr:
    from StringIO import SringIO



class URL(object):
    """
    URL对象，用于对URL进行各种检测
    """
    def __init__(self, url):
        self.url = url
        self.contents = StringIO()
        self.curl = pycurl.Curl()
        self.curl.setopt(pycurl.URL, self.url)
        self.curl.setopt(pycurl.ENCODING, 'gzip')
        self.curl.setopt(pycurl.WRITEFUNCTION, self.contents.write)
        self.curl.setopt(self.curl.FOLLOWLOCATION, True)
        self.curl.setopt(self.curl.TIMEOUT, 10)

    def check_page(self):
        """
        访问页面
        """
        c = self.curl
        try:
            c.perform()
        except pycurl.error, e:
            raise StandardError("pycurl excute error: %s" % str(e))

    def get_perf(self):
        """
        依次却得访问过程中的性能数据
            HTTP状态码
            DNS解析时间, 单位微妙
            建立连接时间, 单位微妙
            准备传输时间, 单位微妙
            传输开始时间, 单位微妙
            重定向执行时间, 单位微妙
            重定向执行数量
            重定向URL
            响应结束时间, 单位微妙
            下载数据包大小, 单位bytes
            HTTP头部大小, 单位bytes
            下载速率, kb/s
        """
        c = self.curl
        perf = dict()
        perf['HTTP_CODE'] = c.getinfo(c.HTTP_CODE)
        perf['NAMELOOKUP_TIME'] = c.getinfo(c.NAMELOOKUP_TIME)
        perf['CONNECT_TIME'] = c.getinfo(c.CONNECT_TIME)
        perf['PRETRANSFER_TIME'] = c.getinfo(c.PRETRANSFER_TIME)
        perf['STARTTRANSFER_TIME'] = c.getinfo(c.STARTTRANSFER_TIME)
        perf['REDIRECT_TIME'] = c.getinfo(c.REDIRECT_TIME)
        perf['REDIRECT_COUNT'] = c.getinfo(c.REDIRECT_COUNT)
        perf['REDIRECT_URL'] = c.getinfo(c.REDIRECT_URL)
        perf['TOTAL_TIME'] = c.getinfo(c.TOTAL_TIME)
        perf['SIZE_DOWNLOAD'] = c.getinfo(c.SIZE_DOWNLOAD)
        perf['HEADER_SIZE'] = c.getinfo(c.HEADER_SIZE)
        perf['SPEED_DOWNLOAD'] = c.getinfo(c.SPEED_DOWNLOAD)
        return perf

    def get_hostname(self):
        """
        捕获url中的host， 比如www.baidu.com
        """
        match = re.search(r'http://(?P<host>[\w.]+)/.*', self.url) 
        if match:
            return match.groupdict()['host']
        else:
            raise StandardError('no hostname catch.')

    def quote(self, s, encoding='utf-8'):
        """
        utf8 encoding quote
        """
        for k, v in s.iteritems():
            if isinstance(v, unicode):
                s[k] = v.encode(encoding)
        return  urlencode(s)

    def login(self, postdata, cookiefile, cookiejar):
        """
        登陆
        """
        c = self.curl
        postfields = self.quote(postdata)
        c.setopt(c.POSTFIELDS, postfields)
        c.setopt(pycurl.COOKIEFILE, cookiefile)
        c.setopt(pycurl.COOKIEJAR, cookiejar)
        try:
            c.perform()
        except pycurl.error, e:
            raise StandardError("pycurl excute error: %s" % str(e))

    def check_login(self):
        """
        登陆检测
        """
        body = self.contents.getvalue()
        pos = body.decode('utf8').find(u'登录成功')
        if pos == -1:
            return 0
        else:
            return 1
        
def get_args():
    """
    Get argument from CLI
    """
    parser = argparse.ArgumentParser(
        description="argument for http request")
    parser.add_argument("--method",
                        required=True,
                        choices=["get", "post"],
                        action="store",
                        help="http request method")
    parser.add_argument("--url",
                        required=True,
                        action="store",
                        help="the website url")
    parser.add_argument("--username",
                        required=False,
                        action="store",
                        help="the username login")
    parser.add_argument("--password",
                        required=False,
                        action="store",
                        help="the password login")
    args = parser.parse_args()
    return args

def main():
    """
    fly...
    """
    args = get_args()
    url = URL(args.url)
    if args.method == "get":
        url.check_page()
        print url.get_perf()
    elif args.method == "post":
        host = url.get_hostname()
        postdata = {"username": args.username,
                    "password": args.password}
        cookiefile = host + ".zoo"
        cookiejar = host + ".zoo"
        url.login(postdata, cookiefile, cookiejar)
        print "check: ", url.check_login()
        print url.get_perf()
       
        
if __name__ == "__main__":
    main()
