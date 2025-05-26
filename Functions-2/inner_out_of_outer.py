def outer():

    def inner():
        print("inner function")

    # return 100,200 #output(100,200)
    # return 'hello good morning' Output hello good morning
    return inner()
result=outer()
print(result)
    

