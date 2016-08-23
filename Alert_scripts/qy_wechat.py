#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# 修改解释器的默认编码为unicode
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import urllib2
import traceback


try:
    import json
except ImportError:
    import simplejson as json


def get(url):
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json')
        res = json.loads(urllib2.urlopen(req).read())
        return res


def post(url, data):
        req = urllib2.Request(url, data)
        res = json.loads(urllib2.urlopen(req).read())
        return res


class WeChatError(StandardError):
    pass


class WeChat(object):
    """
    用于操作企业微信的各种接口
    """
    def __init__(self, key, secret, api_endpoint='https://qyapi.weixin.qq.com'):
        """
        更加配置初始化一个微信类
        :param api_endpoint: 微信的API服务的接口地址
        :param key: 企业号 管理账号的 app id
        :param secret: 企业号 管理账号的 app secret
        :param cache_file: 用于缓存token的文件
        """
        self.key = key
        self.secret = secret
        self.api_endpoint = api_endpoint

    @property
    def token(self):
        return self.__get_token()

    def __get_token(self):
        auth_endpoint = '%s/cgi-bin/gettoken?corpid=%s&corpsecret=%s' % (self.api_endpoint, self.key, self.secret)
        try:
            res = get(auth_endpoint)
        except Exception as e:
            raise WeChatError("get token error: %s" % e.message)
        return res['access_token']

    def send_message(self, username, message, agent_id=0):
        """
        往通讯录人员发送消息.

        :param username: 通讯录人员的用户名
        :param message: 需要发送的信息
        :param agent_id: 企业应用的id，整型。可在应用的设置页面查看
        :return: <tuple>   (bool, message), 对应是否成功和调用返回信息
        """
        print message
        send_text_endpoint = '%s/cgi-bin/message/send?access_token=%s' % (self.api_endpoint, self.token)
        message += '\n'
        data = {
            "touser": username,
            "toparty": "",
            "totag": "",
            "msgtype": "text",
            "agentid": agent_id,
            "text": {"content": message},
            "safe": 0
        }
        data = json.dumps(data, ensure_ascii=False, encoding='utf8')
        try:
            res = post(send_text_endpoint, data)
        except Exception as e:
            traceback.print_exc()
            raise WeChatError("send message failed, %s" % e.message)
        if res['errmsg'] == 'ok':
            return True, "success"
        else:
            return False, res


if __name__ == '__main__':
    username = sys.argv[1]
    message = sys.argv[2:] if sys.argv[2:] else sys.stdin.readlines()
    corpid = 'wx7bf857a93fd16ba5'
    secret = 'n5zfLu-uRfRsdhyrC-DPzIrfO1evg_l1-DU_MuAHEidSVS0eCXKRlY-n4DGibcET'
    wechat = WeChat(corpid, secret)
    status, message = wechat.send_message(username, ''.join(message))
    if status:
        print "send message success!"
    else:
        print "send message failed!, %s" % message

