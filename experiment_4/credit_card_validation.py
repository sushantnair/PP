import re
c = 0
num = input("Enter your credit card number: ")
x = re.search("\A[456]", num)
if x:
    print("Success, as num starts from ", x)
    z = re.search("[a-zA-Z_]", num)
    if z==None:
        print("Success, as the number contains only digits.")
        y = re.findall("\d", num)
        if len(y)==16: 
            print("Success, as number contains ", len(y), " digits.")
            y1 = re.findall("[-]", num)
            if len(y1) == 3: 
                print("Success, as there are exactly three hyphens.")
                w = re.split("[-]", num)
                print(w)
                for i in w:
                    v = len(i)
                    if v == 4:
                        c = c+1
                if c==4:
                    print("Success, as the digits are grouped in pairs of four.")
                    print("Success! Your Credit Card Number is valid.")
                else:
                    print("Failure, as the digits are not in groups of four.")
            else:
                print("Failure, as there are not exactly three hyphens.")
        else:
            print("Failure, as the number does not contain exactly 16 digits.")   
    else:
        print("Failure, as the number contains characters which are not digits")
else:
    print("Failure, as the number does not start from 4, 5 or 6.")
