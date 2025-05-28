import csv
fp=open("emp.csv",'r')
scv_obj=csv.reader(fp)
user_list=list(scv_obj)
for user in user_list:
    print(user[3]) # this for email like this we can print other also 
fp.close()
