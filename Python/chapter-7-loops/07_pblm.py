'''
Print the following pattern
  *
 ***
*****  
'''
n = int(input("please enter the number: "))

for i in range(1, n+1):
    print(" "* (n-i), end="")        
    print("*"* (2*i-1), end="")    
    print("")