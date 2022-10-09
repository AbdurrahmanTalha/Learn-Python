# def square(x):
#     return x * x

square = lambda x: x * x
add = lambda x, y: x + y

result = square(6)
sum = add(50, 100)

print(sum)

numbers = [12, 45, 65, 23, 89, 78, 11]


def double_it(x):
    return x * 2


double_it2 = lambda x: x * 2

doubled_numbers = map(lambda x: x * 2, numbers)
square_numbers = map(lambda x: x * x, numbers)

bigger_number = filter(lambda num: num > 50, numbers);

print(numbers)
print(list(bigger_number))
