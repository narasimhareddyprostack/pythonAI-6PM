#variable lenght argument
def add(a,*b):
    print(a, "-", b)


add(10,20)           #10 -(20)
add(10,20,30)        #10 -(20,30)
add(10,20,30,40)     #10 -(20,30,40)
add(10,20,30,40,50)  #10 -(20,30,40,50)