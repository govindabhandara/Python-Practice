#create an instance of a class  and display its namespace
class Student:
    def __init__(self,student_id,student_name,class_name):
        self.student_id=student_id
        self.student_name=student_name
        self.class_name=class_name
student=Student('1/201',"Govinda Bhandara","BSCCSIT")
print(student.__dict__)