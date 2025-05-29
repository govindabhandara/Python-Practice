def creator():
    i=1
    while i<=200:
        i+=1
        yield i
print(creator())
x=creator()
print(next(x))