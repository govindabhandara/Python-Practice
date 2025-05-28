import json
fp=open("js.json",'r')
employees=json.load(fp)
print(employees)
fp.close()