str1= 'hello'
str2= "shivani"
str3= '''welcome to python programming'''
str4= """have a nice day""" 

print(str1)  # hello
print(str2)  # shivani
print(str3)  # welcome to python programming
print(str4)  # have a nice day


# string concatenation
#  
print(str1 + " " + str2)  # hello shivani
print("hello" + " " + "world")  # hello world
print("shivani"+"soni")  # shivanisoni
print(str3 + "." + str4)  # welcome to python programming . have a nice day 

 # lenghth of string
 #The length of a string in Python is the count of all characters, including spaces.
 #Length = total characters (1-based)

print(len(str1))  # 5
print(len(str3))  # 29


 # string indexing
 # str[0] = "a"    # strings are immutable   # error :   string canot be changed  
 #  Every character in a string—including letters, spaces, numbers, and symbols—has its own index.            
  #  counting starts from 0
   
print(str2[0])  # s
print(str2[3])  # v
print(str4[5])  # a
