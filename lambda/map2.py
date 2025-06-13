enames=["rahul",'sonia','priya']
# def changecase(name):
#     return name.upper()
# new_names=list(map(changecase,enames))
# print(new_names)
print(list(map(lambda ename: ename.upper(),enames)))
