def clean_string(text):
    output = "";
    
    for l in text :
        if(l.isalpha()):
            output+=l;

    return output;


s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output)
