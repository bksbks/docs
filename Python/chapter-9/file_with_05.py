f = open("file.txt")    
print(f.read())
f.close()

# Above code can be written using "with" as follows.Help to exiclude "close"
with open("file.txt")  as f:
    print(f.read())