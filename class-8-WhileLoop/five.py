uids=[101,102,103,104]
enames=('RG','SG','PG','NM')
eids={101,102,101,103,101,104,101}

#Iterate above object using for loop and while loop

for ename in enames:
    print(ename)
print("*******")

i=0
while i<=len(enames)-1:
    print(enames[i])
    i=i+1