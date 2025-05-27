def outer():
    print("outer function")
    def inner():
        print("inner function")

outer()
inner() # name error
#execute inner function, outside function
#return function ref, and call