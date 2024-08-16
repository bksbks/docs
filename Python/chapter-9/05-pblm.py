#Replace the words in Donkey.txt file with ####
words = ["Donkey", "bad", "ganda"]

with open("donkey.txt") as f:
    content = f.read()
for word in words:    
   content = content.replace(word, "#" * len(word))

with open("donkey.txt", "w") as f:
    f.write(content)    