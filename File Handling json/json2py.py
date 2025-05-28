import json
emp_json='''{"eid":101,"ename":"Rahul","esal":45000,"Avail":true}'''
emp_dict=json.loads(emp_json)
print(emp_dict)