letters={"A":"Q","E":"Z",
     "Q":"A","Z":"E",
     "T":"M","M":"T",
     "W":"N","N":"W",
     "O":"R","R":"O",
     "L":"S","S":"L"}
message=("Nobody will ever guess what i'm saying").upper()
encrypted=""
for letter in message:
    if letter in letters:
        encrypted += letters[letter]
    else:
        encrypted +=letter
print(encrypted)
# def code(sentence):
#     sentence = list(sentence)
#     code_letters={"A":"Q","E":"Z","Q":"A","Z":"E","T":"M","M":"T","W":"N","N":"W",
#      "O":"R","R":"O",
#      "L":"S","S":"L"}
#     replaced=[]
#     for letter in sentence:
#         if letter in code_letters.keys():
#             replaced.append(code_letters[letter])
#         else:
#             replaced.append(letter)
#
#     return ''.join(replaced)
#
# print(code("NOBODY WILL EVER GUESS WHAT I'M SAYING"))
