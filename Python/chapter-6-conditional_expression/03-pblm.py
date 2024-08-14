s1 = "how are you bhai"
s2 = "abusive language"
s3 = "harrasment humiliation insult"
s4 = "kill murder assault"

message = input("please enter your message: ")

if((s1 in message) or (s2 in message) or (s3 in message) or (s4 in message)):
    print("This is a spam message")

else:
   print("This is not a spam") 

