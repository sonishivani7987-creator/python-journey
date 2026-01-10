str="Shivani soni "
print(str.upper())  # SHIVANI SONI
print(str.lower())  # shivani soni
print(str.capitalize())  # Shivani soni
print(str.title())  # Shivani Soni
print(str.find("soni"))  # 8  #Finds index of a character/word.
print(str.replace("soni", "best "))  # Shivani best
print(str.count("i"))  # 3  #Counts occurrences of a character/word.
print(str.strip())  #Shivani soni   #Removes leading/trailing whitespace.
print(str.split())  # ['Shivani', 'soni']  #Splits string into a list of words.
print(str.startswith("Shi"))  # True  #Checks if string starts with a specific substring.
print(str.endswith("soni "))  # True  #Checks if string ends with a specific substring.
print(str.endswith("on"))  #false
print(str.isalpha())  # False  #Checks if all characters are alphabetic.
print(str.isdigit())  # False  #Checks if all characters are digits.
print(str.isalnum())  # False  #Checks if all characters are alphanumeric.
print("-".join(['hi', 'python']))