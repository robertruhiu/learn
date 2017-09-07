i = 14
while i > -3:
    if (i % 2) == 0 and i > 0:
        print(str(i)+ "is even")
    elif (i % 2 )!= 0 and i > 0:
        print(str(i)+ "is odd")
    else:
        print(str(i)+ "is negative")
    i = i-3
