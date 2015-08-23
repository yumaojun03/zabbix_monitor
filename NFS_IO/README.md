# NFS io state
通过nfsiostat 检测相关系统nfs 运行状态

    
```
    summary：
        op/s      平均每秒的操作数
        rpc bklog 等待rpc等队列长度
    read:
        ops/s     每秒的读操作数
        kB/s      每秒读的 数据量
        kB/op     1次读操作的数据量
        retrans   数据重新发送的次数
        avg RTT   client发起rpc请求(读) 直到server响应ack 的平均时长（Round Travel Time)
        avg exe   client发起rpc请求(读) 直到rpc完成所用时长，包含RTT

    write:
        ops/s     每秒的读写操作数
        kB/s      每秒写的 数据量
        kB/op     1次写操作的数据量
        retrans   数据重新发送的次数
        avg RTT   client发起rpc请求(写)到server响应ack 的平均时长（Round Travel Time)
        avg exe   client发起rpc请求(写) 直到rpc完成所用时长，包含RTT
```
