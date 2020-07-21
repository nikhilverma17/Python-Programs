##How to raise an error-

##Custom exceptions-user created exception
class LessCharacters(ValueError):
    pass
def check(a):
    if len(a)<5:
        raise LessCharacters('Less than 5 characters')

    else:
        print (f"Hello {a}")




    
name=input("Enter name:")
check(name)
