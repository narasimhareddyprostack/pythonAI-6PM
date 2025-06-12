def smart_div(func):

    def inner(a,b):
        if b==0:
            print("Can't Divide by zero")
        else:
            return func(a,b)
        
    return inner

@smart_div
def calc(a,b):
    return a/b


print(calc(10,5))    #2.0
print(calc(10,0))    #Cannot Divibe by zero
print("GE")