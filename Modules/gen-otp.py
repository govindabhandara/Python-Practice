from random import randint,choices,random
gen_otp=[]
for x in range(4):
    gen_otp.append(randint(0,9))
    print(choices(gen_otp))