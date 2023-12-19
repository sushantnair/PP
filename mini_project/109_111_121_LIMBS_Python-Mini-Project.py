#Personal details
name = input("Enter your good name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
role = input("Enter your role (Student/Faculty): ")
#Book details input
programme = input("Enter the programme in which your book\nmay be found (B. Tech., M. Tech., Ph.D.): ")
field = input("Enter the field in which the subject is found: ")
print("Enter the year relevant to the subject.")
if programme=="B.Tech." or programme=="B. Tech.":
    year = int(input("'1' for FY, '2' for SY, '3' for TY or '4' for LY.\nYear: ")) 
elif programme=="M.Tech." or programme=="M. Tech.":
    year = int(input("'1' for FY, '2' for SY.\nYear: "))
elif programme=="Ph.D." or programme=="PhD":
    year = int(input("Enter a number indicating the number of years you have been doing this course.\nYear: "))
def btech():
    if year==1:
        b_l = open('FY_BTECH_BOOKS.csv', 'r')
        for i in b_l.read().split(","):
            print(i,end="\t")
    elif year==2:
        if field=="Computer Engineering" or "COMPS":
            b_l = open('SY_BTECH_COMPS.csv', 'r')
            print(b_l.read())
        elif field=="Electronics Engineering" or "ETRX":
            b_l = open('SY_BTECH_ETRX.csv', 'r')
            print(b_l.read())
        elif field=="Electronics and Telecommunications Engineering" or "EXTC":
            b_l = open('SY_BTECH_EXTC.csv', 'r')
            print(b_l.read())
        elif field=="Information Technology" or "IT":
            b_l = open('SY_BTECH_IT.csv', 'r')
            print(b_l.read())
        elif field=="Mechanical Engineering" or "MECH":
            b_l = open('SY_BTECH_MECH.csv', 'r')
            print(b_l.read())
    elif year==3:
            print("Not Available!")
    elif year==4:
            print("Not Available!")
    else:
            print("Sorry! Wrong year has been entered!")
def mtech():
    print("Not Available at the moment!")
def phd():
    print("Not Available at the moment!")
if programme=="B. Tech.":
    btech()
elif programme=="M. Tech.":
    mtech()
elif programme=="Ph. D.":
    phd()  
else:
    print("The entered programme does not exist.")
#search algorithm for books - use in-built function
#file handling
def issue():
    subject = input("Enter the subject of the book which you want to issue: ")
    b_i = open('BOOKS_ISSUE.csv', 'a')
    b_i.write(subject)
    b_i.write("\n")
    b_i.close()
    b_i = open('BOOKS_ISSUE.csv', 'r')
    print(b_i.read())
    b_i.close()
    choice()
c = 0
b_i = open('BOOKS_ISSUE.csv', 'r+')
b_i.seek(0)
b_i.truncate()
name1 = "Name of issuer: " + name
b_i = open('BOOKS_ISSUE.csv', 'a')
b_i.write(name1)
b_i.write("\n")
b_i.close()
def choice():
    global c
    ch = int(input("Enter '1' if you want to issue a book, otherwise enter any other character\nChoice: "))
    if ch==1:
        c = c+1
        if c<=3:
            issue()
        else:
            print("Sorry! No more than three books can be issued.") 
            b_i = open('BOOKS_ISSUE.csv', 'r')
            print("The list of books issued during this session is as follows: ")
            print(b_i.read())
    else:
        b_i = open('BOOKS_ISSUE.csv', 'r')
        print("The list of books issued during this session is as follows: ")
        print(b_i.read())
        exit()
choice()

