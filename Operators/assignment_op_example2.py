# Swap two variables x and y without a temporary variable (using arithmetic operators).
x = int(input("enter value of x"))
y = int(input("enter value of y"))

print(f"Before swap: x = {x}, y = {y}")

# Swap using arithmetic operations
x = x + y  
y = x - y  
x = x - y  

print(f"After swap: x = {x}, y = {y}")