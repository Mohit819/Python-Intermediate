##price = 2.95
##money=input("what is the price?")
##while money[-1].isdigit() == False:
##    if money[-1].isdigit() == False:
##        print("Use valid numbers")
##        money=input("what is the price?")
##money=float(money)
##print(money-price)

##upper=0
##string = input("write a string")
##for i in string:
##    if i.isalpha() == True:
##        upper+=1
##    else:
##        upper = upper
##print(upper)

password = input("enter new password")
if password.upper()==False:
    print("use all uppercase letters")
    password = input("enter new password")
if password.isalnum()==False:
    print("use stronger symbols like @ or $")
    password = input("enter new password")
