def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n
n= int(input("Please enter a number: "))
print(sum(n))