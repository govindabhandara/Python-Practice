marks=[36,37,38,39,40]
def add_marks(mark):
    return mark+1

map_obj=map(add_marks,marks)
new_marks=list(map_obj)
print(marks)
print(new_marks)