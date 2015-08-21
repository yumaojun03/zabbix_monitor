# CENTEC 交换机监控方法


## 官方mib库

找官方要到对于的mib文件，然后使用工具加载mib库，
找出对于的OID即可

工具下载地址： [地址](http://www.xixiwg.com/soft/209886.html)


* * *

#### 型号 E580-48X6Q


```
CPU
  ssIndex                          .1.3.6.1.4.1.27975.1.2.1
  ssCpuIdle                        .1.3.6.1.4.1.27975.1.2.11


MEM
  memIndex                        .1.3.6.1.4.1.27975.1.1.1  
  memTotalReal                    .1.3.6.1.4.1.27975.1.1.5
  memTotalUsed                    .1.3.6.1.4.1.27975.1.1.12
  memTotalFree                    .1.3.6.1.4.1.27975.1.1.11
  
  
FAN
  devMFanIndex                         .1.3.6.1.4.1.27975.37.1.1.1.1.3
  devMFanStatus                        .1.3.6.1.4.1.27975.37.1.1.1.1.4
  devMFanSpeed                         .1.3.6.1.4.1.27975.37.1.1.1.1.5
  
  devMFanStatusEntry                   .1.3.6.1.4.1.27975.37.1.1.1.1
  devMFanPosition                      .1.3.6.1.4.1.27975.37.1.1.1.1.1
  devMFanModuleId                      .1.3.6.1.4.1.27975.37.1.1.1.1.2
  devMFanLowSpeed                      .1.3.6.1.4.1.27975.37.1.1.1.1.6
  devMFanHighSpeed                     .1.3.6.1.4.1.27975.37.1.1.1.1.7
  devMFanSpeedAdjust                   .1.3.6.1.4.1.27975.37.1.1.1.1.8
  devMFanSetSpeed                      .1.3.6.1.4.1.27975.37.1.1.1.1.9

POWER
  devMPowerIndex                       .1.3.6.1.4.1.27975.37.1.2.1.1
  devMPowerStatus                      .1.3.6.1.4.1.27975.37.1.2.1.2
  devMPowerWorkStatus                  .1.3.6.1.4.1.27975.37.1.2.1.3
  
  devMPowerType                        .1.3.6.1.4.1.27975.37.1.2.1.4
  devMPowerFanStatus                   .1.3.6.1.4.1.27975.37.1.2.1.5
  devMPowerControlStatus               .1.3.6.1.4.1.27975.37.1.2.1.6
  

TEMP
  ifIndex                              .1.3.6.1.2.1.2.2.1.1
  temperCurrent                        .1.3.6.1.4.1.27975.37.1.10.2.1.5
  
IF
  使用标准mib2
```
