
def dividion_check(func):
    def inner(a,b):
        if b==0:
            print("Can't Divide by zero")
        else:
            return func(a,b)
        
    return inner
@dividion_check
def divide(a,b):
    print(a/b)

divide(10,5)
divide(10,0) 
divide(200,10)
divide(30,0)