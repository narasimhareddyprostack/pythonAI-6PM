from mathex import smart_div

@smart_div
def calc(a,b):
    return a/b 

print(calc(10,5))   #2.0 
print(calc(10,0))   #ZeroDivError:
print("GE")         