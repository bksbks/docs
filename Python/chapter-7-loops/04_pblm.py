#Findout prime number or not 
n = int(input("please eneter a number: "))
for i in range(2, n):
    if(n%i)== 0:
     print("number is not a prime") 
     break
else:
  print("Number is prime")
