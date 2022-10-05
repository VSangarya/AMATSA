'''Tests on driver code'''

import json
from src.driver import CollectMetrics
from datetime import datetime

def test_data_collection():
    success = True
    data = {}
    try:
        if not CollectMetrics(data):
            success = False
    except ValueError: # pylint: disable=bare-except
        success = False
    assert success, "Failed to collect metrics"

def test_json_validation():
    success = True
    client_json = {}
    try:
        # dummy meta-data fields
        version = "1.0"
        client_json["metadata"] = {"version": version, "time": datetime.utcnow().isoformat() + "Z"}

        if CollectMetrics(client_json):
            _ = json.loads(json.dumps(client_json, indent=2))
            print(json.dumps(client_json, indent=2))

    except ValueError: # pylint: disable=bare-except
        success = False
    assert success, "Invalid JSON"
