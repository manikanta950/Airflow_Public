print('Hello' , end="")
a=10
b=11 
print(a)
print(b)
print("hello World" , end="")
print("Today i need to work on to many tasks")

a=13
c='python'
d='mysql'
student_name ='Mani'
Student_Name ='Mani'
studentName ='Mani'
print(a)
print(type(str(c)) , end=",")
print(type(str(a)) , end=",")
print(type(d))
print(student_name)
print(Student_Name)
print(studentName)


"""
print('Hello')
a=10
b=11 
print(a)
print(b)
print("hello World")
print("Today i need to work on to many tasks")

"""


"""
variables
"""

## variables
a=10
emp_name ="bob"
##old_method

"""
print("a value is:",10)
print(a)
print(b)

##traditionmethod
print("Emp name is:" + emp_name)

## current we need to use
print(f"Emp name is:{emp_name}")


## input we need to give
emp_name1 = input("Enter Your name:")
emp_id = input("Please enter your id:")
emp_number = input("Please enter you number :")
print(f"Emp name is : {emp_name1}")
print(f"Emp id is :{emp_id}")
print(f"Emp number is :{emp_number}")


"""

## problem with input is it will take it as a string default
## when we try to add it will give error
## now we need to give int as input in there
## eval function will automatically it will indentify the data type
"""
num1 = eval(input("Enter your num :"))
print(num1)
print(f"Your num is : {num1}")
"""

"""

str1 = "I said i 'll not attend python sessions"
print(str1)

str2 = 'hi \'there me'
print(str2)

"""

##indexing
##slicing

x="Python Script"
print(x)
print(len(x))
print(x[0:3])
print(x[0:7])
print(x[0:-1]) ##removes last one
print(x[::-2]) ## reverse the string
print(x[0:-2:2])

## mutable nd immutable in python is most imp one

x='python'
print(x)
print(id(x))
