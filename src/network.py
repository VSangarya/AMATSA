#!/usr/bin/python
"""This module fetches network information and returns a JSON with the network info data"""
import uuid
import socket
import speedtest
import datetime
from urllib.request import urlopen

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

    def __init__(self):
        self.connection_status = False

    def connect_status(self):
        try:
            host = "http://google.com"
            with urlopen(host) as response: # Python 3.x
                self.connection_status = True
        except: #pylint: disable=bare-except
            self.connection_status = False

    def get_network_info(self):
        self.connect_status()
        self.mac_address = ":".join(["{:02x}".format(uuid.getnode() >> ele
                                & 0xff) for ele in range(0, 8 * 6, 8)][:
                                :-1])
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
        print(self.connection_status)

    def fill_network_info(self, json: dict):
        json["mac_address"] = self.mac_address
        json["ip_address"] = self.ip_address
        json["hostname"] = self.hostname
        json["connection_status"] = self.connection_status
        json["down_speed"] = self.down_speed
        json["up_speed"] = self.up_speed
        json["time_now"] = self.time_now
