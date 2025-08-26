"""
import re

from IPython.lib.pretty import Printable

with open ('test1.py','r') as fo:
    for i in fo:
        #if re.search('python',i):
        #if re.search('[6-9][0-9]{9}',i):
            print(i)



print("hi")
def f1():
    print("hi")
    print("Day2 training")
f1()
print("bye")
f1()
def f2():
    print("2nd function")
f2()

def cal(x,y):
    print(x,y)
    print(x+y)
    print(x*y)

cal(1,2)
cal(5,2)

a=10
def test():
    b=20
    print(a,b)
    print("i am in test" , a)
    print("i am in test", b)

def test2():
    c=30
    print(c)

def f1(x,y):
    print(x,y)
    return (x+y)
k=f1(10,20)
print(k)


def introuduce(name , city , job):
    print(f" my name is {name} , i am from {city}. I am an {job}.")


introuduce(name="Babu" , city="Hyderabad" ,job="AI COACH")

def f1(x,y,op='+'):
    if op=='+':
        print(x+y)
    elif op==-'-'


 def introuduce_kwargs(**kwargs)
     for key, value in kwargs.items():

"""




##print("Day-3_Started")
## functions
## Built in functions
## import builtins
##a[0-9]c ---> will accept a7c only 3 digits
##a[0-9]+c-----> will accept more than 3 digits in 0-9 sector
##functions
##aruguments
##with arguments , without arguments
##function call
##scope of variables
## global and local
##return function
##Modules
## all the 3rd party modules can be accessed (www.pypi.org) (mysql , sybase , Mssql)
## how to use module properties
## if we dont need complete module we can import specific one property