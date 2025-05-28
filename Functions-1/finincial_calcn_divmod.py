def split_money(amount):
    hundreds,remainder=divmod(amount,100)
    fifties,remainder=divmod(remainder,50)
    twenties,remainder=divmod(remainder,20)
    ten,remainder=divmod(remainder,10)
    return hundreds, fifties, twenties,ten

h,f,tw,te=split_money(380)
print(f"Rs 100:{h},Rs 50:{f},Rs 20:{tw},Rs 10:{te}")
#output: Rs 100:3,Rs 50:1,Rs 20:1,Rs 10:1

'''
Real-World Usage
    ATM cash dispenser logic,
    Splitting bills among friends (e.g, Rs87 split into Rs50 + Rs20 + Rs10 + Rs7).
'''