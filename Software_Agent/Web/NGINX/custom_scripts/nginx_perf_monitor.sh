#!/bin/bash
# Created by 紫川秀
# 

status_url=$1
cmd=$2
httpclient=/usr/bin/curl
args=2


if [ $# -ne $args ]; then
    echo "Please input three arguments!!!" 
    exit 2
fi

case ${cmd} in
    # Status 页面返回的状态码
    Status_Code)
        result=`$httpclient -I $status_url 2> /dev/null | grep '\<HTTP' | cut -d' ' -f2`
        echo $result
    ;;
    # 当前活动连接数
    Conn_Active)
        result=`$httpclient $status_url 2> /dev/null | grep '\<Active connections:' | cut -d':' -f2`
        echo $result
    ;;
    # 读取 客户端的连接数
    Conn_Reading)
        result=`$httpclient $status_url 2> /dev/null | grep '\<Reading:' | cut -d':' -f2 | cut -d' ' -f2`
        echo $result
    ;;
    # 响应数据给客户端的连接数
    Conn_Writing)
        result=`$httpclient $status_url 2> /dev/null | grep '\<Reading:' | cut -d':' -f3 | cut -d' ' -f2`
        echo $result
    ;;
    # 开启 keep-alive 的情况下,这个值等于 active – (reading+writing), 意思就是 Nginx 已经处理完正在等候下一次请求指令的驻留连接
    Conn_Waiting)
        result=`$httpclient $status_url 2> /dev/null | grep '\<Reading:' | cut -d':' -f4`
        echo $result
    ;;
    # 请求创建连接次数
    Req_Accepts)
        result=`$httpclient $status_url 2> /dev/null | grep '^ [0-9]\{1,\}' | cut -d' ' -f2`
        echo $result
    ;;
    # 建立连接次数
    Req_Handled)
        result=`$httpclient $status_url 2> /dev/null | grep '^ [0-9]\{1,\}' | cut -d' ' -f3`
        echo $result
    ;;
    # 通过连接发起的总的请求数
    Req_Requests)
        result=`$httpclient $status_url 2> /dev/null | grep '^ [0-9]\{1,\}' | cut -d' ' -f4`
        echo $result
    ;;

    *)
        echo "Usage:$0(Status_Code|Con_Active|...)" 
    ;;
esac
