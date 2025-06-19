#Extract from various sources - Rest API
import requests,json
data=requests.get('https://dummyjson.com/users')
user_data=data.json()
print(type(user_data))  #<class,dict>

users=user_data['users']
print(type(users))      #<class,list>
print(len(users))       #30

#transfor 
female_users=[]
for user in users:
    if user['gender']=='female':
        female_users.append({'uid':user['id'],
                             'name':user['firstName'],
                             'age':user['age']
                             })


print(len(female_users))

#Load into respective destination

fp=open('female.json','w')
json.dump(female_users,fp)
print("New JSON file created")

fp.close()