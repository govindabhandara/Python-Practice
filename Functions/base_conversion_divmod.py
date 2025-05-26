def decimal_to_base(n, base):
    digits = []
    while n > 0:
        n, remainder = divmod(n, base)
        digits.append(remainder)
    return digits[::-1] if digits else [0]

print(decimal_to_base(42, 2))  # Output: [1, 0, 1, 0, 1, 0]

