uids=[101,102,103,104]
enames=('RG','SG','PG','NM')
eids={101,102,101,103,101,104,101}

#Iterate above object using for loop and while loop
for uid in uids:
    print(uid)

print("***********")
i=0
while i<=len(uids)-1:
    print(uids[i])
    i=i+1