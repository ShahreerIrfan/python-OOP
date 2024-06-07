class Phone:
    
    def __init__(self,owner,brand,price):
        self.owener = owner
        self.brand = brand
        self.price = price
    
    def displayInfo(self):
        print(self.owener)
        print(self.price)
        print(self.brand)
    
    made_in = 'China'
    
    def send_sms(self,phone,message):
        text =  f'sending sms to {phone} and message is: {message}'
        print(text)
        
p1 = Phone('Irfan','Xiaomi',63000)

p1.displayInfo()
p1.send_sms(34343434,'Missy I missed to miss you')