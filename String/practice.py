def is_palindrome(p):
    p=p.lower().replace("","")
    return p[::-1]
print(is_palindrome("fuck"))