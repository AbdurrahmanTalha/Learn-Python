
# * Encrypt the following code so no one can get your Strategy

data = "rocket fire"
shift = 1

output = ""

for characters in data:
    output += chr((ord(characters) + shift - 97) % 26 + 97)

print(output)
