dic={"the":"t-word","and":"a-word","cow":"c-word","barn":"b-word"}
nano ="the dogs and cow were in the barn"

#def censor(nano,dic):

#     for values in str:

#         str=str.replace(values, values )
#             return str
#
#          print(str)
replaced_input=[]
nano=nano.split(' ')                #makes nano into a string
for word in nano:                   #word will look up in dictionary
    if word in dic.keys():
        replaced_input.append(dic[word])
    else:
        replaced_input.append(word)
print(" ".join(replaced_input))
