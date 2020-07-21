def abc(s,l):
    c=0
    for i in l:
        if i==s:
            c=c+1
    if c>0:
        print (s,"is present",c,"times")
        print (f'{s}-->{c}')
    else:
        print("-1")



l=['abc','abc','xyz','efg']
s=input("Enter:")

abc(s,l)


#if s in l:
#   print(l.count(s))--> returns the number of times element is present
