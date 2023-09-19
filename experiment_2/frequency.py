#to take string input from the user
py_str = input("Enter a string: ")
#to create an empty dictionary named f_d
f_d = {}
#for loop where char data type is the variable
#and py_str is the iterable
for char in py_str:
    #if the specific character is in f_d
    if char in f_d: 
        #increment the count by 1
        f_d[char]+=1
    #if the specific character is a whitespace
    elif char==' ': 
        continue
    #if the specific character is not in f_d
    else:
        #create a key value for the character
        f_d[char] = 1
#print the 
print("The frequency of the different characters are: ")
print(f_d)
