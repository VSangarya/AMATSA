"""This module fetches disk information and returns a JSON with the disk data"""
import psutil
from utils import size_in_gb

class Disk:
    """Class to fetch, format and return disk information"""
    def __init__(self):
        self.data = {}


    def check_attr(self,attr, val):
        try:
            val = getattr(attr, val)
        except: # pylint: disable=bare-except
            val = None
        return val


    def retrieve_disk_info(self):
        par = psutil.disk_partitions()
        self.data["disk"] = []
        for x in par:
            dsk = psutil.disk_usage(x.mountpoint)
            each_disk = {}

            each_disk["name"] = self.check_attr(x,"device")
            each_disk["type"] = self.check_attr(x,"fstype")
            each_disk["total_size"] = size_in_gb(self.check_attr(dsk,"total"))
            each_disk["used"] = size_in_gb(self.check_attr(dsk,"used"))
            each_disk["free"] = size_in_gb(self.check_attr(dsk,"free"))
            each_disk["percentage"] = self.check_attr(dsk,"percent")

            self.data["disk"].append(each_disk)
        return self.data["disk"]
