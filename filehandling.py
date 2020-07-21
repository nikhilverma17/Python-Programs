#File handling
#modes (4)
#1. read mode denoted as 'r'
#2. write mode denoted as 'w'
#3. append mode denoted as 'a' (creates new file if not present)
#4. read write mode denoted as 'r+'

##f=open('sample.txt','r')
##print(f.read())
##f.seek(0)
##print (f.read())
##print(f.tell())

##print(f.readline(),end="")
##print(f.readline())
##s=f.readlines()
##print (s[1])
####for i in f.readlines():
####    print (i,end="")
##for i in f.readlines()[1:2]:
##    print (i,end="")

f=open('sample.txt','w')
for i in range (6):
    s=input ("Enter:")
    f.write(s+'\n')
f.close()
