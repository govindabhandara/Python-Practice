command = input("Enter command (start/stop/restart): ").lower()

match command:
    case "start":
        print("System started.")
    case "stop":
        print("System stopped.")
    case "restart":
        print("System restarted.")
    case _:
        print("Unknown command!")