def add(a, b):
    sum = a + b
    print(sum)


def deduct(x, y):
    result = x-y
    return result


class Phone:
    color = "Black"
    features = ['camera', 'water-proof', 'can be used as a hammer']

    def call(self):
        print("ring ring")

    def send_sms(self, text, number):
        sms = f'sending sms: {text} to: {number}'
        return sms


my_phone = Phone()

sms = my_phone.send_sms("ELLo", '01325105101')
print(sms)
