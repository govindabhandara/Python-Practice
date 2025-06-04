nums=[1,2,3,4]
print(all(nums))

values = [10, 20, 30]
print(all(x > 5 for x in values))  # Output: True
print(all(x > 25 for x in values))  # Output: False