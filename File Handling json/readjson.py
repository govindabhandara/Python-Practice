import json
fp=open('js.json','r')
employees=json.load(fp)

print(employees)

# for emp in employees:
#     print(emp["id"])
