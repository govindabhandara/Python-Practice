def outer():
    print("Revanth is a boy")

    def inner():
        print("He go to job.")
    return inner 
result=outer()
result()