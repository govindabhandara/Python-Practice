# Check if a string is a palindrome (reads the same forwards and backwards).
def is_palindrome(s):
    s = s.lower().replace("","")
    return s[::-1]
print(is_palindrome("govinda"))