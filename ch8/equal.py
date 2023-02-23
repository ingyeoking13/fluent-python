charles = { 'name' : 'charles', 'born': 1832 }
lewis = charles
print( lewis == charles )
print( lewis is charles )
darwin = { 'name' : 'charles', 'born': 1832 }
print( darwin == charles )
print( darwin is not charles )