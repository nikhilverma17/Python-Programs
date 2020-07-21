##time decorator
import time

t1=time.time()
name=input('Enter name')
age=input('Enter age')

print (f' Your name is {name} and age is {age}')
print ("hello")

t2=time.time()

print(f'Time took if {t2-t1} seconds')

