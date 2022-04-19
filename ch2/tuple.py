# tuple unpacking
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates 
print(latitude, longitude)

latitude, longitude = longitude, latitude # tuple unpacking - exchange value -_- ;;;!!!
print(latitude, longitude)

print( divmod(20, 8) ) # tuple unpacking with asterisk
t = (20, 8) 
print(divmod(*t)) # 
quotient, remainder = divmod(*t)
print(quotient, remainder) 

a,b, *rest = range(5) # asterisk for exceed items
print(a, b, rest)
a, b, *rest = range(3)
print(a, b, rest)
a, b, *rest = range(2)
print(a, b, rest)
a, *rest, b = range(5)
print(a, b, rest)
*head, a, b = range(5)
print(head, a, b)



