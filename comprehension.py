##comprehension

l=[i for i in range(1,11)]
print (l)

l1=[i for i in range(1,11) if i%2==0 ]
print (l1)
d={i:i**3 for i in range(1,11)}
print (d)

s={i for i in range(1,15,2)}
print (s)

g=(i for i in range(2,20,2)) ##generator
print (g)
for i in g:
    print (i, end=" ")

