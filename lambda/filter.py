# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]


# Filter strings that start with 'A'
names = ['Alice', 'Bob', 'Anna', 'Charlie', 'Alex']
a_names = list(filter(lambda name: name.startswith('A'), names))
print(a_names)  # Output: ['Alice', 'Anna', 'Alex']

