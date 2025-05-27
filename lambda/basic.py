# A simple lambda that adds two numbers
add=lambda x,y:x+y
print(add(5,3))

# A lambda with no arguments
greet = lambda: "Hello, World!"
print(greet())  # Output: Hello, World!

# A lambda with default arguments
power = lambda x, y=2: x ** y
print(power(3))    # Output: 9 (3 squared)
print(power(3, 3))  # Output: 27 (3 cubed)