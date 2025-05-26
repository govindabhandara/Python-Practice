# Form validation
username=input("enter username")
email=input("enter email")
is_valid = (len(username) >= 4) and ("@" in email)
print(is_valid)
