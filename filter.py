l=[2,3,4,1,2,5]

def is_even(a):
    if a%2==0:
        return a
x=list(filter(is_even,l))
print (x)
