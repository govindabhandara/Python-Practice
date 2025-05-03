text="I like apples."

#replace all occurances
print(text.replace("apples","oranges"))

# Replace with count
print(text.replace("like","love",1))

# Using str.replace()
s = "hello hello hello"
print(s.replace("hello", "hi", 2))  # "hi hi hello"

# Using re.sub()
import re
s = "cat dog cat dog"
print(re.sub(r'cat', 'bird', s, count=1))  # "bird dog cat dog"

# Using a loop for conditional replacement
s = "1,2,3,4,5"
count = 3
for num in ['X']*count:
    s = s.replace(',', '|', 1)
print(s)  # "1|2|3,4,5"