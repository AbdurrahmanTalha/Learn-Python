x = { 'a' : 1, 'b' :  2, 'c': 3, 'd': 4}
output= []

def create_list(x, output):
   for key, value in x.items():
    output.append(key)
    output.append(value)
    

    
create_list(x, output);
print(output)
d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}
output_2 = []

create_list(d, output_2);

print(output_2)
