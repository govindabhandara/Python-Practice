def creator():
    i=1
    while i<=200:
        yield i
        i+=1
print(creator())
x=creator()
print(next(x))
print(next(x))
print(next(x))
# if we can print remain all then we can use:
print(list(x))