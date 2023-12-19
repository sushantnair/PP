class account():
    def __init__(self, custname, accnum, acctype):
        self.custname = custname
        self.accnum = accnum
        self.acctype = acctype      
        print("The entered name is: ", self.custname) 
        print("The entered account number is: ", self.accnum)  
        print("The entered account type is: ", self.acctype)
class cur_acct(account):
    def __init__(self, origbal, newdeposit):
        self.origbal = origbal
        self.newdeposit = newdeposit
        print("The updated balance is: ", self.origbal + self.newdeposit)
        ch = input("Do you want to withdraw money? If yes, press Y else press any character.")
        if ch=="Y":
            withdrawamt = int(input("Enter the amount you would like to withdraw: "))
            newbal = self.origbal + self.newdeposit - withdrawamt
            if newbal<500:
                print("As your new balance is below Rs. 500, and your account type is Current Account, a service charge of 2% is being levied.")
                SC = 0.02*newbal 
                print("Final balance is: ", newbal - SC)
            else:
                print("Final balance is: ", newbal)
        
class sav_acct(account):
    def __init__(self, origbal, newdeposit):
        self.origbal = origbal
        self.newdeposit = newdeposit
        #assuming the rate of SI to be 7.5 and the interest is calculated out of original balance
        SI = (self.origbal*7.5*1)/100
        print("The interest is: ", SI) 
        print("The amount is: ", SI+self.origbal) 
        print("The updated balance is: ", SI + self.origbal + self.newdeposit)

name = input("Enter your name: ")
accnum = int(input("Enter your account number: "))
acctype = input("Enter CUR for current account and SAV for savings account: ")
balance = int(input("Enter your balance: "))
deposit = int(input("Enter your deposit: "))
Account = account(name, accnum, acctype)
if acctype=="CUR":
    CUR_acct = cur_acct(balance, deposit)
elif acctype=="SAV":
    SAV_acct = sav_acct(balance, deposit)


