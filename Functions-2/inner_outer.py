def outer():
    print("Outer function stopped")

    def inner():
        print("inner function stopped")
        inner()

    def login():
        print("Login Success")
        login()
outer()