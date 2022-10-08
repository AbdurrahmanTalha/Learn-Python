st = input("Please write something: ")

new_string = ""

for char in st:
    if (char.isupper()):
        new_string += char.lower()
    else:
        new_string += char.upper()

print(new_string)
