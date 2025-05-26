#convert local variable to global variable
def funcone():
    global a
    a=100

def functwo():
    print(a)

funcone()
functwo()