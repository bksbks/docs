#convert  forienheat to celsius

def f_to_c(f):
    return 5 *(f-32)/9

f = int(input("Please enter the number in F: "))
c = f_to_c(f)
print(f"{round(c, 2)}c")