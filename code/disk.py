import psutil
import json


class Disk:
  def __init__(self):
    self.data = {}


  def checkAttr(self,attr, val):
    try:
      val = getattr(attr, val)
    except:
      val = None
    return val



  def retrieve_disk_info(self):
    par = psutil.disk_partitions()
    self.data["Disk"] = []
    for x in par:
      dsk = psutil.disk_usage(x.mountpoint)
      each_disk = {}

      each_disk["name"] = self.checkAttr(x,"device")
      each_disk["type"] = self.checkAttr(x,"fstype")
      each_disk["total_size"] = self.checkAttr(dsk,"total")
      each_disk["used"] = self.checkAttr(dsk,"used")
      each_disk["free"] = self.checkAttr(dsk,"free")
      each_disk["percetage"] = self.checkAttr(dsk,"percent")

      self.data["Disk"].append(each_disk)
    return json.dumps(self.data, indent = 2)

"""
if __name__ == "__main__":
  d = Disk()
  print(d.retrieve_disk_info())
"""
