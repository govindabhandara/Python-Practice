#Define function student() and show argument names using attributes
class Student():
    def StudentData(student_id,student_name,student_class):
        return f' Student Id:{student_id}\n Student Name:{student_name}\n Class:{student_class}'
student=Student.StudentData('1/102',"Govinda Bhandara",'BSC csit')
print(student)