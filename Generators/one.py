#Generate number from 1 to 10
import sys
def creators():
    list=[]
    i=1
    while i<=200:
        list.append(i)
        i+=1
    return list
print(creators())
z=sys.getsizeof(list)
print(z)
print([num+10 for num in creators()])

# or we can generate like this
number=list(range(1,200))
print(number)