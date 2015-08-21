#!/usr/bin/env python
# coding:utf-8

"""
Date        : 2015-08-21
Author      : 紫川秀
Email       : yumaojun03@gmail.com
Version     : 0.1
Description :
              用于 zabbix 监控 EXSi GPU
"""



import re
import sys
import json
import paramiko
import argparse


class MySSHClient(object):
    ''' paramiko ssh client.'''

    def __init__(self, server, username, password):
        self.server = server
        self.username = username
        self.password = password
        self.stderr = ''
        self.stdout = ''

    def do_connect(self):
        self.connection = paramiko.SSHClient()
        self.connection.load_system_host_keys()
        self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connection.connect(self.server, username=self.username, password=self.password)

    def execute_cmd(self, cmd):
        if cmd:
            stdin, stdout, stderr = self.connection.exec_command(cmd)
            stdin.close()
            self.stderr = stderr.read()
            self.stdout = stdout.read()
        else:
            print "no command accept"
            sys.exit(2)
        return {'error': self.stderr, 'stdout': self.stdout}

    def do_close(self):
        self.connection.close()


class  GPUPerf(object):
    ''' get the GPU Performace.'''

    def __init__(self, gpu_output):
        self.gpu_output = gpu_output

    def parse(self):
        '''parse the GPU output performace information.'''

        _result_perf = {}
        _result_proc = {}
        perf_pattern = re.compile(r'N/A.* (?P<m_used>[0-9]+)MiB\s+/\s+(?P<m_total>[0-9]+)MiB.*(?P<utali>[0-9]+)%')
        proc_pattern = re.compile(r'[|]\s+(?P<gpu_id>[0-9]+)\s+[0-9]+\s+\S+\s+(?P<process>\w+)\s+(?P<m_used>[0-9]+)MiB')
#        proc_pattern = re.compile(r'[|]\s+(?P<gpu_id>[0-9]+)\s+[0-9]+\s+\S+\s+(?P<process>\w+)\s(?P<name>\S+)\s+(?P<m_used>[0-9]+)MiB')
        list_result = self.gpu_output.splitlines()
        # parse gpu performace
        count = 0
        for line in list_result:
            match = perf_pattern.search(line)
            if match:
                _result_perf['GPU_'+str(count)] = match.groupdict()
                count += 1
        # parse process performace
        for line in list_result:
            match = proc_pattern.search(line)
            if match:
                _result_proc[str(match.groupdict()['process'])] = match.groupdict()

        return _result_perf, _result_proc


def get_args():
    """
    Get arguments from CLI
    """
    parser = argparse.ArgumentParser(
        description='Arguments for talking to ESXi')
  
    parser.add_argument("--host", 
                        required=True,
                        action="store",
                        help="Exsi host ip address") 

    parser.add_argument("--user", 
                        required=True,
                        action="store",
                        help="Exsi host login user") 

    parser.add_argument("--password", 
                        required=True,
                        action="store",
                        help="Exsi host login password") 

    parser.add_argument("--type", 
                        required=True,
                        choices=["performance", "process"],
                        action="store",
                        help="Performance mean the GPU utilization,\
                              process mean which host use this cpu") 

    parser.add_argument("--discovery", 
                        action="store_true",
                        default=False,
                        help="discovery mode for zabbix") 

    parser.add_argument("--gpu_perf_type", 
                        required=False,
                        choices=["gpu", "mem"],
                        action="store",
                        help="gpu mean gpu utilization,\
                              mem mean gpu mem utilization") 

    parser.add_argument("--gpu_id", 
                        required=False,
                        action="store",
                        help="your can --discovery and --type performance chieve the gpu_id list") 

    parser.add_argument("--process_perf_type", 
                        required=False,
                        choices=["gpu", "mem"],
                        action="store",
                        help="gpu mean gpu utilization,\
                              mem mean gpu mem utilization") 

    parser.add_argument("--process_name", 
                        required=False,
                        action="store",
                        help="your can --discovery and --type process achieve the process_name list") 

    args = parser.parse_args()


 

    return args



def Main():
    ''' The main process.'''

    args = get_args()
    client = MySSHClient(server=args.host, username=args.user, password=args.password)
    client.do_connect()
    result = client.execute_cmd('nvidia-smi')['stdout']
    client.do_close()

    gpu = GPUPerf(result)
    perf, proc = gpu.parse()

    if args.type == "performance":
        if args.discovery:
            data = [{"{#GPU_ID}": key} for key in perf.keys()]
            discovery = {"data": data}
            encodedjson = json.dumps(discovery, sort_keys=True, indent=4, separators=(',', ':'))
            print encodedjson
        elif args.gpu_id:
            if args.gpu_perf_type == "gpu":
                print perf[args.gpu_id]['utali']
            elif args.gpu_perf_type == "mem":
                print "%2.2f" % ((float(perf[args.gpu_id]['m_used'])/float(perf[args.gpu_id]['m_total']))*100)
    elif args.type == "process":
      if args.discovery:
            data = [{"{#PROC_ID}": key} for key in proc.keys()]
            discovery = {"data": data}
            encodedjson = json.dumps(discovery, sort_keys=True, indent=4, separators=(',', ':'))
            print encodedjson
      elif args.process_name:
            if args.process_perf_type == "gpu":
                print proc[args.process_name]['gpu_id']
            elif args.process_perf_type == "mem":
                print proc[args.process_name]['m_used']



 
#    for gpu_id, gpu_perf in perf.items():
#         print "ID: %s,  GPU Utalization: %-2.2f%%,  G_MEM Utalization: %-2.2f%%" % (gpu_id, float(gpu_perf['utali']), (float(gpu_perf['m_used'])/float(gpu_perf['m_total'])*100))
#    for gpu_process, gpu_proc in proc.items():
#         print "process: %s,  name: %s,  gpu_id: %s,  G_mem: %sM" % (gpu_process, gpu_proc['name'], gpu_proc['gpu_id'], gpu_proc['m_used'])

if __name__ == "__main__":
    Main()
