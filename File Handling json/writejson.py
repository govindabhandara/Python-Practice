import json
fp=open("js.json",'r')
employees=json.loads(fp)
print(employees)
fp.close()