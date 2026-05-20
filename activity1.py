def powerof2(n):
    if n == 0:
        return 0 
    elif n & (~(n-1 ))== n:
        return 1
    else:
        return 0

n = int(input("Enter your number: "))
if powerof2(n):
    print(n,"is a power of 2")
else:
    print(n,"is not a power of 2")