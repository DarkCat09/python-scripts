# encoding: utf-8
import os
from sys import argv
import time
import json
import requests

file = argv[1]
print(file)

fileready = False
scanreq = requests.post("https://www.virustotal.com/vtapi/v2/file/scan", \
              params={"apikey": "147eac96e8a588d37164c584cdbc9f28d2138558ce7965ffc357dcf29215d963"}, \
              files={"file": (file[file.rfind("\\"):], open(file, 'rb'))})
json_scanreq = json.loads(scanreq.content)
reportreq = None
while not fileready:
    time.sleep(1)
    reportreq = requests.get("https://www.virustotal.com/vtapi/v2/file/report", \
                             params={"apikey": "147eac96e8a588d37164c584cdbc9f28d2138558ce7965ffc357dcf29215d963",\
                                     "resource": json_scanreq["md5"]})
    fileready = (json.loads(reportreq.content)["response_code"] == 1)
print(json.loads(reportreq.content))
