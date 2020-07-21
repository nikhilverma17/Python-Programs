class Circle:
    pi=3.14##class variable
    def __init__(self,radius):
        self.r=radius
    def area(self):
        return self.pi*self.r*self.r
    def cir(self):
        return 2*self.pi*self.r
c=Circle(5)
print("Area=", c.area())
print("Circumference=", c.cir())
