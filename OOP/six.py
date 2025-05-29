class Aaccount():
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_amount=amount
    def open_Account(self):
        print("Account opened")
a1=Aaccount(1,"govinda",5000)
a2=Aaccount(2,"Roma",6000)
