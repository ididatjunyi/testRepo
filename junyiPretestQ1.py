sentence = "Hello my name is idid"

print(sentence)

split = sentence.split(" ")

sentence_rev = ""

for i in range(len(split)):
    for j in range(len(split[i])):
        sentence_rev = sentence_rev + split[i][-j-1]
    sentence_rev = sentence_rev + " "

print(sentence_rev)
