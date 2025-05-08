#for loop with finding indices for  specific items
fruits=['apple','banana','cherry','mango']
target='banana'
for i, fruit in enumerate (fruits, start=1):
    if fruit=='banana':
        print(f"{target} found in {i}")