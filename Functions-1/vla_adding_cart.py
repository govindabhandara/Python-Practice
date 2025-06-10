# Adding any number of items to a cart
def add_to_cart(*items):
    print("Items added to cart")
    for item in items:
        print("-",item)
add_to_cart("laptop","Mouse","keyboard")
