'''num = 0
age = int(input("Enter the age of student: "))
weight = int(input("Enter the weight of student: "))
def exception(c):
    try:
        num = 5/c
    except ZeroDivisionError:
        print("Student is not eligible for registration.")
    else:
        print("Student is successfully registered.")
    finally:
        print("Thank you!")
if age>12 and weight>40:
    exception(0)
elif age>12 and weight<40:
    exception(0)
elif age<12 and weight>40:
    exception(0)
else:
    exception(1)'''
# def calculate(*args): 
#     sum=0 
#     for arg in args: 
#         sum = sum + arg
#     print("The sum is",sum)
# sum=0 
# calculate(10,20,30)
# print("Value of sum outside the function:",sum)
# x = lambda a : a + 1987 
# print(x(2017))
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*2, li))
print(final_list)





    


