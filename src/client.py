"""driver script for data collection"""

import os
import yaml
import json
from elasticsearch import Elasticsearch

data = {}

# read config from yml file
with open(os.path.dirname(os.path.realpath(__file__)) + "/config/amatsa-client.yml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

# collect data
data["version"] = config["version"]

# push json object to elastic backend
token = (config["auth"]["username"], config["auth"]["password"])
es = Elasticsearch(hosts = config["connect"]["endpoint"], ssl_assert_fingerprint = config["connect"]["tls-fingerprint"], basic_auth = token)
resp = es.index(index = config["index"]["name"], document = json.dumps(data))
