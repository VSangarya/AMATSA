"""Tests for the Network module"""
from src.network import Network

def test_network_init():
    success = True
    try:
        _ = Network()
    except: #pylint: disable=bare-except
        success = False
    assert success, "Failed to initialize Network()"