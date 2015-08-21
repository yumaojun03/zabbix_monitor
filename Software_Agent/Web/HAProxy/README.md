# HAProxy Status Page 状态信息描述

## 开启状态页面方法

```
listen stats
    mode http
    bind 0.0.0.0:8808
    stats enable
    stats hide-version
    stats refresh 30s
    stats uri     /haproxyadmin?stats
    stats realm   Haproxy\ Statistics
    stats auth    admin:newmedia
    stats admin if TRUE
```

#### Queue
* Cur: 当前的队列请求数量 (qcur: current queued requests)
* Max：最大的队列请求数量 (qmax: max queued requests)
* Limit：队列限制数量 (qlimit: queue limit)

#### Session rate
* Cur: 每秒的当前回话的限制数量  (rate: number of sessions per second over last elapsed second)
* Max: 每秒的新的最大的回话量    (rate_max: max number of new sessions per second)
* Limit: 每秒的新回话的限制数量   (rate_lim: limit on new sessions per second)

#### Sessions
* Cur: 当前的回话 (scur: current sessions)
* Max: 最大回话 (smax: max sessions)
* Limit: 回话限制 (slim: sessions limit)
* Total: 总共回话量  (stot: total sessions)
* Lbtot: 选中一台服务器所用的总时间(lbtot: total number of times a server was selected)
* Last: 最近一次改变状态的持续时长 (lastchg: last status change ,in seconds)

#### Bytes
* In： 网络的字节数输入总量  (bin: bytes in)
* Out：网络的字节数输出总量  (bout: bytes out)

#### Denied
* Req: 拒绝请求量(dreq: denied requests)
* Resp：拒绝回应(dresp: denied responses)

#### Errors
* Req： 错误请求 (ereq: request errors)
* Conn：错误的连接 (econ: connection errors)
* Resp: 错误的回应(eresp: response errors ,among which srv_abrt)


#### Warnings
* Retr: 重新尝试 (wretr: retries , warning)
* Redis：再次发送 (wredis: redispatches ,warning)


#### Server列表：
* Status:状态，包括up(后端机活动)和down(后端机挂掉)两种状态 (status: status (UP/DOWN/NOLB/MAINT/MAINT(via)...))
* LastChk: 服务检查状态(check_status: status of last health check, 具体见后面36条)
* Wght: 权重 (weight: server weight (server), total weight (backend))
* Act: 活动链接数量 (act: server is active (server), number of active servers (backend) )
* Bck: 备份的服务器数量 (bck: server is backup (server), number of backup servers (backend) )
* Chk： 检查失败的次数(chkfail: number of failed checks)
* Down：由up转换成down的次数 (chkdown: number of UP->DOWN transitions)
* Downtime: 总的downtime 时间 (downtime: total downtime (in seconds))
* Throttle: 设备变热状态(throttle: warm up status)

