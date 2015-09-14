# MySQL
***老版本***:

通过mysqladmin 的 status 和 extended-status 输出，
捕获mysql运行时状态信息  大概监控概要如下：

***新版本***:

通过python库 连接数据库 读取数据库的 schema信息，
分析数据库运行状态，具有良好的扩展性 

> 使用说明

```
[root@mylab custom_scripts]# python mysql_perf_monitor.py --help
usage: mysql_perf_monitor.py [-h] --host HOST --user USER --passwd PASSWD --db
                             DB
                             
                             {bytes_received,bytes_sent,com_commit,com_delete,com_insert,com_rollback,com_select,com_update,data_read,data_reads,data_writes,data_written,flush_commands,log_fsyncs,log_written,open_tables,opened_tables,pages_data,pages_dirty,pages_flushed,pages_free,pages_total,questions,row_lock_current_waits,row_lock_time,rows_deleted,rows_inserted,rows_read,rows_updated,slave_delayed,slave_running,slow_queries,threads_cached,threads_connected,threads_created,threads_running,uptime}
                             ...

Artuments for connect to MySQL.

positional arguments:
  {bytes_received,bytes_sent,com_commit,com_delete,com_insert,com_rollback,com_select,com_update,data_read,data_reads,data_writes,data_written,flush_commands,log_fsyncs,log_written,open_tables,opened_tables,pages_data,pages_dirty,pages_flushed,pages_free,pages_total,questions,row_lock_current_waits,row_lock_time,rows_deleted,rows_inserted,rows_read,rows_updated,slave_delayed,slave_running,slow_queries,threads_cached,threads_connected,threads_created,threads_running,uptime}

optional arguments:
  -h, --help            show this help message and exit
  --host HOST           mysql host address
  --user USER           mysql login user name
  --passwd PASSWD       mysql login password
  --db DB               mysql login database
```

> 例子

```
[root@mylab custom_scripts]# python mysql_perf_monitor.py --host hostip --user username  --passwd password --db mysql slave_delayed
0

```


####功能

* **基本状态信息统计**
* **增删查改 事物等语句执行次数统计**
* **流量相关 语句执行次数统计**
* **线程状态**
* **InnoDB引擎Row状态**
* **InnoDB引擎Lock状态**
* **InnoDB Buffer Pool Page状态**
* **InnoDB 引擎Data状态**
* **InnoDB Log写状态**
* **主从相关 从IO SQL线程状态 和 Delay 状态**


