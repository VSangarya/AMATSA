'''Client Code integrates all metrics and send to Elastic Server'''

import json
import os
import sys
import yaml
from datetime import datetime
from elasticsearch import Elasticsearch
# import tests.test_driver
#from unittest import TestCase
from src.disk import Disk
from src.system import System
from src.network import Network
from src.gpu import GPUdata


def CollectMetrics(obj: dict) -> bool:
    """This method collects client metrics and returns them in a json"""
    # empty json objects
    agent = {}
    metrics = {}
    netw = {}

    try:
        # instances for data collection
        fs = Disk()
        sy = System()
        net = Network()
        # disk info
        client_disk_info = fs.retrieve_disk_info()
        obj["disk"] = client_disk_info
        # system info
        sy.FillSystemInfo(json=agent)
        sy.FillSystemMetrics(json=metrics)
        obj["agent"] = agent
        obj["metrics"] = metrics
        #network info
        net.get_network_info()
        net.fill_network_info(netw)
        obj["network"] = netw
        #gpu info
        client_gpu = GPUdata()
        gpu_info = client_gpu.retrieve_gpu_info()
        if not gpu_info:
            gpu_info = None
        obj["gpu"] = gpu_info
        #converting to json string
    except ValueError:
        return False

    return True

if __name__ == "__main__":
    client_json = {}
    # read config from yml file
    with open(os.path.dirname(os.path.realpath(__file__)) + "/config/amatsa-client.yml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    # collect meta-data fields
    version = config["version"]
    client_json["metadata"] = {"version": version, "time": datetime.utcnow().isoformat() + "Z"}
    token = (config["auth"]["username"], config["auth"]["password"])
    if not CollectMetrics(client_json):
        sys.exit(1)
    client_json = json.dumps(client_json, indent=2)
    print("final_json", client_json)
    print("client_json",client_json)
    try:
        # push to elastic
        hosts_config = config["connect"]["endpoint"]
        ssl_fingerprint = config["connect"]["tls-fingerprint"]
        es = Elasticsearch(hosts=hosts_config, ssl_assert_fingerprint=ssl_fingerprint, basic_auth=token)
        resp = es.index(index=config["index"]["name"], document=client_json)
    except ValueError:
        print("Failed to send data to backend", file=sys.stderr)
        sys.exit(1)
