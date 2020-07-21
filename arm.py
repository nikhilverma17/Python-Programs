n=int(input("Number:"))
m=n
s=0
while(n>0):
    t=n%10
    c=t**3
    n=n//10
    s=s+c
print(s)
if (s==m):
    print ("Armstrong")
else:
    print ("Not an armstrong")
