#  question on slicing 
# take input and print middle 3 character  ,last 2 character

str = input("Enter the string: ")  # green  
length = len(str)
mid = length // 2
print("Middle 3 characters:", str[mid-1:mid+2])
print("Last 2 characters:", str[-2:])  