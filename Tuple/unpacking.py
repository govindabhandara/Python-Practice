my_tuple=1,"hello",3.14
a,b,c=my_tuple
print(a)
print(b)
print(c)

# Unpacking with * (variable-length unpacking)
tuple=[1,2,3,4,5]
a,*b,c=tuple
print(a)
print(b)
print(c)