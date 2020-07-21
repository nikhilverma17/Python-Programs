def add():
    return a+b

def sub():
    return a-b

def mul():
    return a*b

ch=input("Enter choice:")
a=int(input("Number 1:"))
b=int(input("Number 2:"))
d={'add':add(),'sub':sub(),'mul':mul()}
if ch in d:
    print (d[ch])

