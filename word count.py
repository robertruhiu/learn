text=("the quick brown fox jumped over the lazy dog")
textd={}                    #initiate an empty dictionary
for word in text.split(): #split each word in the text
    if word in textd.keys():
        textd[word]+=1      #incrimental counter
    else:
        textd[word]=1
print(textd)