以下是csv风格的状态统计数据，也是官方对 status页面的一个说明
详情见  [url](http://cbonte.github.io/haproxy-dconv/configuration-1.4.html#9.1)

```
  0. pxname: proxy name
  1. svname: service name (FRONTEND for frontend, BACKEND for backend, any name
    for server)
  2. qcur: current queued requests
  3. qmax: max queued requests
  4. scur: current sessions
  5. smax: max sessions
  6. slim: sessions limit
  7. stot: total sessions
  8. bin: bytes in
  9. bout: bytes out
 10. dreq: denied requests
 11. dresp: denied responses
 12. ereq: request errors
 13. econ: connection errors
 14. eresp: response errors (among which srv_abrt)
 15. wretr: retries (warning)
 16. wredis: redispatches (warning)
 17. status: status (UP/DOWN/NOLB/MAINT/MAINT(via)...)
 18. weight: server weight (server), total weight (backend)
 19. act: server is active (server), number of active servers (backend)
 20. bck: server is backup (server), number of backup servers (backend)
 21. chkfail: number of failed checks
 22. chkdown: number of UP->DOWN transitions
 23. lastchg: last status change (in seconds)
 24. downtime: total downtime (in seconds)
 25. qlimit: queue limit
 26. pid: process id (0 for first instance, 1 for second, ...)
 27. iid: unique proxy id
 28. sid: service id (unique inside a proxy)
 29. throttle: warm up status
 30. lbtot: total number of times a server was selected
 31. tracked: id of proxy/server if tracking is enabled
 32. type (0=frontend, 1=backend, 2=server, 3=socket)
 33. rate: number of sessions per second over last elapsed second
 34. rate_lim: limit on new sessions per second
 35. rate_max: max number of new sessions per second
 36. check_status: status of last health check, one of:
        UNK     -> unknown
        INI     -> initializing
        SOCKERR -> socket error
        L4OK    -> check passed on layer 4, no upper layers testing enabled
        L4TMOUT -> layer 1-4 timeout
        L4CON   -> layer 1-4 connection problem, for example
                   "Connection refused" (tcp rst) or "No route to host" (icmp)
        L6OK    -> check passed on layer 6
        L6TOUT  -> layer 6 (SSL) timeout
        L6RSP   -> layer 6 invalid response - protocol error
        L7OK    -> check passed on layer 7
        L7OKC   -> check conditionally passed on layer 7, for example 404 with
                   disable-on-404
        L7TOUT  -> layer 7 (HTTP/SMTP) timeout
        L7RSP   -> layer 7 invalid response - protocol error
        L7STS   -> layer 7 response error, for example HTTP 5xx
 37. check_code: layer5-7 code, if available
 38. check_duration: time in ms took to finish last health check
 39. hrsp_1xx: http responses with 1xx code
 40. hrsp_2xx: http responses with 2xx code
 41. hrsp_3xx: http responses with 3xx code
 42. hrsp_4xx: http responses with 4xx code
 43. hrsp_5xx: http responses with 5xx code
 44. hrsp_other: http responses with other codes (protocol error)
 45. hanafail: failed health checks details
 46. req_rate: HTTP requests per second over last elapsed second
 47. req_rate_max: max number of HTTP requests per second observed
 48. req_tot: total number of HTTP requests received
 49. cli_abrt: number of data transfers aborted by the client
 50. srv_abrt: number of data transfers aborted by the server (inc. in eresp)
```

* * *

# Unix Socket Commands

## 开启Unix Socket 方法


```
添加入 global 段
stats socket /var/lib/haproxy/stats
```

官网有更详尽的解释： [url](http://cbonte.github.io/haproxy-dconv/configuration-1.4.html#9.2)

以下是通过help却出来的一些简要的帮助信息

```
clear counters : clear max statistics counters (add 'all' for all counters)
clear table    : remove an entry from a table
help           : this message
prompt         : toggle interactive mode with prompt
quit           : disconnect
show info      : report information about the running process
show pools     : report information about the memory pools usage
show stat      : report counters for each proxy and server
show errors    : report last request and response errors for each proxy
show sess [id] : report the list of current sessions or dump this session
show table [id]: report table usage stats or dump this table's contents
get weight     : report a server's current weight
set weight     : change a server's weight
set server     : change a server's state or weight
set table [id] : update or create a table entry's data
set timeout    : change a timeout setting
set maxconn    : change a maxconn setting
set rate-limit : change a rate limiting value
disable        : put a server or frontend in maintenance mode
enable         : re-enable a server or frontend which is in maintenance mode
shutdown       : kill a session or a frontend (eg:to release listening ports)
show acl [id]  : report avalaible acls or dump an acl's contents
get acl        : reports the patterns matching a sample for an ACL
add acl        : add acl entry
del acl        : delete acl entry
clear acl <id> : clear the content of this acl
show map [id]  : report avalaible maps or dump a map's contents
get map        : reports the keys and values matching a sample for a map
set map        : modify map entry
add map        : add map entry
del map        : delete map entry
clear map <id> : clear the content of this map
set ssl <stmt> : set statement for ssl
```
