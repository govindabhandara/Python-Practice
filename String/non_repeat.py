# Find the first non-repeating character in a string.
def first_non_repeating_char(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for char in s:
        if freq[char] == 1:
            return char
    return None

print(first_non_repeating_char("swiss"))  # Output: 'w'