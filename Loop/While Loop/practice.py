password="govinda"
attempts=3
sucess=False
while attempts >0 and not sucess:
    guess=input(f"enter password {attempts} left")
    if guess==password:
        sucess=True
        print("Access Granted")
    else:
        attempts-=1
        print("incorrect password")

        if not sucess:
            print("Access denied. No attempts left")