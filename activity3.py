def x_raised_to_y(x,y):
    result = 1
    while y>0:
        if y%2 == 0:
            x = x*x
            y >>= 1
        else:
            result = result*x
            y = y-1
    return result

x = int(input("Enter your base number: "))
y = int(input("Enter your exponent value: "))

print(x_raised_to_y(x,y))