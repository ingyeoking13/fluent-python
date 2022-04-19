lax_coordinates = (33.9425, -118.408056) # tuple unpacking
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

from collections import namedtuple # named tuple
City = namedtuple('City', 'name country population coordinates') # named tuple
tokyo = City('Tokyo', 'JP', '36.933', (35.689722, 139.691667))
print(tokyo) 
print(tokyo.population, tokyo.coordinates, tokyo[1])
print(City._fields) #namedtuple property
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
print(delhi_data)
delhi = City._make(delhi_data)
print(delhi)
print(delhi._asdict()) #namedtuple asdict -> dictionary type


