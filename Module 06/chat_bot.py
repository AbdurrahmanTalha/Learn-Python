""" Chatbot.

    Steps: 
    1. Input/listening
    2. Process/Decide
    3. Output/Talk bACK
"""

greet_words = ["hi", "hello", "yoo"]
bye_words = ["cya", "bye", "good bye", "assalamualikum assalam"]
bad_words = ["shit", "picchi", "pocha"]


def listen():
    return input("Say something: ")


def decide(command):
    # print(command)
    command = command.lower()
    broken_words = command.split(" ")
    # print(broken_words)

    for w in broken_words:
        if (w in greet_words):
            print("yoo")
            break
        elif (w in bye_words):
            print("cyaaa")
            break
        elif (w in bad_words):
            print("chill bro")
            break


def talk_back():
    pass


while True:
    command = listen()
    decide(command)
