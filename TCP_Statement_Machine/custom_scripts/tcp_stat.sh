#!/bin/bash

STAT=$1

CMD=/usr/sbin/ss

#description:
#    client:
#        sync_sent     请求TCP连接(SYN = 1)
#        established   连接建立 
#        fin-wait-1    请求断开，等待服务器端的ACK(FIN = 1)
#        fin-wait-2    请求断开，等待服务器端的FIN 
#        time-wait     等待最后一个ACK确定的到达，等待2个Maximum Segment Life 时长
#
#    server:
#        sync_received  确认连接(确认SYN)  
#        close-wait    等待APP完成连接断开前的处理 
#        last-ack      等待client 最后的ACK的到达


case ${STAT} in
    syn-sent)
        result=`$CMD -o state syn-sent | wc -l `
        echo $[$result-1]
        ;;
    syn-received)
        result=`$CMD -o state syn-recv | wc -l `
        echo $[$result-1]
        ;;
    established)
        result=`$CMD -o state established | wc -l `
        echo $[$result-1]
        ;;
    fin-wait-1)
        result=`$CMD -o state fin-wait-1 | wc -l `
        echo $[$result-1]
        ;;
    fin-wait-2)
        result=`$CMD -o state fin-wait-2 | wc -l `
        echo $[$result-1]
        ;;
    time-wait)
        result=`$CMD -o state time-wait | wc -l `
        echo $[$result-1]
        ;;
    close-wait)
        result=`$CMD -o state close-wait | wc -l `
        echo $[$result-1]
        ;;
    last-ack)
        result=`$CMD -o state last-ack | wc -l `
        echo $[$result-1]
        ;;
    *)
        echo "$0 {syn-sent|syn-received|established|...}"
        ;;
esac
