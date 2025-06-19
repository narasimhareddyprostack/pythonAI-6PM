import json

fp=open('emp.json','r')
employee_list=json.load(fp)
print(type(employee_list))
print(employee_list)

for emp in employee_list:
    print(emp['ename'])