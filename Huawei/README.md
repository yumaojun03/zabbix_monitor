# HUAWEI 交换机监控通用方法

华为的交换机都提供了比较丰富的mib文档可供参考
其中一种是通过官方公开的mib文件可以查看，而另
一种则是 可以直接通过官方下载 mib文件的想法说明
第二种方法比较通俗易懂，推荐使用。

在本文的后面会直接列出 一些型号的交换机的相关OID
，方便查阅。

* * *

## 方法一： mib库文件

1.  ***oidview网站***

    这是一种比较通用的方法，几乎所有知名厂商的mib库里
    里面都有，而且 可以查看 mib-tree 和 下载mib库文件
    
    厂商列表：[all vendor](http://www.oidview.com/mibs/detail.html)
    
    以huawei为例，我们可以在里边里面找打 HUAWEI Technology Co.,Ltd，
    进入该页面或可以看到 huawei的 mib 树，而且可以下载mib文件
    
    oidview huawei mib tree：[huawei-mib-OID-VIEW](http://www.oidview.com/mibs/2011/HUAWEI-MIB.html)
    oidview  mib download：[mib-download](http://www.oidview.net/tools/index.html)

2. ***华为公开的mib文件库***

    通过华为公开在github上的mib文件,通过查看这些mib文件
    可以找到你需要的监控对象的OID，但是 需要能看懂mib文件
    
    华为mib库的目录：[华为mib](https://github.com/stackforge/compass-core/tree/master/mibs)
      * ROOT: [华为mib](https://github.com/stackforge/compass-core/tree/master/mibs)
      * CPU: [CPU](https://github.com/stackforge/compass-core/blob/master/mibs/HUAWEI-CPU-MIB.mib)
      * MEM: [MEM](https://github.com/stackforge/compass-core/blob/master/mibs/HUAWEI-MEMORY-MIB.mib)
      * IF:  [IF](https://github.com/stackforge/compass-core/blob/master/mibs/HUAWEI-IF-EXT-MIB.mib)
      * TCP: [TCP](https://github.com/stackforge/compass-core/blob/master/mibs/TCP-MIB.mib)
      * UDP: [UDP](https://github.com/stackforge/compass-core/blob/master/mibs/UDP-MIB.mib)
      * Temperature: [EXTENT](https://github.com/stackforge/compass-core/blob/master/mibs/HUAWEI-ENTITY-EXTENT-MIB.mib)

3. ***找别人贴出来的OID*** 
    
    网上也有人贴出来关于Ｓ系列的华为交换机的OID
    
    网上帖子： [帖子](http://support.huawei.com/ecommunity/bbs/10243823.html)



## 方法二： 官方mib文档

华为官网也提供mib库的说明文档，非常详尽，可以根据设备型号进行查看 非常方便
，有篇帖子有介绍:

如何下载官网mib参考文档 [帖子2](http://support.huawei.com/ecommunity/bbs/10245735.html)

下面简单介绍一下此方法：
  1. 进入官方mib 查询页面 [mib-search](http://support.huawei.com/enterprise/news?lang=zh#idAbsPath=0301_10001%7C1382082906220&ot=clk&pid=1382082906220&t=923&type=0301)
  2. 在搜索栏上点击全部，然后输入 mib s5700 进行搜索
  3. 下载mib 参考文档，然后查看，mib参考文档非常易读，非常方便查看
  
* * * 

### 型号： S5710

```
Vendor:
  HUAWEI OID             : 1.3.6.1.4.1.2011
  huaweiUtility          : 1.3.6.1.4.1.2011.6
  hwDev                  : 1.3.6.1.4.1.2011.6.3

CPU
  hwCpuDevTable          : 1.3.6.1.4.1.2011.6.3.4
  hwCpuDevEntry          : 1.3.6.1.4.1.2011.6.3.4.1
  hwCpuDevIndex          ：1.3.6.1.4.1.2011.6.3.4.1.1
  hwCpuDevDuty           : 1.3.6.1.4.1.2011.6.3.4.1.2

MEM
  hwMemoryDev            : 1.3.6.1.4.1.2011.6.3.5
MEM
  hwMemoryDevTable       : 1.3.6.1.4.1.2011.6.3.5.1
  hwMemoryDevEntry       : 1.3.6.1.4.1.2011.6.3.5.1.1
  hwMemoryDevModuleIndex : 1.3.6.1.4.1.2011.6.3.5.1.1.1
  hwMemoryDevSize        : 1.3.6.1.4.1.2011.6.3.5.1.1.2
  hwMemoryDevFree        : 1.3.6.1.4.1.2011.6.3.5.1.1.3
  hwMemoryDevRawSliceUsed: 1.3.6.1.4.1.2011.6.3.5.1.1.4
  hwMemoryDevFail        : 1.3.6.1.4.1.2011.6.3.5.1.1.6
  hwMemoryDevFailNoMem   : 1.3.6.1.4.1.2011.6.3.5.1.1.7
MEM Buffer
  hwBufferTable          : 1.3.6.1.4.1.2011.6.3.5.2
  hwBufferEntry          : 1.3.6.1.4.1.2011.6.3.5.2.1
  hwBufferModuleIndex    : 1.3.6.1.4.1.2011.6.3.5.2.1.1
  hwBufferSize           : 1.3.6.1.4.1.2011.6.3.5.2.1.2
  hwBufferCurrentTotal   : 1.3.6.1.4.1.2011.6.3.5.2.1.3
  hwBufferCurrentUsed    : 1.3.6.1.4.1.2011.6.3.5.2.1.4

Fan
 hwEntityFanSlot         : 1.3.6.1.4.1.2011.5.25.31.1.1.10.1.1
 hwEntityFanSn           : 1.3.6.1.4.1.2011.5.25.31.1.1.10.1.2
 hwEntityFanReg          : 1.3.6.1.4.1.2011.5.25.31.1.1.10.1.3
 hwEntityFanSpdAdjMode   : 1.3.6.1.4.1.2011.5.25.31.1.1.10.1.4
 hwEntityFanSpeed        : 1.3.6.1.4.1.2011.5.25.31.1.1.10.1.5
 hwEntityFanPresent      : 1.3.6.1.4.1.2011.5.25.31.1.1.10.1.6
 hwEntityFanState        : 1.3.6.1.4.1.2011.5.25.31.1.1.10.1.7
 
OpticalModule
 hwEntityOpticalVendorSn   : 1.3.6.1.4.1.2011.5.25.31.1.1.3.1.4
 hwEntityOpticalTemperature: 1.3.6.1.4.1.2011.5.25.31.1.1.3.1.5
 hwEntityOpticalRxPower    : 1.3.6.1.4.1.2011.5.25.31.1.1.3.1.8
 hwEntityOpticalTxPower    : 1.3.6.1.4.1.2011.5.25.31.1.1.3.1.9
 
Summary
 hwEntityCpuUsage        : 1.3.6.1.4.1.2011.5.25.31.1.1.1.1.5
 hwEntityMemUsage        : 1.3.6.1.4.1.2011.5.25.31.1.1.1.1.7
 hwEntityTemperature     : 1.3.6.1.4.1.2011.5.25.31.1.1.1.1.11

IF:
 hwIFExtIndex            : 1.3.6.1.4.1.2011.5.25.41.1.1.1.1.1
 hwIFExtFlowStatus       : 1.3.6.1.4.1.2011.5.25.41.1.1.1.1.8
 hwIFExtInputOctetRate       : 1.3.6.1.4.1.2011.5.25.41.1.1.1.1.19
 hwIFExtInputHighOctetRate   : 1.3.6.1.4.1.2011.5.25.41.1.1.1.1.20
 hwIFExtOutputOctetRate      : 1.3.6.1.4.1.2011.5.25.41.1.1.1.1.21
 hwIFExtOutputHighOctetRate  : 1.3.6.1.4.1.2011.5.25.41.1.1.1.1.22



```