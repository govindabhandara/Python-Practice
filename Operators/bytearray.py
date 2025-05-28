list1=[80,40,81,14,255,0]
ba=bytearray(list1)
print(type(ba))
ba[1]=41
print(ba)
print(81 in ba)
for value in ba:
    print(value)