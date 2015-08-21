# Netscaler 硬负载监控方法

NetScaler是业界领先的服务交付平台。Netscaler支持广泛平台，
拥有全面的应用安全设定、加速和负载均衡（包含GSLB）功能

## 方法一官方mib文档

官方mib 文档 [netscaler-mib](http://www.mibdepot.com/cgi-bin/getmib3.cgi?win=mib_a&r=citrix&f=NS-ROOT-MIB.mib&v=v2&t=tree)

## 方法二oidview网站查看

这是一种比较通用的方法，几乎所有知名厂商的mib库里面都有，
而且 可以查看 mib-tree 和 下载mib库文件
    
厂商列表：[all vendor](http://www.oidview.com/mibs/detail.html)
    
以netscaler为例，我们可以在里边里面找打 NetScaler，
进入该页面或可以看到 fortinet的 mib 树，而且可以下载mib文件
    
oidview NetScaler mib tree：[NetScaler-mib-OID-VIEW](http://www.oidview.com/mibs/5951/NS-ROOT-MIB.html)
    
oidview  mib download：[mib-download](http://www.oidview.net/tools/index.html)

## 方法三 第三方帖子

参考帖子 [netscaler-monitor-for-zabbix](http://www.tuicool.com/articles/m2YnI3v)

* * *

#### Netscaler7500

    
```
system:

  nsResourceGroup          1.3.6.1.4.1.5951.4.1.1.41
  numCPUs                  1.3.6.1.4.1.5951.4.1.1.41.3
  resCpuUsage              1.3.6.1.4.1.5951.4.1.1.41.1
  memSizeMB                1.3.6.1.4.1.5951.4.1.1.41.4 
  resMemUsage              1.3.6.1.4.1.5951.4.1.1.41.2
  
  nsCPUTable               1.3.6.1.4.1.5951.4.1.1.41.6
  nsCPUEntry               1.3.6.1.4.1.5951.4.1.1.41.6.1
  nsCPUname                1.3.6.1.4.1.5951.4.1.1.41.6.1.1
  nsCPUusage               1.3.6.1.4.1.5951.4.1.1.41.6.1.2

service：

  totalClientConnections   1.3.6.1.4.1.5951.1.2.1.1.0
  curClientConnections     1.3.6.1.4.1.5951.1.2.1.2.0
  totalServerConnections   1.3.6.1.4.1.5951.1.2.1.3.0
  curServerConnections     1.3.6.1.4.1.5951.1.2.1.4.0
  clientConnRefused        1.3.6.1.4.1.5951.1.2.1.5.0
  
  unackSyn                 1.3.6.1.4.1.5951.1.2.1.15.0
  curClientEstablishedConn 1.3.6.1.4.1.5951.1.2.1.16.0
  curServerEstablishedConn 1.3.6.1.4.1.5951.1.2.1.17.0
  

IF:

  nsIfStatsTable            1.3.6.1.4.1.5951.4.1.1.54
  nsIfStatsEntry            1.3.6.1.4.1.5951.4.1.1.54.1
  ifName                    1.3.6.1.2.1.31.1.1.1.1

  ifMedia                   1.3.6.1.4.1.5951.4.1.1.54.1.2
  ifTotRxBytes              1.3.6.1.4.1.5951.4.1.1.54.1.3
  ifRxAvgBandwidthUsage     1.3.6.1.4.1.5951.4.1.1.54.1.4
  ifTotRxPkts               1.3.6.1.4.1.5951.4.1.1.54.1.5
  ifRxAvgPacketRate         1.3.6.1.4.1.5951.4.1.1.54.1.6

  ifTotTxBytes              1.3.6.1.4.1.5951.4.1.1.54.1.7
  ifTxAvgBandwidthUsage     1.3.6.1.4.1.5951.4.1.1.54.1.8
  ifTotTxPkts               1.3.6.1.4.1.5951.4.1.1.54.1.9
  ifTxAvgPacketRate         1.3.6.1.4.1.5951.4.1.1.54.1.10
          
  ifTotRxMbits              1.3.6.1.4.1.5951.4.1.1.54.1.19
  ifTotTxMbits              1.3.6.1.4.1.5951.4.1.1.54.1.20
  ifTotNetScalerPkts        1.3.6.1.4.1.5951.4.1.1.54.1.21
        
```

