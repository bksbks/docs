#Replace the word in Donkey.txt file with ####
word = "Donkey"

with open("donkey.txt") as f :
    content = f.read()
contentNew = content.replace(word, "####")

with open("donkey.txt", "w") as f:
    content = f.write(contentNew)