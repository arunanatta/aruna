import json
import subprocess
import sys

with open('dependencies.json') as json_data:
    dependencies = json.load(json_data)

dependencies = dependencies["Dependencies"]
for key, value in dependencies.items():
    package = key+'=='+value
    res = subprocess.run(["pip", "install",package])
   # print(res)
    if res.returncode==0:
        print("{} successfully installed".format(key))
    else:
        print("Error in installing {}".format(key))
