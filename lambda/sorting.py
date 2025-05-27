# Sort a list of tuples by the second element
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)  # Output: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]


# Sort a list of dictionaries by a specific key
people = [{'name': 'John', 'age': 45}, {'name': 'Diana', 'age': 35}, {'name': 'Aaron', 'age': 24}]
people.sort(key=lambda x: x['age'])
print(people)
# Output: [{'name': 'Aaron', 'age': 24}, {'name': 'Diana', 'age': 35}, {'name': 'John', 'age': 45}]