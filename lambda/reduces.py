# #reduce function :
# reduce () -reduces  sequence of elements  into a single element.
# reduce(function,sequence)

from functools import reduce
marks=[35,36,38,39,37]
result=reduce(lambda a,b:a+b,marks)
print(result)