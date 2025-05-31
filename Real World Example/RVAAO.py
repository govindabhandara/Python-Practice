#Retrive the value of an attribute from an object

class Student():
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade

s=Student("Govinda","A")

#Dynamically get the value of 'name'
print(getattr(s,'name'))

#if attribute doesn't exist. return default
print(getattr(s,"age","Not available"))