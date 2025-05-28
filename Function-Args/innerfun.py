def outer():
    print("Outer function - starting")
    
    def inner():
        print("Inner Function")

    inner()

outer()
outer()
