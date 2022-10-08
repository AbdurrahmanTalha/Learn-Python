stringNumber = input("Please write a number: ")


number = type(int(stringNumber))

for i in range(10):
    for x in range(i):
        print(f"{x} ", end="")
    print("\n")
