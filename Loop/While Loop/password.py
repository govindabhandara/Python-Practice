PASSWORD = "secret"
attempts = 3
success = False

while attempts > 0 and not success:
    guess = input(f"Enter password ({attempts} attempts left): ")
    if guess == PASSWORD:
        success = True
        print("Access granted!")
    else:
        attempts -= 1
        print("Incorrect password.")

if not success:
    print("Access denied. No attempts left.") 