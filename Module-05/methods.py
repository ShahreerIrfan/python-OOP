class Phone:
    price = 2000
    color = 'Blue'
    brand = 'Samsung'
    featute = ['Camera','Speaker','Hammer']
    
    def calll(self):
        print('Calling a person')
        
    def send_sms(self,phone,message):
        text = f'sending SMS to {phone} and message is: {message}'
        return text
    
p1 = Phone()

print(p1.featute[0])

p1.calll()

print(p1.send_sms('Samsung','how are you today'))