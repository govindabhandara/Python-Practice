def check_divide(func):

    def inner(a,b):
        if b==0:
            print("can't divide by zero")
        else:
            return func(a,b)
    return inner
@check_divide
def divide(a,b):
    print(a/b)

divide(10,2)
divide(10,0) 