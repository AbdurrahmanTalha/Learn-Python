a = ['Oh,', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

def create_new_string(s, a):
    broken_str = s.split(" ");
    output_str = ""
    
    for i in a:
        index = broken_str.index(i);
        output_str += broken_str[index+1] + " ";
    
    return output_str
            
    
output= create_new_string(s, a);
print(output)
