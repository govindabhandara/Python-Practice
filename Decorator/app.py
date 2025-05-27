def page_check(func):
    def inner(name,login):
        if login==False:
            print("Please Try to Login")
        else:
            return func(name,login)
    return inner

def home_page(name,login):
    print("home_page",name)
@page_check
def order_page(name,login):
    print("order_page",name)

@page_check
def payment_page(name,login):
    print("payment_page",name)

home_page("rahul",True)
order_page("sonia",False)
payment_page("priyanka",False)