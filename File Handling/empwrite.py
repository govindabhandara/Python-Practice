import csv
fp=open("user.csv",'w',newline="")
csv_obj=csv.writer(fp)
csv_obj.writerow(["username","email","location"])
csv_obj.writerow(["Govinda","govinda@gmail.com","chennai"])
csv_obj.writerow(["surendra","surendra@gmail.com","Banglore"])
fp.close()