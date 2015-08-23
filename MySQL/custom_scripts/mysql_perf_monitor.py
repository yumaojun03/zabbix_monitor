#!/usr/bin/env python
# coding: utf-8


"""
Date        : 2015-07-22
Author      : 紫川秀
Email       : yumaojun03@gmail.com
Version     : 0.1
Description :
              用于 zabbix 监控 mysql
"""


import argparse, MySQLdb
import inspect

class Checks():
    """
    method of the mysql check
    """
    def uptime(self):
        """
        MySQL Server 的运行时间，单位是秒
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'UPTIME'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def questions(self):
        """
        Client 发起的总的请求次数
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'QUESTIONS'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def slow_queries(self):
        """
        慢查询的次数，具体可以看  slow query log
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'SLOW_QUERIES'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def open_tables(self):
        """
        Server过去打开过的表的一个 总和
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'OPEN_TABLES'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def opened_tables(self):
        """
        当前打开的 table 数量
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'OPENED_TABLES'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def flush_commands(self):
        """
        Server  执行 flush-*, refresh, and reload  这些指令的 总次数
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'FLUSH_COMMANDS'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def com_insert(self):
        """
        insert 语句执行次数
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'COM_INSERT'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def com_delete(self):
        """
        delete 语句执行次数
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'COM_DELETE'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def com_select(self):
        """
        select 语句执行次数
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'COM_SELECT'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def com_update(self):
        """
        update 语句执行次数
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'COM_UPDATE'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def com_commit(self):
        """
        commit 语句执行次数
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'COM_COMMIT'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def com_rollback(self):
        """
        rollback 语句执行次数
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'COM_ROLLBACK'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def bytes_sent(self):
        """
        Server 响应的总的数据量
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'BYTES_SENT'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def bytes_received(self):
        """
        Server 接收到的请求的总的数据量
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'BYTES_RECEIVED'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def threads_running(self):
        """
        当前活动的线程数
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'THREADS_RUNNING'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def threads_connected(self):
        """
        当前打开的连接数(包括活动连接与非活动连接)
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'THREADS_CONNECTED'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def threads_created(self):
        """
        新创建的连接数(如果此值过大，则说明线程池太小，\
        需要调大线程池：thread_cache_size ，\
        可以按照此百分比增大：Threads_created/Connections
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'THREADS_CREATED'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def threads_cached(self):
        """
        线程池中剩余线程
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'THREADS_CACHED'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def threads_cached(self):
        """
        线程池中剩余线程
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'THREADS_CACHED'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def rows_inserted(self):
        """
        InnoDB 写入行的数量
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_ROWS_INSERTED'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def rows_updated(self):
        """
        InnoDB 更新行的数量
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_ROWS_UPDATED'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def rows_deleted(self):
        """
        InnoDB 删除行的数量
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_ROWS_DELETED'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def rows_read(self):
        """
        InnoDB 读取行的数量
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_ROWS_READ'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def row_lock_current_waits(self):
        """
        InnoDB 行锁的个数(被施加了独占锁的行数)
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_ROW_LOCK_CURRENT_WAITS'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def row_lock_time(self):
        """
        InnoDB 行锁的时长(所有操作 等待独占锁释放 的总的时间)
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_ROW_LOCK_TIME'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def pages_data(self):
        """
        InnoDB Buffer Pool 包含数据的页的数量(包括 dirty 和 clean)
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_BUFFER_POOL_PAGES_DATA'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def pages_dirty(self):
        """
        InnoDB Buffer Pool 包含ditry 数据的页的数量
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_BUFFER_POOL_PAGES_DIRTY'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def pages_free(self):
        """
        InnoDB Buffer Pool 空余的，可以使用的页的数据
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_BUFFER_POOL_PAGES_FREE'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def pages_total(self):
        """
        InnoDB Buffer Pool total pages 
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_BUFFER_POOL_PAGES_TOTAL'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]


    def pages_flushed(self):
        """
        InnoDB Buffer Pool 置换页中数据的请求次数
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_BUFFER_POOL_PAGES_FLUSHED'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def data_reads(self):
        """
        InnoDB 数据读总次数
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_DATA_READS'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def data_writes(self):
        """
        InnoDB 数据写总次数
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_DATA_WRITES'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def data_written(self):
        """
        InnoDB 数据读总大小
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_DATA_WRITTEN'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def data_read(self):
        """
        InnoDB 数据写总大小
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_DATA_READ'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def log_fsyncs(self):
        """
        InnoDB 往磁盘同步日志的总次数
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_OS_LOG_FSYNCS'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]

    def log_written(self):
        """
        InnoDB 往磁盘同步日志的总大小
        """
        sql = "SELECT VARIABLE_VALUE \
               FROM INFORMATION_SCHEMA.GLOBAL_STATUS \
               WHERE VARIABLE_NAME LIKE 'INNODB_OS_LOG_WRITTEN'"
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print i[0]


class Main(Checks):
    """
    main to run.
    """
    def __init__(self):
        """
        arguments for connect to mysql server 
        """
        parser = argparse.ArgumentParser(
            description="Artuments for connect to MySQL.")

        parser.add_argument("--host",
                            required=True,
                            action="store",
                            help="mysql host address")

        parser.add_argument("--user",
                            required=True,
                            action="store",
                            help="mysql login user name")

        parser.add_argument("--passwd",
                            required=True,
                            action="store",
                            help="mysql login password")

        parser.add_argument("--db",
                            required=True,
                            action="store",
                            help="mysql login database")

        subparsers = parser.add_subparsers() 

        for name in dir(self):
            if not name.startswith("_"):
                p = subparsers.add_parser(name)
                method = getattr(self, name)
                argnames = inspect.getargspec(method).args[1:]
                for argname in argnames:
                    p.add_argument(argname)
                p.set_defaults(func=method, argnames=argnames)
        

        self.args = parser.parse_args()

    def _db_connect(self):
        """
        connect to mysql server
        archive db obj and cursor obj
        """
        a = self.args
        self.db = MySQLdb.connect(host=a.host,
                               user=a.user,
                               passwd=a.passwd,
                               db=a.db,
                               charset="utf8")

        self.cur = self.db.cursor()

    def _db_close(self):
        """
        close mysql connection
        """
        self.db.close() 

    def __call__(self):
        """
        execute mysql check method
        """ 
        try:
            a = self.args
            callargs = [getattr(a, name) for name in a.argnames]
            self._db_connect()
            try:
                return self.args.func(*callargs)
            finally:
                self._db_close()
        except Exception, err:
            print 0
            print str(err)


if __name__ == "__main__":
    main = Main()
    main()
