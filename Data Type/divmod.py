a=10
b=3
print(divmod(a,b))  #Output: (3, 1)

c,d=10.5,3
print(divmod(c,d)) #Output: (3.0,1.5)

e,f=-10,3
print(divmod(e,f))  #Output (-4, 2)

total_secs=7562
hours,remaining_sec=divmod(total_secs,3600)
minutes,seconds=divmod(remaining_sec,60)
print(f"{hours} hours, {minutes} minutes,{seconds},seconds")
#Output 2 hours, 6 minutes,2,seconds

#Implement Pagination
total_items=23
items_per_page=5
full_pages,remaining_items=divmod(total_items,items_per_page)
print(f"Full pages:{full_pages},Remaining items:{remaining_items}")
#Output Full pages:4,Remaining items:3

