def outer():
    print("outer Function")
    def inner():
        print("inner function")
    return inner  # Return the function object, not the result of calling it

result = outer()
result() 
result()  
result()  
result()  