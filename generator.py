##generators- iterator

def sq(a):
    for i in range (1,a+1):
        yield i

x=sq(10)
##print (type(x))

for i in x:
    print (i)


for i in x:
    print (i**2)

for i in sq(10):
    print (i**3)
        
