# ESXi6.0监控

**设备**： DEL(R720)

**概述**： 宿主机采用VMWare的 EXSI6.0 做Hypervisor，因此
监控主要是针对EXSI6.0进行，监控的方式有2种：Zabbix自带的
通过VMware web service 进行的监控和 使用SNMP进行的监控，下面
会介绍2种监控的实施方法，但是最终会选用 SNMP这种监控方式进行
因为自带的 VMware web service 监控实在有些简陋。

* * *

**实施**：

***zabbix 自带简单监控***

1. Zabbix自带模板，可查考官方: [VMWare Monitor](https://www.zabbix.com/documentation/2.4/manual/vm_monitoring)   
    * 创建vCentor主机，指定3个变量比如：
         1. {$URL} ==> https://vcentor_ip/sdk
         2. {$USERNAME} ==> vcentor_user
         3. {$PASSWORD} ==> vcentor_pass
    * 为该主机套上模板：  Template Virt VMware


***使用SNMP进行监控***

2. 添加VMware ESX SNMP模板
    * 下载SNMP模板：[VMware ESX SNMP](https://share.zabbix.com/index.php?option=com_mtree&task=att_download&link_id=165&cf_id=24)
    * 开启宿主机的SNMP服务
         1. 通过ssh 连上exsi服务器
         2. 修改snmp的community：esxcli system snmp set --communities <community>
         3. 开启snmp服务： esxcli system snmp set --enable true
    * 调整防火墙方向snmp服务
         1. esxcli network firewall ruleset set --ruleset-id snmp --allowed-all true
         2. esxcli network firewall ruleset set --ruleset-id snmp --enabled true
         3. /etc/init.d/snmpd restart
    * 导入VMware ESX SNMP模板到zabbix
         1. 登陆zabbix WEB GUI，点击 Template
         2. 点击 Import
         3. 选择下载下来的模板文件，点击确定
    * 使用模板
         1. 为模板添加变量
            1.  {$SNMP_COMMUNITY} ==> community
            2.  {$SNMP_PORT} ==> 161
         2. 登陆zabbix WEB GUI，点击 Configuration - Hosts
         3. 创建主机，套上该模板

      
  ***注意***： 我已经整理好了模板，就在当前目录下： zabbix_template_ESXi.xml



     
```
vmwDiskShares       .1.3.6.1.4.1.6876.3.3.1.4
vmwNumReads         .1.3.6.1.4.1.6876.3.3.1.5
vmwKbRead           .1.3.6.1.4.1.6876.3.3.1.6
vmwNumWrites        .1.3.6.1.4.1.6876.3.3.1.7
vmwKbWritten        .1.3.6.1.4.1.6876.3.3.1.8
```
