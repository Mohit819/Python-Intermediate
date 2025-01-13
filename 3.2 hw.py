
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
for i in password:
    if i == "a":
        password = password.replace("a","@")
    if i == "s":
        password = password.replace("s","$")
    if i == "l":
        password = password.replace("l","|")
    if i.isupper()==False:
        password = password.replace(i,i.upper())
    elif i.islower()==False:
        password = password.replace(i,i.lower())
print("use",password,"instead")



