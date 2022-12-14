"""Tests for the Network module"""
from src.network import Network
import re

def test_network_init():
    success = True
    try:
        _ = Network()
    except:#pylint: disable=bare-except
        success = False
    assert success, "Failed to initialize Network()"

def test_network_entries():
    success = True
    json = {}
    try:
        net_obj = Network()
        net_obj.get_network_info()
        net_obj.fill_network_info(json)
        for k, v in json.items():
            if isinstance(v, str) and str in (None, "unknown"):
                print(f"Value [{v}] for '{k}' is not expected, expected str.")
                success = False
            else:
                print(f"{k}:{v}, type:{type(v)}")
    except: #pylint: disable=bare-except
        success = False
    assert success, "Failed to collect Network info"

def test_network_datatype():
    success = True
    json = {}
    try:
        net_obj = Network()
        net_obj.get_network_info()
        net_obj.fill_network_info(json)
    except: #pylint: disable=bare-except
        print("Failed to collect Network metrics")
        success = False
    data_types = {"mac_address" : str, "ip_address" : str, "hostname" : str, "connection_status" : bool,
                  "down_speed" : float, "up_speed" : float, "time_now" : str, "connected_interface" : str}
    for k, v in json.items():
        if not isinstance(v, data_types[k]) :
            print(f"For data '{k}', type should be {data_types[k]}, not {type(v[k])}")
            success = False
    assert success

def test_macadd():
    success = True
    json = {}
    try:
        net_obj = Network()
        net_obj.get_network_info()
        net_obj.fill_network_info(json)
        if not re.match(r"([0-9a-fA-F]{2}[-:]){5}[0-9a-fA-F]{2}$", json["mac_address"], re.IGNORECASE):
            success = False
    except: #pylint: disable=bare-except
        print("Invalid Mac address validation")
        success = False
    assert success
