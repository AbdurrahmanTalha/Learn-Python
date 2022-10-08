password = input("Please write a password: ")

uppercase, lowercase, digits, symbols = 0, 0, 0, 0

for i in password:
    if i.isupper():
        uppercase += 1
    elif i.islower():
        lowercase += 1
    elif i.isdigit():
        digits += 1
    elif i.isalpha() == False:
        symbols += 1

print(f"Uppercase {uppercase}")
print(f"Lowercase {lowercase}")
print(f"Digits {digits}")
print(f"Symbols {symbols}")
