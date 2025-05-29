class Account():
    def __init__(self,id,name,bal):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=bal
a1=Account(101,"rahul",45000)
a2=Account(102,"govinda",45303)
print(a1.__dict__)
print(a2.__dict__)