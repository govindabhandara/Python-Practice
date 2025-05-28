username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "secret123":
    print("Access granted!")
elif username == "guest" and password == "welcome":
    print("Limited access.")
else:
    print("Invalid credentials!")