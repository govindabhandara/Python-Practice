while True:
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("You chose Option 1")
    elif choice == "2":
        print("You chose Option 2")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice")