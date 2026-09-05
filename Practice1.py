a = [1, 2, 3]
b = a

print(a is b)

a = [1, 2, 3]
#the is keyword asks if two variables refer to the same object. The is operator should never be used for the numbers or texts as it creates error when the numbers get bigger. They could be used for checking 'None'.
#the == operator asks if the have equivalent values
print(a is b)

x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y) #this is floor division. Python floors towards infinity. Applying this to a negative number, outputs a number less than it. For eg. -10//3 outputs a -4
print(x % y)
print(x ** y)

#Python is said to be dynamically typed because variables are bound to objects at runtime,and also the variables do not have fixed types unlike in statically typed languages where the variable type must be declared permanently locking it to that type
x = 10
y = 2

z = x / y
print(z)
print(type(z))
print(type(x/y))
print(5//2)


voltage = 0 #Python treats 0 as false and 1 as true

if voltage:
    print("Voltage present")
else:
    print("No voltage")
    
voltage = 24

print(voltage < 25)
print(voltage <= 24)
print(voltage == 24)
print(voltage != 12)
print(voltage > 30) #These eveluate to give a Boolean output

#Indexing in Python starts at 0 because it represents an offset from the beginning
#Lists are mutable, that is, their values can be changed and values can be added to or removed from them

for n, sample in enumerate(samples): #allows to access the index and its value
    print(n, sample)