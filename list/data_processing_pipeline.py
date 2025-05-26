# Data cleaning workflow
raw_data = ["  ALICE  ", "bob", "  Charlie  ", "DAVE"]

clean_data = [name.strip().title() for name in raw_data]
print(clean_data)
# Result: ['Alice', 'Bob', 'Charlie', 'Dave']
