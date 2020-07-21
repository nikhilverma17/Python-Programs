##inheritance

class Phone:
    def __init__(self,brand,modelno,price):
        self.b=brand
        self._m=modelno ##protected
        self.__p=price  ##private  ##name mangling

    def fullspecs(self):
        return f"{self.b} {self._m} and price is {self._Phone__p}"


    def __str__(self):
        return self.b


    def __repr__(self): ##for complete object representation
        return f"\'{self.b}\',\'{self._m}\',{self._Phone__p}"


    def __len__(self):
        return len(f"{self.b}")


    def __add__(self,other):
        return self._Phone__p + other._Phone__p
    def __mul__(self,other):
        return self._Phone__p * other._Phone__p



p1=Phone('Nokia','3300',1500)
p2=Phone('Samsung','Guru',1200)
##print (p1.__dict__)
##print (p1._Phone__p)
##print (p1.fullspecs())

print (p1)
print (repr(p1))
print (len(p1))
print (p1+p2)
print (p1*p2)
