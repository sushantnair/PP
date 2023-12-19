num = int(input("Enter a number to find its factorial: "))
def fact(num):
    if num==1:
        return num
    else:
        num = num - 1
        return num*fact(num)
print("The factorial of ", num, " is ", num*fact(num)) 