emp= {
    'eid':101,
    "Name":'Rahul',
    'esal':45000.45,
    'Loc':'Banglore'
    }
for key in emp:
    # print(key)
    # print(emp[key])
    print(key,":",emp[key])
for k, v in emp.items():
    print(f"{k} => {v}")

for v in emp.values():
    print(v)

