#  assignment question - take diameter as input and calculate the area of a circle .

diameter = int(input("enter the value of diameter :"))  # remember datatype of input is string so we have to convert it into integer
radius = diameter / 2
area = 3.14 * (radius ** 2) 
print("the radius of circle is :", radius)
print("the area of circle is :", area)


food= "samosa"
age= 20
area= 660.98
name= "shivani"
print(type(food))
print(type(age))
print(type(area))
print(type(name))
print("data type of  variable name is :", type(name))