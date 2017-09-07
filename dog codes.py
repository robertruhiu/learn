#hd..h...d..h.d..h.h
#the output should be hd..hd.....hd....h.h
#inp="hd..h...d..h.d...h.h"
#inp[5],inp[8]=inp[8],inp[5]
#print(inp)


# inp ="hd..h...d..h.d..h.h "
# nap = list(inp)
# nap[5],nap[8]=inp[8],inp[5]
# nap[12],nap[13]=inp[13],inp[12]
# str1 = ''.join(nap)
# print (str1)

# inp="hd..h...d..h.d..h.h "
# index=0
# lasth=0
# while index<len(inp):
#     if inp[index]=="d" and inp[index-1]!="h":
#         inp=inp[:lasth]+inp[index]+inp[lasth+1:index]+inp[index+1:len(inp)]
#     elif inp=="h":
#         lasth=index
# index+=1
# print(inp)
inp ="hddfhdhfghjfdsffh "
str = list(inp)
line=0
while(line<len(str)):
    if str[line]=="h" and not(str[line+1]=="d"):
        for ch in str[line+1]:
            if ch =="d":
                str[line+1],ch=ch,str[line+1]
    line+1
print("".join(str))
