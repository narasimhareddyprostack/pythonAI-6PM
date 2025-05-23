def login(uname, status):
    #write business login
    if status == True:
        return "Login Success"
    else:
        return "Login Failed"

msg1=login("Rahul",True)
msg2=login("Sonia",False)
msg3=login("Priyanka",True)
print(msg1)
print(msg2)
print(msg3)