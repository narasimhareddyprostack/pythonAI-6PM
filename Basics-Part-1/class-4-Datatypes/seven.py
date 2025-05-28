#create 
enames=("Rahul","Sonia","Priyanka")
#read
print(enames)
#read tuple elements? using index 
print(enames[0])
print(enames[1])
print(enames[2])
#update & Delete 
enames[0] = "Rahul Gandhi" 
'''
TypeError: 'tuple' object does not support item assignment
'''
print(enames)
