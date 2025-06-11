def outer():
    print("Outer function")

    def inner():
        print("inner function")
    return inner
result=outer()
result()
result()