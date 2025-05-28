sales=[250,310,180,400,290]
total=0
for sale in sales:
    total+= sale
average=total/len(sales)
print(f"Average sales:{average}")