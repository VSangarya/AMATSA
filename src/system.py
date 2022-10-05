"""File contains definition for System class"""


import platform
import psutil
import sys
import time
import uuid
from datetime import datetime
from src.utils import size_in_gb

UNKNOWN = "unknown"

class System:
    """Defines methods to retrieve machine info"""
    hostname = None
    bios_uuid = None
    platform_name = None
    release = None
    version = None
    machine = None
    is_x64 = None
    physical_cores = None
    logical_cores = None
    total_memory = None

    def __init__(self) -> None:
        # hostname
        self.hostname = platform.node()
        if not self.hostname:
            self.hostname = UNKNOWN

        self.bios_uuid = str(uuid.UUID(int=uuid.getnode()))
        if not self.bios_uuid:
            self.bios_uuid = self.hostname

        # platform - Windows, Linux, Darwin etc.
        # release - NT, 2.2.0, 21.6.0
        # version - kernel version number
        (self.platform_name, self.release, self.version) = platform.system_alias(platform.system(), platform.release(), platform.version())
        if not self.platform_name:
            self.platform_name = UNKNOWN
        if not self.release:
            self.release = UNKNOWN
        if not self.version:
            self.version = UNKNOWN

        # machine - x86_64, arm64
        self.machine = platform.machine()
        if not self.machine:
            self.machine = UNKNOWN

        # architecture - boolean flag determines 64bit os
        self.is_x64 = sys.maxsize > 2**32

        # physical cpu cores
        self.physical_cores = psutil.cpu_count(logical=False)
        if not self.physical_cores:
            self.physical_cores = UNKNOWN

        # logical cpu cores
        self.logical_cores = psutil.cpu_count(logical=True)
        if not self.logical_cores:
            self.logical_cores = UNKNOWN

        # physical memory
        mem = psutil.virtual_memory()
        self.total_memory = size_in_gb(mem.total)
        if not self.total_memory:
            self.total_memory = UNKNOWN

    def FillSystemInfo(self, json: dict):
        """This method fills the colelcted system info from the object's attributes"""
        json["hostname"] = self.hostname
        json["bios_uuid"] = self.bios_uuid
        json["platform"] = self.platform_name
        json["release"] = self.release
        json["version"] = self.version
        json["machine"] = self.machine
        json["is64bit"] = self.is_x64
        json["physical_cores"] = self.physical_cores
        json["logical_cores"] = self.logical_cores
        json["total_memory_gb"] = self.total_memory

    def FillSystemMetrics(self, json: dict):
        """This method fills system information that is more prone to change"""
        # cpu utilization in %
        cpu_load = [x/self.logical_cores * 100 for x in psutil.getloadavg()]
        json["cpu_load_5min"] = round(cpu_load[1], 2)
        json["cpu_load_15min"] = round(cpu_load[2], 2)

        # available memory
        json["avail_memory_gb"] = size_in_gb(psutil.virtual_memory().available)

        # time since last boot
        current_time = datetime.fromtimestamp(time.time())
        boot_time = datetime.fromtimestamp(psutil.boot_time())
        diff = current_time - boot_time
        json["boot_days_ago"] = diff.days
