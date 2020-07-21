##Decorators

def outer_func(any_func):
    def inner_func(*args,**kwargs):
        print(any_func(*args,**kwargs))
        print("This is decorator")
    return inner_func



@outer_func
def a(x,y):
    return x+y
a(5,6)
##var = outer_func(a)
##var(6,7)
@outer_func
def b():
    return "hello from b"
b()
##var = outer_func(b)
##var()
