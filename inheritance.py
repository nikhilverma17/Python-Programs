##inheritance

class Phone:
    def __init__(self,brand,modelno,price):
        self.b=brand
        self.m=modelno
        self.p=price

    def fullspecs(self):
        return f"{self.b} {self.m} and price is {self.p}"



class Smartphone(Phone):
    def __init__(self,brand,modelno,price, camera):
        Phone.__init__(self,brand,modelno,price)
        self.c=camera

    def fullspecs(self):
        return f"{self.b} {self.m} and price is {self.p} and camera is {self.c}"

class Flagshipphone(Smartphone):
    def __init__(self,brand,modelno,price,camera,RAM):
        Smartphone.__init__(self,brand,modelno,price,camera)
        self.r=RAM
    def fullspecs(self):
        return f"{self.b} {self.m} and price is {self.p} and camera is {self.c} and RAM is {self.r}"


p1=Phone('Nokia','3300',1500)
p2=Smartphone('Redmi','Mi7pro',12000,'64mp')
p3=Flagshipphone('Asus','ROG',30000,'120mp','8GB')

print (p1.fullspecs())
print (p2.fullspecs())
print (p3.fullspecs())


print (help(p3))
print (Flagshipphone.__mro__)
