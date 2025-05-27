# numbers=[1,2,3,4,5,6,7,8,9,10]
# def is_odd(number):
#     if number%2!=0:
#         return True
#     else:
#         return False
    
# new_odd=list(filter(is_odd,numbers))
# print(numbers)
# print(new_odd)

numbers=[1,2,3,4,5,6,7,8,9,10]
is_odd=list(filter(lambda num:num%2!=0,numbers))
print(numbers)
print(is_odd)