##laptop
##brand,modelno,price(10%disc)
class Laptop:
    dis=(0.10)
    def __init__(self,brand,modelno,price):
        self.b=brand
        self.m=modelno
        self.p=price
    def discount(self):
        return (self.p-self.dis*self.p)
ob1=Laptop('Lenevo','Ideapad',40000)
ob2=Laptop('HP','Pavilion',45000)
ob3=Laptop('Asus','Razor',50000)

ob2.dis=0.50
print (ob1.discount())
print (ob2.discount())
print (ob3.discount())
