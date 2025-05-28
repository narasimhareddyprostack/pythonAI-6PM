def outer():
    def m1():
        print("inner fun - m1")
    def inner():
        print("inner funciton")
    return inner

value=outer()
#print(value)
value()