import csv
fp=open("emp.csv",'w',newline="")
csv_obj=csv.writer(fp)
csv_obj.writerow(["eid","ename","esal"])
n=int(input("enter no. of employee"))
for i in range(n):
    eid=int(input("enter eid"))
    ename=input("enter ename")
    esal=float(input("enter esal"))

    csv_obj.writerow([eid,ename,esal])
fp.close()