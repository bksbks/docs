a = (2, 45, 66, 87, 446, 2, 56, 2)

print(type(a)) 

#lists no of occurences
no = a.count(2) 
print(no)

# lists index number
no = a.index(66)  
print(no)

#concatenate
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated = tuple1+tuple2
print(concatenated)


#repeated
tuple1 = (1, 2, 3)
repeated = tuple1 * 3
print(repeated)

# true or false     
print(2 in tuple1)
print(4 in tuple1)
print(len(tuple1))

#unpack into individual variable
tuple = (1, 2, 3)
a, b, c = (1, 2, 3)
print(a, b, c)

#sliced
tuple = (1, 2, 3, 4, 5, 6, 7, 8)
sliced = tuple[3:7]
print(sliced)









