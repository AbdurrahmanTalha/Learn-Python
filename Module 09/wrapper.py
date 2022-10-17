# def do_something(x, y):
#     print(x, y)
#     return

# do_something(10, 20)

def do_something(work):
    print("Start the work")
    work()
    print("done with work")


def practice_coding():
    print("I'm practicing python")


do_something(practice_coding)
