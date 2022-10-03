import json
import disk
from getmac import get_mac_address as gma
import os
import yaml
import json
from elasticsearch import Elasticsearch



if __name__ == "__main__":
    
    client_json = {}

# read config from yml file
    with open(os.path.dirname(os.path.realpath(__file__)) + "/config/amatsa-client.yml", "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

# collect data
    client_json["version"] = config["version"]

# push json object to elastic backend
    token = (config["auth"]["username"], config["auth"]["password"])
    
    client_id=str((gma()))
    client_json["id"]=client_id
    client_disk=disk.Disk()
    client_disk_info=client_disk.retrieve_disk_info()
    client_json["Disk"]=client_disk_info
    




    client_json=json.dumps(client_json)
    es = Elasticsearch(hosts = config["connect"]["endpoint"], ssl_assert_fingerprint = config["connect"]["tls-fingerprint"], basic_auth = token)
    resp = es.index(index = config["index"]["name"], document = client_json)
    # print(client_json)