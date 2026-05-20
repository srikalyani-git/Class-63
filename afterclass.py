def powerof8():
    n = int(input("Enter your number: "))
    count = 0
    if n == 0:
        print("the number is not a power of 8")
    elif n & (~(n&(n-1))):
        while n > 1:
            n >>= 1
            count +=1
        if count % 3 == 0:
            print("the number is a power of 8")
        else:
            print("the number is not a power of 8")

powerof8()