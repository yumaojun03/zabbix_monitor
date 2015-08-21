#!/usr/bin/env python
# coding: utf-8

"""
Date        : 2015-08-21
Author      : 紫川秀
Email       : yumaojun03@gmail.com
Version     : 0.1
Description :
              用于 zabbix 监控 haproxy
"""



import socket
import argparse
import json
import csv

class HAProxyStats(object):
    """
    Used for communicating with HAProxy 
    through its local UNIX socket interface.
    """

    def __init__(self):
        self.socket_name = None
        self.parsed_status = []
        self.front_servers = {}
        self.back_servers= {}

    def get_args(self):
        """
        Get argument from CLI.
        """
        parser = argparse.ArgumentParser(
            description='Arguments for get haproxy status')
        
        parser.add_argument("--socket", 
                            required=True,
                            action="store",
                            help="HAProxy service socket file path")

        parser.add_argument("--type", 
                            required=True,
                            choices=["frontend", "backend"],
                            action="store",
                            help="HAProxy frontend and backend")

        parser.add_argument("--discovery",
                            action="store_true",
                            default=False,
                            help="discovery mode for zabbix")

        parser.add_argument("--front_name", 
                            required=False,
                            action="store",
                            help="HAProxy frontend name,\
                                  You can use --discovery to list.")

        parser.add_argument("--back_name", 
                            required=False,
                            action="store",
                            help="HAProxy frontend name,\
                                  You can use --discovery to list.")

        parser.add_argument("--params", 
                            required=False,
                            choices=["sessions-per-second",
                                     "sessions-current",
                                     "sessions-max",
                                     "sessions-limit",
                                     "sessions-total",
                                     "sessions-rate-limit",
                                     "sessions-rate-max",
                                     "bytes-in",
                                     "bytes-out",
                                     "server-active",
                                     "server-backup",
                                     "connection-errors",
                                     "failed-health-checks",
                                     "response-errors",
                                     "responses-denied",
                                     "responses-1xx",
                                     "responses-2xx",
                                     "responses-3xx",
                                     "responses-4xx",
                                     "responses-5xx",
                                     "responses-xxx",
                                     "client-aborts",
                                     "server-aborts",
                                     "lb-total",
                                     "request-errors",
                                     "requests-denied",
                                     "requests-per-second",
                                     "requests-per-second-max",
                                     "requests-total",
                                     "requests-queued-current",
                                     "requests-queued-max",
                                     "server-type",
                                     "server-weight",
                                     "retries",
                                     "redispatches",
                                    ],
                            action="store",
                            help="HAProxy status data")

        args = parser.parse_args()
        return args        

    def execute(self, command):
        """
        Executes a HAProxy command by sending a message to a HAProxy's local
        TODO: UNIX socket and waiting up to 'timeout' milliseconds for the response.
        """
        client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        client.connect(self.socket_name)
        client.send(command + "\n")

        buffer = []
        while True:
            d = client.recv(16384)
            if d:
                buffer.append(d)
            else:
                break

        data = ''.join(buffer)
        client.close()
        return (data.decode('utf-8').split('\n'))    

    def num(self, s):
        """
        Converte string to number.
        """
        if s:
            return int(s)
        else:
            return 0

    def createKeyedStatus(self, servers):
        """
        Create key.
        """
        new_servers = {} 
        for server in servers:
            new_servers[server['# pxname'] + "_" + server['svname']] = {
                'sessions-per-second': self.num(server['rate']),
                'sessions-current': self.num(server['scur']),
                'sessions-max': self.num(server['smax']),
                'sessions-limit': self.num(server['slim']),
                'sessions-total': self.num(server['stot']),
                'sessions-rate-limit': self.num(server['rate_lim']),
                'sessions-rate-max': self.num(server['rate_max']),
                'bytes-in': self.num(server['bin']),
                'bytes-out': self.num(server['bout']),
                'server-active': self.num(server['act']),
                'server-backup': self.num(server['bck']),
                'connection-errors': self.num(server['econ']),
                'failed-health-checks': self.num(server['hanafail']),
                'response-errors': self.num(server['eresp']),
                'responses-denied': self.num(server['dresp']),
                'responses-1xx': self.num(server['hrsp_1xx']),
                'responses-2xx': self.num(server['hrsp_2xx']),
                'responses-3xx': self.num(server['hrsp_3xx']),
                'responses-4xx': self.num(server['hrsp_4xx']),
                'responses-5xx': self.num(server['hrsp_5xx']),
                'responses-xxx': self.num(server['hrsp_other']),
                'client-aborts': self.num(server['cli_abrt']),
                'server-aborts': self.num(server['srv_abrt']),
                'lb-total': self.num(server['lbtot']),
                'request-errors': self.num(server['ereq']),
                'requests-denied': self.num(server['dreq']),
                'requests-per-second': self.num(server['req_rate']),
                'requests-per-second-max': self.num(server['req_rate_max']),
                'requests-total': self.num(server['req_tot']),
                'requests-queued-current': self.num(server['qcur']),
                'requests-queued-max': self.num(server['qmax']),
                'server-type': self.num(server['type']),
                'server-weight': self.num(server['weight']),
                'retries': self.num(server['wretr']),
                'redispatches': self.num(server['wredis']),
            }
        return new_servers


    def parseStatusPage(self):
        """
        Parse the unix socket command result of show stat.
        Generate front_servers and back_servers.
        """
        
        self.raw_status = '\n'.join(self.execute('show stat'))
        reader = csv.DictReader(self.raw_status.split('\n'), delimiter=',') 
        for row in reader:
            self.parsed_status.append(row)

        front = filter(lambda x: x['svname'] == "FRONTEND", self.parsed_status)
        back = filter(lambda x: x['svname'] != "FRONTEND", self.parsed_status)

        self.front_servers = self.createKeyedStatus(front)
        self.back_servers = self.createKeyedStatus(back)

    def run(self):
        args = self.get_args()
        self.socket_name = args.socket

        self.parseStatusPage()
        if args.type == "frontend":
            if args.discovery:
                data = [{"{#FRONT_NAME}": key} for key in self.front_servers.keys()]
                discovery = {"data": data}
                encodedjson = json.dumps(discovery, sort_keys=True, indent=4, separators=(',', ':'))
                print encodedjson
            if  args.front_name:
                if args.params:
                    print self.front_servers[args.front_name][args.params]
                else:
                    print self.front_servers[args.front_name]
                
        if args.type == "backend":
            if args.discovery:
                data = [{"{#BACK_NAME}": key} for key in self.back_servers.keys()]
                discovery = {"data": data}
                encodedjson = json.dumps(discovery, sort_keys=True, indent=4, separators=(',', ':'))
                print encodedjson
            if  args.back_name:
                if args.params:
                    print self.back_servers[args.back_name][args.params]
                else:
                    print self.back_servers[args.back_name]


def Main():
    stats = HAProxyStats()
    stats.run()

if __name__ == "__main__":
    Main()
    
