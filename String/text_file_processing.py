# Log file analyzer
with open("server.log", "r") as file:
    for line in file:
        if "ERROR" in line:
            print(f"Found error: {line[:100]}...")  # Show first 100 chars