'''Client Code integrates all metrics and send to Elastic Server'''

import json
from src.disk import Disk
from src.system import System
from src.network import Network
import os
import gpu
import sys
import yaml
from datetime import datetime
from elasticsearch import Elasticsearch

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

        # network info
        net.get_network_info()
        net.fill_network_info(netw)
        obj["network"] = netw

        obj = json.dumps(obj, indent=2)
        #print("final_json", obj)

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
    # client_id=str((gma()))
    # client_json["id"]=client_id
    client_disk = disk.Disk()
    client_disk_info = client_disk.retrieve_disk_info()
    client_json["disk"] = client_disk_info
    agent = {}
    client_system = system.System()
    client_system.FillSystemInfo(json = agent)
    metrics = {}
    client_system.FillSystemMetrics(json=metrics)
    client_json["agent"] = agent
    client_json["metrics"] = metrics
    n = network.Network()
    n.get_network_info()
    network = {}
    n.fill_network_info(network)
    # print(client_json)
    client_json["network"] = network
    client_gpu = gpu.GPUdata()
    gpu_info=client_gpu.retrieve_gpu_info()
    if len(gpu_info) ==n0:
        gpu_info = None
    client_json["gpu"] = gpu_info
    client_json = json.dumps(client_json,indent = 2)
    tests.driver_tests.validate_json(client_json)
    print("final_json", client_json)
    if not CollectMetrics(client_json):
        sys.exit(1)
    try:
        # push to elastic
        es = Elasticsearch(hosts=config["connect"]["endpoint"], ssl_assert_fingerprint=config["connect"]["tls-fingerprint"], basic_auth=token)
        resp = es.index(index=config["index"]["name"], document=client_json)
    except ValueError:
        print("Failed to send data to backend", file=sys.stderr)
        sys.exit(1)
