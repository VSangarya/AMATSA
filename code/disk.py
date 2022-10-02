import psutil
import json


class Disk:
  def __init__(self):
    self.data = {}

  def retrieve_disk_info(self):
    par = psutil.disk_partitions()
    self.data["Disk"] = []
    for x in par:
      dsk = psutil.disk_usage(x.mountpoint)
      each_disk = {}
      each_disk["name"] = x.device if hasattr(x,"device") else None
      each_disk["type"] = x.fstype if hasattr(x,"fstype") else None
      each_disk["total_size"] = dsk.total if hasattr(dsk,"total") else None
      each_disk["used"] = dsk.used if hasattr(dsk,"used") else None
      each_disk["free"] = dsk.free if hasattr(dsk,"free") else None
      each_disk["percetage"] = dsk.percent if hasattr(dsk,"percent") else None
      
      self.data["Disk"].append(each_disk) 
    return self.data

 
if __name__ == "__main__":
  d = Disk()
  disk_data = json.dumps(d.retrieve_disk_info(), indent = 2)
  #print(disk_data)

