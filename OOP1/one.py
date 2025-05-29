class Account():
    min_bal=500
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_amount=amount

    def deposit_amount(self,amount):
        self.acc_amount+=amount

    def withdraw_amount(self,amount):
        self.acc_amount-=amount

a1=Account(101,"Govinda",50000)
a2=Account(102,"Rahul",60000)
print(a1.__dict__)
print(a2.__dict__)
a1.deposit_amount(5000)
a2.deposit_amount(5000)
print(a1.__dict__)
print(a2.__dict__)
a1.withdraw_amount(10000)
a2.withdraw_amount(10000)
print(a1.__dict__)
print(a2.__dict__)
