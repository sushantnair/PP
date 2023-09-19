armnum = 0
num = int(input("Enter a number to check if it is Armstrong or not: "))
orignum = num
if(num<0):
    print("An invalid input has been entered.")
else:
    while(num!=0):
        num2 = int(num%10)
        armnum += pow(num2, 3)
        num = int((num-num2)/10)
    if armnum == orignum:
        print("The number ", orignum, "is an Armstrong number.")
    else:
        print("The number ", orignum, "is not an Armstrong number.")
