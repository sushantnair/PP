file1 = open("file1.txt", 'w')
file1.write("Computer Engineering")
file1.close()
file2 = open("file2.txt", 'w')
file2.write("Electronics and Telecommunications Engineering")
file2.close()
file3 = open("file3.txt", 'w')
file3.write("Electronics Engineering")
file3.close()
file4 = open("file4.txt", 'w')
file4.write("Information Technology")
file4.close()
file5 = open("file5.txt", 'w')
file5.write("Mechanical Engineering")
file5.close()
file = input("There are five files in existence: file1.txt to file5.txt\nEnter the name of any file you want to open: ")
if file=="file1.txt":
    file1 = open("file1.txt", 'r')
    file1w = open("file1u.txt", 'w')
    for line in file1:
        file1w.write(line.upper())
    file1w.close()
    file1w = open("file1u.txt", 'r')
    print(file1w.read())
elif file=="file2.txt":
    file2 = open("file2.txt", 'r')
    file2w = open("file2u.txt", 'w')
    for line in file2:
        file2w.write(line.upper())
    file2w.close()
    file2w = open("file2u.txt", 'r')
    print(file2w.read())
elif file=="file3.txt":
    file3 = open("file3.txt", 'r')
    file3w = open("file3u.txt", 'w')
    for line in file3:
        file3w.write(line.upper())
    file3w.close()
    file3w = open("file3u.txt", 'r')
    print(file3w.read())
elif file=="file4.txt":
    file4 = open("file4.txt", 'r')
    file4w = open("file4u.txt", 'w')
    for line in file4:
        file4w.write(line.upper())
    file4w.close()
    file4w = open("file4u.txt", 'r')
    print(file4w.read())
elif file=="file5.txt":
    file5 = open("file5.txt", 'r')
    file5w = open("file5u.txt", 'w')
    for line in file5:
        file5w.write(line.upper())
    file5w.close()
    file5w = open("file5u.txt", 'r')
    print(file5w.read())
else:
    print("Sorry! The entered file does not exist.")