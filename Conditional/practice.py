command=input("Enter your Command").lower()

match command:
    case "start":
        print("system Started")
    case "stop":
        print("system stopped")
    case "restart":
        print("system restarted")
    case _:
        print("unknown command")
        
