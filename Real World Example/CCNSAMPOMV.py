#create a class  named student with arrtibutes,modify, and print original and modified values.
class Student:
    student_name='Govinda Bhandara'
    marks=93

print((f"Student Name:{getattr(Student,'student_name')}"))
print((f"marks:{getattr(Student,'marks')}"))
setattr(Student,'student_name',"Govinda Bhandara")
setattr(Student,'marks',95)
print((f"Student Name:{getattr(Student,'student_name')}"))
print((f"marks:{getattr(Student,'marks')}"))