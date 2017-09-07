for row in range(3):
    for space in range(2-row):
        print(" "),
    for star in range(1+(row*2)):
        print("*"),
    print("\n")
