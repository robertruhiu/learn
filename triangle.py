for line in [1,2,3,2,1]:
    #print ("line {}".format(line))
    for space in range(3-line):
       print(" ",end="")
    for stars in range(2*line-1):
        print("*",end="")
    print("")

