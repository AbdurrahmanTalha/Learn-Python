replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."



def replace_word(lst, s):
    it = iter(lst)
    
    dictionary = dict(zip(it, it))
    keys = list(dictionary.keys())
    
    broken_str = s.split(" ");
    
    for k in keys:
        index = broken_str.index(k)
        broken_str[index] = dictionary.get(k);
    
    output_str = "";
    
    for i in broken_str:
        output_str+= i + " ";
        
    return output_str;


final_string = replace_word(replace_with, s)
print(final_string)
