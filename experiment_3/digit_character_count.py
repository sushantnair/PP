st = input("Enter a string: ")
cstr=0
cdig=0
for var in st:
    if var.isdigit()==True:
        cdig+=1
    elif var.isspace()==True:
        continue
    else:
        cstr+=1
print("The number of digits are: ", cdig)
print("The number of characters are: ", cstr)