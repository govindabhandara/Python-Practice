def decimal_points(n,base):
    digits=[]
    while n>0:
        n,remainder =divmod(n,base)
        digits.append(remainder)
    return digits[::-1] if digits else[0]
print(decimal_points(42,2))
