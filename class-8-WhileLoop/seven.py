employees=[
            {'eid':101,'ename':"Rahul",'gender':'Male'},
            {'eid':102,'ename':"Sonia",'gender':'Female'},
            {'eid':103,'ename':"Priyanka",'gender':'Female'},
            {'eid':104,'ename':"Modi",'gender':'Male'},
            {'eid':105,'ename':"Amith",'gender':'Male'},
            {'eid':106,'ename':"DK Shiv",'gender':'Male'}
           ]
#iterate object employees object and print employee names
for emp in employees:
    print("Employee Name:",emp['ename'])
print("***********")

i=0
while i<=len(employees)-1:
    print(employees[i]['ename'])
    i=i+1