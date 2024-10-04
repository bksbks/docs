marks = {
     "Barkath" : 45,
     "Ramesh"  : 67,
     "kane"   :  56,
     "shanu" : 90
} 

#print(marks, type(marks))

print(marks["Barkath"]) #printts error if doesn't find it.
print(marks.get("Barkath")) #prints none if doesn't find it.
