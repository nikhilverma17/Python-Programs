def only_dtype_allow(dtype):
    def outer(func):
        def inner_func(*args):
            a=[]
            for i in args:
                a.append(type(i)==dtype)
            if (all(a)==True):
                  func(*args)
            else:
                print ("Invalid Argument")
        return inner_func
    return outer



@only_dtype_allow(int)
def add_all(*args):
    s=0
    for i in args:
        s+=i
    print (s)

add_all(2,3,4,5,1,9,10)

@only_dtype_allow(str)
def add_all(*args):
    s=''
    for i in args:
        s+=i
    print (s)

add_all('a','b','c')
