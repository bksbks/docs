#Wipe out all the content in a file
with open("test.txt", "w") as f:
    content = f.write("")
