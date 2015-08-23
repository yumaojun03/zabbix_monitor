# Nginx
通过nginx的status页面，检测nginx运行状况

## 开启Stub Status

    
```
location /nginx_status {
  stub_status on;
  access_log off;
  allow 127.0.0.1;
  deny all;
}
```
## 监控范围概述
    
```
     Status_Code   页面返回的状态码
     Conn_Active   当前活动连接数
     Conn_Reading  读取 客户端的连接数
     Conn_Writing  响应数据给客户端的连接数
     Conn_Waiting  开启 keep-alive 的情况下,这个值等于 active – (reading+writing), 意思就是 Nginx 已经处理完正在等候下一次请求指令的驻留连接
     Req_Accepts   请求创建连接次数
     Req_Hanled    建立连接次数
     Req_Requests  通过连接发起的总的请求数
```

