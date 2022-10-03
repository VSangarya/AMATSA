import uuid
import socket
import speedtest
import datetime
import urllib.request


UNKNOWN = "unknown"

class network:
    macaddr = None
    ipaddr = None
    hostname = None
    time_now = None
    downspeed = None
    upspeed = None
    speedtest = None
    connection_status = None

    def __init__(self):
        self.adapterlist ={}
        self.connection_status =False

    def connectStatus(self):
        try:
            host = 'http://google.com'
            urllib.request.urlopen(host)  # Python 3.x
            self.connection_status =False
        except:
            self.connection_status = False

    def get_network_info(self):
        self.connectStatus()
        self.macaddr = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1])
        if not self.macaddr:
            self.macaddr =UNKNOWN

        self.hostname = socket.gethostname()
        if not self.hostname:
            self.hostname= UNKNOWN
            self.ipaddr =UNKNOWN
        else:
            self.ipaddr = socket.gethostbyname(self.hostname)

        if self.connection_status == True:
            self.speedtest = speedtest.Speedtest(secure=1)
            self.time_now = datetime.datetime.now().strftime("%H:%M:%S")
            self.downspeed = round((round(self.speedtest.download()) / 1048576), 2)
            self.upspeed = round((round(self.speedtest.upload()) / 1048576), 2)
        else:
            self.downspeed =UNKNOWN
            self.upspeed =UNKNOWN

    def FillNetworkInfo(self, json: dict):
        json["macaddr"] = self.macaddr
        json["ipaddr"] = self.ipaddr
        json["hostname"] = self.hostname
        json["connectStatus"] = self.connectStatus
        json["downspeed"] = self.downspeed
        json["upspeed"] = self.upspeed
        json["time_now"] = self.time_now


