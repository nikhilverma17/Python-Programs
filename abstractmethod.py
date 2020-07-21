##Abstract Method-

class Animal:
    def __init__(self,name):
        self.n=name

    def sound(self):
        raise NotImplementedError('You have to define this method in sub class')


class Cat(Animal):
    def __init__(self,name,sound):
        Animal.__init__(self,name)
        self.s=sound

    def sound(self):
        return f"{self.n} does {self.s}"


class Dog(Animal):
    def __init__(self,name,sound):
        Animal.__init__(self,name)
        self.s=sound


    def sound(self):
        return f"{self.n} does {self.s}"

objc=Cat('Liza','meow meow')
objd=Dog('Tiger', 'wuff wuff')

print(objc.sound())
print(objd.sound())


