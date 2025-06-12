def smart_div(func):

    def inner(a,b):
        if b==0:
            print("Can't Divide By Zero")
        else:
            return func(a,b)
    return inner