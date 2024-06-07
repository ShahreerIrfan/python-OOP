class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []
    
    def add_to_cart(self,item,price,qunatity):
        products = {'item':item,'price':price,'quantity':qunatity}
        
        self.cart.append(products)
    
    def get_cart(self):
        return self.cart
    
    total = 0
    
    def checkout(self,amount):
        for item in self.cart:
            self.total+=item['price'] * item['quantity']
        print(f'Yur total bill is: {self.total}')
        if amount<self.total:
            print(f'Not much ammount you given {amount} taka but your bill is {self.total} taka')
        else:
            print(f'You paid {amount} taka and you will get back {amount-self.total} taka')
        
        
        
        
s1 = Shopping("Irfan")
s1.add_to_cart('Jama',200,3)
s1.add_to_cart('Kapor',201,5)

cartt = s1.get_cart()

s1.checkout(1608)

# print(cartt)
