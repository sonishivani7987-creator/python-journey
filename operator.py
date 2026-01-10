# arithmetic operators 

x= 10 
y= 5
 

print("addition :", x + y)
print("subtraction :", x - y) 
print("multiplication :", x * y)
print("division :", x / y)
print("floor division :", x // y)
print("modulus :", x % y)
print("exponentiation :", x ** y)
#  comparison operators

print("equal to :", x == y) #False

print("not equal to :", x != y) #True
print("greater than :", x > y) #True
print("less than :", x < y) #False
print("greater than or equal to :", x >= y) #True
print("less than or equal to :", x <= y) #False

# logical operators

print(x>y and x<y) #False
print(x>y or x<y) #True
print(not(x>y)) #False

# assignment operators

a = 10
b = 5
a += b  # a = a + b
print("after a += b, value of a is :", a) #15

a -= b  # a = a - b
print("after a -= b, value of a is :", a) #10

a *= b  # a = a * b
print("after a *= b, value of a is :", a) #50

a /= b  # a = a / b
print("after a /= b, value of a is :", a) #10    # latest value of a is always used.



 #assignment question  1

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print("Fahrenheit:", fahrenheit)
print("Kelvin:", kelvin)


# assignment question 2

# take inputs
total_bill = float(input("Enter total bill amount: "))
friends = int(input("Enter number of friends: "))

# calculation
each_pay = total_bill / friends

# output
print("Each will pay:", each_pay)

# printing data types
print("Type of total_bill:", type(total_bill))
print("Type of friends:", type(friends))
print("Type of each_pay:", type(each_pay))    # Variable names in Python cannot contain spaces.

