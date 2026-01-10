#  text[:6]  # Slice from start only
#  text[0:6]  Slice from start to end
#Start index → included
#End index → excluded
#Indexing starts from 0


str = "shivanisoni"
print(str[0:6])  # shivan
print(str[:6])   # shivan
print(str[6:])   # isoni 
print(str[:])    # shivanisoni
print(str[2:8])  # ivanis
print(str[3:9])  # vanison 
print(str[-2:-9])  # (empty string)
print(str[-9:-2])  # ivanis
