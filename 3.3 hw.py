lst1=["hi","hello","bonjour","Hola"]
while lst1 == lst1:
    print(lst1)
    i = input("do you want to add to the list")
    if i == "yes":
        add = input("what do you want to add")
        lst1 = lst1 + [add]
        print(lst1)
    f = input("do you want to modify the list")
    if f == "yes":
        index = int(input("at what index do you want to modify"))
        if index + 1 > len(lst1):
            print("print a valid index")
            index = int(input("at what index do you want to modify"))
        else:
            modify=input("what string should be here")
            lst1[index]=modify
            
##a string holds one thing but a list hold multiple things.
##you could get an index error by entering an index that doesn't exist.
