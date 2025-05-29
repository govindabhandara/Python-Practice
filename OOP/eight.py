class Account():
    def __init__(self,id,name,bal):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=bal
    def deposit_amount(self,amount):
        self.acc_bal+=amount

    def withdraw_amount(self,amount):
        self.acc_bal-=amount

a1=Account(101,"Govinda",50000)
a2=Account(102,"Rahul",60000)
a1.deposit_amount(2000)
a2.deposit_amount(3000)
print(a1.__dict__)
print(a2.__dict__)
a1.withdraw_amount(10000)
a2.withdraw_amount(10000)
print(a1.__dict__)
print(a2.__dict__)