text='I love Programming.'
vowels='aeiouAEIOU'
count=0
for char in text:
    if char in vowels:
        count+=1
print(f"The number of vowels is {count}")


