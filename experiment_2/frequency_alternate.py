string = input('Enter a string')
strlist = string.split()
strdict = dict()
for word in strlist:
    print(word)
    for character in word:
        strdict[character] = strdict.get(character, 0) + 1
print(strdict)