#creating file rollcall.txt
file = open("rollcall.txt", 'w')
file.write("Roll No\t\tName\tDepartment")
file.close()
noi = int(input("Enter the number of data sets to be fed into the file: "))
for i in range(0, noi):
    roll_num = input("Enter the roll number of the student: ")
    name = input("Enter the name of the student: ")
    dept = input("Enter the department of the student: ")
    file = open("rollcall.txt", 'a')
    lines = "\n", roll_num, "\t\t", name, "\t", dept, "\n"
    file.writelines(lines)
    file.close()
file = open("rollcall.txt", 'r')
print(file.read())
#Lesson #1: Only string data type values can be written into files