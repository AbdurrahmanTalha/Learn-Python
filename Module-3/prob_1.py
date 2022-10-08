
# * Clean the data and get a String output 'a e i o u'

data = "aNtEriOur\n\t>>"

new_data = data.lower()
output_data = ""


for characters in new_data:
    if (characters == "a") or (characters == "e") or (characters == "i") or (characters == "o") or (characters == "u"):
        output_data += characters + " "

print(output_data)
