'''Client Code integrates all metrics and send to Elastic Server'''

import json
# from xmlrpc import client
import disk
import system
import network
import os
import yaml
import datetime
from elasticsearch import Elasticsearch
import tests.driver_tests



if __name__ == "__main__":
    client_json = {}
# read config from yml file
    with open(os.path.dirname(os.path.realpath(__file__)) + "/config/amatsa-client.yml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
# collect data
    version = config["version"]
    client_json["metadata"] = {"version":version,"time":str(datetime.datetime.now().isoformat()[:-3]+"Z")}
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
    client_system.FillSystemMetrics(json = metrics)
    client_json["agent"] = agent
    client_json["metrics"] = metrics
    #More code for other metrics
    n = network.Network()
    n.get_network_info()
    network = {}
    n.fill_network_info(network)
    # print(client_json)
    client_json["network"] = network
    client_json = json.dumps(client_json,indent = 2)
    tests.driver_tests.validate_json(client_json)
    print("final_json",client_json)
    es = Elasticsearch(hosts = config["connect"]["endpoint"],ssl_assert_fingerprint=config["connect"]["tls-fingerprint"],basic_auth = token)
    resp = es.index(index = config["index"]["name"], document = client_json)

