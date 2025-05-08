while True:
    user_input = input("Enter a number between 1 and 10: ")
    if user_input.isdigit() and 1 <= int(user_input) <= 10:
        break
    print("Invalid input. Try again.")
print(f"You entered: {user_input}")