import pyjokes

print("Type Yes if you want to hear a Joke and No if not");

while True: 
    s = input("Say something: ");
    
    if s.lower() == 'yes':
        print(pyjokes.get_joke());    
    elif s.lower() == 'no':
        print("ok");
        continue
