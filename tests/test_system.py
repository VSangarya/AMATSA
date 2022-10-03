"""Tests for the System module"""
from src.system import System

def test_system_init():
    success = True
    try:
        _ = System()
    except: # pylint: disable=bare-except
        success = False
    assert success, "Failed to initialize System()"

def test_system_data():
    success = True
    json = {}
    try:
        sys = System()
        sys.FillSystemInfo(json)
        for k, v in json.items():
            if isinstance(v, str) and str in (None, "unknown"):
                print(f"Value [{v}] for '{k}' is not expected, expected str.")
                success = False
            else:
                print(f"{k}:{v}, type:{type(v)}")
    except: # pylint: disable=bare-except
        success = False
    assert success, "Failed to collect system info"

def test_system_metrics():
    success = True
    json = {}
    try:
        sys = System()
        sys.FillSystemMetrics(json)
        for k, v in json.items():
            if isinstance(v, int) and v < 0:
                print(f"Value [{v}] for '{k}' is not expected, expected int.")
                success = False
            elif isinstance(v, float) and v == 0.0:
                print(f"Value [{v}] for '{k}' is not expected, expected float.")
                success = False
            else:
                print(f"{k}:{v}, type:{type(v)}")
    except: # pylint: disable=bare-except
        success = False
    assert success, "Failed to collect system metrics"
