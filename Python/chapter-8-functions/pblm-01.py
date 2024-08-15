#Findout the greatest number in given 3 numbers

def function(a, b, c):
    if(a>b and a>c):
      return a
    elif(b>a and b>c):
      return b
    elif(c>a and c>b):
      return c
a = 1
b = 2
c = 3

print(function(a, b, c))
