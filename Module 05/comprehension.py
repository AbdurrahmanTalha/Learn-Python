nums = [12, 45, 65, 23, 89, 78, 11]

odd_numbers = []

for i in nums:
    if (i % 2 == 1):
        odd_numbers.append(i)

# print(odd_numbers)
odd_numbers2 = [i for i in nums if i % 2 == 1]
print(odd_numbers2)
