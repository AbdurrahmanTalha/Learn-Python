numbers = [12, 45, 65, 23, 89, 78, 11]
nums = {12, 45, 56, 45, 12, 89}
numbers_tuple = 12, 45, 56, 45, 12, 89, 53
marks = {"physics": 12, "chemistry": 45, "math": 56}
sum = 0

# for i in numbers:
#     sum += i

# for i in nums:
#     sum+= i;


# for i in numbers_tuple:
#     sum += i

# for i in marks:
#     value = marks[i]
#     sum += value

for subject, mark in marks.items():
    sum+= mark

print(sum)
