'''Client Code integrates all metrics and send to Elastic Server'''

import json
from src.disk import Disk
from src.system import System
from src.network import Network
import os
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

    if not CollectMetrics(client_json):
        sys.exit(1)

    try:
        # push to elastic
        es = Elasticsearch(hosts=config["connect"]["endpoint"],ssl_assert_fingerprint=config["connect"]["tls-fingerprint"],basic_auth=token)
        resp = es.index(index=config["index"]["name"], document = client_json)
    except ValueError:
        print("Failed to send data to backend", file=sys.stderr)
        sys.exit(1)
