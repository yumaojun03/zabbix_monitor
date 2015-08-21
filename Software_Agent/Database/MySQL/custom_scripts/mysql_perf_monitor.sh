#!/bin/sh 
# Created by 紫川秀
MYSQL_USER=$1
MYSQL_PWD=$2
MYSQL_COM=$3
ARGS=3

if [ -x /usr/bin/mysqladmin ]; then
    Bin_file=/usr/bin/mysqladmin
elif [ -x /usr/local/bin/mysqladmin ]; then
    Bin_file=/usr/local/bin/mysqladmin
else
   echo "$Bin_file can't find."
fi

if [ -x /usr/bin/mysql ]; then
    Bin_mysql=/usr/bin/mysql
elif [ -x /usr/local/bin/mysql ]; then
    Bin_mysql=/usr/local/bin/mysql
else
    echo "$Bin_mysql can't find."
fi

if [ $# -ne "$ARGS" ];then
    echo "Please input three arguments!!!" 
    exit 2
fi

case ${MYSQL_COM} in
    # 基本状态信息统计
        # 存活状态
    Ping)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  ping &> /dev/null && echo 1 || echo 0`
            echo $result 
            ;;
        #  MySQL Server 的运行时间，单位是秒
    Uptime)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  status 2> /dev/null | grep -o  'Uptime:[[:space:]]*[0-9]\+' |cut -d":" -f2`
            echo $result 
            ;;
        # 活动线程的数量，也就是 client 数量
    Threads)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  status 2> /dev/null | grep -o  'Threads:[[:space:]]*[0-9]\+' |cut -d":" -f2`
            echo $result 
            ;;
        # Client 发起的总的请求次数
    Questions)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD} status 2> /dev/null | grep -o  'Questions:[[:space:]]*[0-9]\+' |cut -d":" -f2`
            echo $result 
            ;;
        # 慢查询的次数，具体可以看  slow query log 
    Slow_queries)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD} status 2> /dev/null | grep -o  'Slow[ ]queries:[[:space:]]*[0-9]\+' |cut -d":" -f2`
            echo $result 
            ;;
        # 平均每秒请求次数
    Queries_per_second_avg)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD} status 2> /dev/null | grep -o  'Queries[ ]per[ ]second[ ]avg:[[:space:]]*[0-9.]\+' | cut -d":" -f2`
            echo $result 
            ;;
        # Server过去打开过的表的一个 总和
    Opens)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD} status 2> /dev/null | grep -o  'Opens:[[:space:]]*[0-9]\+' |cut -d":" -f2`
            echo $result 
            ;;
        # Server  执行 flush-*, refresh, and reload  这些指令的 总次数
    Flush_tables)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD} status 2> /dev/null | grep -o  'Flush[ ]tables:[[:space:]]*[0-9]\+' |cut -d":" -f2`
            echo $result 
            ;;
        # 当前打开的 table 数量
    Open_tables)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD} status 2> /dev/null | grep -o  'Open[ ]tables:[[:space:]]*[0-9]\+' |cut -d":" -f2`
            echo $result 
            ;;

    # 增删查改 事物等语句执行次数统计                 
        # insert 语句执行次数
    Com_insert)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD} extended-status 2> /dev/null |grep '\<Com_insert\>'   | cut -d"|" -f3`
                echo $result 
                ;;
        # delete 语句执行次数
    Com_delete)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD} extended-status 2> /dev/null |grep '\<Com_delete\>'   | cut -d"|" -f3`
                echo $result 
                 ;;
        # select 语句执行次数
    Com_select)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD} extended-status 2> /dev/null |grep '\<Com_select\>'   | cut -d"|" -f3`
                echo $result 
                ;;
        # update 语句执行次数
    Com_update)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD} extended-status 2> /dev/null |grep  '\<Com_update\>'  | cut -d"|" -f3`
            echo $result 
            ;;
        # commit 语句执行次数
    Com_commit)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Com_commit\>'   | cut -d"|" -f3`
                echo $result 
                ;;
        # rollback 语句执行次数
    Com_rollback)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Com_rollback\>' | cut -d"|" -f3`
                echo $result 
                ;;

    # 流量相关 语句执行次数统计                         
        # Server 响应的总的数据量
    Bytes_sent)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Bytes_sent\>'   | cut -d"|" -f3`
                echo $result 
                ;;
        # Server 接收到的请求的总的数据量
    Bytes_received)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Bytes_received\>' |cut -d"|" -f3`
                echo $result 
                ;;

    # 线程状态
        # 当前活动的线程数
    Threads_running)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Threads_running\>' | cut -d"|" -f3`
                echo $result 
                ;;
        # 当前打开的连接数(包括活动连接与非活动连接)
    Threads_connected)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Threads_connected\>' | cut -d"|" -f3`
                echo $result 
                ;;
        # 新创建的连接数(如果此值过大，则说明线程池太小，需要调大线程池：thread_cache_size ，可以按照此百分比增大：Threads_created/Connections
    Threads_created)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Threads_created\>' | cut -d"|" -f3`
                echo $result 
                ;;
        # 线程池中剩余线程
    Threads_cached)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Threads_cached\>' | cut -d"|" -f3`
                echo $result 
                ;;

    # InnoDB引擎Row状态
        # 写入行的数量
    Rows_inserted)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Innodb_rows_inserted\>' | cut -d"|" -f3`
                echo $result 
                ;;
        # 更新行的数量
    Rows_updated)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Innodb_rows_updated\>' | cut -d"|" -f3`
                echo $result 
                ;;
        # 删除行的数量
    Rows_deleted)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Innodb_rows_deleted\>' | cut -d"|" -f3`
                echo $result 
                ;;
        # 读取行的数量
    Rows_read)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Innodb_rows_read\>' | cut -d"|" -f3`
                echo $result 
                ;;
        # 行锁的个数(被施加了独占锁的行数)
    Rows_lock_number)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Innodb_row_lock_current_waits\>' | cut -d"|" -f3`
                echo $result 
                ;;
        # 行锁的时长(所有操作 等待独占锁释放 的总的时间)
    Rows_lock_time)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Innodb_row_lock_time\>' | cut -d"|" -f3`
                echo $result 
                ;;

    # InnoDB Buffer Pool Page状态
        # 包含数据的页的数量(包括 dirty 和 clean)
    Page_data)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Innodb_buffer_pool_pages_data\>' | cut -d"|" -f3`
                echo $result 
                ;;
        # 包含ditry 数据的页的数量
    Page_dirty)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Innodb_buffer_pool_pages_dirty\>' | cut -d"|" -f3`
                echo $result 
                ;;
        # 空余的，可以使用的页的数据
    Page_free)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Innodb_buffer_pool_pages_free\>' | cut -d"|" -f3`
                echo $result 
                ;;
        # 置换页中数据的请求次数
    Page_flush)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Innodb_buffer_pool_pages_flushed\>' | cut -d"|" -f3`
                echo $result 
                ;;

    # InnoDB 引擎Data状态
        # InnoDB 数据读总次数
    Data_reads)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Innodb_data_reads\>' | cut -d"|" -f3`
                echo $result 
                ;;
        # InnoDB 数据写总次数
    Data_writes)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Innodb_data_writes\>' | cut -d"|" -f3`
                echo $result 
                ;;
        # InnoDB 数据读总大小
    Data_read)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Innodb_data_read\>' | cut -d"|" -f3`
                echo $result 
                ;;
        # InnoDB 数据写总大小
    Data_written)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Innodb_data_written\>' | cut -d"|" -f3`
                echo $result 
                ;;
     
    # InnoDB Log写状态
        # InnoDB 往磁盘同步日志的总次数
    Log_fsyncs)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Innodb_os_log_fsyncs\>' | cut -d"|" -f3`
                echo $result 
                ;;
        # InnoDB 往磁盘同步日志的总大小
    Log_written)
        result=`${Bin_file} -u${MYSQL_USER} -p${MYSQL_PWD}  extended-status 2> /dev/null |grep '\<Innodb_os_log_written\>' | cut -d"|" -f3`
                echo $result 
                ;;

    # 主从相关 从IO SQL线程状态 和 Delay 状态
        # Slave_IO 状态
    Slave_IO)
        result=`${Bin_mysql} -u${MYSQL_USER} -p${MYSQL_PWD}  -h 127.0.0.01 -ne "SHOW SLAVE STATUS\G" 2> /dev/null |grep Slave_IO_Running |grep Yes &> /dev/null && echo "OK" || echo "False"`
               echo $result
               ;;
        # Slave_SQL 状态
    Slave_SQL)
        result=`${Bin_mysql} -u${MYSQL_USER} -p${MYSQL_PWD}  -h 127.0.0.01 -ne "SHOW SLAVE STATUS\G" 2> /dev/null |grep Slave_SQL_Running |grep Yes &> /dev/null && echo "OK" || echo "False"`
               echo $result
               ;;
        # Slave 落后 Master 时长，单位秒
    Slave_delay)
        result=`${Bin_mysql} -u${MYSQL_USER} -p${MYSQL_PWD}  -h 127.0.0.01 -ne "SHOW SLAVE STATUS\G" 2> /dev/null |grep Seconds_Behind_Master | cut -d':' -f2`
               echo $result
               ;;
        *)
        echo "Usage:$0(Uptime|Com_update|...)" 
        ;;
esac
