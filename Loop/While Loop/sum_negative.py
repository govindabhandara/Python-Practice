total = 0
number = int(input("Enter a number (negative to stop): "))

while number >= 0:
    total += number
    number = int(input("Enter another number (negative to stop): "))

print(f"Total sum: {total}")