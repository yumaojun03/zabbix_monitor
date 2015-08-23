# NVIDIA K1
通过python parimiko库，连接Esxi， 运行nvidia显卡相关命令，解析结果，获取K1卡的运行状况

为了方便和zabbix结合，提供了自动发现功能(--discovery)

    
```
GPU
    GPU ID
    GPU Utilization
    GPU MEM Total
    GPU MEM Usage
    GPU MEM Utilization

Process
    Process Name
    Process GPU ID
    Process MEM Usage
```
