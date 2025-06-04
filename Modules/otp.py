import random
def gen_otp():
    return ''.join(str(random.randint(0,9)) for _ in range(4))

otp=gen_otp()
print(f"Generated otp is {otp}")

