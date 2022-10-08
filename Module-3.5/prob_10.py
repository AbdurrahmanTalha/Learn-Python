stringNumber = input("Please write a Number: ")

number = int(stringNumber)

i = 1

while i <= number:

    x = 0
    while x < i:
        print("*", end=" ")
        x += 1
    print("")
    i += 1

i = number
while i > 0:

    x = 0
    while x < i:
        print("*", end=" ")
        x += 1
    print("")
    i -= 1
