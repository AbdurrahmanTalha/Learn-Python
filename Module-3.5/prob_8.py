n1 = int(input("Please write a number: "))
n2 = int(input("Please write another number: "))


for number in range(n1, n2 + 1):

    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)
