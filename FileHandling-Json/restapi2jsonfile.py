import requests
import json 

data=requests.get('https://jsonplaceholder.typicode.com/users')
users=data.json()
print(type(users))
fp=open('users.json','w')
json.dump(users,fp)
print("new users.json file created")
fp.close()