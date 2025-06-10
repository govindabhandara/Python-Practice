def create_profile(**details):
    print("User Profile:")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")

create_profile(name="Milan", age=25, country="Nepal", language="Python")
