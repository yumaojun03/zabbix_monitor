# FortiGate防火墙监控方法

FortiGate 防火墙是 Fortinet, Inc 公司的产品，
要想获取其OID有2种方法

## 方法一： mib文件

1.  ***oidview网站***

    这是一种比较通用的方法，几乎所有知名厂商的mib库里
    里面都有，而且 可以查看 mib-tree 和 下载mib库文件
    
    厂商列表：[all vendor](http://www.oidview.com/mibs/detail.html)
    
    以huawei为例，我们可以在里边里面找打 Fortinet, Inc，
    进入该页面或可以看到 fortinet的 mib 树，而且可以下载mib文件
    
    oidview huawei mib tree：[fortinet-mib-OID-VIEW](http://www.oidview.com/mibs/12356/FORTINET-FORTIGATE-MIB.html)
    
    oidview  mib download：[mib-download](http://www.oidview.net/tools/index.html)



## 方法二： mib参考文档

官网上没找到，以后补充


#### 型号：1000C
    
```
HA Cluster: 
  fgHaTables	                    1.3.6.1.4.1.12356.101.13.2
  fgHaStatsTable	                1.3.6.1.4.1.12356.101.13.2.1
  fgHaStatsEntry	                1.3.6.1.4.1.12356.101.13.2.1.1

  fgHaStatsIndex	                1.3.6.1.4.1.12356.101.13.2.1.1.1
  fgHaStatsAvCount	                1.3.6.1.4.1.12356.101.13.2.1.1.10
  fgHaStatsHostname	                1.3.6.1.4.1.12356.101.13.2.1.1.11
  fgHaStatsSyncStatus	            1.3.6.1.4.1.12356.101.13.2.1.1.12
  fgHaStatsSyncDatimeSucc	        1.3.6.1.4.1.12356.101.13.2.1.1.13
  fgHaStatsSyncDatimeUnsucc	        1.3.6.1.4.1.12356.101.13.2.1.1.14
  fgHaStatsGlobalChecksum	        1.3.6.1.4.1.12356.101.13.2.1.1.15
  fgHaStatsMasterSerial	            1.3.6.1.4.1.12356.101.13.2.1.1.16
  fgHaStatsSerial	                1.3.6.1.4.1.12356.101.13.2.1.1.2
  fgHaStatsCpuUsage	                1.3.6.1.4.1.12356.101.13.2.1.1.3
  fgHaStatsMemUsage	                1.3.6.1.4.1.12356.101.13.2.1.1.4
  fgHaStatsNetUsage	                1.3.6.1.4.1.12356.101.13.2.1.1.5
  fgHaStatsSesCount	                1.3.6.1.4.1.12356.101.13.2.1.1.6
  fgHaStatsPktCount	                1.3.6.1.4.1.12356.101.13.2.1.1.7
  fgHaStatsByteCount	            1.3.6.1.4.1.12356.101.13.2.1.1.8
  fgHaStatsIdsCount	                1.3.6.1.4.1.12356.101.13.2.1.1.9
  
  
CPU and MEM:
  fgProcessors	                    1.3.6.1.4.1.12356.101.4.4
  fgProcessorCount	                1.3.6.1.4.1.12356.101.4.4.1
  fgProcessorTable	                1.3.6.1.4.1.12356.101.4.4.2
  fgProcessorEntry	                1.3.6.1.4.1.12356.101.4.4.2.1
  
  fgProcessorEntIndex	            1.3.6.1.4.1.12356.101.4.4.2.1.1
  fgProcessorSysUsage	            1.3.6.1.4.1.12356.101.4.4.2.1.10
  fgProcessorUsage	                1.3.6.1.4.1.12356.101.4.4.2.1.2
  fgProcessorUsage5sec	            1.3.6.1.4.1.12356.101.4.4.2.1.3
  fgProcessorType          	        1.3.6.1.4.1.12356.101.4.4.2.1.4
  fgProcessorContainedIn  	        1.3.6.1.4.1.12356.101.4.4.2.1.5
  fgProcessorPktRxCount	            1.3.6.1.4.1.12356.101.4.4.2.1.6
  fgProcessorPktTxCount	            1.3.6.1.4.1.12356.101.4.4.2.1.7
  fgProcessorPktDroppedCount        1.3.6.1.4.1.12356.101.4.4.2.1.8
  fgProcessorUserUsage	            1.3.6.1.4.1.12356.101.4.4.2.1.9

IF:
  使用标准的mib2 监控

```