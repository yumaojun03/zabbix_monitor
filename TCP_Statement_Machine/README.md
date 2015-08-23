# TCP Statement Machine
通过ss命令 检测系统TCP连接状态


    
```
description:
    client:
        sync_sent     请求TCP连接(SYN = 1)
        established   连接建立 
        fin-wait-1    请求断开，等待服务器端的ACK(FIN = 1)
        fin-wait-2    请求断开，等待服务器端的FIN 
        time-wait     等待最后一个ACK确定的到达，等待2个Maximum Segment Life 时长

    server:
        sync_received  确认连接(确认SYN)  
        close-wait    等待APP完成连接断开前的处理 
        last-ack      等待client 最后的ACK的到达
```
