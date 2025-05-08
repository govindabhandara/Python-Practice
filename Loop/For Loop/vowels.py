text="Programming is fun."
vowels='aeiouAEIOU'
count=0
for char in text:
    if char in vowels:  
        count+=1
print("no of vowels:",count)