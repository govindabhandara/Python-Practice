# Use a ternary operator to find the maximum of two numbers.

a=int(input ("enter a"))
b=int(input ("enter b"))
if (a>b):
    print("a is maximum")
else:
    print (" b is maximum")

print("a is maximum" if a>b else "b is maximum")