# marks=[36,37,38,39,40]
# new_marks=[]
# for mark in marks:
#     new_marks.append(mark+1)
# print(new_marks)

marks=[36,37,38,39,40]
new_marks=[]
def add_marks(mark):
    return mark+1
for mark in marks:
    new_marks.append(add_marks(mark))
print(new_marks)