##docstring

def outer_func(func):
    def inner_func(*args,**kwargs):
        print(f'You are calling {func.__name__} function')
        print(func.__doc__)
        print(func(*args,**kwargs))
    return inner_func


@outer_func

def add(a,b):
    '''Adds two nos'''
    return a+b

add(4,5)


@outer_func

def sub(a,b):
    '''Subtract two nos'''
    return a-b

sub(5,6)
