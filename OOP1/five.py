class Account():
    def __init__(self,a,b):
        self.id=a
        self.name=b
    def display(self):
        print("faculty id",self.id)
        print("faculty name",self.name)
a1=Account(1,"romeo")
a2=Account(2,"Milan")
a1.display()
a2.display()