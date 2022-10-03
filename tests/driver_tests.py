'''Tests on driver code'''

import json
def validate_json(json_string):
    success=True
    try:
        _=  json.loads(json_string)
    except: # pylint: disable=bare-except
        success=False
    print(success)
    assert success,"Invalid JSON"
