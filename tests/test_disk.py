"""Tests for the Disk module"""
from src.disk import Disk

def test_disk_init():
    success = True
    try:
        _ = Disk()
    except: # pylint: disable=bare-except
        success = False
    assert success, "Failed to initialize Data()"


def test_disk_datatype():
    success = True
    try:
        disk = Disk()
        data = disk.retrieve_disk_info()
    except: # pylint: disable=bare-except
        print("Failed to collect Data metrics")
        success = False
    num = (float, int)
    data_types = {"name" : str, "type" : str, "total_size" : num, "used" : num, "free" : num, "percentage" : num}
    for each in data:
        for field in each.keys():
            if not isinstance(each[field], data_types[field]) :
                print(f"For data '{field}', type should be {data_types[field]}, not {type(each[field])}")
                success = False
    assert success


def test_disk_values():
    success = True
    try:
        disk = Disk()
        data = disk.retrieve_disk_info()

        fields = ["total_size", "used", "free", "percentage"]
        for each in data:
            for each_field in fields:
                if each[each_field] < 0:
                    print(f"For disk data '{each_field}', value cannot be negative")
                    success = False
    except: # pylint: disable=bare-except
        print("Failed to collect Data metrics")
        success = False
    assert success
