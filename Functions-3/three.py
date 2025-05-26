a=100    #global variable

def funcone():
    b=200  # local variable scope  // within the function 

def functwo():
    a=20
    print(a+b)

funcone()
functwo()

# Here, NameError: name 'b' is not defined