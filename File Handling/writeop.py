#read "n" of employee and data from user, print in emp.csv
import csv
fp=open("abc.csv",'w',newline="")
csv_obj=csv.writer(fp)
csv_obj.writerow(["id","first_name","ip_address"])

n=int(input("number of employee"))
for i in range(n):
    id=input("enter id")
    first_name=input("enter first_name")
    ip_address=input("ip_address")

    csv_obj.writerow([id,first_name,ip_address])

fp.close()
