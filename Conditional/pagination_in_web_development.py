total_items=47
items_per_page=10
total_pages,remaining_items=divmod(total_items,items_per_page)
if remaining_items >0:
    total_items+=1
    print(f"Total pages: {total_pages}")
#output Total pages: 4
'''
Real-World Usage:
    Displaying Search results (e.g.,Google's "page  1 of 5")
    API responses with pagination (e.g.,limit=10 & offset=20)
'''

