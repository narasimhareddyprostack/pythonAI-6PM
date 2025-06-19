import json 
employees=[
          {'eid': 101, 
           'ename': 'Alice', 
           'gender': 'Female', 
           'availability': True
           }, {'eid': 102, 'ename': 'Bob', 'gender': 'Male', 'availability': False}, {'eid': 103, 'ename': 'Charlie', 'gender': 'Male', 'availability': True}]

emp_json=json.dumps(employees)
print(type(emp_json))
print(emp_json)