def divide(a,b):
    try:
        c=a/b

    except ZeroDivisionError as e:
        print(e)


    except NameError as e:
        print(e)



    except Exception as e:
        print(e)
    
    
    else:
        print (c)




divide(6,3)
divide(6,0)
divide(6,'3')
divide(6,x)##error occured at calling
