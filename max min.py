def minMax(thelist):
    min=thelist[0]
    max=thelist[0]
    for everynumber in thelist:
        if everynumber>max:
            max=everynumber
        if everynumber<min:
            min=everynumber
    return min,max

thelist =[40,35,18,49,100]
print minMax(thelist)
