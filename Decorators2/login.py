def login_req(func):

    def inner(status):
        if status ==False:
            print("Login Required")
        else:
            return func(status)
        
    return inner    

