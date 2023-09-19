#A list is created with the input from the user
py_list = eval(input("Enter the values of a list: "))
#A dictionary is created, and the values of the list
#are passed to the dictionary as key values. But since
#a dictionary cannot have duplicate key values, so only
#one unique copy of each value in the list is sent to
#the dictionary. After that, the dictionary is 
#converted back into a list.
py_list = list(dict.fromkeys(py_list))
print(py_list)

