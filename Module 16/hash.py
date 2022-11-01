import hashlib

# Rtrams
# smart
# Splkyoanr

email = "abdurrahmantalha.dev@gmail.com"
pwd = "CharsOnTableWith3Legs"
pwd_encode = pwd.encode()
pwd_hash = hashlib.md5(pwd_encode).hexdigest()

your_email = "abdurrahmantalha.dev@gmail.com"
your_password = "CharsOnTableWith3Legs"

your_password_encode = your_password.encode()
your_password_hashed = hashlib.md5(your_password_encode).hexdigest()

if your_email == email and your_password_hashed == pwd_hash:
    print("right user")
else:
    print("Wrong user")
hacker_email = "abdurrahmantalha.dev@gmail.com"
hacker_psw = "efb4c35b73b4a69598cd9506998135ba"


