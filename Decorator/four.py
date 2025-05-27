def user_uppercase(func):
    def inner():
        msg=func()
        return msg.upper()
    return inner
@user_uppercase
def print_user():
    return "Hi,Govinda Bhandara"
print(print_user())