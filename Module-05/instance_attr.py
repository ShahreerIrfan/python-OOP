class Shop:
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = []
        
    def add_to_cart(self,item):
        self.cart.append(item)
        
    def total_cart_item(self):
        for item in self.cart:
            print(item)
            
buyer1 = Shop("Irfan")
buyer1.add_to_cart('Grori')
buyer1.add_to_cart('Chosma')
buyer1.add_to_cart('Bag')

print(buyer1.cart)          

buyer2 = Shop("Tanvir")
buyer2.add_to_cart('Ganja')
buyer2.add_to_cart('Mod')
buyer2.add_to_cart('Yaba')
print(buyer2.cart)