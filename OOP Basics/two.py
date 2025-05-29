class Account():
    min_bal=500

    def open_Account(self):
        print("Account open")

    def deposit_Amount(self):
        print("Amount Deposited")

a1=Account()

print(a1.min_bal)
a1.open_Account()
a1.deposit_Amount()