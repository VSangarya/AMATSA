"""Tests for the Network module"""
from src.network import Network

def test_network_init():
    success = True
    try:
        _ = Network()
    except:
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
    except:
        success = False
    assert success, "Failed to collect Network info"