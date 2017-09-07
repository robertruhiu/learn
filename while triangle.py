line=1
counter=1
while line>0:
    if line==3:
        counter=-1
    #print(line)

    for spaces in range(3-line):
        print(" ",end="")
    for stars in range((2*line)-1):
        print("*",end="")
    print("")
    line+=counter
