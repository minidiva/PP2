x = 5 #INT
y = "John" #STRING

#Casting

x = int(4)
y = str("fourty eight")
z = float(3)

print(type(x))

# '' is the same as "" and even '''

#Names

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John" #OK

2myvar = "John"
my-var = "John"
my var = "John" #Not OK

#styles 

firstSecondThird = '2324234'
FirstSecondThird = '234234'
first_second_third = '786543'

#many variable

x, y, z = "Orange", "Banana", "Cherry" #OK

x = y = z = "Orange" #OK

fruits = ['a', 'b', 'c']
x,y,z = fruits #OK
print(x)
print(y)
print(z) 

print(x + y) #output void function
print(x, y)

x = "awesome" #global var

def myfunc():
  x = "fanta" #local var
  print("Python is " + x)

myfunc()

#global can be used to make global variables explicitly