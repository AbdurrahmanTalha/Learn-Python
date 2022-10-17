def do_something():
    print("inside of the function 'do_something'")

    def inner_function():
        print("Inside the inner function")
    inner_function()


do_something()
