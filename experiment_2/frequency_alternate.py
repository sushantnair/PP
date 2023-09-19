string = input('Enter a string')
strdict = dict()
for line in string:
    line = line.rstrip()
    print(line)
    for word in line:
        strdict[word] = strdict.get(word, 0) + 1
print(strdict)