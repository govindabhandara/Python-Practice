username=input("enter username: ").strip()
email=input("enter email: ").lower()
if "@" not in email or "." not in email:
    print("invalid format")