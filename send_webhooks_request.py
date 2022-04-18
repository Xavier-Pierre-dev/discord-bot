import requests
import json

webhook_url = ""

data = {
    "name": "John Smith",
    "Channel URL": ""
}

header = {"Content-Type": "application/json"}

r = requests.post(url=webhook_url, data=json.dumps(data), headers=header)
