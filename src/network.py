#!/usr/bin/python
"""This module fetches network information and returns a JSON with the network info data"""
#pylint: disable=consider-using-f-string
import socket
import speedtest
import datetime
from urllib.request import urlopen
from uuid import getnode as get_mac
import psutil

UNKNOWN = "unknown"


class Network:
    """Class to fetch, format and return network information"""
    mac_address = None
    ip_address = None
    hostname = None
    time_now = None
    down_speed = None
    up_speed = None
    speed_test = None
    connection_status = None
    addresses = None
    stats = None
    connected_interface = None

    def __init__(self):
        self.connection_status = False

    def connect_status(self):
        try:
            host = "http://google.com"
            with urlopen(host): # Python 3.x
                self.connection_status = True
        except: #pylint: disable=bare-except
            self.connection_status = False

    def get_network_info(self):
        self.connect_status()
        mac = get_mac()
        self.mac_address =":".join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
        if not self.mac_address:
            self.mac_address = UNKNOWN

        self.hostname = socket.gethostname()
        if not self.hostname:
            self.hostname = UNKNOWN
            self.ip_address = UNKNOWN
        else:
            self.ip_address = socket.gethostbyname(self.hostname)

        if self.connection_status:
            self.speed_test = speedtest.Speedtest(secure=1)
            self.time_now = datetime.datetime.now().strftime("%H:%M:%S")
            self.down_speed = round(round(self.speed_test.download())
                                   / 1048576, 2)
            self.up_speed = round(round(self.speed_test.upload())
                                 / 1048576, 2)
        else:
            self.down_speed = UNKNOWN
            self.up_speed = UNKNOWN
        self.addresses = psutil.net_if_addrs()
        self.stats = psutil.net_if_stats()
        self.connected_interface =UNKNOWN
        prefixes =['169.254','127.']
        for intface, addr_list in self.addresses.items():
            if any(getattr(addr, 'address').startswith(tuple(prefixes)) for addr in addr_list):
                continue
            elif intface in self.stats and getattr(self.stats[intface], "isup"):
                self.connected_interface =intface

    def fill_network_info(self, json: dict):
        json["mac_address"] = self.mac_address
        json["ip_address"] = self.ip_address
        json["hostname"] = self.hostname
        json["connection_status"] = self.connection_status
        json["down_speed"] = self.down_speed
        json["up_speed"] = self.up_speed
        json["time_now"] = self.time_now
        