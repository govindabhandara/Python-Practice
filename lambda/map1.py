marks=[35,36,37,38,39,40]
print(list(map(lambda mark:mark+1,marks)))

nums=[2,3,4,5,6]
print(list(map(lambda num:num+1,nums)))

ages=[24,45,34,54]
map_obj=map(lambda age: age+1,ages)
new_age=list(map_obj)
print(new_age)