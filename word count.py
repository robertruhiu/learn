text=("the quick brown fox jump over the lazy dog")
textd={}                    #initiate an empty dictionary
for name in text.split(): #split each word in the text
    if name in textd.keys():
        textd[name]+=1
    else:
        textd[name]=1
    print(textd)
