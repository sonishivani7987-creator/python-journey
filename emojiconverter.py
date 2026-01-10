msg = input("Enter your message: ")

msg = msg.replace(":)", "😊")
msg = msg.replace(":(", "☹️")
msg = msg.replace(";)", "😉")
msg = msg.replace(":D", "😃")

print(msg)


#concatenation
print("Have a nice day " + "😊")


# repetition
print(":) " * 3)  

# membership 

"a" in "happy"  # True
"x" not in "happy"  # True

#len()function
print(len("😊😊😊"))  # 3
