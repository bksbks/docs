#Findout python in present in the log.txt
with open("log.txt") as f:
    content = f.read()
if("python" in content):
    print("python is present in the log.txt")    
else:
    print("python is not present in the log.txt")        
