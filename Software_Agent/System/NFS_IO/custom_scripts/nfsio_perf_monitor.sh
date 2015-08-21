#!/bin/bash

NFS_IO=$1

CMD=/usr/sbin/nfsiostat

#description:
#    summary：
#        op/s      平均每秒的操作数
#        rpc bklog 等待rpc等队列长度
#    read:
#        ops/s     每秒的读操作数
#        kB/s      每秒读的 数据量
#        kB/op     1次读操作的数据量
#        retrans   数据重新发送的次数
#        avg RTT   client发起rpc请求(读) 直到server响应ack 的平均时长（Round Travel Time)
#        avg exe   client发起rpc请求(读) 直到rpc完成所用时长，包含RTT
#
#    write:
#        ops/s     每秒的读写操作数
#        kB/s      每秒写的 数据量
#        kB/op     1次写操作的数据量
#        retrans   数据重新发送的次数
#        avg RTT   client发起rpc请求(写)到server响应ack 的平均时长（Round Travel Time)
#        avg exe   client发起rpc请求(写) 直到rpc完成所用时长，包含RTT


case ${NFS_IO} in
    op_s)
        result=`$CMD | grep -A 1 'rpc bklog' |tail -1| awk -F' ' '{print $1}'`
        echo ${result}
        ;;
    bklog)
        result=`$CMD | grep -A 1 'rpc bklog' |tail -1| awk -F' ' '{print $2}'`
        echo ${result}
        ;;
    read_ops_s)
        result=`$CMD | grep -A 1 '^read:' |tail -1| awk -F' ' '{print $1}'`
        echo ${result}
        ;;
    read_kB_s)
        result=`$CMD | grep -A 1 '^read:' |tail -1| awk -F' ' '{print $2}'`
        echo ${result}
        ;;
    read_kB_op)
        result=`$CMD | grep -A 1 '^read:' |tail -1| awk -F' ' '{print $3}'`
        echo ${result}
        ;;
    read_retry)
        result=`$CMD | grep -A 1 '^read:' |tail -1| awk -F' ' '{print $4}'`
        echo ${result}
        ;;
    read_retry_perc)
        result=`$CMD | grep -A 1 '^read:' |tail -1| awk -F' ' '{print $5}' | grep -o '[^(].*[^%)]'`
        echo ${result}
        ;;
    read_rtt)
        result=`$CMD | grep -A 1 '^read:' |tail -1| awk -F' ' '{print $6}'`
        echo ${result}
        ;;
    read_exe)
        result=`$CMD | grep -A 1 '^read:' |tail -1| awk -F' ' '{print $7}'`
        echo ${result}
        ;;
    write_ops_s)
        result=`$CMD | grep -A 1 '^write:' |tail -1| awk -F' ' '{print $1}'`
        echo ${result}
        ;;
    write_kB_s)
        result=`$CMD | grep -A 1 '^write:' |tail -1| awk -F' ' '{print $2}'`
        echo ${result}
        ;;
    write_kB_op)
        result=`$CMD | grep -A 1 '^write:' |tail -1| awk -F' ' '{print $3}'`
        echo ${result}
        ;;
    write_retry)
        result=`$CMD | grep -A 1 '^write:' |tail -1| awk -F' ' '{print $4}'`
        echo ${result}
        ;;
    write_retry_perc)
        result=`$CMD | grep -A 1 '^write:' |tail -1| awk -F' ' '{print $5}' | grep -o '[^(].*[^%)]'`
        echo ${result}
        ;;
    write_rtt)
        result=`$CMD | grep -A 1 '^write:' |tail -1| awk -F' ' '{print $6}'`
        echo ${result}
        ;;
    write_exe)
        result=`$CMD | grep -A 1 '^write:' |tail -1| awk -F' ' '{print $7}'`
        echo ${result}
        ;;
esac
