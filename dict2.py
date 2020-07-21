d={1:'odd',2:'even',3:'odd',4:'even',5:'odd',6:'even',7:'odd',8:'even',9:'odd',10:'even',}
for i in range(1,len(d)):
    print (d[i])

num=int(input("No-"))
print (d[num])

d2={'Name':'Saif','Course':'Python','Age':'26'}
s=input("Choice:")
if s in d2:
    print (d2[s])
else:
    print ("Wrong input")
