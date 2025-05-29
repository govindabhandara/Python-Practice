class faculty():
    def  __init__(self):
        self.id=int(input("enter faculty id"))
        self.name=input("enter name")
        self.salary=float(input("enter salary"))

    def display(self):
        print("facult id:",self.id)
        print("Facult name:",self.name)
        print("faculty salary",self.salary)

a=faculty()
a.display()