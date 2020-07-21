##Exception handling
##1- try
##2- except
##3- else
##4- finally
while True:
    try:
        age=int(input("Enter your age:"))
    except ValueError as e:
        print  (e)

    except Exception as e:##this block must be defined after all exceptions
        print(e)
    else:
        if age>18:
            print ("eligible")
            break
        else:
            print ("not eligible")
            break
    finally:
        print ("Successfully Done")
