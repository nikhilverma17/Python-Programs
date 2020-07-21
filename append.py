##f=open('new.txt','a')
##f.write("Hello world!!!")
##f.close()

##with block-does not open corrupt file, closes itself


with open('pqr.txt','r') as rf:
    with open('abc.txt','a') as wf:
        wf.write(rf.read())
