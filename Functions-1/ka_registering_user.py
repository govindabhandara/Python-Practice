def register_user(name,email,age=None):
    print(f"Name: {name}")
    print(f"Email: {email}")
    if age:
        print(f"age : {age}")
register_user("Govinda Bhandara","gvndbhandara@gmail.com",age=26 )