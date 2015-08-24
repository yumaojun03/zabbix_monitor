# MySQL
* 老版本:通过mysqladmin 的 status 和 extended-status 输出，
捕获mysql运行时状态信息  大概监控概要如下：
* 新版本  通过python库 连接数据库 读取数据库的 schema信息，
分析数据库运行状态，具有良好的扩展性 

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


