
def outer(func):
    def inner_func(*args):
        a=[]
        for i in args:
            a.append(type(i)==int)
        if (all(a)==True):
            func(*args)
        else:
            print ("Input correct numbers")
    return inner_func



@outer
def add_all(*args):
    s=0
    for i in args:
        s+=i
    print (s)

add_all(2,3,4,5,1,9,10)
