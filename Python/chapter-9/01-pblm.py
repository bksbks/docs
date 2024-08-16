#Read the file and Print if word Barkath is present in the file or not. 
f = open("file.txt")    
content = f.read()
if("Barkath" in content):
    print("The word Barkath is present in the content")

else:
    print("The word Barkath is not present in the content")    
 
f.close()