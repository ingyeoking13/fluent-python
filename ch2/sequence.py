chars =  "abcdefghijk"
codes = [ c for c in chars ] # list comprehension
print(codes)

codes_condition = [ c for c in chars if c not in 'hijk'] # list comprehension with condition
print(codes_condition)
codes_condition = list(filter(lambda c: c not in 'hijk', map(lambda c:c , codes))) # map and filter(condition)
print(codes_condition)



# cartesian product
colors = ["black", "white"]
sizes = ["S", "W", "L"]
tshirts = [(color, size) for color in colors 
                         for size in sizes]
print(tshirts)

# generator expression 
chars = "abcdefgijk"
tuple_ge = tuple(char for char in chars)  # can leave out parentheses if function require one params
print(tuple_ge)
import array
arr_ge = array.array('u', (char for char in chars)) # require parentheses 
print(arr_ge, arr_ge[0], arr_ge[1])
tshirts = ('%s %s' % (c, s) for c in colors for s in sizes) # generator expression
print([t for t in tshirts])

