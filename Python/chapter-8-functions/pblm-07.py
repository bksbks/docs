#Remove the text
def rem(l, word):
    for item in l:
        l.remove(word)
        return l

l = [ "Harry", "Rohan", "Shubham", "an"]    

print(rem(l, "an"))


# strip the text 
def rem(l, word):
    n = [ ]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = [ "Barkath", "an", "Rohan", "Kan"]      
print(rem(l, "an"))   