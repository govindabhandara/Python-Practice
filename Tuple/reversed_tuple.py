animals=('rabbit',"cat","dog")
y=list(animals)
y.reverse()
x=tuple(y)
print(x)

fruits=("watermelon","apple","banana")
print(fruits[::-1])

number=(1,2,3,4)
reversed_tuple=tuple(reversed(number))
print(reversed_tuple)

#using loop
my_tuple = (10, 20, 30, 40)
reversed_tuple = tuple(my_tuple[i] for i in range(len(my_tuple)-1, -1, -1))
print(reversed_tuple)  # Output: (40, 30, 20, 10)