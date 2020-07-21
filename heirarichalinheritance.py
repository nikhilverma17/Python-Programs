class Vehicle:
    def __init__(self,name,modelno,price):
        self.n=name
        self.m=modelno
        self.p=price


class Bike(Vehicle):
    def __init__(self,name,modelno,price,category):
        Vehicle.__init__(self,name,modelno,price)
        self.c=category


    def dis(self):
        return f"{self.n} {self.m} {self.p} {self.c}"


class Car(Vehicle):
    def __init__(self,name,modelno,price,kind):
        Vehicle.__init__(self,name,modelno,price)
        self.k=kind

        self.n=name

    def dis(self):
        return f"{self.n} {self.m} {self.p} {self.k}"



ob1=Bike('Pulsar','123','50000','Sports')
ob2=Car('XUV','564','1250000','SUV')
print(ob1.dis())
print(ob2.dis())

#print(help(ob1))
