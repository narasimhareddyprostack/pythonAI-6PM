import json 

employee_json_str='''
                    [
    {
        "eid": 101,
        "ename": "Alice",
        "gender": "Female",
        "availability": true
    },
    {
        "eid": 102,
        "ename": "Bob",
        "gender": "Male",
        "availability": false
    },
    {
        "eid": 103,
        "ename": "Charlie",
        "gender": "Male",
        "availability": true
    }
]

                  '''


employee_list=json.loads(employee_json_str)
print(type(employee_list))
print(employee_list)
