a=100 # a is global variable so we can access all over module/file

def funcone():
    print(a)

def functwo():
    print(a)

def functhree():
    print(a)

funcone()
functwo()
functhree()