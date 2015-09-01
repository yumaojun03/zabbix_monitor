# zabbix 结合微信接口

## 准备微信公众号

1. 申请微信公众号 [申请地址](https://mp.weixin.qq.com/)
2. 通过二维码添加用户




## 准备脚本

1. 调整脚本, 配置微信公众号 用户名和密码
  * 使用pip安装 微信公众平台SDK: pip install wechat-sdk
  * 修改Main函数的登陆用户为你的微信公众账号： w = MyWechat(username='your username', password='your pass')
  
**脚本编写时参考的文档**：
  * [微信公众平台 Python SDK](http://wechat-python-sdk.readthedocs.org/)
  * [非官方接口操作说明](http://wechat-python-sdk.readthedocs.org/zh_CN/master/ext.html)


## 准备zabbix
1. 将脚本放置到zabbix 告警插件目录下，比如： /usr/local/zabbix/share/zabbix/alertscripts/
2. 在zabbix 前端给用户配置好 接受消息的media即可

**参考的博客**： 
  * 参考了师兄的博客 [典韦博客](http://mp.weixin.qq.com/s?__biz=MzA3MzYwNjQ3NA==&mid=207765620&idx=1&sn=5958e76998e4773435dd09bbd3da6c34&scene=2&srcid=F767yLKyTCsOWT8NXY2h&from=timeline&isappinstalled=0#rd)

