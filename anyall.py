##any and all
l=[2,3,4,6,8,10]
a=[]
for i in l:
    a.append(i%2==0)
print(all(a))
