# The function calls itself called recursive function
# for factorial
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
result=factorial(6)
print(result)

'''
6*factorial(5)
6*5*factorial(4)
6*5*4*factorial(3)
6*5*4**3*factorial(2)
6*5*4**3*2*1
'''

