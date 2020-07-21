##Decorators

def outer_func(any_func):
    def inner_func():
        print(any_func())
        print("This is decorator")
    return inner_func

def a():
    return "hello from a"

var = outer_func(a)
var()
def b():
    return "hello from b"
