i = 1
j = 1
c=0
cp=0
cc=0
#this for loop can go for 20,000-1 iterations
#which means a total of 20,000-1 inputs can 
#be accepted at maximum
for i in range(1, 20000):
    num = int(input("Enter an integer: "))
    if num==-1:
        break
    elif num<=0:
        print("An incorrect input has been entered. So, the input is ignored")
        continue
    elif num==1:
        print("The number ", num, " is composite.")
        cc+=1
    else:
        c = 0 #for the next number, counter has to be reset
        for j in range(1, num):
            if num%j==0:
                c+=1
        if c<=1:
            print("The number ", num, " is prime.")
            cp+=1
        else:
            print("The number ", num, " is composite.")
            cc+=1
print("The number of prime numbers entered are ", cp)
print("The number of composite numbers entered are ", cc)
