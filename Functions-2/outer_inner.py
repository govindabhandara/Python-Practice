def outer():
    print("outer function")

    def inner():
        print("Inner function")

    inner()
    inner()
outer()