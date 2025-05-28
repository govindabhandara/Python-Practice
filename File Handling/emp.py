import csv
fp=open("emp.csv",'r')
csv_obj=csv.reader(fp)
user_list=list(csv_obj)
for user in user_list:
    print(user)
fp.close()