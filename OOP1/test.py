class Test():
    def __init__(self):
        self.a=10

    def m1(self):
        self.b=20

    @classmethod
    def m2(self):
        self.c=30

    @staticmethod
    def m3(self):
        self.d=40

t1=Test()
t1.e=50

t2=Test()
t2.m2()
t2.m1()

print(t1.__dict__)
print(t2.__dict__)