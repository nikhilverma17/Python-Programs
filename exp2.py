##s="123abc456"
##123456
##s2="-123abc456"
##-123456
##s3="123-abc&456"
##123456

s=input("Enter String")
l=len(s)
st=''
if s[0]=="-":
    st+=s[0]
for i in s:
    if ord(i)<58 and ord (i)>46:
        st+=i


print (st)
