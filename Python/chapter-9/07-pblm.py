#copy the file
with open("source.txt") as f:
    content = f.read()

with open("copy.txt", "w") as f:
    f.write(content)

