import os
import time
import string
import random
import requests
from sys import argv

file = argv[1]
print(file)
print(os.path.exists(file))

try:
    convreq1 = requests.post("https://api2.online-convert.com/jobs", headers=\
                            {'X-Oc-Api-Key': 'f3e92e642b8c41cc0ee73937d7459f81', 'Content-Type': 'application/json'}, \
                            data='{"conversion": [{"category": "image", "target": "ico"}]}')
    print(convreq1.content)
    convreq2 = requests.post("https://www13.online-convert.com/dl/web2/upload-file/"+convreq1.json()["id"], headers=\
                             {'X-Oc-Api-Key': 'f3e92e642b8c41cc0ee73937d7459f81', 'X-Oc-Upload-Uuid': \
                              ''.join(random.SystemRandom().choices(string.ascii_lowercase + string.digits, k=8))}, \
                             files={"file" : (file[file.rfind("\\")+1:], open(file, 'rb'), "image/png")})
    print(convreq2.content)
    time.sleep(2)
    convreq3 = requests.get("https://api2.online-convert.com/jobs/"+convreq1.json()["id"], headers=\
                            {'X-Oc-Api-Key': 'f3e92e642b8c41cc0ee73937d7459f81'})
    resultfile = open(argv[1][:argv[1].rfind("\\")]+argv[1][argv[1].rfind("\\"):argv[1].rfind(".")]+".ico", 'wb')
    resultfile.write(convreq3.content)
    resultfile.close()
except Exception as ex:
    print(ex)

input("")
