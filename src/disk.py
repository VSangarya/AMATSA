"""This module fetches disk information and returns a JSON with the disk data"""
import psutil
import json


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
        self.data["Disk"] = []
        for x in par:
            dsk = psutil.disk_usage(x.mountpoint)
            each_disk = {}

            each_disk["name"] = self.check_attr(x,"device")
            each_disk["type"] = self.check_attr(x,"fstype")
            each_disk["total_size"] = self.check_attr(dsk,"total")
            each_disk["used"] = self.check_attr(dsk,"used")
            each_disk["free"] = self.check_attr(dsk,"free")
            each_disk["percetage"] = self.check_attr(dsk,"percent")

            self.data["Disk"].append(each_disk)
        return json.dumps(self.data, indent = 2)

""" # pylint: disable=pointless-string-statement
if __name__ == "__main__":
  d = Disk()
  print(d.retrieve_disk_info())
"""
