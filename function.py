##function

def add(a,b):
    print(a+b)

add(3,5)

def add1(*args):
    s=0
    for i in args:
        s+=i
    print (s)
add1(1,2,3,4,5)

def add2(a,*args,b=10):
    s2=a+b
    for i in args:
        s2+=i
    print(s2)
    print(a,b)

add2(10,5,5)

def add3():
    d=2
    e=3
    print(d+e)

add3()
