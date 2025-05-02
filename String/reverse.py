def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))

# or
def reverse_string(y):
    return''.join(reversed(y))
print(reverse_string("hello"))

#or
def reverse_string(s):
    result=""
    for char in s:
        result=char + result
    return result 
print(reverse_string("hello"))