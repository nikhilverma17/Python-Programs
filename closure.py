#closures:-function returning func
def power(x):
    def base(a):
        return a**x
    return base

var=power(7)
print(var(4))
