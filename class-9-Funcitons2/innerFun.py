def outer():
    print("Outer Function")

    def inner():
        print("Inner Function")

    #nner()
    #inner()
    return inner

inner=outer()
inner()