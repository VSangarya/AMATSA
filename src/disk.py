"""This module fetches disk information and returns a JSON with the disk data"""
import psutil
from utils import size_in_gb
from system import System
import re

class Disk:
    """Class to fetch, format and return disk information"""
    def __init__(self):
        self.data = {}
        self.sys = System()


    def check_attr(self,attr, val):
        try:
            val = getattr(attr, val)
        except: # pylint: disable=bare-except
            val = None
        return val


    def format_darwin(self, data):
        disk_nums = [ [] for i in range(len(data["disk"]))]
        for i in range(0,len(disk_nums)):
            result = re.search(r"/dev/disk(\d+)s", data["disk"][i]["name"])
            if result is not None:
                result = int(result.group(0).replace("/dev/disk","").replace("s",""))
                data["disk"][i]["number"] = result
                disk_nums[result].append(data["disk"][i])
        res = [ele for ele in disk_nums if ele != []]

        final_disk = []
        for each_disk in res:
            print(each_disk)
            total_size = each_disk[0]["total_size"]
            used = each_disk[0]["used"]
            free = each_disk[0]["free"]
            name = "/dev/disk"+str(each_disk[0]["number"])
            type = each_disk[0]["type"] # pylint: disable=W0622
            percentage = round((used/total_size)*100,2) 

            summed_disk ={
                "name" : name,
                "type" : type,
                "total_size" : total_size,
                "used" : used,
                "free" : free,
                "percentage" : percentage
            }

            final_disk.append(summed_disk)
        return final_disk


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

        if self.sys.platform_name == "Darwin" :
            self.data["disk"] = self.format_darwin(self.data)

        return self.data["disk"]



