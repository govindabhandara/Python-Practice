def page_check(func):
    def inner(name,login):
        if login==False:
            print("try again")
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
home_page("govinda",False)
order_page("rahul",False)
payment_page("milan",True)