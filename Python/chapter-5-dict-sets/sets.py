s = {1, 4, 5, 8}

a = set()  # a empty set 

b = {2, 3, 5, 6, 7, 6} # will not repeat duplicate values

print(b)

b = {2, 3, 5, 6, 7, 6, "Barkath"} 
print(b)

#add
b = {2, 3, 5, 6, 7, 6, "Barkath"} 
b.add(566)
print(b)

#remove
b.remove(566)

#to clear everything 
b.clear()