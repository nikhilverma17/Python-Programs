##s="123abc456"
##123456
##s2="-123abc456"
##-123456
##s3="123-abc&456"
##123456

s=input("Enter String")
l=len(s)
l=['0','1','2','3','4','5','6','7','8','9']

if s[0]=="-" and s[1] in l:
    print(s[0],end="")
for i in s:
    if i in l:
        print (i,end="")
