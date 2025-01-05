
a1=1
B1=2
_c1=3
print( a1, B1, _c1)
print( "This is type of a1", type( a1))


print("Numeric Data Type= ",3," ",7.83," ",6+2j)
print("String Data Type= ","This is Python String",'And we are learning Programming')
print("Boolean Data Type= ",True)
print("Sequenced Data Type= ",[12,15,16,18]," ",(11,14,17,19))
print("Dictionary= ", {"name": "Rohan", "age": 25, "Student": True, "Stream": "MBA"})

string = "15"
number = 7
string_number = int(string) 
sum= number + string_number
print("The Sum of both the numbers is: ", sum)

a = 7
print(type(a))

b = 3.0
print(type(b))

# Python converts c to float 
c = a + b
print(c)
print(type(c))

# Global and Local Variables
# Variables that are defined inside a function body have a local scope, and those defined outside have a global scope

a = 1
def x1():
	print('Inside x1() : ', a)
def x2():
	a = 2
	print('Inside x2() : ', a)# Here a= 2 using local a
def x3():
	global a
	a = 3
	print('Inside x3() : ', a) # Here a= 3 using global a 'cos we have written global a first 
print('global : ', a)
x1()
print('global : ', a)
x2()
print('global : ', a)
x3()
print('global : ', a) # value of a has changed in function x3

