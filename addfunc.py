def add(*args):
    s=0
    for i in args:
        s=s+i
    print (s)
def calc(str):
    print (eval(str))
add(2,3,4,5,6)
calc(input("Expression:"))

