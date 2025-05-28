import json

emp_dict={'eid': 101, 
          'ename': 'Rahul', 
          'esal': 45000, 
          'Avail': True,
          'discount':None}

emp_json=json.dumps(emp_dict)
print(emp_json)