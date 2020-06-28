class product:
    deliveryCharge=50
    def __init__(self,nam="Teddy Bear", prc=500):
        self.name=nam
        self.price=prc
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price + product.deliveryCharge
    def __str__(self):
        return "The {} will cost you Rs.{}.".format(self.get_name(),self.get_price())
class gift(product):
    def __init__(self,nam,prc,wrapcharge):
        super().__init__(nam, prc)
        self.wch=wrapcharge
    def get_price(self):
        return self.price + product.deliveryCharge + self.wch

    
p1=gift("Teddy",500,100)
p1.__str__()
